"""Prepara las placas fotográficas del video a partir del brand-kit de Aura Hogar.

Uso:  python tools/prep_images.py
Genera assets/img/*.jpg (versión encendida y, donde hace falta, versión "apagada").
"""
import os
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
SRC = os.path.join(PROJ, "..", "recursos presupuestador", "brand-kit", "imagery", "photography")
LOGO = os.path.join(PROJ, "..", "recursos presupuestador", "brand-kit", "logos", "original",
                    "aura-logo-removebg-preview.png")
OUT = os.path.join(PROJ, "assets", "img")
os.makedirs(OUT, exist_ok=True)


def load(rel, crop=None):
    im = Image.open(os.path.join(SRC, rel)).convert("RGB")
    if crop:
        im = im.crop(crop)
    return im


def fit_h(im, h):
    w = round(im.width * h / im.height)
    im = im.resize((w, h), Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=55, threshold=2))


def fit_w(im, w):
    h = round(im.height * w / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=55, threshold=2))


def grade(im, contrast=1.06, sat=0.94):
    """Unifica el look: un poco más de contraste, saturación contenida."""
    im = ImageEnhance.Contrast(im).enhance(contrast)
    return ImageEnhance.Color(im).enhance(sat)


def dark(im, level=0.2, sat=0.35, tint=(0.82, 0.92, 1.18)):
    """Versión 'luces apagadas': oscura, desaturada y fría."""
    a = np.asarray(ImageEnhance.Color(im).enhance(sat)).astype(np.float32) / 255.0
    a = np.power(a, 1.35) * level
    a *= np.array(tint, dtype=np.float32)
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))


def save(im, name, q=90):
    p = os.path.join(OUT, name)
    im.save(p, quality=q, subsampling=0)
    print(f"{name:22s} {im.size}")


# Escena 1 / clímax: la casa de noche
hero = grade(fit_w(load("sophia/hero.webp", (250, 0, 1524, 887)), 1400))
save(hero, "hero_lit.jpg")
save(dark(hero, level=0.36), "hero_dark.jpg")

# Escena 2: living
home = grade(fit_h(load("home/Home.webp"), 1330))
save(home, "home_lit.jpg")
save(dark(home, level=0.2), "home_dark.jpg")

H = 1330
for rel, name in [
    ("sophia/iluminacion.webp", "ilum.jpg"),
    ("sophia/persianas.webp", "pers_lit.jpg"),
    ("sophia/climatizacion.webp", "clim.jpg"),
    ("sophia/seguridad.webp", "seg.jpg"),
    ("sophia/audio.webp", "audio.jpg"),
    ("sophia/control-voz.webp", "voz.jpg"),
]:
    im = grade(fit_h(load(rel), H))
    save(im, name)
    if name == "pers_lit.jpg":
        save(dark(im, level=0.24, sat=0.5, tint=(0.9, 0.95, 1.1)), "pers_dark.jpg")

# Cerradura sobre negro
lock = grade(fit_w(load("sophia/smart-lock.webp", (384, 0, 1152, 1024)), 1080), contrast=1.04, sat=1.0)
save(lock, "lock.jpg")

# Logo
logo = Image.open(LOGO).convert("RGBA")
bbox = logo.getbbox()
logo = logo.crop(bbox)
logo.save(os.path.join(OUT, "logo.png"))
print("logo.png", logo.size)

# Grano de película (tile)
rng = np.random.default_rng(7)
n = rng.normal(128, 38, (512, 512)).clip(0, 255).astype(np.uint8)
Image.fromarray(n, "L").save(os.path.join(OUT, "grain.png"))
print("grain.png")
