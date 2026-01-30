# MetaFixer2

MetaFixer2 is a small utility for fixing and customizing EXIF metadata in image files via the 'Open with...' option in XnView image viewer.
It consists of:

- **metafixer2.py** — a Python script with a simple Tkinter GUI for selecting lens and camera presets, then applying them via ExifTool.
- **run_metafixer2.sh** — a Bash wrapper that ensures XnView MP (or other apps) pass file arguments correctly to the Python script.

---

## Features

- Apply lens presets (e.g. Yashica Tomioka 60mm, Risespray 25mm CCTV, EF28mm f/2.8).
- Apply camera presets (Canon APS-C crop, Full Frame sync, Canon 1D crop, Canon EOS 50e).
- Single summary message per file (success or error).
- Works around XnView MP’s argument‑passing quirks (especially in Flatpak builds).

---

## Requirements

- Python 3
- Tkinter (usually included with Python on Linux)
- [ExifTool](https://exiftool.org/) installed and available at `/usr/bin/exiftool`
- [XnviewMP](https://www.xnview.com/en/xnview-mp/) installed.

---

## Installation

1. Clone or copy this repository:
   ```bash
   git clone https://github.com/yourusername/metafixer2.git
   cd metafixer2
2. Customize the Python app's menu to your own preferences for lenses, camera and/or crop factors.
3. Customize the bash scrip wrapper to your OS's own paths and preferred folders.
