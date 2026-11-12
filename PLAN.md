# PLAN — Reels automáticos de Aura Hogar

> Armado el 2026-11-10 en la notebook. **Actualizado el 2026-11-12: el render pasa de Remotion a Hyperframes** (ver "Qué cambió").
> **Se ejecuta en la PC de escritorio** (más potente). La notebook tiene 7,7 GB de RAM y no alcanza para video 4K + transcripción.
> Objetivo: Gonzalo deja un video en `entrada/`, dice "procesá el video", y recibe en `salida/` un reel profesional con el estilo de `ESTILO.md`.

---

## Qué cambió el 2026-11-12 (leer primero)

**Decisión de Gonzalo:** se saltea la prueba de Video Editor Architect y se construye el sistema propio, usando **Hyperframes** para el render en lugar de Remotion.

**Por qué:**
- El 2026-11-12 se hizo en la notebook un reel de marca de 43 s con Hyperframes (HTML + CSS + GSAP → MP4) y **a Gonzalo le gustó el look**. El intento anterior con DaVinci había fallado por estilo, no por técnica: el estilo era el riesgo principal y ya está resuelto en esta herramienta.
- Ese reel está copiado en `referencia-look/reel-marca/` y es la **referencia visual aprobada**: tipografías, tamaños, colores, animación de textos y el cierre con isotipo salen de ahí.
- Se evita la duda de licencia de Remotion (gratis solo hasta 3 personas).

**Qué sigue igual:** `ESTILO.md` (manda sobre lo estético), `marca/`, `contexto/`, `obras/`, el flujo de Drive (§2b), el formato de `plan.json` (§4) y todos los pasos de FFmpeg.

**Qué NO se probó todavía (verificar esta noche, no dar por hecho):**
- Hyperframes con **video filmado** adentro (el reel de referencia usa solo fotos).
- La transcripción de Hyperframes (`hyperframes transcribe`) con audio de obra en español. Si no anda bien, usar faster-whisper (§1).
- Subtítulos palabra por palabra en Hyperframes.

---

## ★ Esta noche — alcance realista

No es el sistema completo. Son tres hitos, en orden, mostrando el resultado a Gonzalo en cada uno:

| # | Hito | Listo cuando… |
|---|---|---|
| **N1** | Setup en la PC de escritorio | `npx hyperframes doctor` muestra FFmpeg, FFprobe, Chrome y el transcriptor en verde |
| **N2** | Audio + transcripción | Un video real de `Drive/Reels/entrada` sale con voz limpia y `transcripcion.json` con tiempos **por palabra** correctos |
| **N3** | **Plantilla "Obra" (lo más importante)** | Render de 10–15 s con gancho, eyebrow, subtítulos y cierre. **Gonzalo aprueba el look.** Iterar acá hasta que le guste |

Recién con N3 aprobado se sigue con los hitos H4–H7 (§5).

**Antes de arrancar, Gonzalo tiene que dejar al menos un video real hablando en obra en `Drive/Reels/entrada`.** Si no hay ninguno, pedírselo; no inventar material ni usar video generado.

### N1 — Setup (PC de escritorio, Windows)

1. Verificar e instalar lo que falte:
   - `git`, **Node.js 22 o superior** (`node -v`), **Python 3.11+**.
   - **FFmpeg con ffprobe en el PATH:** `winget install --id Gyan.FFmpeg -e --accept-source-agreements --accept-package-agreements` y abrir una terminal nueva.
   - **Google Chrome** (Hyperframes lo usa para capturar los cuadros).
   - **Google Drive para escritorio** con sesión iniciada (§2b). Anotar la letra de unidad en `config.json`.
   - Placa de video: `nvidia-smi`. Anotar si hay NVIDIA.
2. Hyperframes. La versión probada es **0.9.39**; fijar esa para que el resultado sea igual al de la notebook:
   ```
   npx -y hyperframes@0.9.39 telemetry disable
   npx -y hyperframes@0.9.39 doctor
   ```
   `doctor` dice qué falta y con qué comando se instala. Si no encuentra FFmpeg aunque esté instalado, definir `HYPERFRAMES_FFMPEG_PATH` y `HYPERFRAMES_FFPROBE_PATH` con la ruta a cada `.exe`.
