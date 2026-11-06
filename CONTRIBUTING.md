# Contributing to Stark Icons

Thanks for wanting to help. This file covers process and the things that are
easy to get wrong in this repository specifically.

**Read [DESIGN.md](./DESIGN.md) before drawing anything.** It has the palette,
the artboard, the construction rules, and — more importantly — when an icon
should be redrawn at all and when it should be left alone.

---

## The one thing that catches everyone

This theme is about 8,700 symlinks and 16,900 real files. One icon often serves
dozens of application names, and `16@2x`, `22@2x`, `24@2x`, `32@2x` and
`scalable@2x` are links to their base directories, not copies.

**Never copy the tree with `cp -r`.** It follows every symlink and writes a
separate copy. The result still works, but it grows from 69 MB to over 200 MB
and the links between an icon and the names that share it are gone — edit one
file afterwards and the other copies keep the old artwork.

Use `git clone`, `cp -a`, or `rsync -a`.

### Checking after any copy or archive

```bash
find . -type l | wc -l                         # expect 8763
find . -type l ! -exec test -e {} \; -print    # must print nothing
du -sh --exclude=.git .                        # expect ~69M
ls -ld *@2x                                    # expect 5 links
```

Reading the failures:

| Symptom                                 | Cause                                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------------- |
| 0 symlinks, ~203 MB                     | copied with `cp -r`, or unzipped                                                         |
| 8758 symlinks, no `@2x`                 | the five root links were never made, or the archiver skipped them                        |
| 5 broken links named `16/16`, `22/22` … | `ln -s` was run while `16@2x` still existed as a directory, so the link landed inside it |

To repair the last one:

```bash
rm -f 16/16 22/22 24/24 32/32 scalable/scalable
ln -s 16 16@2x
ln -s 22 22@2x
ln -s 24 24@2x
ln -s 32 32@2x
ln -s scalable scalable@2x
```

Zip archives flatten symlinks, and some graphical archivers silently skip the
five `@2x` directory links to avoid recursion. Prefer `git clone`, or
`tar czf` run from the parent directory.

---

## Adding an alias, not a file

If an application needs an icon that already exists under another name, add a
symlink rather than a second copy:

```bash
cd scalable/apps
ln -s terminal.svg my-terminal-app.svg
```

That is how the upstream theme handles the other 8,700 cases, and it means a
future change to `terminal.svg` reaches every name at once.

---

## Where files go

| Path                       | Holds                                                                  |
| -------------------------- | ---------------------------------------------------------------------- |
| `scalable/apps/`           | Application icons. Most lookups land here                              |
| `16/apps/`                 | The only small-size apps directory. Check it when changing an app icon |
| `16/`, `22/`, `24/`, `32/` | Fixed-size actions, devices, places, panel, mimetypes                  |
| `symbolic/`                | Monochrome symbolic icons                                              |
| `*/panel/`                 | Panel icons — monochrome by design, leave them that way                |

Panel and symbolic icons should not gain colour. They are drawn to be
recoloured by the shell.

---

## Provenance

If you contribute an asset that is not your own work — an icon, an image, a
snippet of someone else's SVG — record it in `STARK-CHANGES.md` with its
source, author and licence. If you cannot establish where it came from or what
licence it carries, do not submit it.

Do not remove upstream attribution from `README.md` or `STARK-CHANGES.md`.
Those credits are a licence requirement, not decoration.

---

## Pull requests

- Keep changes small and reviewable. One icon, or one theme area, per PR.
- Say why each replaced icon needed replacing. "Not in our style" is not a
  reason — see `DESIGN.md` §5.
- Note anything you deliberately left alone.
- Say which sizes you tested at, and attach the renders if you can.
- Update `STARK-CHANGES.md` in the same PR.

Everything here is GPL-3.0. By contributing you agree your work ships under the
same licence.
