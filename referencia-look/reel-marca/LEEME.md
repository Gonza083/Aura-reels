# Reel de marca — referencia de look

Reel publicitario de Aura Hogar (43,2 s, 1080×1920) hecho con Hyperframes 0.9.39 el 2026-11-12. **Gonzalo aprobó cómo se ve.** Es la referencia visual para las plantillas de `render/`: no editarlo, copiar de acá.

## Qué reutilizar
- `index.html` — estilos de texto compartidos (clases `ah-hl`, `ah-lede`, `ah-mono`, `ah-num`), grano y viñeta.
- `compositions/s7.html` — cierre con isotipo dorado, destello y textos.
- `compositions/s3.html` — etiqueta + número que cuenta, sobre imagen.
- `assets/fonts/Manrope.ttf` — tipografía de marca.

## Para renderizarlo
```
python tools/make_music.py                      # genera assets/music.wav (no está en git)
npx hyperframes@0.9.39 check
npx hyperframes@0.9.39 render -q high -f 30 -o renders/prueba.mp4
```
Necesita FFmpeg y ffprobe en el PATH.

## Avisos
- `tools/prep_images.py` lee las fotos originales de una carpeta que solo existe en la notebook. No hace falta correrlo: las imágenes ya están en `assets/img/`.
- La música está generada por código y Gonzalo todavía no opinó sobre cómo suena.
- Tiene golpes de sonido en los cortes y un cierre largo: válido para un tráiler de marca, **no** para los reels de obra (ver `ESTILO.md`).
