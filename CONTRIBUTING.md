# Contributing to Stark Icons

Thanks for wanting to help. This file covers the things that are easy to get
wrong in this repository specifically.

## The one thing that catches everyone

This theme is about 8,700 symlinks and 16,900 real files. One icon often serves
dozens of application names, and `16@2x`, `22@2x`, `24@2x`, `32@2x` and
`scalable@2x` are links to their base directories, not copies.

**Never copy the tree with `cp -r`.** It follows every symlink and writes a
separate copy. The result still works, but it grows from 69 MB to over 200 MB
and the links between an icon and the names that share it are gone — edit one
file afterwards and the other copies keep the old artwork.

Use `git clone`, or `cp -a`, or `rsync -a`. After any copy or archive
round-trip, check:

```bash
find . -type l | wc -l     # expect ~8763
du -sh --exclude=.git .    # expect ~69M
find . -type l ! -exec test -e {} \; -print   # must print nothing
```

If the first number is 0 and the second is ~200M, the links were flattened.
Start again from a fresh clone.

Zip archives are the usual culprit. Prefer `tar czf`, or just push to git.

## Adding an alias, not a file

If an application needs an icon that already exists under another name, add a
symlink rather than a second copy:

```bash
cd scalable/apps
ln -s terminal.svg my-terminal-app.svg
```

That is how the upstream theme handles the other 8,700 cases, and it means a
future change to `terminal.svg` reaches every name at once.

## Drawing a new Stark icon

Only a small number of icons carry original Stark artwork. If you are adding
one:

- 256×256 artboard, `viewBox="0 0 256 256"`.
- Rounded-square silhouette at `x=8 y=8 w=240 h=240 rx=52`.
- Keep anything meaningful inside 36–220 on both axes.
- One gold idea per icon. Red is for identity marks and is rare. Cyan is rarer
  still, and only for signal or power ideas.
- A shape must differ from what sits behind it by more than one palette step.
  Charcoal on the background gradient is invisible, because the gradient's top
  stop *is* charcoal.
- Round caps and joins.
- No embedded bitmaps, external fonts, stylesheets, scripts or filters.
- Name the groups: `background`, `surface`, `frame`, `symbol`, `accent`,
  `highlight`, in that order. Deleting `background` should leave a usable
  transparent variant.

Palette:

| Name | Hex |
| ---- | --- |
| Graphite | `#18191D` |
| Charcoal | `#26282E` |
| Steel | `#343842` |
| Bone | `#EBE8E2` |
| Silver | `#A5A9B2` |
| Stark Gold | `#D6A84E` |
| Stark Red | `#B3272D` |
| Reactor Cyan | `#55DEE0` |

Render at 16, 24, 32, 48, 64 and 128 before opening a pull request. An icon
that only works at 128 is not finished. Thin strokes are the usual failure: a
10-unit stroke on a 256 canvas is under a pixel at 16px and greys out.

## When to leave an icon alone

The project's default is to preserve upstream artwork. Replace an icon only
when there is a clear reason — it uses a hue outside the palette, or it is a
signature desktop icon with no Stark identity. "It is not in our style" is not
on its own a reason to redraw 25,000 files.

Brand icons such as Firefox stay as they are. Recognition matters more than
consistency for those.

## Where files go

| Path | Holds |
| ---- | ----- |
| `scalable/apps/` | Application icons. Most lookups land here |
| `16/apps/` | The only small-size apps directory. Check it when changing an app icon |
| `16/`, `22/`, `24/`, `32/` | Fixed-size actions, devices, places, panel, mimetypes |
| `symbolic/` | Monochrome symbolic icons |
| `*/panel/` | Panel icons. These are monochrome by design — leave them that way |

Panel and symbolic icons should not gain colour. They are drawn to be recoloured
by the shell.

## Provenance

If you contribute an asset that is not your own work — an icon, an image, a
snippet of someone else's SVG — record it in `STARK-CHANGES.md` with its source,
author and licence. If you cannot establish where it came from or what licence
it carries, do not submit it.

Do not remove upstream attribution from `README.md` or `STARK-CHANGES.md`. Those
credits are a licence requirement, not decoration.

## Pull requests

- Keep changes small and reviewable. One icon or one theme area per PR.
- Say why each replaced icon needed replacing.
- Note anything you deliberately left alone.
- Mention which sizes you tested at.

Everything here is GPL-3.0. By contributing you agree your work ships under the
same licence.
