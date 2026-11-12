"""Arma hojas de contacto con los cuadros de un directorio de snapshots."""
import sys, glob, os, re
from PIL import Image, ImageDraw
d, out = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 6
fs = sorted(glob.glob(os.path.join(d, "*.png")), key=lambda f: float(re.search(r"([\d.]+)s", os.path.basename(f)).group(1)) if re.search(r"([\d.]+)s", os.path.basename(f)) else 0)
W = 330; H = int(W * 1920 / 1080)
for part in range(0, len(fs), cols):
    chunk = fs[part:part + cols]
    s = Image.new("RGB", (W * len(chunk) + 4 * (len(chunk) - 1), H + 22), (40, 0, 60))
    dr = ImageDraw.Draw(s)
    for i, f in enumerate(chunk):
        im = Image.open(f).convert("RGB").resize((W, H), Image.LANCZOS)
        s.paste(im, (i * (W + 4), 22)); dr.text((i * (W + 4) + 4, 5), os.path.basename(f), fill="white")
    s.save(f"{out}_{part // cols}.jpg", quality=88)
    print(f"{out}_{part // cols}.jpg")