3. Transcriptor: `doctor` marca `whisper-cpp` como faltante y muestra cómo instalarlo (o bajar `whisper-bin-x64.zip` de las releases de whisper.cpp y definir `HYPERFRAMES_WHISPER_PATH` apuntando a `whisper-cli.exe`). Ver `npx hyperframes docs transcribe`.
4. **Leer las guías de Hyperframes antes de escribir una sola escena.** Vienen dentro del paquete, en la carpeta `dist/skills/` (buscarla en la caché de npx o en `node_modules/hyperframes/`):
   - `hyperframes/SKILL.md` — el contrato de render (obligatorio).
   - `hyperframes/references/format.md`, `motion.md`, `captions.md`, `types/vertical.md`.
   - `media-use/references/media-treatments.md` — cómo corregir color y tratar video filmado.
5. Probar que el entorno renderiza, con la referencia:
   ```
   cd referencia-look/reel-marca
   python tools/make_music.py        # regenera assets/music.wav (no va a git)
   npx hyperframes@0.9.39 check
   npx hyperframes@0.9.39 render -q high -f 30 -o renders/prueba.mp4
   ```
   Tiene que salir un MP4 de 43,2 s igual al aprobado. Si esto falla, arreglarlo antes de seguir.
6. Anotar todo en `NOTAS-EJECUCION.md`: qué se instaló, qué falló, qué quedó pendiente.

### N2 — Audio y transcripción

Con un video real copiado a `trabajo/<id>/` (nunca trabajar sobre el archivo de Drive, §2b):
1. Ingesta y audio según §2 pasos 1–2.
2. Transcripción con tiempos por palabra. Probar primero `npx hyperframes transcribe` (idioma `es`). Revisar a mano 20–30 s: que las palabras coincidan y que escriba bien Sophia, Hikvision, Omada, Chajarí. Si confunde marcas o los tiempos están corridos, pasar a **faster-whisper** (`large-v3` con GPU, `medium` en CPU, `word_timestamps=True`, `initial_prompt` con el vocabulario de §7).
3. Mostrarle a Gonzalo el audio limpio contra el original y un tramo de la transcripción.

### N3 — Plantilla "Obra"

Crear el proyecto de render en `render/` (§3) y construir la plantilla A de `ESTILO.md` sobre 10–15 s del video real:
- Tomar de `referencia-look/reel-marca/` los estilos de texto (`index.html`, clases `ah-*`), la fuente (`assets/fonts/Manrope.ttf`) y la escena de cierre (`compositions/s7.html`).
- **Lo que cambia respecto de la referencia**, porque `ESTILO.md` manda:
  - Subtítulos: Manrope 600, MAYÚSCULAS, 52–60 px, 2–4 palabras por bloque, palabra por palabra con fade corto (80–120 ms), una palabra clave en tan.
  - **Sin golpes ni subidas de sonido en los cortes.** El reel de referencia los tiene porque es un tráiler de marca; los reels de obra no.
  - Zooms solo de énfasis, máximo uno cada 6–8 s.
  - Cierre de 2–3 s, no de 8.
- Zona segura de Instagram en 1080×1920: nada de texto en los 168 px de arriba; todo lo que se lee entre 168 y 1330 px; abajo de 1330 solo imagen.
- Mirar cuadros antes de renderizar (`npx hyperframes snapshot --at 1,3,5`) y mostrarle a Gonzalo el MP4, no una descripción.

---

## 0. Antes de empezar (en la PC de escritorio)

1. **Revisar el intento anterior.** En esa PC ya se trabajó con DaVinci Resolve. Buscar la carpeta/scripts y anotar en `NOTAS-EJECUCION.md` qué funcionó (ej. limpieza de audio, transcripción) y qué se puede reutilizar. El resultado no convenció por el **estilo** → no reutilizar plantillas visuales de ahí.
2. Setup: ver N1.
3. Crear `.venv` de Python e instalar dependencias (§3).

