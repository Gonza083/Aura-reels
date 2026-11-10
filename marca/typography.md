# Aura Hogar — Tipografía

> **[CÓDIGO]** = extraído del proyecto · **[INTERPRETACIÓN]** = lectura del diseño · **[RECOMENDACIÓN]** = sugerencia propia.

## 1. Familias

```text
FONT FAMILY
Display / Titulares:  Manrope        (Google Fonts vía next/font, variable CSS --font-manrope)
Texto / UI:           Inter          (Google Fonts vía next/font, aplicada en <html>)
Técnica / Mono:       ui-monospace, monospace   (fuente del sistema, NO se carga ninguna)
```

**[CÓDIGO]** `app/layout.tsx`:

```ts
const inter = Inter({ subsets: ["latin"] })
const manrope = Manrope({
  subsets: ["latin"],
  weight: ["200", "300", "400", "500", "600"],
  variable: "--font-manrope",
  display: "swap",
})
// <html lang="es" className={`${inter.className} ${manrope.variable}`}>
```

- **Manrope** se aplica explícitamente con `font-family: var(--font-manrope, inherit)` en titulares (`.display-h`, `.h1-size`, `.h2-size`, `.h3-size`), en el wordmark "Aura Hogar" del header, en los títulos de cards y en el menú mobile.
- **Inter** es la fuente base de todo el documento (cuerpo, navegación, botones, formularios).
- **Mono**: `.mono { font-family: ui-monospace, monospace }` para numeraciones ("01", "02"), etiquetas técnicas, badges de modelo, compat-tags y links tipo "Ver todos →".
- **No hay archivos de fuentes locales** en el proyecto (`.woff`, `.ttf`, `.otf`): ambas familias se descargan y auto-hospedan con `next/font/google` en build.
- **Google Fonts**: Manrope, Inter.

## 2. Pesos

```text
WEIGHTS (uso real contado en el código)
200  ExtraLight  — Manrope — titulares display, números de stats, menú mobile   (17 usos)
300  Light       — Manrope/Inter — lede, cuerpo, h2, títulos de cards, wordmark (42 usos)
400  Regular     — nav, h3, títulos de pasos                                    (15 usos)
500  Medium      — eyebrows, botones, labels, links "Conocer más"               (43 usos)
600  SemiBold    — badges de estado, botón hover de project-card               (3 usos + 8 font-semibold)
700  Bold        — solo en project-modal.tsx (componente sin uso)               (1 uso)
```

**[INTERPRETACIÓN]** La marca se apoya en **pesos muy livianos (200–300) para titulares grandes** y **500 para elementos pequeños en mayúsculas**. El contraste de jerarquía se logra por tamaño, no por peso. Los pesos 600/700 son excepcionales.

## 3. Escala tipográfica

**[CÓDIGO]** Definida en `components/services/service-shared.tsx` (clases compartidas) y repetida con variaciones en cada página. Todos los tamaños grandes son fluidos con `clamp()`.

```text
HEADINGS
Display (hero):  Manrope 200 · clamp(52px, 9vw, 140px) · line-height .95 · letter-spacing -.04em
                 (Home: clamp(52px, 8.5vw, 128px) · Contacto/Proyectos: clamp(48px, 8vw, 120px))
H1:              Manrope 200 · clamp(36px, 5.5vw, 88px) · lh 1.02 · ls -.035em
H2:              Manrope 300 · clamp(26px, 3.2vw, 54px) · lh 1.08 · ls -.025em
                 (Home usa .display-h a clamp(32px,3.5vw,56px) y clamp(36px,4vw,64px))
H2 CTA final:    Manrope 200 · clamp(36px, 5vw, 80px)
H3:              Manrope 400 · clamp(20px, 1.8vw, 30px) · lh 1.15 · ls -.02em
H3 card:         Manrope 300 · 20px (cards chicas) / clamp(22px, 2vw, 36px) (cards grandes)

BODY
Lede:            Inter 300 · clamp(17px, 1.4vw, 21px) · lh 1.45 · ls -.01em
Body large:      Inter 17px · lh 1.6
Body:            Inter 300 · 15px · lh 1.5–1.6
Small:           Inter 300 · 13–14px · lh 1.45
Caption/footer:  Inter 12px (text-xs)

UI
Eyebrow:         Inter 500 · 12px · UPPERCASE · letter-spacing .22em
Eyebrow footer:  Inter 500 · 11px · UPPERCASE · letter-spacing .2em
Nav link:        Inter 400 · 13px · letter-spacing .04em
Botón:           Inter 500 · 15px (hero/CTA) · 14px (medio) · 13px (header) · ls -.01em
Label form:      Inter 500 · 12px · UPPERCASE · ls .14em
Input:           Inter 300 · 15px
Mono label:      ui-monospace · 11–12px · UPPERCASE · ls .12em–.2em
Stat value:      Manrope 200 · clamp(32px, 4vw, 56px) · lh 1 · ls -.03em
Marquee:         200 · clamp(36px, 5vw, 80px) · ls -.03em · color rgba(198,172,143,.16)
Menú mobile:     Manrope 200 · clamp(28px, 7vw, 40px) · ls -.02em
Wordmark header: Manrope 300 · 18px · ls -.01em · #fff
```

