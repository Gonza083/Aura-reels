# PLAN — Reels automáticos de Aura Hogar

> Armado el 2026-11-10 en la notebook. **Se ejecuta en la PC de escritorio** (más potente).
> Objetivo: Gonzalo deja un video en `entrada/`, dice "procesá el video", y recibe en `salida/` un reel profesional con el estilo de `ESTILO.md`.

---

## ★ FASE 1 (EMPEZAR ACÁ) — Probar Video Editor Architect antes de construir

> Decisión de Gonzalo, 2026-11-10: **antes de construir desde cero, probar [Video Editor Architect](https://github.com/Hainrixz/video-editor-architect)** (MIT, de @soyenriquerocha) y entrenarlo con el estilo de Aura. Usa las mismas piezas que este plan (Claude dirige, whisper.cpp transcribe, Remotion renderiza), funciona en Windows y en español, entrena estilos a partir de creadores de referencia y aprende de las correcciones (`/ajustar`).
> **Las secciones 1–7 de este plan pasan a ser el Plan B** (construir propio) si la Fase 1 no convence. ESTILO.md, marca/, contexto/, obras/ y la parte de Drive (§2b) valen para los dos caminos.

### Pasos

1. **Setup** (ver también §0): Node.js **24+**, Git, Claude Code actualizado, Google Drive para escritorio.
2. **Clonar al lado de este repo** (no adentro):
   ```
   cd ..
   git clone https://github.com/Hainrixz/video-editor-architect.git aura-editor
   cd aura-editor
   npm ci
   npm run instalar            # muestra qué falta
   npm run instalar -- --si    # lo instala (ffmpeg, whisper.cpp, uv/Python, yt-dlp, Chromium, fuentes)
   npx tsx herramientas/doctor.ts
   claude
   ```
   Luego `/empezar`. Idioma: español. Nombre: Gonzalo.
3. **Entrenar el estilo "aura-obra"** con `/entrenar-estilo` usando como referencia:
   - **@nettcontrol** → formato base (hablando en obra, subtítulo mayúsculas con palabra clave resaltada).
   - **@smarthome.ar** → sobriedad y tipografía fina (sobre todo para el estilo "aura-terminado").
   - NO usar @normotica para el look (solo sirve para ideas de ganchos).
4. **Ajustar el perfil a la marca** antes de aprobarlo. Pasarle a Claude `../Aura-reels/ESTILO.md` y `../Aura-reels/marca/` y pedir que el perfil respete:
   - Tipografía **Manrope**; subtítulos blancos; **un solo acento: tan `#C6AC8F`**; fondos de placa `#0A0908`.
   - **Sin stickers, memes ni efectos de sonido** (o casi ninguno); sin colores saturados; zooms solo de énfasis.
   - Cierre con isotipo (`../Aura-reels/marca/logos/isotipo-dorado.png`) + CTA. Cargar el logo con `/stickers`.
   - Todo lo de "Lo que NO queremos" de ESTILO.md va a la sección "lo que nunca va" del perfil.
5. **Primer reel de prueba:** copiar un video de `G:/Mi unidad/Reels/entrada` a la carpeta de crudos del editor y pedir `/editar`. Iterar con `/ajustar` hasta que Gonzalo diga que le gusta.
6. **Opcionales que cuestan plata** (Apify, Gemini): **decir que no** salvo que Gonzalo lo pida explícitamente.
7. **Anotar todo** en `../Aura-reels/NOTAS-EJECUCION.md`: qué funcionó, qué no, ajustes hechos al perfil.

### Cómo decidir (al final de la noche)
| Resultado | Siguiente paso |
|---|---|
| El reel le gusta o está cerca | Seguir con Video Editor Architect. Guardar el editor con sus estilos en un **repo privado** propio (ej. `Gonza083/aura-editor`) y sumar el flujo de Drive (§2b) |
| Le gusta el motor pero no se logra el look | Ajustar el perfil / plantillas de Remotion del editor |
| No convence | Pasar al Plan B (secciones 1–7) reutilizando lo aprendido |

### Licencia de Remotion
Remotion es gratis para empresas de **hasta 3 personas**. Aura tiene 2 socios fijos (el resto son subcontratados), así que probablemente aplique la versión gratuita. **Confirmar en https://www.remotion.dev/docs/license/faq antes del uso regular.** Si no aplicara: licencia de empresa (mín. US$ 100/mes) o pasar el render a ffmpeg.

---

## 0. Antes de empezar (en la PC de escritorio)

1. **Revisar el intento anterior.** En esa PC ya se trabajó con DaVinci Resolve. Buscar la carpeta/scripts y anotar en `NOTAS-EJECUCION.md`:
   - qué se hizo, qué funcionó (ej. limpieza de audio, transcripción), qué se puede reutilizar.
   - El resultado no convenció por el **estilo** → no reutilizar plantillas visuales de ahí.
2. **Verificar herramientas** (instalar las que falten):
   - `git`, **Node.js 20+**, **Python 3.11+**, **ffmpeg** (con ffprobe) en el PATH.
   - Placa de video: `nvidia-smi`. Si hay NVIDIA → Whisper en GPU (CUDA). Si no → CPU con modelo `medium`.
3. Crear `.venv` de Python e instalar dependencias (ver sección 3).
4. **Google Drive para escritorio** instalado y con sesión iniciada (ver sección 2b). Anotar la letra de unidad (ej. `G:\`) en `config.json`.

---

## 1. Decisión de arquitectura

**Python + ffmpeg + faster-whisper + Remotion, orquestado por Claude Code.**

| Pieza | Para qué | Por qué esta y no otra |
|---|---|---|
| **ffmpeg** | Normalizar video, limpiar audio, cortar, mezclar música, color | Estándar, gratis, rápido |
| **faster-whisper** (large-v3 en GPU) | Transcripción con tiempos **por palabra** | Necesario para cortar silencios/muletillas y animar subtítulos palabra a palabra |
| **Claude Code** (la propia sesión) | Leer la transcripción y decidir: gancho, cortes, palabras clave, textos, música | Sin API key ni costos extra; Gonzalo ya usa Claude Code. Más adelante se puede pasar a la API si quiere 100% desatendido |
| **Remotion** (React → video) | Render final: subtítulos animados, gancho, eyebrow, zooms, placas, cierre | Control total del diseño con código → se logra el look sobrio de marca. DaVinci por script es duro y la API externa requiere Studio (pago) |
| DaVinci Resolve | **Opcional**, retoque manual si alguna vez hace falta | No es parte del flujo automático |

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
   ├─3 TRANSCRIPCIÓN  faster-whisper, idioma "es", word_timestamps=True → trabajo/<id>/transcripcion.json
   │
   ├─4 PLAN DE EDICIÓN  Claude lee transcripción + ESTILO.md + contexto/ + obras/ y escribe
   │                    trabajo/<id>/plan.json  (estructura en sección 4) y un resumen corto:
   │                    "Plantilla OBRA · 42 s · Gancho: '...' · corta 0:12–0:19 (repite) · cierre: ..."
   │
   ├─5 APROBACIÓN     Gonzalo lee el resumen (30 s) → "dale" o correcciones. (Se puede saltar con --auto)
   │
   ├─6 CORTE          ffmpeg aplica los segmentos del plan → video_cortado.mp4 + color (LUT/eq cálido)
   │                  Recalcular tiempos de palabras sobre el video cortado.
   │
   ├─7 RENDER         Remotion: composición ReelObra o ReelTerminado con props = plan.json
   │                  (subtítulos, gancho, eyebrow, zooms, placas, cierre, música con ducking)
   │
   └─8 SALIDA         salida/2026-11-12_obra-js_reel.mp4  (H.264, 1080x1920, 30fps, AAC 48k)
                      salida/2026-11-12_obra-js_portada.jpg  (frame del gancho)
                      salida/2026-11-12_obra-js_copy.txt  (texto para la publicación + hashtags)
```

**Comando objetivo:** `python reel.py [video] [--tipo obra|terminado] [--auto]`
(sin `video` procesa todo lo nuevo de la carpeta de entrada) y en Claude Code simplemente: *"procesá los videos de entrada"*.

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
├── config.example.json               ← rutas de ejemplo (config.json real no va a git)
├── marca/ contexto/ obras/ referencias/ ← info de Aura (ya existe)
├── entrada/   salida/   trabajo/      ← NO van a git (videos)
├── musica/                            ← pistas libres de derechos + musica.json (tags: mood, bpm)
├── pipeline/                          ← Python
│   ├── reel.py            orquestador (pasos 1–8)
│   ├── ingesta.py         normalizar video
│   ├── audio.py           limpieza + loudnorm
│   ├── transcribir.py     faster-whisper
│   ├── cortar.py          aplicar segmentos + remapear tiempos
│   ├── color.py           look cálido consistente
│   └── requirements.txt   faster-whisper, ffmpeg-python, pydantic
└── render/                            ← Remotion (Node)
    ├── src/
    │   ├── ReelObra.tsx         plantilla A
    │   ├── ReelTerminado.tsx    plantilla B
    │   ├── componentes/  Subtitulos.tsx, Gancho.tsx, Eyebrow.tsx, PlacaSeccion.tsx,
    │   │                 Cierre.tsx, ZoomEnfasis.tsx
    │   └── tema.ts              colores y tipografías de marca (de marca/tokens.json)
    └── public/  isotipo-dorado.png, fuentes Manrope
```

---

## 4. Formato de `plan.json` (contrato entre Claude y Remotion)

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
| **H1** | Setup + revisión del intento con DaVinci | Herramientas verificadas, notas del intento anterior escritas |
| **H2** | Audio + transcripción | Un video real sale con voz limpia y `transcripcion.json` con tiempos por palabra correctos |
| **H3** | **Plantilla visual en Remotion (lo más importante)** | Render de 10 s con subtítulos, gancho, eyebrow y cierre. **Gonzalo aprueba el look** comparando con @nettcontrol / @smarthome.ar. Iterar acá hasta que le guste: tamaños, tipografía, animación, posición |
| **H4** | Plan de edición por Claude | Con un video real, Claude genera `plan.json` + resumen razonable (buen gancho, cortes correctos) |
| **H5** | Punta a punta + Drive | Video subido a `Drive/Reels/entrada` → reel completo en `Drive/Reels/salida` |
| **H6** | Plantilla Terminado + música | Segundo formato funcionando; biblioteca de 6–10 pistas con tags |
| **H7** | Ajuste fino | 3 reels reales procesados, ajustes de estilo anotados en ESTILO.md |

> Prioridad: **H3 antes que automatizar todo.** El intento anterior falló por estilo, no por técnica.

---

## 6. Música

- Fuentes libres de derechos y aptas para Instagram: YouTube Audio Library, Pixabay Music (verificar licencia de cada pista).
- Estilo: ambient cálido, piano/electrónica suave, sin voces. 6–10 pistas con `musica/musica.json` (`archivo, mood, bpm, energia`).
- Claude elige la pista según el tono del video. Ducking automático bajo la voz (sidechaincompress en ffmpeg o volumen por segmento en Remotion).
- Alternativa: no poner música y agregar audio en tendencia desde la app de Instagram al publicar (decidir con Gonzalo).

---

## 7. Riesgos y cómo manejarlos

| Riesgo | Mitigación |
|---|---|
| Ruido de obra (viento, amoladora, eco) | Probar afftdn vs DeepFilterNet con un video real; si el audio es muy malo, avisar en vez de empeorarlo |
| Whisper confunde marcas (Sophia, Hikvision, Omada) | Pasar `initial_prompt` con vocabulario: "Aura Hogar, Sophia, Hikvision, Omada, TP-Link, World Leds Go, Full Lock, Chajarí, domótica" |
| Video horizontal o con el sujeto descentrado | Recorte con detección de cara (mediapipe) o fondo desenfocado |
| Logo solo en PNG 503 px | Alcanza para el cierre (≈220 px). A futuro conseguir versión vectorial |
| Render lento | Remotion con `--concurrency` según núcleos; render en la PC potente |
| Resultado "genérico" otra vez | H3 con aprobación explícita de Gonzalo antes de seguir |

---

## 8. Fuera de alcance (por ahora)
- Publicar automáticamente en Instagram.
- Generar imágenes/video con IA (Higgsfield, etc.). Ver regla de autenticidad en ESTILO.md.
- Edición multicámara o videos largos de YouTube.