---

## 1. Decisión de arquitectura

**Python + FFmpeg + transcripción por palabra + Hyperframes, orquestado por Claude Code.**

| Pieza | Para qué | Por qué esta y no otra |
|---|---|---|
| **FFmpeg** | Normalizar video, limpiar audio, cortar, mezclar música | Estándar, gratis, rápido. Además Hyperframes lo necesita para armar el MP4 |
| **Transcripción** (`hyperframes transcribe` o faster-whisper) | Tiempos **por palabra** | Necesario para cortar silencios y muletillas y para animar subtítulos |
| **Claude Code** (la propia sesión) | Leer la transcripción y decidir: gancho, cortes, palabras clave, textos, música | Sin API key ni costos extra |
| **Hyperframes** (HTML → video) | Render final: subtítulos, gancho, eyebrow, zooms, placas, cierre | Look ya aprobado por Gonzalo (2026-11-12). Control total del diseño con código |
| DaVinci Resolve | **Opcional**, retoque manual | No es parte del flujo automático |

Descartados: **Remotion** (mismo trabajo que Hyperframes, con duda de licencia) y **Video Editor Architect** (usa Remotion; no se llegó a probar).

### Reglas de Hyperframes que rompen el render si se ignoran
Resumen del contrato (`SKILL.md` tiene el detalle; `npx hyperframes check` avisa la mayoría):
- `index.html` monta una escena por archivo de `compositions/`. Cada escena va entera dentro de `<template>`, con su raíz `#root`, y registra **una** línea de tiempo pausada: `window.__timelines["<id>"] = tl`. El id del host, el de la escena y la clave de la línea de tiempo tienen que ser el mismo.
- Todo elemento con tiempo lleva `class="clip"`, `data-start` y `data-duration`.
- Nada de `Date.now()`, `Math.random()`, timers ni `repeat: -1`: todo lo visible depende solo del tiempo.
- Usar `fromTo`, no `from`. Si dos animaciones tocan la misma propiedad del mismo elemento, la segunda lleva `immediateRender: false`.
- **Video filmado:** el tiempo va en el `<video>`, no en un contenedor. Con sonido propio: `data-has-audio="true"`; sin sonido: `muted`. La música y la voz aparte van en un `<audio>` con `id`.
- Zoom o paneo de un video: animar un contenedor adentro del clip, no el `<video>`.
- Color, grano y viñeta sobre video filmado: con `npx hyperframes media-treatment`, no con filtros CSS.
- Fuentes que no vienen incluidas (Manrope) necesitan `@font-face` apuntando a `assets/fonts/`.
- Con poca memoria, renderizar con `-w 2`. En la PC de escritorio dejar que elija solo.

---

## 2. El flujo

```
entrada/2026-11-12_obra-js.mp4
   │
   ├─1 INGESTA        ffprobe → orientación, fps, duración. Normaliza a 1080x1920 @30fps.
   │                  Si es horizontal: recorte centrado (o fondo desenfocado si no entra el sujeto).
   │
   ├─2 AUDIO          ffmpeg: highpass 80Hz → reducción de ruido (afftdn; evaluar DeepFilterNet si
   │                  queda mejor con viento/eco de obra) → compresor suave → loudnorm -14 LUFS.
   │
   ├─3 TRANSCRIPCIÓN  idioma "es", tiempos por palabra → trabajo/<id>/transcripcion.json
   │
   ├─4 PLAN DE EDICIÓN  Claude lee transcripción + ESTILO.md + contexto/ + obras/ y escribe
   │                    trabajo/<id>/plan.json  (estructura en §4) y un resumen corto:
   │                    "Plantilla OBRA · 42 s · Gancho: '...' · corta 0:12–0:19 (repite) · cierre: ..."
   │
   ├─5 APROBACIÓN     Gonzalo lee el resumen (30 s) → "dale" o correcciones. (Se puede saltar con --auto)
   │
   ├─6 CORTE          ffmpeg aplica los segmentos del plan → video_cortado.mp4
   │                  Recalcular tiempos de palabras sobre el video cortado.
   │
   ├─7 RENDER         Hyperframes: plantilla Obra o Terminado, con los datos de plan.json
   │                  (subtítulos, gancho, eyebrow, zooms, placas, cierre, música con ducking)
   │
   └─8 SALIDA         salida/2026-11-12_obra-js_reel.mp4  (H.264, 1080x1920, 30fps, AAC 48k)
                      salida/2026-11-12_obra-js_portada.jpg  (frame del gancho)
                      salida/2026-11-12_obra-js_copy.txt  (texto para la publicación + hashtags)
```

