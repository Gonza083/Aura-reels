# CLAUDE.md — aura-reels

Sistema para convertir videos de obra de **Aura Hogar** en reels profesionales para Instagram (@aurahogaroficial).
Dueño: **Gonzalo Díaz**, Chajarí, Entre Ríos. Todo en **español rioplatense** ("vos").

## Leer primero, en este orden
1. `ESTILO.md` — qué es un reel "Aura". Manda sobre cualquier decisión estética.
2. `PLAN.md` — **empezar por "Qué cambió" y "Esta noche" (hitos N1–N3)**. El render se hace con **Hyperframes** (no Remotion ni Video Editor Architect), hito por hito, mostrando resultados a Gonzalo en cada uno.
3. `NOTAS-EJECUCION.md` (si existe) — avances y decisiones tomadas durante la construcción.

## Contexto disponible
- `marca/` — guía de marca, colores (`tokens.json`), tipografía, logos, fotos de proyectos y de Sophia.
- `contexto/` — quién es Aura, tono, ganchos y guiones de reels ya escritos, plan de crecimiento, fichas de productos (Sophia, Hikvision, Omada).
- `obras/` — fichas de las obras (código, ubicación, qué se instaló). Usar para el eyebrow (`OBRA · CASA JS · CHAJARÍ`) y para textos correctos.
- `referencias/` — cuentas de Instagram de referencia y qué tomar de cada una.
- `referencia-look/reel-marca/` — reel de marca hecho con Hyperframes que Gonzalo aprobó el 2026-11-12. Es la referencia visual; no editarlo, copiar de ahí.

## Cómo trabajar con Gonzalo
- Pragmático: quiere resultados que se vean bien y le ahorren tiempo, no tecnología por la tecnología.
- El intento anterior (con DaVinci) no lo convenció **por el estilo** → priorizar el look (hito N3) y pedir su aprobación antes de automatizar todo.
- Explicar en simple, sin jerga. Mostrar el resultado (render corto) en vez de describirlo.
- Las obras son reales: nunca inventar instalaciones ni generar imágenes de obras con IA.

## Cuando el sistema ya funciona
Ante "procesá el video" / "procesá los videos de entrada":
1. Correr pasos 1–3 del pipeline (ingesta, audio, transcripción).
2. Escribir `plan.json` siguiendo ESTILO.md (gancho fuerte, cortes de silencios/muletillas, palabras clave en tan, plantilla correcta).
3. Mostrar el resumen corto y esperar el "dale" (salvo que pida `--auto`).
4. Renderizar y entregar reel + portada + copy en `salida/`.

## Videos: vienen de Google Drive
Las carpetas de entrada y salida reales están en Google Drive (montado con Drive para escritorio), definidas en `config.json`. Copiar siempre a `trabajo/` local antes de procesar y **nunca borrar originales de Drive**. Detalle en PLAN.md § 2b.

## Git
Videos (`entrada/`, `salida/`, `trabajo/`), `config.json`, `node_modules/` y `.venv/` no se suben. Repo privado.
