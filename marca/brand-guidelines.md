# Aura Hogar — Brand Guidelines

> Documento de referencia de la identidad visual **tal como existe hoy** en el sitio web de Aura Hogar. No propone una identidad nueva.
>
> **Cómo leer este documento**
> - **[CÓDIGO]** — dato encontrado literalmente en el proyecto (valores exactos).
> - **[INTERPRETACIÓN]** — lectura del diseño a partir de cómo se usan los elementos.
> - **[RECOMENDACIÓN]** — sugerencia propia derivada del análisis; no está en el código.
>
> Detalle ampliado en: `colors/colors.md`, `typography/typography.md`, `logos/README.md`, `icons/README.md`, `imagery/README.md`, `ui/*/*.md`, `assets/metadata.md`.

---

## 1. Sobre la marca

**[CÓDIGO]** (metadata, `AURA_HOGAR_CONTEXTO.md`, `DATOS.txt`, textos del sitio)

**Aura Hogar** es una empresa de **domótica y tecnología para el hogar** con base en **Chajarí, Entre Ríos, Argentina**, con más de 2 años de trayectoria y un equipo de 7 profesionales (ingenieros, técnicos electromecánicos, área comercial). Diseña, instala y da soporte a:

1. **Casa Inteligente** — automatización integral con el sistema **SOPHIA** (iluminación, persianas, clima, audio, riego, escenas, paneles táctiles).
2. **Cámaras y Monitoreo** — CCTV Hikvision, NVR, videoportería.
3. **Cerraduras Digitales** — smart locks con huella, código y app.
4. **Iluminación Premium** — LED de diseño (World Leds Go: spots, tiras, líneas Runners y Wally).
5. **Redes y Conectividad** — WiFi 6 mesh.

Se involucra desde las primeras etapas de la obra junto a arquitectos, electricistas y desarrolladores. No publica precios: **todo se consulta por WhatsApp** (+54 9 3456 022800). Instagram: @aurahogaroficial. Dominio: aurahogar.com.

**Misión** [CÓDIGO]: *"Brindar soluciones tecnológicas confiables, simples de usar y pensadas para durar en el tiempo. Creemos en la tecnología como una herramienta para mejorar la calidad de vida, no para complicarla."*

**Claim principal** [CÓDIGO]: **"Tu hogar, inteligente."**

---

## 2. Identidad visual

**[INTERPRETACIÓN]** La web comunica una marca **premium, cálida, arquitectónica y sobria**, más cercana a un estudio de arquitectura o a una marca de diseño de interiores que a una empresa de tecnología convencional.

| Rasgo | Cómo se manifiesta |
| --- | --- |
| **Premium / lujo silencioso** | Negro casi puro con tostados cálidos, titulares enormes en peso ExtraLight, mucho aire, ningún color saturado. |
| **Arquitectura** | Grilla de líneas de 80 px en los héroes, divisores de 1 px, numeración "01 · 02 · 03", layouts asimétricos, fotos de casas contemporáneas. |
| **Tecnología discreta** | La tecnología aparece en detalles: fuente monoespaciada para etiquetas técnicas, badges de modelo, specs, mockups de app. Nunca iconografía "tech" llamativa ni azules eléctricos. |
| **Calidez / luz** | El acento tan `#C6AC8F` funciona como "luz cálida": resplandores radiales ("aurora") y fotos nocturnas con iluminación ámbar. Vincula el nombre *Aura* con el halo de luz. |
| **Minimalismo** | Un solo color de acento, dos tipografías, íconos de línea chicos, sin ilustraciones ni patrones decorativos más allá de la grilla. |
| **Contraste por bloques** | Las páginas alternan secciones **negras** (`#0A0908`) y **cream** (`#EAE0D5`), con alguna sección **slate** (`#22333B`) en los servicios. |
| **Cercanía local** | "Aura Hogar · Chajarí, Entre Ríos" aparece en héroes, OG image y footer; el copy usa **voseo rioplatense**. |

**Estética de referencia** [INTERPRETACIÓN]: tono tipo "Apple/editorial" — tipografía display gigante con tracking negativo, eyebrows en mayúsculas espaciadas, fondos oscuros con fotografía a sangre. El borrador `adaptar/smart-locks.html` (fuera del sitio) muestra el mismo lenguaje, lo que confirma que es una dirección intencional.

