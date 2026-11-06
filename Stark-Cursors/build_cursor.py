#!/usr/bin/env python3
"""
Build an XCursor binary from a single SVG.

XCursor format reference: the file is a header, a table of contents, then
one image chunk per size. Pixels are 32-bit ARGB with premultiplied alpha,
little-endian.

Usage:
    python3 build_cursor.py input.svg output_name hotspot_x hotspot_y [sizes...]

Hotspot is given in the SVG's own coordinate space (its viewBox), and is
scaled for each output size.
"""
import struct
import sys
import io

import cairosvg
from PIL import Image

MAGIC = b"Xcur"
HEADER_SIZE = 16
VERSION = 0x00010000
CHUNK_IMAGE = 0xFFFD0002
IMAGE_HEADER_SIZE = 36
IMAGE_VERSION = 1


def render(svg_path, size):
    png = cairosvg.svg2png(url=svg_path, output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def to_argb_premultiplied(img):
    """XCursor wants premultiplied ARGB words, little-endian."""
    out = bytearray()
    for r, g, b, a in img.getdata():
        if a != 255:
            r = (r * a) // 255
            g = (g * a) // 255
            b = (b * a) // 255
        out += struct.pack("<I", (a << 24) | (r << 16) | (g << 8) | b)
    return bytes(out)


def build(svg_path, sizes, hot_x, hot_y, svg_canvas):
    images = []
    for size in sizes:
        img = render(svg_path, size)
        scale = size / svg_canvas
        # round, then clamp inside the image
        hx = min(size - 1, max(0, round(hot_x * scale)))
        hy = min(size - 1, max(0, round(hot_y * scale)))
        images.append((size, img, hx, hy))

    ntoc = len(images)
    toc_size = ntoc * 12
    offset = HEADER_SIZE + toc_size

    toc = b""
    body = b""
    for size, img, hx, hy in images:
        toc += struct.pack("<III", CHUNK_IMAGE, size, offset + len(body))
        pixels = to_argb_premultiplied(img)
        body += struct.pack(
            "<IIIIIIIII",
            IMAGE_HEADER_SIZE, CHUNK_IMAGE, size, IMAGE_VERSION,
            img.width, img.height, hx, hy, 0,  # delay 0 = static
        ) + pixels

    header = struct.pack("<4sIII", MAGIC, HEADER_SIZE, VERSION, ntoc)
    return header + toc + body, images


if __name__ == "__main__":
    svg, out = sys.argv[1], sys.argv[2]
    hx, hy = float(sys.argv[3]), float(sys.argv[4])
    canvas = float(sys.argv[5])
    sizes = [int(s) for s in sys.argv[6:]] or [24, 32, 48, 64]

    data, images = build(svg, sizes, hx, hy, canvas)
    with open(out, "wb") as fh:
        fh.write(data)

    print(f"{out}: {len(data)} bytes, {len(images)} sizes")
    for size, img, x, y in images:
        print(f"  {size:>3}px  hotspot ({x}, {y})")
