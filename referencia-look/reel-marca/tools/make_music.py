"""Música original del video Aura Hogar, sintetizada por código (sin samples).

Uso:  python tools/make_music.py   ->  assets/music.wav
100 BPM, Re menor. Golpes en 2.4, 7.2, 12.0, 16.8, 21.6, 26.4 (clímax) y 34.8 (cierre).
"""
import os
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
BPM = 100.0
BEAT = 60.0 / BPM          # 0.6 s
BAR = 4 * BEAT             # 2.4 s
DUR = 43.2
N = int(DUR * SR)
rng = np.random.default_rng(11)

T_S2, T_S3, T_S4, T_S5, T_S6, T_S7 = 7.2, 12.0, 16.8, 21.6, 26.4, 34.8


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12.0)


def buf():
    return np.zeros((N, 2), dtype=np.float64)


def add(dst, sig, t0, gain=1.0, pan=0.0):
    """Suma sig (mono o estéreo) en dst a partir de t0 segundos."""
    i0 = int(round(t0 * SR))
    if i0 >= N:
        return
    if sig.ndim == 1:
        l = np.cos((pan + 1) * np.pi / 4)
        r = np.sin((pan + 1) * np.pi / 4)
        sig = np.stack([sig * l, sig * r], axis=1)
    n = min(len(sig), N - i0)
    if i0 < 0:
        sig = sig[-i0:]
        n = min(len(sig), N)
        i0 = 0
    dst[i0:i0 + n] += sig[:n] * gain


def tt(d):
    return np.arange(int(d * SR)) / SR


def lp(x, fc, order=2):
    sos = signal.butter(order, min(fc, SR * 0.45), "low", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=0)


def hp(x, fc, order=2):
    sos = signal.butter(order, fc, "high", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=0)


def bp(x, f1, f2, order=2):
    sos = signal.butter(order, [f1, f2], "band", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=0)


def adsr(d, a, dec, s, r):
    n = int(d * SR)
    e = np.full(n, s, dtype=np.float64)
    na, nd, nr = int(a * SR), int(dec * SR), int(r * SR)
    na = max(1, min(na, n))
    e[:na] = np.linspace(0, 1, na)
    nd = min(nd, n - na)
    if nd > 0:
        e[na:na + nd] = np.linspace(1, s, nd)
    nr = min(nr, n)
    e[-nr:] *= np.linspace(1, 0, nr)
    return e


def saw(f, t, ph=0.0):
    return 2.0 * ((f * t + ph) % 1.0) - 1.0


def supersaw(m, d, voices=5, det=0.11):
    """Acorde/nota ancha en estéreo."""
    t = tt(d)
    out = np.zeros((len(t), 2))
    f0 = hz(m)
    for v in range(voices):
        off = (v - (voices - 1) / 2) / max(1, (voices - 1) / 2)
        f = f0 * 2 ** (off * det / 12.0)
        s = saw(f, t, rng.random())
        p = off * 0.8
        out[:, 0] += s * np.cos((p + 1) * np.pi / 4)
        out[:, 1] += s * np.sin((p + 1) * np.pi / 4)
    return out / voices


# ---------------------------------------------------------------- armonía
CH = {
    "Dm": dict(bass=38, pad=[50, 57, 64, 65, 69], arp=[62, 65, 69, 76, 74, 69, 65, 76]),
    "Bb": dict(bass=34, pad=[46, 53, 57, 62, 65], arp=[62, 65, 70, 74, 69, 65, 70, 77]),
    "F":  dict(bass=41, pad=[53, 60, 67, 69],     arp=[60, 65, 69, 72, 67, 65, 69, 77]),
    "C":  dict(bass=36, pad=[48, 55, 62, 64, 67], arp=[60, 64, 67, 74, 72, 67, 64, 76]),
}
PROG = ["Dm", "Dm", "Bb",            # S1  (0 – 7.2)
        "Dm", "Bb",                  # S2
        "F", "C",                    # S3
        "Dm", "Bb",                  # S4
        "F", "C",                    # S5
        "Dm", "Bb", "F", "C"]        # S6  (el compás 14 se corta a la mitad)