---

## 3. Logo

**[CÓDIGO]** Ver `logos/README.md`.

| Variante | Archivo | Estado |
| --- | --- | --- |
| **Isotipo dorado metalizado** (principal) | `logos/original/aura-logo-removebg-preview.png` — PNG transparente 503×496 | ✅ En uso (header y footer) |
| Isotipo tan plano sobre blanco | `logos/favicon/*` (16 a 512 px) | ✅ Solo favicons |
| Logotipo / wordmark como archivo | — | ❌ No existe (el nombre se escribe como texto) |
| Horizontal / vertical | — | ❌ No existen |
| Blanco / negro (monocromo) | — | ❌ No existen |
| Vectorial (SVG) | — | ❌ No existe |

**Descripción del símbolo** [INTERPRETACIÓN]: dos triángulos de contorno grueso — uno grande con una abertura en el lado derecho y otro más chico que se encastra en ella — formando una "A" estilizada que también evoca un techo o una montaña.

**Uso actual** [CÓDIGO]:
- Tamaño: 28×28 px, siempre a la izquierda del nombre "Aura Hogar".
- Fondo: siempre oscuro (`#0A0908`).
- Espaciado símbolo–nombre: 10 px (header) / 8 px (footer).
- Wordmark: Manrope 300, 18 px, blanco (header) — Inter semibold, cream (footer).

**Recomendaciones** [RECOMENDACIÓN]:
- Usar el isotipo dorado solo sobre fondos oscuros (negro o slate).
- Respetar un margen libre alrededor del símbolo de al menos ⅓ de su altura (proporción usada en el header).
- No deformar, recolorear ni aplicar sombras/efectos al PNG metalizado.
- Unificar el wordmark en Manrope 300 (es el que se ve primero y el que coincide con los titulares).
- Encargar a un diseñador la versión vectorial y las variantes monocromas; hoy el PNG de 503 px limita el uso en impresión o gran formato.

---

## 4. Colores

**[CÓDIGO]** Ver `colors/colors.md` y `colors/tokens.json`.

| Color | HEX | RGB | Rol |
| --- | --- | --- | --- |
| **Aura Tan** | `#C6AC8F` | 198, 172, 143 | **Acento de marca**: CTAs, palabra destacada de titulares, íconos, eyebrows, glows, bordes |
| **Aura Black** | `#0A0908` | 10, 9, 8 | Fondo oscuro principal (héroes, header, footer, CTAs) |
| **Aura Cream** | `#EAE0D5` | 234, 224, 213 | Fondo claro principal (secciones alternas) |
| **Aura Brown** | `#5E503F` | 94, 80, 63 | Texto y detalles sobre cream |
| **Aura Slate** | `#22333B` | 34, 51, 59 | Fondo alternativo oscuro (una sección por servicio), tooltip |
| Blanco | `#FFFFFF` | 255, 255, 255 | Texto sobre oscuro; superficie de cards claras |

**Reglas observadas en el código**:
- El **tan es el único acento**. No hay un segundo color de acento.
- Texto secundario, bordes y fondos se resuelven con **el mismo color en transparencia** (`rgba`), no con grises: tan .55 para eyebrows, blanco .55–.68 para textos, tan .1–.18 para bordes.
- Estados: éxito `#34D399` (verde, fuera de paleta), en curso = tan con pulso, error de formulario `#E0A08A` (terracota).

**Proporción aproximada** [INTERPRETACIÓN]: ~60% negro, ~30% cream, ~5% slate, ~5% tan (acento).

---

## 5. Tipografía

**[CÓDIGO]** Ver `typography/typography.md`.

| Familia | Uso | Pesos |
| --- | --- | --- |
| **Manrope** (Google Fonts) | Titulares, wordmark, números de stats, menú mobile | 200, 300, 400 (cargados: 200–600) |
| **Inter** (Google Fonts) | Cuerpo, navegación, botones, formularios, eyebrows | 300, 400, 500 |
| **ui-monospace** (sistema) | Numeraciones, etiquetas técnicas, modelos, ubicación | 400 |

**Jerarquía clave**:

