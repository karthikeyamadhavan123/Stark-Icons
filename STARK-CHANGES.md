# Stark Icons — changes from Dracula Icons

Stark Icons is an adaptation of [Dracula Icons](https://github.com/m4thewz/dracula-icons)
by Matheus Vitor. Almost all of the artwork in this repository is still his
work, or the work of the projects he drew from. This file records exactly what
is not.

## Inheritance chain

```text
Papirus ──┐
          ├─► Dracula Icons ──► Stark Icons
Tela ─────┘   (recoloured)      (8 files replaced)
```

Per the upstream README:

| Area                                      | Original source |
| ----------------------------------------- | --------------- |
| Apps, mimetypes, scalable devices         | Tela-circle     |
| Places, actions, 16/22/24 devices         | Papirus         |

Dracula Icons recoloured those two sets to the Dracula palette. Stark Icons
keeps that work intact and replaces only the small number of files listed
below.

All three upstreams are GPL-3.0, so the chain is licence-compatible.

## Files replaced with original Stark artwork

Drawn for this project on a 256x256 artboard. No upstream paths were reused,
recoloured, or traced.

| File                                        | Why |
| ------------------------------------------- | --- |
| `scalable/apps/terminal.svg`                | Upstream is flat grey with no accent. The terminal is the signature developer icon and carried no identity. |
| `scalable/apps/file-manager.svg`            | Upstream folder is Dracula green, a hue absent from the Stark palette, and the file manager is one of the most visible icons on the desktop. |
| `scalable/apps/nemo.svg`                    | Was separate blue-purple folder artwork. Now a symlink to `file-manager.svg`, matching how `system-file-manager.svg` already behaves upstream. |
| `scalable/apps/preferences-system.svg`      | Upstream is a toggle switch in a circle. Replaced with a gear so the signature set shares one shape language. Weakest case of the six — see "Judgement calls". |
| `16/apps/preferences-system.svg`            | Same artwork. `16/apps` is the only small-size apps directory in the repo, so without this the 16px settings icon would still be the old one. |
| `scalable/apps/accessories-text-editor.svg` | Upstream pencil is pink, outside the palette. This is the icon Mint's `xed` resolves to. |
| `scalable/apps/utilities-system-monitor.svg`| Upstream is a purple disc. Purple is not in the Stark palette. |
| `scalable/apps/totem.svg`                   | Upstream is a teal clapperboard. This is what Mint's `xplayer` resolves to. |

## Other changes

| File             | Change |
| ---------------- | ------ |
| `index.theme`    | `Name=` and `Comment=` only. `Inherits=`, `Directories=`, `ScaledDirectories=` and every per-directory block are untouched. |
| `LICENSE.md`     | **Added.** The upstream README links to `./LICENSE.md` but no such file is tracked in the repository. GPL-3.0 text supplied so the stated licence is actually present. |
| `STARK-CHANGES.md` | This file. |

## Deliberately left alone

- Every other icon in `scalable/`, `16/`, `22/`, `24/`, `32/`, `symbolic/`.
- `firefox.svg` and other brand icons. Changing them would cost recognition
  for no gain, and the upstream Firefox mark is already neutral against a dark
  desktop.
- `scalable/apps/software-center.svg`, `file-roller.svg`,
  `accessories-image-viewer.svg` — reviewed, already dark and restrained
  enough to sit beside Stark Mint.
- `16/panel/file-manager.svg`, `22/panel/`, `24/panel/` — panel icons are
  monochrome by design and should stay that way.
- All symlinks, MIME associations and `Inherits=` fallbacks.
- `README.md`, `Preview.png` — upstream attribution and credits intact.

## Judgement calls worth revisiting

**Settings.** The upstream toggle-in-a-circle icon is genuinely good in
isolation. It was replaced for family consistency, not because it was bad.
Reverting it is a one-file `git checkout`.

**Silhouette mixing.** The eight Stark icons use a rounded square. Much of the
surrounding Dracula set uses circles and free shapes. Upstream was already
mixed, so this is not new, but the Stark icons do read as a distinct cluster.

**Two text editors.** `xed` resolves to `accessories-text-editor.svg`, which is
now Stark. `gedit` resolves to a separate `text-editor.svg`, which is not. If
you run both, they will not match.

## Stark palette

| Name         | Hex       |
| ------------ | --------- |
| Graphite     | `#18191D` |
| Charcoal     | `#26282E` |
| Steel        | `#343842` |
| Bone         | `#EBE8E2` |
| Silver       | `#A5A9B2` |
| Stark Gold   | `#D6A84E` |
| Stark Red    | `#B3272D` |
| Reactor Cyan | `#55DEE0` |

## Licence

GPL-3.0, inherited from Dracula Icons, Tela and Papirus. The Stark artwork
listed above is released under the same licence. Do not remove upstream
attribution from `README.md` or this file.