def section(t):
    for name, lim in (("S1", T_S2), ("S2", T_S3), ("S3", T_S4), ("S4", T_S5), ("S5", T_S6), ("S6", T_S7)):
        if t < lim:
            return name
    return "S7"


pad, arp, bass, drums, fx, bells, lead = buf(), buf(), buf(), buf(), buf(), buf(), buf()

# ---------------------------------------------------------------- pad
PAD_FC = dict(S1=520, S2=950, S3=1500, S4=2200, S5=1500, S6=5200, S7=800)
PAD_G = dict(S1=0.55, S2=0.6, S3=0.6, S4=0.65, S5=0.6, S6=0.9, S7=0.6)
for b, name in enumerate(PROG):
    t0 = b * BAR
    sec = section(t0)
    d = BAR + 1.2 if t0 + BAR < T_S7 else (T_S7 - t0) + 0.15
    chord = np.zeros((int(d * SR), 2))
    for m in CH[name]["pad"]:
        chord += supersaw(m, d)
        if sec == "S6":
            chord += 0.5 * supersaw(m + 12, d)
    chord = lp(chord, PAD_FC[sec], 2)
    att = 1.6 if b == 0 else (0.05 if sec == "S6" else 0.5)
    rel = 1.1 if t0 + BAR < T_S7 else 0.12
    chord *= adsr(d, att, 0.4, 0.85, rel)[:, None]
    add(pad, chord, t0, PAD_G[sec] * 0.2)

# S7: acorde final sostenido
d = DUR - T_S7
fin = np.zeros((int(d * SR), 2))
for m in [38, 50, 57, 62, 65, 69, 76]:
    fin += supersaw(m, d, det=0.08)
fin = lp(fin, 1100, 2) * adsr(d, 0.02, 2.5, 0.5, 4.5)[:, None]
add(pad, fin, T_S7, 0.17)

# drone grave de la intro
t = tt(T_S2 + 1.0)
dr = (np.sin(2 * np.pi * hz(26) * t) * 0.9 + np.sin(2 * np.pi * hz(38) * t) * 0.5
      + lp(saw(hz(38), t), 180) * 0.25)
dr *= adsr(len(t) / SR, 2.2, 0.1, 1.0, 1.4)
add(pad, dr, 0.0, 0.2)


# ---------------------------------------------------------------- arpegio
def pluck(m, d=0.42, fc=2400, bright=0.5):
    t = tt(d)
    f = hz(m)
    s = saw(f, t, rng.random()) * (0.5 + bright * 0.4) + np.sign(np.sin(2 * np.pi * f * t)) * 0.25
    s = lp(s, fc, 2)
    return s * np.exp(-t * 11.0) * adsr(d, 0.003, 0.05, 1.0, 0.05)


ARP_FC = dict(S2=1500, S3=2400, S4=3400, S5=2800, S6=5200)
ARP_G = dict(S2=0.22, S3=0.28, S4=0.3, S5=0.3, S6=0.3)
for b, name in enumerate(PROG):
    t0 = b * BAR
    sec = section(t0)
    if sec == "S1":
        continue
    notes = CH[name]["arp"]
    for i in range(16):
        ts = t0 + i * BEAT / 4
        if ts >= T_S7:
            break
        # la entrada del arpegio va abriéndose dentro de S2
        fade = min(1.0, (ts - T_S2) / 2.4 + 0.35) if sec == "S2" else 1.0
        fc = ARP_FC[sec] * (0.6 + 0.4 * fade)
        if sec == "S5":   # tensión: el filtro se abre hacia el clímax
            fc = 1400 + 4200 * ((ts - T_S5) / (T_S6 - T_S5)) ** 2
        acc = 1.0 if i % 4 == 0 else (0.62 if i % 2 == 0 else 0.5)
        m = notes[i % 8] + (12 if (sec == "S6" and i % 8 in (3, 7)) else 0)
        add(arp, pluck(m, fc=fc), ts, ARP_G[sec] * acc * fade, pan=(-0.55 if i % 2 == 0 else 0.55))

