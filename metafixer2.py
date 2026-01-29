import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
import os

if len(sys.argv) < 2:
    sys.exit("No file provided!")

image_path = sys.argv[1]

def run_exiftool(tags):
    cmd = ["/usr/bin/exiftool", "-all=", "-tagsfromfile", "@", "-all:all", "-unsafe"] \
          + tags + ["-overwrite_original", image_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stderr

# --- GUI Setup ---
root = tk.Tk()
root.title("Lens & Camera Fixer")
root.geometry("340x520")

lens_var = tk.StringVar()
camera_var = tk.StringVar()

# --- Lens Selection ---
tk.Label(root, text="Select the lens:", font=('Arial', 10, 'bold')).pack(pady=(15, 5))
tk.Radiobutton(root, text="Yashica Tomioka 60mm", variable=lens_var, value="yashica").pack(anchor='w', padx=20)
tk.Radiobutton(root, text="Risespray 25mm CCTV", variable=lens_var, value="risespray").pack(anchor='w', padx=20)
tk.Radiobutton(root, text="EF28mm f/2.8", variable=lens_var, value="ef28").pack(anchor='w', padx=20)

# --- Camera Selection ---
tk.Label(root, text="Select the camera:", font=('Arial', 10, 'bold')).pack(pady=(20, 5))
tk.Radiobutton(root, text="Canon APS-C Crop (1.6x)", variable=camera_var, value="apsc").pack(anchor='w', padx=20)
tk.Radiobutton(root, text="Full Frame Sync (1:1)", variable=camera_var, value="fullframe").pack(anchor='w', padx=20)
tk.Radiobutton(root, text="Canon 1D Crop (1.3x)", variable=camera_var, value="canon1d").pack(anchor='w', padx=20)
tk.Radiobutton(root, text="Canon EOS 50e Body", variable=camera_var, value="eos50e").pack(anchor='w', padx=20)

# --- Apply Button ---
def apply_selection():
    errors = []

    # Lens presets
    if lens_var.get() == "yashica":
        code, err = run_exiftool(["-LensModel=Yashica Tomioka 60mm f/2.8 Macro", "-FNumber=2.8", "-FocalLength=60"])
        if code != 0: errors.append(err)
    elif lens_var.get() == "risespray":
        code, err = run_exiftool(["-LensModel=Risespray 25mm f/1.8 CCTV", "-FNumber=2.8", "-FocalLength=25",
                                  "-FocalLengthIn35mmFormat=50", "-ApertureValue=16"])
        if code != 0: errors.append(err)
    elif lens_var.get() == "ef28":
        code, err = run_exiftool(["-LensModel=EF28mm f/2.8", "-FocalLength=28", "-FNumber=10"])
        if code != 0: errors.append(err)
                                                                                                             [ Read 83 lines ]