```text
Display   Manrope 200 · clamp(52px, 9vw, 140px) · lh .95 · ls -.04em
H1        Manrope 200 · clamp(36px, 5.5vw, 88px) · lh 1.02 · ls -.035em
H2        Manrope 300 · clamp(26px, 3.2vw, 54px) · lh 1.08 · ls -.025em
H3        Manrope 400 · clamp(20px, 1.8vw, 30px) · lh 1.15 · ls -.02em
Lede      Inter 300 · clamp(17px, 1.4vw, 21px) · lh 1.45
Body      Inter 300 · 15–17px · lh 1.6
Eyebrow   Inter 500 · 12px · MAYÚSCULAS · ls .22em
Mono      ui-monospace · 11–12px · MAYÚSCULAS · ls .12–.2em
Botón     Inter 500 · 13–15px · ls -.01em
```

**Tratamientos firma** [CÓDIGO]:
- Titular con la **última palabra en tan** y **punto final**: "Tu hogar, *inteligente.*"
- Titulares limitados a `14ch` de ancho.
- Eyebrow con separador "·": "AURA HOGAR · CHAJARÍ, ENTRE RÍOS".

---

## 6. Fotografía

**[INTERPRETACIÓN]** Ver `imagery/README.md`.

- **Temas**: casas contemporáneas, interiores amplios, living, dormitorios, jardines y piscinas; producto aislado (cámaras, cerraduras, paneles); celular con la app en mano.
- **Luz**: predominan escenas **nocturnas o de atardecer con luz LED cálida indirecta**. La luz es el hilo conductor con el color tan.
- **Paleta**: tierra, arena, madera, piedra, negro; baja saturación. Excepción: cielos azules en las fotos reales de obra y la imagen de redes.
- **Dos registros**: imágenes aspiracionales de estilo render (servicios, SOPHIA, home) y fotos reales de obra (portfolio). Las segundas tienen menor producción y proporciones variadas.
- **Tratamiento en la web** [CÓDIGO]: fotos a sangre con **overlay negro en degradé** (imagen a opacidad .45–.55 en héroes; overlay hasta .92 en la base de las cards) + grilla + glow tan. Producto con `object-contain` sobre `#101010`/`#1A1A1C`.
- **Sin personas protagonistas**: solo aparecen parcialmente (manos o torso sosteniendo el celular) y en una foto real de obra.

---

## 7. Iconografía

**[CÓDIGO]** Ver `icons/README.md`.

- Librería única: **Lucide** (línea, stroke 2, esquinas redondeadas, 24×24).
- Tamaño en UI: **11–20 px**; color **tan** sobre oscuro.
- Contenedor opcional: caja 32–36 px, radio 8, fondo tan al 10%.
- Ícono más usado: `MessageCircle` (WhatsApp).
- Rol secundario y funcional; nunca ilustrativo.

---

## 8. UI

**[CÓDIGO]** Ver `ui/buttons/buttons.md`, `ui/cards/cards.md`, `ui/navigation/navigation.md`, `ui/other/other-components.md`.

### Botones
- **Siempre pill** (`border-radius: 999px`), Inter 500.
- **Primario**: fondo tan, texto negro, `padding 18px 32px`, 15 px; hover `opacity .88`.
- **Ghost**: transparente, texto blanco, borde blanco .2; hover fondo blanco .06.
- Íconos: `MessageCircle` a la izquierda (WhatsApp) o `ArrowRight` a la derecha (navegar).
- Casi todos los CTAs llevan a WhatsApp con mensaje precargado.

### Cards
- **Con foto**: radio 20 px, sombra `0 4px 24px rgba(0,0,0,.12)`, overlay negro, texto abajo; hover `-4px` + sombra mayor + zoom de foto 1.04–1.06.
- **De contenido (oscuras)**: radio 24 px, borde tan .14, fondo tan .04 en degradé, padding 36 px; hover borde tan .3.
- **De contenido (claras)**: radio 24 px, fondo blanco, borde brown .14.

### Navegación
- Header **sticky, 64 px, negro translúcido con blur**, se opaca al hacer scroll.
- Links 13 px blanco .55 → blanco. Dropdown de servicios en grilla 2×N con íconos tan. CTA pill "Consultar".
- Menú mobile a pantalla completa con links gigantes en Manrope 200.