# delay de corchea con puntillo sobre el arpegio
dl = int(0.45 * SR)
wet = np.zeros_like(arp)
wet[dl:] = arp[:-dl][:, ::-1] * 0.36
wet[2 * dl:] += arp[:-2 * dl] * 0.16
arp = arp + lp(wet, 2600)

# ---------------------------------------------------------------- bajo
BASS_G = dict(S3=0.5, S4=0.55, S6=0.7)
for b, name in enumerate(PROG):
    t0 = b * BAR
    sec = section(t0)
    root = CH[name]["bass"]
    if sec in ("S3", "S4", "S6"):
        for i in range(8):
            ts = t0 + i * BEAT / 2
            if ts >= T_S7:
                break
            m = root + (12 if (i in (3, 7) and sec != "S3") else 0)
            t = tt(0.3)
            s = lp(saw(hz(m), t, 0.0), 420 if sec != "S6" else 700, 2) * 0.8 + np.sin(2 * np.pi * hz(m) * t)
            s *= np.exp(-t * 6.0) * adsr(0.3, 0.004, 0.05, 1.0, 0.04)
            add(bass, s, ts, BASS_G[sec] * (1.0 if i % 2 == 0 else 0.75))
    elif sec in ("S2", "S5"):
        d = BAR
        t = tt(d)
        s = (np.sin(2 * np.pi * hz(root) * t) + 0.35 * lp(saw(hz(root + 12), t), 300)) * adsr(d, 0.08, 0.3, 0.8, 0.5)
        add(bass, s, t0, 0.34)


# ---------------------------------------------------------------- batería
def kick(power=1.0):
    t = tt(0.42)
    f = 46 + 130 * np.exp(-t * 34)
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) * np.exp(-t * 8.5)
    click = hp(rng.normal(0, 1, len(t)), 2500) * np.exp(-t * 220) * 0.25
    return np.tanh((s + click) * 1.6) * power


def clap():
    t = tt(0.32)
    n = bp(rng.normal(0, 1, len(t)), 900, 4200)
    e = np.exp(-t * 26)
    for dly in (0.0, 0.011, 0.023):
        k = int(dly * SR)
        e[k:] += np.exp(-t[:len(t) - k] * 90) * 0.5
    return n * e * 0.5


def hat(open_=False):
    t = tt(0.22 if open_ else 0.06)
    return hp(rng.normal(0, 1, len(t)), 7500, 4) * np.exp(-t * (16 if open_ else 75))


kick_times = []
# S2: latido suave en 1 y 3
for b in (3, 4):
    for k in (0, 2):
        add(drums, lp(kick(), 180), b * BAR + k * BEAT, 0.42)
for b in range(5, 15):
    t0 = b * BAR
    sec = section(t0)
    if sec == "S5":
        continue
    for k in range(4):
        ts = t0 + k * BEAT
        if ts >= T_S7:
            break
        g = 0.95 if sec == "S6" else 0.78
        add(drums, kick(), ts, g)
        kick_times.append(ts)
        # hats
        add(drums, hat(), ts + BEAT / 2, 0.16 if sec == "S3" else 0.2, pan=0.25)
        if sec in ("S4", "S6"):
            add(drums, hat(), ts + BEAT / 4, 0.09, pan=-0.3)
            add(drums, hat(), ts + 3 * BEAT / 4, 0.09, pan=-0.3)
        if sec == "S6" and k == 3:
            add(drums, hat(True), ts + BEAT / 2, 0.14, pan=0.25)
        if sec in ("S4", "S6") and k in (1, 3):
            add(fx if False else drums, clap(), ts, 0.5 if sec == "S6" else 0.36)

# S5 compás 10: redoble que acelera hacia el clímax
roll_t = T_S6 - BAR
steps = [0, 0.6, 1.2, 1.5, 1.8, 1.95, 2.1, 2.175, 2.25, 2.325]
for i, s in enumerate(steps):
    add(drums, clap(), roll_t + s, 0.16 + 0.03 * i)
