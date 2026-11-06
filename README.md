<h1 align="center">Stark Icons</h1>

<p align="center">
  An industrial icon theme for Linux desktops, built to sit alongside
  <a href="https://github.com/KDev/stark-mint-theme">Stark Mint</a>.
</p>

<p align="center">
  <a href="#install">Install</a> •
  <a href="#whats-different">What's different</a> •
  <a href="#credits">Credits</a> •
  <a href="#licence">Licence</a>
</p>

---

Stark Icons is an adaptation of [Dracula Icons](https://github.com/m4thewz/dracula-icons)
by Matheus Vitor. It keeps that theme's full coverage — around 25,000 files
across apps, mimetypes, places, devices, actions and symbolic icons — and
replaces a small number of signature desktop icons with original artwork in the
Stark palette.

Most of what you see is still upstream work. See [Credits](#credits).

## Install

Clone into your icons directory:

```bash
git clone https://github.com/karthikeyamadhavan123/Stark-Icons
```

Or download the repository and move it to `~/.icons` (create the directory if
it does not exist), or to `/usr/share/icons` to install for all users.

Then pick **Stark Icons** in your desktop's appearance settings. On Linux Mint
Cinnamon that is Themes → Icons.

If the theme does not appear, refresh the cache and restart the shell:

```bash
gtk-update-icon-cache -f ~/.icons/Stark-Icons
```

On Cinnamon, `Ctrl+Alt+Esc` restarts the shell. Cinnamon caches icon themes, so
this step is usually what makes a newly installed or edited theme show up.

### A note on cloning

This repository uses symlinks heavily — roughly 8,700 of them. One icon file
often serves dozens of application names, and the `@2x` directories are links
rather than copies. Clone it with git, or unpack a `tar` archive of it. Copying
the extracted files with `cp -r` will follow every link and write a separate
copy, which triples the size on disk and breaks the link between an icon and
the names that share it. Use `cp -a` or `rsync -a` if you need to copy it by
hand.

## What's different

Eight files carry original Stark artwork. Everything else is upstream.

| Icon | Resolves for |
| ---- | ------------ |
| Terminal | `gnome-terminal`, `org.gnome.Terminal` and 43 other names |
| File manager | `nemo`, `system-file-manager` and 20 others |
| Settings | `preferences-system` and 26 others, at both scalable and 16px |
| Text editor | `xed`, `accessories-text-editor` and 29 others |
| System monitor | `gnome-system-monitor` and 15 others |
| Media player | `xplayer`, `totem` and 8 others |

Brand icons such as Firefox are left alone on purpose. Changing them costs
recognition without making the desktop more coherent.

`STARK-CHANGES.md` lists every modified file, the reason for each change, and
what was deliberately left untouched.

### Palette

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

## Credits

Stark Icons is not original work from scratch. The great majority of the
artwork comes from three upstream projects, all GPL-3.0:

| Project | Author | What it contributes |
| ------- | ------ | ------------------- |
| [Dracula Icons](https://github.com/m4thewz/dracula-icons) | Matheus Vitor | The theme this one is adapted from: structure, coverage, and the recolouring work |
| [Tela Circle](https://github.com/vinceliuice/Tela-circle-icon-theme) | vinceliuice | Apps, mimetypes and scalable devices, via Dracula |
| [Papirus](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme) | Papirus Development Team | Places, actions and the 16/22/24 devices, via Dracula |

Please do not remove these credits. They are required by the licence, and they
are accurate: this project is a small set of changes on top of a great deal of
other people's work.

## Licence

GNU General Public License v3.0. See [LICENSE](./LICENSE).

The original Stark artwork in this repository is released under the same
licence, so the whole theme can be redistributed as one piece.

## Trademarks

Stark Icons is an independent community project. It is not affiliated with,
endorsed by or sponsored by Marvel, Disney, Linux Mint, or the authors of
Dracula Icons, Tela or Papirus. Application icons are named for the programs
they theme; the trademarks in those names belong to their respective owners.