### Patrones distintivos
- **Eyebrow** + titular display + lede, alineados a la izquierda y abajo del hero.
- **SectionRule** "01 · Etiqueta" con línea de 1 px.
- **Grillas con gap de 1 px** sobre fondo hairline (stats, specs) — divisores finos sin bordes.
- **Pills** de características, **badges mono** de modelo.
- **Marquee** de palabras gigantes en tan al 16%.

---

## 9. Espaciado

**[CÓDIGO]** Valores recurrentes:

| Token | Valor | Uso |
| --- | --- | --- |
| Ancho máximo | **1280 px** (`max-w-7xl`) | Contenedor de todas las secciones y header |
| Ancho CTA final | 800 px / `max-w-4xl` | Bloques centrados |
| Gutter lateral | **32 px mobile / 48 px desktop** (`px-8 md:px-12`) | Todas las páginas (header: 32 px fijo; footer: 16 px — inconsistente) |
| Sección (home) | **96 px** arriba/abajo | Servicios, proceso, portfolio |
| Sección (servicios) | **144 px** (`py-36`) | Páginas de servicio |
| CTA final | 140/100 px (home) · 160/120 px (servicios) | Cierre de página |
| Hero | `min-height: 100svh` (70vh en Nosotros), contenido abajo con 72 px de padding inferior | |
| Título → contenido | 48–56 px | `marginBottom` de encabezados de sección |
| Grillas de cards | gap **16 px** (servicios home) · **24 px** (features, proyectos) | |
| Grillas de dos columnas texto/imagen | gap **72–80 px** | `.showcase` |
| Padding interno de cards | 20–48 px (36 px típico) | |

**Escala observada** [INTERPRETACIÓN]: múltiplos de 4/8 → 8 · 12 · 16 · 20 · 24 · 28 · 32 · 48 · 56 · 64 · 72 · 80 · 96 · 144. El sitio es **generoso en aire**: secciones altas y titulares con mucho espacio alrededor.

**Breakpoints** [CÓDIGO]: 480, 640, 720, 768 (menú mobile), 900, 980 px; más los de Tailwind (`sm`, `md`, `lg`).

---

## 10. Bordes y radios

**[CÓDIGO]**

| Radio | Uso |
| --- | --- |
| **999 px (pill)** | **Botones, badges, pills, filtros, nav de secciones** — el más frecuente (30 usos) |
| 24 px | Feature cards, pillars, cajas de imagen (`vis-box`) |
| 20 px | Cards con foto (servicio, proyecto), CTA intermedia |
| 16 px | Dropdown, info cards, spec grid, tiles de app |
| 12 px | Inputs de formulario |
| 10 px | Ítems del dropdown |
| 8 px | Cajas de íconos |
| 6 px | Logo en header, compat-tags |
| 0.5 rem | `--radius` de shadcn (sin uso visible) |

**Bordes**: siempre **1 px**, nunca sólidos: tan `.08–.22` sobre oscuro, brown `.1–.25` sobre claro, blanco `.08–.22` en botones y mockups. En hover suben a `.3–.5`.

**[INTERPRETACIÓN]** Todo es redondeado y suave: no hay esquinas rectas salvo divisores de sección.

---

## 11. Sombras

**[CÓDIGO]** Uso **escaso**; la profundidad se logra con transparencias y blur, no con sombras.

| Sombra | Uso |
| --- | --- |
| `0 4px 24px rgba(0,0,0,.12)` | Cards con foto (reposo) |
| `0 16px 48px rgba(0,0,0,.22)` | Cards con foto (hover) |
| `0 24px 64px rgba(0,0,0,.6)` | Dropdown del header |
| `0 8px 24px rgba(0,0,0,.25)` | Pill "Ver proyecto" en hover |
| `0 60px 120px rgba(0,0,0,.6)` | Mockup de teléfono |
| `0 0 0 6px rgba(198,172,143,.12)` | Halo del punto tan en héroes |
| `shadow-lg` → `shadow-xl` | Botón flotante WhatsApp (Tailwind) |