# relleno antes del golpe final
for i, s in enumerate([0.3, 0.45, 0.525]):
    add(drums, clap(), T_S7 - 0.6 + s, 0.3 + 0.06 * i)


# ---------------------------------------------------------------- golpes, subidas
def impact(power=1.0, tail=2.6):
    t = tt(tail)
    f = 34 + 62 * np.exp(-t * 9)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.2)
    thud = lp(rng.normal(0, 1, len(t)), 260, 2) * np.exp(-t * 7) * 1.4
    air = bp(rng.normal(0, 1, (len(t), 2)), 500, 6000) * (np.exp(-t * 3.2) * 0.22)[:, None]
    mono = np.tanh((boom + thud) * 1.5)
    return (np.stack([mono, mono], axis=1) + air) * power


def swell(d, power=1.0, f1=300, f2=7000):
    """Aire que crece hacia el corte (reverse)."""
    t = tt(d)
    n = rng.normal(0, 1, (len(t), 2))
    lo = bp(n, f1, f1 * 4)
    hi = bp(n, f2 / 3, f2)
    x = (t / d)
    env = x ** 3
    s = lo * (1 - x)[:, None] + hi * x[:, None]
    return s * env[:, None] * power


def riser(d, power=1.0):
    t = tt(d)
    x = t / d
    f = hz(50) * 2 ** (x ** 1.6 * 2.0)                 # dos octavas
    ph = np.cumsum(f) / SR
    tone = (saw(1.0, ph) + saw(1.005, ph, 0.3)) * 0.5
    tone = lp(tone, 3800) * x ** 2
    trem = 0.75 + 0.25 * np.sin(2 * np.pi * (4 + 12 * x) * t)
    s = np.stack([tone * trem, tone * trem[::-1]], axis=1) * 0.5
    return (s + swell(d, 0.9)) * power


add(fx, impact(0.5, 3.0), 2.4)            # aparece la marca
add(fx, swell(1.4, 0.35), T_S2 - 1.4)
add(fx, impact(0.75), T_S2)
add(fx, swell(0.7, 0.3), T_S3 - 0.7)
add(fx, impact(0.5, 1.8), T_S3)
add(fx, swell(0.9, 0.36), T_S4 - 0.9)
add(fx, impact(0.7), T_S4)
add(fx, swell(0.9, 0.36), T_S5 - 0.9)
add(fx, impact(0.65, 3.2), T_S5)
add(fx, riser(BAR, 0.5), T_S6 - BAR)
add(fx, impact(1.15, 3.2), T_S6)
add(fx, swell(0.6, 0.42), 30.0 - 0.6)
add(fx, impact(0.6, 2.0), 30.0)           # aterriza la frase del clímax
add(fx, swell(1.0, 0.5), T_S7 - 1.0)
add(fx, impact(1.25, 4.5), T_S7)          # cierre
add(fx, impact(0.6, 4.0), 36.0)           # aterriza el logo

# luz que se enciende en la intro (1.8 s): aire grave suave
add(fx, swell(1.6, 0.22, 120, 2400), 0.2)


# ---------------------------------------------------------------- campanas y melodía
def bell(m, d=3.2):
    t = tt(d)
    f = hz(m)
    idx = 2.2 * np.exp(-t * 3.0)
    s = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * 3.01 * t))
    s += 0.3 * np.sin(2 * np.pi * f * 2 * t) * np.exp(-t * 4)
    return s * np.exp(-t * 1.6) * adsr(d, 0.004, 0.1, 1.0, 0.4)


for ts, m, g, p in [(1.2, 74, 0.2, -0.3), (3.6, 81, 0.24, 0.3), (4.8, 77, 0.22, -0.2), (6.0, 76, 0.2, 0.2),
                    (7.2, 74, 0.2, 0.0), (9.6, 77, 0.16, 0.3), (21.6, 81, 0.22, -0.3), (22.8, 77, 0.18, 0.3),
                    (36.0, 74, 0.3, 0.0), (37.2, 81, 0.26, 0.3), (38.4, 77, 0.24, -0.3), (39.6, 76, 0.22, 0.2),
                    (40.8, 74, 0.26, 0.0)]:
    add(bells, bell(m), ts, g, pan=p)

