# Aura Hogar — Logos

> **[CÓDIGO]** = verificado en el proyecto · **[INTERPRETACIÓN]** = lectura del diseño · **[RECOMENDACIÓN]** = sugerencia propia.

## Resumen

El proyecto tiene **un único logo de marca**: un **isotipo** (símbolo sin texto) formado por dos triángulos de contorno — uno grande con un corte en el lado derecho y uno más chico que se encastra en ese corte — que en conjunto sugieren una "A" / un techo / una montaña. **[INTERPRETACIÓN]**

- **No existe** un logotipo con el nombre "Aura Hogar" como archivo. En la web, el nombre se escribe como **texto vivo** al lado del isotipo.
- **No existen** versiones horizontal, vertical, blanca ni negra como archivos. **No existe** versión vectorial (SVG/AI/PDF) del logo.
- Existen **dos tratamientos de color** del mismo símbolo: dorado metalizado (logo usado en la web) y tan plano sobre blanco (favicons).

## Inventario

| Archivo (en brand-kit) | Formato | Dimensiones | Transparencia | Uso actual | Fondo recomendado | Ruta original |
| --- | --- | --- | --- | --- | --- | --- |
| `original/aura-logo-removebg-preview.png` | PNG RGBA | 503 × 496 px (símbolo útil ≈ 332 × 283 px) | **Sí** | **Logo principal.** Header (28×28, `border-radius:6`, `opacity:.92`) y footer (28×28, `rounded-sm`) de todas las páginas. | Oscuro (`#0A0908`). Así se usa en todo el sitio. | `public/icons/aura-logo-removebg-preview.png` |
| `favicon/favicon.ico` | ICO (16, 32 px, 32 bit) | 16 × 16 / 32 × 32 | Canal alfa presente, **fondo blanco opaco** | Existe pero **no está referenciado** en `<head>` | Claro | `public/icons/favicon.ico` |
| `favicon/favicon-16x16.png` | PNG | 16 × 16 | Fondo blanco opaco | `<link rel="icon" sizes="16x16">` | Claro | `public/icons/favicon-16x16.png` |
| `favicon/favicon-32x32.png` | PNG | 32 × 32 | Fondo blanco opaco | `<link rel="icon" sizes="32x32">` | Claro | `public/icons/favicon-32x32.png` |
| `favicon/apple-touch-icon.png` | PNG | 180 × 180 | Fondo blanco opaco | `<link rel="apple-touch-icon">` | Claro | `public/icons/apple-touch-icon.png` |
| `favicon/android-chrome-192x192.png` | PNG | 192 × 192 | Fondo blanco opaco | No referenciado (el `site.webmanifest` que lo usaría **no existe**) | Claro | `public/icons/android-chrome-192x192.png` |
| `favicon/android-chrome-512x512.png` | PNG | 512 × 512 | Fondo blanco opaco | Ídem | Claro | `public/icons/android-chrome-512x512.png` |

**Colores medidos en los archivos** [CÓDIGO — muestreo de píxeles]:
- Logo principal: gradiente dorado metalizado con brillos; tonos dominantes ≈ `#D8B888`, `#D0B080`, `#C8A870`, reflejos ≈ `#F8F0D0`.
- Favicons: símbolo tan plano `#DDB788` sobre blanco `#FFFFFF`.

## Estado de cada categoría

| Carpeta | Estado |
| --- | --- |
| `original/` | ✅ 1 archivo (logo principal / isotipo dorado). |
| `isotipo/` | El logo principal **es** el isotipo. No se duplicó el archivo: usar `original/aura-logo-removebg-preview.png`. |
| `horizontal/` | ❌ No existe como archivo. En la web se arma en código (ver "Lockup en la web"). |
| `vertical/` | ❌ No existe. |
| `blanco/` | ❌ No existe. |
| `negro/` | ❌ No existe. |
| `favicon/` | ✅ 6 archivos. |

## Lockup en la web (logo + nombre, construido en código)

**[CÓDIGO]** `components/header.tsx`:

```
[isotipo 28×28 · radius 6 · opacity .92]  ← gap 10px →  "Aura Hogar"
                                                        Manrope 300 · 18px · ls -.01em · #FFFFFF
```

**[CÓDIGO]** `components/footer.tsx`:

```
[isotipo 28×28 · rounded-sm]  ← gap 8px (space-x-2) →  "Aura Hogar"
                                                        Inter semibold · text-lg · tracking-wide · #EAE0D5
```

**[CÓDIGO]** `app/opengraph-image.tsx` (imagen para redes, 1200×630): **no usa el isotipo**. Usa un cuadrado 36×36 (radius 8, fondo `rgba(198,172,143,.15)`, borde tan .3) con un **círculo tan de 16px** adentro + "Aura Hogar" (22px, peso 300, blanco) + divisor vertical + "CHAJARÍ, ENTRE RÍOS" en mayúsculas tan .5.

## Archivos que parecen logos pero NO son de Aura Hogar

**[CÓDIGO]** No se copiaron al brand kit:

| Archivo | Qué es |
| --- | --- |
| `public/icon.svg`, `public/apple-icon.png`, `public/icon-dark-32x32.png`, `public/icon-light-32x32.png` | Logo de **v0 (Vercel)**, restos de la plantilla. Al estar en `public/` (no en `app/`), Next.js no los usa automáticamente. |
| `public/placeholder-logo.png`, `public/placeholder-logo.svg` | Placeholder genérico de la plantilla (triángulo punteado). |
| `public/marcas/client-1…6.png` | Logos de **marcas asociadas/proveedores** (Hikvision, World Leds Go, Sophia, Full Lock System, Soul Hogares Inteligentes, Dahua). Son marcas de terceros; ver `../assets/metadata.md`. |

## Recomendaciones de uso

- **[CÓDIGO → práctica actual]** El logo siempre aparece chico (28 px), sobre negro, a la izquierda del nombre.
- **[RECOMENDACIÓN]** Espacio de respeto: el código usa 10 px de separación con un isotipo de 28 px (≈ 1/3 de la altura del símbolo). Mantener al menos esa proporción alrededor del símbolo.
- **[RECOMENDACIÓN]** Usar la versión dorada metalizada sólo sobre fondos oscuros (`#0A0908`, `#22333B`); sobre cream el contraste del dorado es bajo.
- **[RECOMENDACIÓN]** No usar los favicons (tan sobre blanco) como logo en piezas de comunicación: son de baja resolución y el blanco de fondo es opaco.
- **[RECOMENDACIÓN / faltante]** Para un kit completo haría falta encargar: versión vectorial (SVG) del isotipo, variante monocromática blanca y negra, y un logotipo/lockup horizontal oficial con el nombre. **No se generaron** porque no existen en el proyecto y no se quiso inventar.