**Efectos de "luz" en lugar de sombra**: glows radiales tan (`rgba(198,172,143,.12–.2)`), `backdrop-filter: blur(8–20px)` en header, stats y badges.

---

## 12. Animaciones

**[CÓDIGO]**

| Animación | Detalle | Dónde |
| --- | --- | --- |
| **Reveal on scroll** | `opacity 0→1` + `translateY(28px→0)`, **1.1 s `cubic-bezier(.2,.7,.2,1)`**, escalonado .08 s (d1–d4), IntersectionObserver threshold .1 | Servicios, contacto |
| **FadeUp de hero** | `translateY(24px)`, .8 s, delays 0 / .15 / .3 s | Home |
| **FadeIn** (componente) | `translateY(28px)`, .65 s ease | `components/fade-in.tsx` |
| **Card fade-up** | 20 px, .55 s | Grilla de proyectos al filtrar |
| **Hover de card** | `translateY(-4px)` + sombra, .5 s · zoom de imagen 1.04–1.06, .7 s | Cards |
| **Hover de botón** | opacidad .88, .3 s | Primarios |
| **Header** | cambio de fondo/borde al scrollear, .35 s | Header |
| **Chevron** | rotación 180°, .25 s | Dropdown / acordeón |
| **Marquee** | `translateX(0 → -50%)` lineal infinito, 22–38 s; pausa en hover | Logos de marcas, palabras |
| **Scroll line** | línea tan que recorre 80 px, 2.4 s `cubic-bezier(.65,0,.35,1)` infinito | "Descubrir" en héroes |
| **Pulse** | punto del badge "En ejecución" | Project card |
| **Scale** | `hover:scale-110`, .3 s | Solo botón WhatsApp flotante |

**Curva de marca** [CÓDIGO]: `cubic-bezier(.2,.7,.2,1)` — arranque rápido, frenado largo y suave.

**Accesibilidad** [CÓDIGO]: `prefers-reduced-motion` desactiva marquee y fade-ups en la home y en proyectos (no en todas las páginas).

**[INTERPRETACIÓN]** Movimiento **lento, suave y sutil**: desplazamientos cortos (4–28 px), duraciones largas (.5–1.1 s), nada rebota ni gira.

---

## 13. Tono de comunicación

**[CÓDIGO]** (copy existente)

- **Voseo rioplatense**: "Consultá gratis", "Contanos tu idea", "Abrí con huella", "Controlá más de 50 dispositivos".
- **Titulares cortos con punto final**: "Nuestros servicios.", "El proceso.", "Proyectos recientes."
- **Cercano y directo**, sin tecnicismos en titulares; los datos técnicos van en specs y etiquetas mono.
- **Beneficio antes que producto**: "Diseñado para tu vida, instalado en tu hogar."
- **CTA siempre conversacional** hacia WhatsApp: "Consultá por WhatsApp", "Hablemos por WhatsApp".

---

## 14. Do / Don't

### ✅ DO

- **[CÓDIGO]** Mantener **un único color de acento**: tan `#C6AC8F`.
- **[CÓDIGO]** Usar negro `#0A0908` y cream `#EAE0D5` como fondos, alternando bloques.
- **[CÓDIGO]** Resolver jerarquías secundarias con **transparencias** del mismo color (tan, blanco, brown en `rgba`), no con grises nuevos.
- **[CÓDIGO]** Titulares en **Manrope 200–300, grandes, con tracking negativo**; destacar la última palabra en tan y cerrar con punto.
- **[CÓDIGO]** Eyebrows en **mayúsculas, 12 px, tracking .22em**.
- **[CÓDIGO]** Botones **pill**; primario tan con texto negro, secundario ghost.
- **[CÓDIGO]** Íconos **Lucide de línea**, chicos, en tan.
- **[CÓDIGO]** Fotos con **overlay negro en degradé** para que el texto se lea encima.
- **[CÓDIGO]** Bordes de **1 px translúcidos**, radios generosos (20–24 px en cards).
- **[CÓDIGO]** Animaciones suaves con `cubic-bezier(.2,.7,.2,1)`, desplazamientos cortos.
- **[CÓDIGO]** Escribir en español con **voseo**.
- **[RECOMENDACIÓN]** Priorizar fotografía con **luz cálida, arquitectura contemporánea y escenas nocturnas**, coherente con el set actual.
- **[RECOMENDACIÓN]** Dar mucho espacio vacío: secciones de 96–144 px de alto de padding.

