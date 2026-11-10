# ESTILO — Qué es un reel "Aura"

> Definido con Gonzalo el 2026-11-10. Este documento manda sobre cualquier decisión estética.
> Si algo no está acá, consultar `marca/brand-guidelines.md`.

## La idea en una frase

**Sobrio con impacto.** Se ve como un estudio de arquitectura, pero engancha en los primeros 2 segundos.
La marca es *premium, cálida, arquitectónica y sobria* (lujo silencioso). Nada de estética "influencer de tecnología".

## Lo que NO queremos (por qué falló el intento anterior)

- Estilo genérico de editor automático: subtítulos gigantes amarillos, emojis, efectos de sonido "whoosh" en cada corte, zooms constantes.
- Colores saturados, flechas, stickers, transiciones llamativas.
- Que parezca hecho por una app y no por una marca.

## Referencias (Instagram)

| Cuenta | Qué tomar | Qué NO tomar |
|---|---|---|
| **@nettcontrol** (MX, integrador de lujo) | **El formato base.** Dueño hablando en obra, señalando lo que explica. Subtítulo en mayúsculas blanco, abajo, con **una palabra clave resaltada en color cálido** ("Fueron las cámaras **AVIGILON**"). | Sus ganchos son flojos (≈500 vistas): mejorar el arranque. |
| **@smarthome.ar** (CABA) | **Plantilla "Terminado".** Tomas lentas, tipografía fina en mayúsculas, una frase centrada ("CORTINAS AUTOMATIZADAS", "UNA CASA QUE SE ADAPTA A VOS"). 100k+ vistas. | — |
| **@normotica** (AR) | **Ideas de ganchos y temas** ("El pronóstico te miente, tu jardín no", "Domótica vs. fiaca", rankings). | El look: demasiado llamativo (flechas, naranja saturado, textos enormes). |

## Paleta para video (de la marca)

| Uso | Color |
|---|---|
| Texto principal subtítulos | `#FFFFFF` |
| **Palabra clave resaltada** | `#C6AC8F` (aura-tan) — el único acento |
| Fondo placas / cierre | `#0A0908` (aura-black) |
| Texto secundario en placas | `rgba(255,255,255,.55)` |
| Etiquetas chicas (eyebrow) | `rgba(198,172,143,.6)` mayúsculas, tracking amplio |
| Alternativa placa clara (con moderación) | `#EAE0D5` cream con texto `#0A0908` |

Nunca usar colores fuera de esta paleta en textos o gráficos.

## Tipografía

- **Manrope** (Google Fonts). Titulares/ganchos: peso 200–300, grande, tracking negativo leve (-0.02em).
- Subtítulos: Manrope 600, MAYÚSCULAS, 52–60 px sobre 1080 de ancho, sombra suave (no contorno grueso).
- Etiquetas/eyebrows: Manrope 500, mayúsculas, 22–26 px, letter-spacing .2em.
- Contraste por **tamaño**, no por peso (regla de la marca).

## Dos plantillas

### Plantilla A — "OBRA" (estilo C, la principal)
Gonzalo hablando a cámara en obra: avance, explicación de lo que se está instalando.

- **0–2 s — Gancho:** frase corta en pantalla (Manrope 300, grande, parte superior-central), sobre el video. Una palabra en tan. Debe generar curiosidad o tensión. Ej: *"Esta casa no va a tener ni una llave de luz común"*.
- **Eyebrow fijo arriba (sutil):** `OBRA · CASA JS · CHAJARÍ` en tan .6, chico. Da contexto y marca serie.
- **Subtítulos:** 2–4 palabras por bloque, aparecen sincronizados palabra a palabra (sin rebote, fade/slide corto de 80–120 ms). 1 palabra clave por frase en tan (marcas, números, beneficios: "SOPHIA", "60 DEPARTAMENTOS", "DESDE EL CELULAR").
- **Ritmo:** cortar silencios > 0,35 s y muletillas ("eh", "este", repeticiones, arranques fallidos). Dejar respirar 0,1–0,15 s entre frases.
- **Movimiento:** zoom-in lento (punch-in 1.00→1.08) solo en momentos de énfasis, máx. 1 cada 6–8 s. Nada de sacudidas.
- **Placas de sección (opcional):** fondo negro 0,8 s con texto fino: *"Así empezó"* / *"Así quedó"*.
- **Color:** corrección cálida suave, contraste levemente subido, negros profundos. Look consistente entre reels.
- **Audio:** voz limpia y adelante (-14 LUFS integrado). Música ambiente muy baja (-28 a -32 dB bajo la voz, con ducking).
- **Cierre (2–3 s):** placa negra `#0A0908`, isotipo dorado centrado, "Aura Hogar" Manrope 300, y debajo CTA en tan: *"Escribinos antes de cerrar las paredes"* (o CTA del guion).

### Plantilla B — "TERMINADO"
Proyecto terminado, recorrido de la casa. Con o sin Gonzalo.

- Ritmo lento, cinematográfico. Tomas de 2–4 s.
- Sin subtítulos palabra a palabra: **una frase por escena**, centrada, Manrope 200–300 mayúsculas, tracking amplio (estilo @smarthome.ar).
- Si Gonzalo habla, subtítulos sobrios como Plantilla A pero más chicos.
- Música ambiente más protagonista; si hay voz, ducking.
- Mismo cierre que la Plantilla A.

## Duración
Depende del video. Guía: avance de obra 30–60 s; terminado 20–45 s. Nunca alargar artificialmente: si el contenido da 25 s, son 25 s.

## Tono de textos en pantalla
Español rioplatense ("vos"), directo, seguro, aspiracional. Vende estilo de vida y tranquilidad, no especificaciones técnicas.
Ver `contexto/ganchos_y_promesas_reels.md` y `contexto/aura-hogar-marca.md`.

## Regla de oro de autenticidad
Las obras son reales y eso es lo que vende. **Nunca** generar con IA imágenes de instalaciones que no hizo Aura ni presentarlas como propias. IA solo para limpieza, edición y gráficos.