## 4. Interlineado

| Contexto | line-height |
| --- | --- |
| Display | `.95` (muy cerrado) |
| H1 | `1.02` |
| H2 | `1.08` |
| H3 | `1.15` |
| Lede | `1.4–1.5` |
| Cuerpo | `1.5–1.6` |
| Stats | `1` |

## 5. Letter-spacing

| Valor | Uso |
| --- | --- |
| `-.04em` | Display |
| `-.035em` | H1 |
| `-.025em` / `-.03em` | H2, stats, marquee |
| `-.02em` | H3, títulos de card, menú mobile |
| `-.01em` | Lede, botones, wordmark |
| `.04em` | Links de navegación |
| `.12em`–`.18em` | Mono labels, labels de formulario |
| `.2em`–`.22em` | Eyebrows (el patrón más reconocible) |

**[INTERPRETACIÓN]** Regla implícita: **cuanto más grande el texto, más negativo el tracking; los textos chicos en mayúsculas van muy espaciados.**

## 6. Tratamientos característicos

- **Palabra final en tan**: los titulares hero cierran con la última palabra o frase en `#C6AC8F` y con punto final — "Tu hogar, **inteligente.**", "Nuestros **proyectos.**", "Esta página **no existe.**".
- **Titulares con punto final**: "Nuestros servicios.", "El proceso.", "Proyectos recientes."
- **Ancho de línea limitado** en `ch`: titulares `max-width: 14ch`, lede `44–48ch`.
- **Numeración mono** "01 · Etiqueta" con línea inferior (`SectionRule`).
- **Separador "·"** en eyebrows: "Aura Hogar · Chajarí, Entre Ríos", "Domótica · Seguridad · Iluminación · Redes".

## 7. Inconsistencias detectadas

1. **Wordmark con dos tipografías distintas**: header = Manrope 300, 18px; footer = Inter `font-semibold tracking-wide` (`text-lg`). OG image = sin fuente cargada (renderiza con la sans por defecto del generador, no Manrope).
2. **`font-family: "Inter,'Helvetica Neue',Arial,sans-serif"` escrito a mano** en `ServiceShell` y en `/contacto`. `next/font` publica Inter con un nombre interno generado, por lo que ese string literal probablemente no la encuentra y cae a Helvetica Neue/Arial en esas páginas (salvo que el usuario tenga Inter instalada). En el resto del sitio Inter sí se aplica vía `inter.className`.
3. **`--font-sans: var(--font-geist-sans)` / `--font-mono: var(--font-geist-mono)`** en `app/globals.css` referencian Geist, que no se carga. Son restos de la plantilla.
4. **Clases de escala duplicadas**: `.display-h`, `.eyebrow`, `.mono` se redefinen en cada página con tamaños ligeramente distintos en lugar de vivir en un único lugar.
5. **Mono sin fuente definida**: `ui-monospace` depende del sistema operativo (SF Mono en Mac, Cascadia/Consolas en Windows). El borrador `adaptar/smart-locks.html` sí usa JetBrains Mono, pero no está en el sitio.

## 8. Referencia rápida para diseñadores

**[RECOMENDACIÓN]** Para piezas fuera de la web (redes, presentaciones), replicar: Manrope ExtraLight/Light para titulares con tracking negativo, Inter Regular/Light para texto, y Inter Medium en mayúsculas espaciadas (+22%) para etiquetas.