**Comando objetivo:** `python reel.py [video] [--tipo obra|terminado] [--auto]`
(sin `video` procesa todo lo nuevo de la carpeta de entrada) y en Claude Code simplemente: *"procesá los videos de entrada"*.

**Cómo llegan los datos del plan a Hyperframes:** el paso 7 genera el proyecto de ese reel a partir de la plantilla (copia la plantilla a `trabajo/<id>/render/`, escribe los subtítulos y textos en el HTML, y renderiza). Los elementos con tiempo tienen que quedar escritos en el HTML, no creados por script en el navegador.

---

## 2b. Videos desde Google Drive

Los videos de Gonzalo están en Google Drive. **No se descargan a mano ni se suben a git**: se usa **Google Drive para escritorio**, que monta el Drive como una unidad (ej. `G:\Mi unidad\`).

```
📱 Graba en obra → sube a Drive/Reels/entrada (desde el celular)
💻 PC escritorio ve  G:\Mi unidad\Reels\entrada
     → reel.py COPIA el video a trabajo/<id>/ (disco local, rápido) y procesa ahí
     → deja el resultado en G:\Mi unidad\Reels\salida
📱 El reel aparece en el Drive del celular → lo sube a Instagram
```

**`config.json`** (en la raíz, NO va a git porque cambia en cada PC; versionar `config.example.json`):
```json
{
  "carpeta_entrada": "G:/Mi unidad/Reels/entrada",
  "carpeta_salida":  "G:/Mi unidad/Reels/salida",
  "carpeta_trabajo": "trabajo",
  "mover_procesados_a": "G:/Mi unidad/Reels/entrada/procesados"
}
```
Si no existe `config.json`, usar las carpetas locales `entrada/` y `salida/` del proyecto (sirve para pruebas).

**Reglas:**
- **Nunca procesar directo sobre el archivo de Drive**: primero copiar a `trabajo/` (local). Evita lentitud y archivos a medio sincronizar.
- Antes de copiar, esperar a que el archivo esté completo (tamaño estable durante unos segundos) por si todavía se está subiendo.
- **Nunca borrar originales de Drive.** Al terminar, mover el original a `entrada/procesados/` (o registrar en `trabajo/procesados.json`) para no procesarlo dos veces.
- Videos de celular en 4K pueden pesar varios GB: mostrar progreso de la copia.
- Limpiar `trabajo/<id>/` después de entregar (dejar solo `plan.json` y `transcripcion.json` por si hay que re-renderizar).
- Los reels finales pesan poco (20–50 MB): van a Drive sin problema.

**Videos viejos:** Gonzalo tiene muchos videos ya en Drive. Se pueden mover de a poco a `Reels/entrada` para procesarlos; no hace falta procesar todo de una.

---

## 3. Estructura del proyecto a construir

```
aura-reels/
├── CLAUDE.md, PLAN.md, ESTILO.md     ← documentación (ya existe)
├── NOTAS-EJECUCION.md                ← se crea al ejecutar: avances y decisiones
├── config.example.json               ← rutas de ejemplo (config.json real no va a git)
├── marca/ contexto/ obras/ referencias/ ← info de Aura (ya existe)
├── referencia-look/reel-marca/       ← reel de marca aprobado el 2026-11-12 (ya existe). NO editar: es la referencia
├── entrada/   salida/   trabajo/      ← NO van a git (videos)
├── musica/                            ← pistas libres de derechos + musica.json (tags: mood, bpm)
├── pipeline/                          ← Python
│   ├── reel.py            orquestador (pasos 1–8)
│   ├── ingesta.py         normalizar video
│   ├── audio.py           limpieza + loudnorm
│   ├── transcribir.py     tiempos por palabra
│   ├── cortar.py          aplicar segmentos + remapear tiempos
│   ├── armar_render.py    plan.json → proyecto Hyperframes del reel
│   └── requirements.txt
└── render/                            ← plantillas Hyperframes
    ├── obra/              plantilla A: index.html + compositions/ (gancho, cuerpo con subtítulos, cierre)
    ├── terminado/         plantilla B
    └── assets/            fonts/Manrope.ttf, isotipo-dorado.png
```

---

## 4. Formato de `plan.json` (contrato entre Claude y el render)

```json
{
  "plantilla": "obra",
  "obra": { "codigo": "JS", "nombre": "Casa JS", "lugar": "Chajarí" },
  "eyebrow": "OBRA · CASA JS · CHAJARÍ",
  "gancho": { "texto": "Esta casa no va a tener ni una llave común", "resaltar": ["ni una llave"], "duracion": 2.2 },
  "segmentos": [ { "inicio": 0.42, "fin": 6.10 }, { "inicio": 7.30, "fin": 18.95 } ],
  "subtitulos": [
    { "palabras": [ {"t": "TODO", "i": 0.42, "f": 0.61}, {"t": "CONTROLADO", "i": 0.61, "f": 1.10} ],
      "resaltar": ["CONTROLADO"] }
  ],
  "zooms": [ { "en": 9.4, "duracion": 1.5, "escala": 1.08 } ],
  "placas": [ { "en": 0, "texto": "Así quedó" } ],
  "musica": { "pista": "ambient-calido-01.mp3", "volumen_db": -30, "ducking": true },
  "cierre": { "cta": "Escribinos antes de cerrar las paredes" },
  "copy": "Texto para la publicación…"
}
```
Validar con pydantic antes del render. Los tiempos de `subtitulos` y `zooms` son sobre el video **ya cortado**.

---

## 5. Hitos de ejecución (en orden — mostrar resultado a Gonzalo en cada uno)

| # | Hito | Listo cuando… |
|---|---|---|
| **N1–N3** | Ver "Esta noche" | Setup, audio + transcripción, y look de la plantilla Obra aprobado |
| **H4** | Plan de edición por Claude | Con un video real, Claude genera `plan.json` + resumen razonable (buen gancho, cortes correctos) |
| **H5** | Punta a punta + Drive | Video subido a `Drive/Reels/entrada` → reel completo en `Drive/Reels/salida` |
| **H6** | Plantilla Terminado + música | Segundo formato funcionando; biblioteca de 6–10 pistas con tags |
| **H7** | Ajuste fino | 3 reels reales procesados, ajustes de estilo anotados en ESTILO.md |
| **H8** | *(Opcional)* Prueba de voz generada | Gonzalo escuchó las muestras y decidió si sirve o no (§6b) |

> Prioridad: **N3 antes que automatizar todo.**

---

## 6. Música

- Fuentes libres de derechos y aptas para Instagram: YouTube Audio Library, Pixabay Music (verificar licencia de cada pista).
- Estilo: ambient cálido, piano/electrónica suave, sin voces. 6–10 pistas con `musica/musica.json` (`archivo, mood, bpm, energia`).
- Claude elige la pista según el tono del video. Ducking automático bajo la voz (sidechaincompress en ffmpeg o la curva de volumen de Hyperframes).
- Alternativa: no poner música y agregar audio en tendencia desde la app de Instagram al publicar (decidir con Gonzalo).
- La música del reel de referencia está generada por código (`referencia-look/reel-marca/tools/make_music.py`). Gonzalo todavía no opinó sobre cómo suena; no tomarla como estándar.

---

## 6b. Voz generada (herramienta opcional)

> Agregado el 2026-11-12 a pedido de Gonzalo. **No es parte del flujo automático ni de los hitos de esta noche.** Se prueba recién después de aprobar el look (N3).

**Para qué sí:** videos donde Gonzalo no aparece — plantilla "Terminado" (recorrido de una casa) o piezas de marca como el reel de referencia.
**Para qué no:** reels de obra. Ahí habla Gonzalo a cámara y esa voz real es lo que vende; nunca reemplazarla ni taparla.

**Prueba (hito H8, unos 10 minutos, sin costo):**
1. Instalar el generador de voz local de Hyperframes. `npx hyperframes doctor` muestra el comando (el 2026-11-12 era `pip install kokoro-onnx soundfile`). Ver `npx hyperframes tts --help`.
2. Generar la misma frase con cada voz disponible en español, por ejemplo: *"Un hogar que se adapta a vos."* y *"Escribinos antes de cerrar las paredes."*
3. Dejar las muestras en `trabajo/prueba-voz/` y que **Gonzalo las escuche y decida**. Claude no puede juzgar cómo suena.

**Qué no se sabe (no se probó):** cómo suena en español. Lo esperable es acento neutro o de España, no rioplatense; con textos en "vos" puede sonar raro.

**Según lo que decida Gonzalo:**
| Resultado | Siguiente paso |
|---|---|
| Alguna voz le gusta | Sumar a `plan.json` un campo opcional `voz` (texto por escena) y mezclarla con ducking de la música, solo en la plantilla "Terminado" |
| El acento no convence | Descartar. La voz la graba Gonzalo con el celular y se sincroniza |
| Quiere su propia voz generada | Evaluar la clonación de voz de Higgsfield. **Gasta créditos: consultar el costo y pedirle el OK antes de usarla** |

---

## 7. Riesgos y cómo manejarlos

| Riesgo | Mitigación |
|---|---|
| Ruido de obra (viento, amoladora, eco) | Probar afftdn vs DeepFilterNet con un video real; si el audio es muy malo, avisar en vez de empeorarlo |
| El transcriptor confunde marcas (Sophia, Hikvision, Omada) | Vocabulario de apoyo: "Aura Hogar, Sophia, Hikvision, Omada, TP-Link, World Leds Go, Full Lock, Chajarí, domótica" |
| Video horizontal o con el sujeto descentrado | Recorte con detección de cara (mediapipe) o fondo desenfocado |
| Logo solo en PNG 503 px | Alcanza para el cierre (≈360 px en la referencia). A futuro conseguir versión vectorial |
| Render lento con video 4K | Normalizar a 1080×1920 en la ingesta antes de entrar a Hyperframes |
| Hyperframes no rinde con video filmado o subtítulos por palabra | No está probado. Si falla: quemar subtítulos con FFmpeg (archivo ASS) y usar Hyperframes solo para gancho, placas y cierre |
| Fotos de obra con cartelería "SOUL" | No usarlas en piezas de Aura Hogar |
| Resultado "genérico" otra vez | N3 con aprobación explícita de Gonzalo antes de seguir |

---

## 8. Otras herramientas evaluadas

| Herramienta | Veredicto | Por qué |
|---|---|---|
| **Hyperframes** | ✅ Usar | Look aprobado el 2026-11-12 |
| **Video Editor Architect** ([repo](https://github.com/Hainrixz/video-editor-architect)) | ⏸ No se probó | Era la Fase 1 original. Queda como alternativa si el camino propio se complica |
| **Motion Architect** ([repo](https://github.com/Hainrixz/motion-architect)) | ❌ No | Solo Mac/Linux |
| **Creative Architect** ([repo](https://github.com/Hainrixz/creative-architect)) | ❌ No para reels de obra | Genera fotos/videos con IA; choca con la regla de autenticidad de ESTILO.md |

## 9. Fuera de alcance (por ahora)
- Publicar automáticamente en Instagram.
- Generar imágenes o video de obras con IA. Ver regla de autenticidad en ESTILO.md.
- Voz en off generada dentro del flujo automático. Queda como herramienta opcional a probar (§6b).
- Edición multicámara o videos largos de YouTube.