# melodía del clímax (negras / blancas)
MEL = [(0, 81, 2), (2, 77, 1), (3, 76, 1),
       (4, 74, 3), (7, 77, 1),
       (8, 81, 2), (10, 84, 2),
       (12, 79, 1), (13, 76, 1)]
for beat, m, ln in MEL:
    d = ln * BEAT + 0.25
    s = supersaw(m, d, voices=5, det=0.14) + 0.4 * supersaw(m - 12, d, voices=3)
    s = lp(s, 4200) * adsr(d, 0.015, 0.2, 0.75, 0.22)[:, None]
    add(lead, s, T_S6 + beat * BEAT, 0.22)


# ---------------------------------------------------------------- sidechain
duck = np.ones(N)
rel = int(0.3 * SR)
curve = 1 - 0.55 * np.exp(-np.arange(rel) / (0.085 * SR))
for ts in kick_times:
    i0 = int(ts * SR)
    n = min(rel, N - i0)
    duck[i0:i0 + n] = np.minimum(duck[i0:i0 + n], curve[:n])
pad *= duck[:, None]
bass *= (0.35 + 0.65 * duck)[:, None]
lead *= (0.5 + 0.5 * duck)[:, None]


# ---------------------------------------------------------------- reverb
def make_ir(d, fc):
    t = tt(d)
    ir = rng.normal(0, 1, (len(t), 2)) * np.exp(-t * (6.9 / d))[:, None]
    ir[: int(0.012 * SR)] *= np.linspace(0, 1, int(0.012 * SR))[:, None]
    ir = lp(ir, fc)
    return ir / np.sqrt((ir ** 2).sum(axis=0)).max()


def reverb(x, ir):
    out = np.stack([signal.fftconvolve(x[:, c], ir[:, c])[:N] for c in range(2)], axis=1)
    return out


IR_L = make_ir(3.4, 5200)
send = pad * 0.5 + arp * 0.55 + bells * 1.0 + lead * 0.7 + fx * 0.45 + hp(drums, 500) * 0.12
wet = hp(reverb(send, IR_L), 180)

mix = (pad * 1.0 + arp * 0.95 + bass * 0.8 + drums * 0.85 + fx * 0.8 + bells * 0.8 + lead * 0.95 + wet * 0.5)

# dinámica general por sección (crece hasta el clímax)
tl = np.arange(N) / SR
pts_t = [0, 2.4, T_S2, T_S3, T_S4, T_S5, T_S6 - 0.01, T_S6, T_S7, DUR]
pts_g = [0.75, 0.85, 0.9, 0.95, 1.0, 0.92, 1.0, 1.12, 1.05, 1.0]
mix *= np.interp(tl, pts_t, pts_g)[:, None]

mix = hp(mix, 28)
# fade final
fo = int(1.6 * SR)
mix[-fo:] *= (np.linspace(1, 0, fo) ** 1.6)[:, None]
mix[: int(0.01 * SR)] *= np.linspace(0, 1, int(0.01 * SR))[:, None]

# limitador suave + normalización a -1 dBFS
mix = mix / np.percentile(np.abs(mix), 99.9) * 0.82
mix = np.tanh(mix * 1.15) / np.tanh(1.15)
mix = mix / np.abs(mix).max() * 0.89

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "music.wav")
wavfile.write(out, SR, (mix * 32767).astype(np.int16))
rms = lambda a, b: 20 * np.log10(np.sqrt((mix[int(a * SR):int(b * SR)] ** 2).mean()) + 1e-9)
print("ok", out, f"dur={N / SR:.2f}s peak={np.abs(mix).max():.2f}")
for a, b, n in [(0, 7.2, "S1"), (7.2, 12, "S2"), (12, 16.8, "S3"), (16.8, 21.6, "S4"), (21.6, 26.4, "S5"),
                (26.4, 34.8, "S6"), (34.8, 43.2, "S7")]:
    print(n, f"{rms(a, b):.1f} dBFS RMS")
