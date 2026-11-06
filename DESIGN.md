# Stark Icons — design philosophy

This file exists so that someone new can draw an icon that looks like it
belongs, without having to reverse-engineer the existing ones.

---

## 1. What this project is

Stark Icons is **not** a from-scratch icon set. It is a small layer of original
artwork on top of [Dracula Icons](https://github.com/m4thewz/dracula-icons),
which itself sits on Tela and Papirus.

That shapes everything below. The job is not to redraw 25,000 icons in a new
style. The job is to change the handful of icons a person actually looks at
every day, and leave the rest alone.

If you remember one thing from this file: **the default is to preserve.**

---

## 2. The look

**Stark Hybrid** — industrial hardware crossed with clean technical symbols.

Think machined aluminium and anodised parts, not glass and neon. The reference
is the Iron Man Mark III armour: plated surfaces, precise edges, gold where
something matters.

What that means in practice:

- Dark graphite surfaces, not bright ones
- Geometry that looks measured, not sketched
- Gold used sparingly, so it still reads as an accent
- Nothing glossy, nothing glowing

Avoid: gradients with more than two stops, drop shadows, glass and blur
effects, chrome, neon glow, bevels, and decorative lines that are not part of
the symbol.

One gradient is allowed per icon — the background plate, two stops, for depth.
That is the only one.

---

## 3. Palette

| Name         | Hex       | Where it goes                       |
| ------------ | --------- | ----------------------------------- |
| Graphite     | `#18191D` | Icon background, knocked-out holes  |
| Charcoal     | `#26282E` | Plates and discs the symbol sits on |
| Steel        | `#343842` | Borders, structural bodies          |
| Bone         | `#EBE8E2` | The primary symbol                  |
| Silver       | `#A5A9B2` | Secondary symbol, mechanical parts  |
| Stark Gold   | `#D6A84E` | The accent                          |
| Stark Red    | `#B3272D` | Identity marks only                 |
| Reactor Cyan | `#55DEE0` | Signal and power ideas only         |

### Rules that actually bind

**One gold idea per icon.** A cursor, a seam, a ring, a progress arc. Not two
gold things competing for attention. If everything is accented, nothing is.

**Red is rare.** It appears in two of the six Stark icons. It marks identity,
not decoration.

**Cyan is rarer.** One icon out of six. Before reaching for it, check the idea
is really about signal, power or live data. "It looked nice" is not a reason.

**Not every icon is equally colourful.** The terminal is nearly monochrome on
purpose, so that settings and media player have room to be brighter. A set
where every icon shouts is a set where none of them do.

**Preserve brand colours when changing them costs recognition.** Firefox stays
as Firefox. A user scanning a dock is looking for a shape and a colour they
already know. Consistency is not worth more than being findable.

### The contrast rule

A shape must differ from what is behind it by **more than one palette step.**

This is not a style preference, it is a bug that already happened. The first
version of `file-manager.svg` filled the folder with charcoal `#26282E`. But
the background gradient's top stop _is_ charcoal. The folder vanished into the
backdrop and the icon read as three floating lines below 48px.

Bodies that need to read as a silhouette use steel `#343842` or lighter.

---

## 4. Construction

### Artboard

- `viewBox="0 0 256 256"`
- Silhouette: `x=8 y=8 w=240 h=240 rx=52`
- Safe area: **36 to 220** on both axes. Nothing meaningful outside it.
- Centre the symbol on (128, 128) unless the composition has a clear reason
  not to — the text editor's page-and-pencil pairing is the one exception.

The background is two stacked rectangles: a flat graphite fill, then the same
rectangle with a vertical charcoal-to-graphite gradient. The flat fill
underneath means the icon never renders transparent if a renderer drops the
gradient.

### Layers

Same groups, same order, every time. Groups with nothing in them are left out
rather than kept empty.

```xml
<g id="background">  <!-- rounded square: flat fill, then gradient -->
<g id="surface">     <!-- plates, discs, pages under the symbol -->
<g id="frame">       <!-- the 4-unit steel borders -->
<g id="symbol">      <!-- the application mark, bone or silver -->
<g id="accent">      <!-- the gold idea; red or cyan when earned -->
<g id="highlight">   <!-- the 10% bone rim light along the top edge -->
```

Deleting `#background` leaves a usable transparent variant with the symbol
intact. That is why the silhouette border lives in `frame`, not `background`.

The rim light in `#highlight` is byte-identical across every Stark icon. It
does more to make the set read as one family than any other single element.
Copy it, do not redraw it.

### Shapes before strokes

Build symbols from filled shapes first. Use strokes for outlines, rings, and
cases where a stroked path is genuinely the right primitive — the terminal
chevron, the globe meridians.

### Stroke weights

| Use                                             | Units |
| ----------------------------------------------- | ----- |
| Structural borders                              | 4     |
| Outlined symbol detail (meridians, rings, arcs) | 10–12 |
| Primary stroked symbols                         | 14–26 |

**Why primary strokes are heavy.** The obvious instinct is 8–10 units, which
looks right on screen at full size. It fails at small sizes, and here is the
arithmetic:

- The canvas is 256 wide.
- A 10-unit stroke is 10 ÷ 256 = 0.039, so **3.9%** of the icon's width.
- Rendered at 16px: 16 × 0.039 = **0.63 of a pixel.**

A sub-pixel stroke gets averaged into the background and turns grey. It does
not read as a line.

Papirus and Tela sit nearer 8–12% of canvas width for primary marks, which on
a 256 canvas is 20–30 units. The Stark icons land in that range: terminal
chevron 20, play triangle 14, pencil 26.

Round caps and round joins, everywhere.

### Technical limits

No embedded bitmaps. No external fonts, stylesheets or images. No scripts. No
filters. The SVG must be self-contained and editable by hand.

---

## 5. When to redraw an icon, and when not to

Replace an upstream icon only when one of these is true:

- It uses a hue that is not in the Stark palette, **and** it is an icon people
  see often. A green folder in the dock is worth fixing. A green icon six
  menus deep is not.
- It is a signature desktop icon carrying no identity at all.

Not reasons to redraw:

- "It is not in our style." That argument applied consistently means redrawing
  25,000 files, which is not this project.
- "I could do it better." Possibly, but every redraw is a file that no longer
  benefits from upstream fixes.

**When uncertain, preserve.**

### The six, and why each one changed

| Icon           | Reason                                                                            |
| -------------- | --------------------------------------------------------------------------------- |
| Terminal       | Flat grey, no accent. The signature developer icon had no identity                |
| File manager   | Dracula green, a hue absent from the palette, and highly visible                  |
| Settings       | Toggle-in-a-circle. Replaced for family consistency — the weakest case of the six |
| Text editor    | Pink pencil, outside the palette                                                  |
| System monitor | Purple disc, outside the palette                                                  |
| Media player   | Teal clapperboard, outside the palette                                            |

Settings is listed honestly: the upstream icon was good in isolation. It was
changed because the signature set should share one shape language, not because
it was bad. That is the thinnest justification in the set, and it is recorded
here rather than hidden.

---

## 6. Checks before opening a pull request

1. Renders at 16, 24, 32, 48, 64 and 128, and is recognisable at **every** one.
   An icon that only works at 128 is not finished.
2. Silhouette matches: `x=8 y=8 w=240 h=240 rx=52`.
3. Nothing meaningful outside 36–220.
4. One gold idea. Red and cyan only if earned.
5. Every body differs from its backdrop by more than one palette step.
6. No `<image>`, `xlink:href`, `<script>`, `<filter>`, or font reference.
7. `viewBox` is exactly `0 0 256 256`.
8. Groups named and ordered as above.
9. Sits beside the existing Stark icons without looking like a different
   project.

A quick way to check sizes:

```bash
for s in 16 24 32 48 64 128; do
  rsvg-convert -w $s -h $s your-icon.svg -o /tmp/icon-$s.png
done
```

Then look at them on a dark background, at actual size, not zoomed.

---

## 7. Known inconsistencies

Recorded honestly so nobody thinks they are hidden bugs:

- **The Stark icons read as a cluster.** They use a rounded square; much of the
  surrounding Dracula set uses circles and free shapes. Upstream was already
  mixed, so this is not new, but it is visible.
- **The untouched neighbours are brighter.** The green archive manager and blue
  image viewer sit loudly beside near-monochrome Stark icons. The archive
  manager is the strongest candidate for the next pass.
- **Two text editors.** `xed` resolves to the Stark icon. `gedit` resolves to a
  separate file that is still upstream. If you run both, they will not match.

See `STARK-CHANGES.md` for the full record of what changed and what did not.