### ❌ DON'T

- **[CÓDIGO → derivado]** No introducir colores saturados (azules eléctricos, rojos, violetas): no existen en la paleta.
- **[CÓDIGO → derivado]** No usar tan como color de texto sobre cream (contraste 1.7:1) ni texto blanco sobre tan (2.2:1).
- **[CÓDIGO → derivado]** No usar botones rectangulares ni con esquinas chicas.
- **[CÓDIGO → derivado]** No usar pesos bold (700+) en titulares: la marca se apoya en pesos livianos.
- **[CÓDIGO → derivado]** No usar sombras fuertes ni múltiples; preferir glows tan y transparencias.
- **[RECOMENDACIÓN]** No mezclar otras librerías de íconos ni íconos rellenos.
- **[RECOMENDACIÓN]** No usar el logo metalizado sobre fondos claros ni sobre fotos sin overlay.
- **[RECOMENDACIÓN]** No usar fotografía fría, de stock genérico con personas posando, ni imágenes con cables/equipos a la vista.
- **[RECOMENDACIÓN]** No usar animaciones con rebote, rotación o escalado exagerado.

---

## 15. Inconsistencias detectadas (documentadas, no corregidas)

1. **Logo**: el isotipo del sitio es dorado metalizado; el de los favicons es tan plano `#DDB788` (más saturado que `#C6AC8F`); la **OG image no usa el logo** (usa un círculo tan dentro de un cuadrado).
2. **Wordmark**: Manrope 300 en header vs. Inter semibold tracking-wide en footer.
3. **Sin logo vectorial** ni variantes monocromas/horizontales.
4. **Favicons y metadata**: `favicon.ico` y los `android-chrome-*` no están referenciados; `site.webmanifest` y `safari-pinned-tab.svg` se referencian pero **no existen**; `theme-color #ffffff`, `TileColor #da532c` y `mask-icon #5bbad5` son defaults de generador.
5. **Restos de plantilla v0**: `public/icon.svg`, `apple-icon.png`, `icon-dark/light-32x32.png`, placeholders, `styles/globals.css` (tema gris sin usar), variables `--font-geist-*`.
6. **Tipografía**: `ServiceShell` y `/contacto` declaran `font-family: "Inter, 'Helvetica Neue', Arial"` como texto literal, que probablemente no coincide con la Inter de `next/font` y cae a Helvetica/Arial. La OG image se genera sin Manrope.
7. **Estilos duplicados**: `.display-h`, `.eyebrow`, `.hero-grid`, `.cta-glow`, botones, etc. se redefinen en cada página con pequeñas variaciones (opacidad de la grilla .15–.28, tamaños display 120–140 px, hover .82/.88, borde ghost .18/.2/.22).
8. **Colores fuera de paleta**: botón flotante WhatsApp en verdes Tailwind con `scale-110`; badge "Finalizado" en verde esmeralda; `project-modal.tsx` (sin uso) con `emerald`/`amber` y botón blanco sobre tan.
9. **Variables HSL de shadcn** redondeadas: no reproducen exactamente los HEX de marca. El tema `.dark` está definido pero no se usa. `--primary` = slate, mientras que el primario real de la UI es tan.
10. **Contenedores distintos**: header 1280/32 px, secciones 1280/48 px, footer `container` + 16 px.
11. **Imágenes**: `proyecto-jps.jpg` es TIFF y `lamparas-decorativas.jpg` es PNG con extensión `.jpg`; `color-vu.png` (8,4 MB) y `visualizacion-celular.png` (6,5 MB) muy pesadas; varias imágenes duplicadas en `public/`; OG images declaradas como 1200×630 aunque sus tamaños reales difieren; `/images/security/hero-sistema-seguridad.jpg` (OG de Seguridad) no existe; hero de Nosotros pendiente de foto.
12. **Copy**: el tooltip del botón WhatsApp dice "¡Chatea con nosotros!" (sin voseo) mientras el resto del sitio usa voseo.
13. **`prefers-reduced-motion`** solo se respeta en home y proyectos.
