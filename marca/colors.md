# Aura Hogar — Paleta de colores

> **Leyenda de origen**
> - **[CÓDIGO]** dato extraído literalmente del proyecto.
> - **[INTERPRETACIÓN]** lectura del diseño a partir de cómo se usa el color.
> - **[RECOMENDACIÓN]** sugerencia propia, no presente en el código.

## 1. Paleta de marca (5 colores)

**[CÓDIGO]** Definida en `tailwind.config.ts` (`theme.extend.colors`) como `aura-*`, y repetida como constantes JS (`TAN`, `BLACK`, `SLATE`, `CREAM`, `BROWN`) en `components/services/service-shared.tsx`, `components/header.tsx`, `app/page.tsx`, `app/nosotros/page.tsx`, `app/contacto/page.tsx`, `app/proyectos/ProjectsClient.tsx`, `app/not-found.tsx`.

| Rol (interpretado) | Nombre en código | HEX | RGB | HSL | Uso real en la web |
| --- | --- | --- | --- | --- | --- |
| **Primario / acento de marca** | `aura-tan` · `TAN` | `#C6AC8F` | 198, 172, 143 | 32°, 33%, 67% | CTAs principales (fondo de botón), palabra destacada en titulares ("inteligente.", "proyectos.", "no existe."), íconos, eyebrows, bordes y glows (siempre en rgba). Es el color más usado de la marca (27 usos HEX + >150 usos en `rgba(198,172,143,α)`). |
| **Fondo oscuro principal** | `aura-black` · `BLACK` | `#0A0908` | 10, 9, 8 | 30°, 11%, 4% | Fondo de héroes, header, footer, secciones de proceso, CTA final, página de contacto, 404, OG image. Texto sobre botones tan. |
| **Fondo claro principal** | `aura-cream` · `CREAM` | `#EAE0D5` | 234, 224, 213 | 31°, 33%, 88% | Secciones claras alternadas (servicios, portfolio, marcas), `--background` del tema claro, texto del footer. |
| **Texto/acento sobre claro** | `aura-brown` · `BROWN` | `#5E503F` | 94, 80, 63 | 33°, 20%, 31% | Texto secundario, eyebrows y bordes en secciones cream (siempre en `rgba(94,80,63,α)`), hover de links mono. |
| **Fondo alternativo oscuro** | `aura-slate` · `SLATE` | `#22333B` | 34, 51, 59 | 199°, 27%, 18% | Una sección por página de servicio (persianas, iluminación, seguridad, cerraduras), tooltip del botón WhatsApp, gradiente del hero de Nosotros, `--primary` de shadcn. Es el único color frío de la paleta. |
| Texto sobre oscuro | — | `#FFFFFF` | 255, 255, 255 | 0°, 0%, 100% | Titulares y texto en secciones oscuras; se usa casi siempre con opacidad (ver §3). 56 usos de `#fff`. |

### Muestras

```
█ #0A0908  aura-black   ████████████████████  fondo oscuro
█ #22333B  aura-slate   ████████████████████  fondo alternativo
█ #5E503F  aura-brown   ████████████████████  texto sobre cream
█ #C6AC8F  aura-tan     ████████████████████  ACENTO DE MARCA
█ #EAE0D5  aura-cream   ████████████████████  fondo claro
```

## 2. Roles de color

| Rol | Color | Fuente |
| --- | --- | --- |
| Color primario de marca | `#C6AC8F` tan | [INTERPRETACIÓN] es el único color "de acento" y el que diferencia a la marca. **Nota:** en las variables shadcn `--primary` es `#22333B` (slate), pero ningún componente shadcn se usa en el sitio. |
| Color secundario | `#22333B` slate (fondo) / `#5E503F` brown (texto) | [INTERPRETACIÓN] |
| Acento | `#C6AC8F` tan | [CÓDIGO] |
| Background principal | `#0A0908` black (predomina en héroes y CTAs) | [INTERPRETACIÓN] — el sitio alterna black/cream; el negro domina la primera impresión. |
| Background secundario | `#EAE0D5` cream | [CÓDIGO] `--background` del tema claro |
| Superficie de cards claras | `#FFFFFF` | [CÓDIGO] `--card: 0 0% 100%`, `.fcard-light{background:#fff}` |
| Texto principal (oscuro) | `#FFFFFF` | [CÓDIGO] |
| Texto principal (claro) | `#0A0908` | [CÓDIGO] |
| Texto secundario (oscuro) | `rgba(255,255,255,.45–.68)` | [CÓDIGO] |
| Texto secundario (claro) | `rgba(94,80,63,.5–.8)` | [CÓDIGO] |
| Bordes (oscuro) | `rgba(198,172,143,.08–.22)` | [CÓDIGO] |
| Bordes (claro) | `rgba(94,80,63,.1–.25)` | [CÓDIGO] |
| Focus ring | `#C6AC8F` (`outline:2px solid #C6AC8F`, `ring-aura-tan`) | [CÓDIGO] |

## 3. Escala de opacidades (patrón real)

**[CÓDIGO]** La marca casi nunca usa sus colores sólidos para texto secundario, bordes o fondos: usa el mismo color con alfa. Valores más frecuentes:

### Tan `rgba(198,172,143, α)` — sobre fondo oscuro

| α | Uso típico |
| --- | --- |
| `.04–.06` | Fondo de cards/CTAs oscuras (`fcard-dark`, CTA intermedia) |
| `.07` | Líneas de la grilla del hero |
| `.08–.1` | Divisores, fondo de ícono en menú, hover de ítem |
| `.12–.14` | Bordes de cards, hairlines de stats, glow del CTA |
| `.15–.22` | Bordes de dropdown, pills, inputs |
| `.3–.4` | Bordes en hover, badge premium |
| `.4–.5` | Números mono, labels de stats |
| `.55–.65` | **Eyebrows** (el valor más usado: `.55`) |

### Blanco `rgba(255,255,255, α)` — texto sobre oscuro

| α | Uso |
| --- | --- |
| `.2–.22` | Borde de botón ghost |
| `.45` | Texto de cuerpo tenue (proceso, 404) |
| `.55` | Links de navegación inactivos, lede de CTA (el más usado) |
| `.6–.68` | Lede de héroes |
| `.85` | Valores en spec grid |

### Brown `rgba(94,80,63, α)` — sobre cream

| α | Uso |
| --- | --- |
| `.1–.15` | Divisores y bordes |
| `.4–.55` | Eyebrows, números, links mono |
| `.65–.8` | Texto de cuerpo |

### Black `rgba(10,9,8, α)` — overlays

| α | Uso |
| --- | --- |
| `.75` / `.94` | Header (sin scroll / con scroll) |
| `.85` | Stat cells con blur, barra de navegación de secciones |
| `.92` | Base de los overlays de fotos |

## 4. Gradientes

**[CÓDIGO]** Todos los gradientes de marca son **radiales tan muy tenues** o **lineales negros para legibilidad**. Ver código completo en `../imagery/backgrounds/backgrounds.css`.

| Gradiente | Valor | Dónde |
| --- | --- | --- |
| Overlay hero | `linear-gradient(180deg, rgba(10,9,8,.55) 0%, rgba(10,9,8,.2) 40%, rgba(10,9,8,.92) 100%)` | Héroes con foto |
| Overlay card | `linear-gradient(to top, rgba(10,9,8,.92) 0%, rgba(10,9,8,.2) 60%, transparent 100%)` | Cards de servicio y proyecto |
| Aurora / glow | `radial-gradient(closest-side, rgba(198,172,143,.12–.2), transparent 60–70%)` | Héroes, CTA final, 404, OG |
| Hero Nosotros | `linear-gradient(135deg, #0A0908 0%, rgba(34,51,59,.85) 50%, rgba(10,9,8,.95) 100%)` | `/nosotros` |
| Badge premium | `linear-gradient(135deg, rgba(198,172,143,.18), rgba(198,172,143,.06))` | Badges |
| Mockup de teléfono | `linear-gradient(180deg,#111,#000)` / `#0a0a0a → #050505` / `#1a1a1c → #050505` | Casa Inteligente |
| Botón WhatsApp flotante | `from-green-500 to-green-600` (`#22C55E → #16A34A`) | `components/whatsapp-button.tsx` |

## 5. Colores de estado y funcionales

| Estado | Color | RGB | Dónde | Nota |
| --- | --- | --- | --- | --- |
| Éxito / "Finalizado" | `#34D399` (punto), `#6EE7B7` (texto), `rgba(52,211,153,.2/.3)` (fondo/borde) | 52,211,153 | `components/projects/project-card.tsx` | Verde esmeralda Tailwind, fuera de paleta. |
| En curso / "En ejecución" | `#C6AC8F` + animación `pulse` | — | project-card | Usa el tan de marca. |
| Error de formulario | `#E0A08A` | 224,160,138 | `app/contacto/page.tsx` | Terracota suave, coherente con la calidez de la paleta. |
| Destructive (shadcn) | `hsl(0 84.2% 60.2%)` ≈ `#EF4444` / dark `≈ #7F1D1D` | — | `app/globals.css` | Default de shadcn, no se ve en el sitio. |
| WhatsApp flotante | `#22C55E → #16A34A`, hover `#16A34A → #15803D`, ring `#86EFAC` | — | `whatsapp-button.tsx` | Verde Tailwind genérico (no el verde oficial de WhatsApp). |

## 6. Neutros oscuros auxiliares

**[CÓDIGO]** Aparecen puntualmente como superficies:

| HEX | Dónde |
| --- | --- |
| `#111111` | Fondo de `.vis-box` y del contenedor de imagen de project-card (mientras carga) |
| `#12100E` | Dropdown de servicios del header (`rgba(18,16,14,.97)`), `<option>` de select en contacto |
| `#15130F` | Textura placeholder oscura |
| `#101010`, `#1A1A1C`, `#0A0A0A`, `#050505`, `#000` | Cajas de producto y mockup de teléfono (Cerraduras, Iluminación, Casa Inteligente) |
| `#E0D5C6`, `#D1C3B0` | Textura placeholder clara |

## 7. Variables CSS (shadcn) — `app/globals.css`

**[CÓDIGO]** El tema de shadcn fue re-mapeado a la paleta Aura:

| Variable | Claro (`:root`) | Oscuro (`.dark`) |
| --- | --- | --- |
| `--background` | cream | black |
| `--foreground` | black | cream |
| `--card` | `#FFFFFF` | slate |
| `--primary` | slate | cream |
| `--secondary` | tan | brown |
| `--muted-foreground` | brown | tan |
| `--accent` | brown | tan |
| `--border` / `--input` | tan | brown |
| `--ring` | slate | cream |
| `--radius` | `0.5rem` | — |

**Observación:** los valores HSL de las variables están redondeados y no reproducen exactamente los HEX de marca (ej. `30 27% 87%` = `#E7DED5` en vez de `#EAE0D5`; `30 32% 67%` = `#C6AB90` en vez de `#C6AC8F`). La diferencia es imperceptible pero existe. El tema `.dark` está definido pero **no se usa**: `next-themes` está instalado y `components/theme-provider.tsx` existe, pero no se monta en `app/layout.tsx`.

## 8. Colores fuera de paleta / inconsistencias

| Color | Dónde | Observación |
| --- | --- | --- |
| `#DDB788` | Todos los favicons (`public/icons/*`) | El tan de los favicons es **más saturado** que `#C6AC8F`. |
| Gradiente dorado metálico | `aura-logo-removebg-preview.png` | El logo usado en header/footer es dorado con brillo/metalizado, no un tan plano. |
| `#DA532C`, `#5BBAD5`, `theme-color #ffffff` | `app/layout.tsx` (`msapplication-TileColor`, `mask-icon`, `theme-color`) | Valores por defecto de un generador de favicons; no tienen relación con la marca. |
| Verdes Tailwind (`green-*`, `emerald-*`), `amber-200` | WhatsApp flotante, project-card, project-modal (sin uso) | Fuera de la paleta. |
| `styles/globals.css` | — | Copia sin usar del tema neutro por defecto de shadcn (blanco/gris). No aplica al sitio. |

## 9. Contraste (calculado, WCAG 2.1)

| Combinación | Ratio | Resultado |
| --- | --- | --- |
| Blanco sobre `#0A0908` | 19.9:1 | AAA |
| `#0A0908` sobre `#EAE0D5` | 15.3:1 | AAA |
| `#EAE0D5` sobre `#22333B` | 10.1:1 | AAA |
| `#C6AC8F` sobre `#0A0908` (texto tan en oscuro / texto negro en botón tan) | 9.2:1 | AAA |
| `#5E503F` sobre `#EAE0D5` | 6.0:1 | AA |
| Blanco sobre `#C6AC8F` | 2.2:1 | ❌ No apto para texto (solo aparece en `project-modal.tsx`, sin uso) |
| `#C6AC8F` sobre `#EAE0D5` | 1.7:1 | ❌ No apto para texto |

**[RECOMENDACIÓN]** Mantener tan solo sobre fondos oscuros para texto, y sobre cream usar brown.

## 10. Tokens para desarrolladores

Ver `tokens.json` en esta misma carpeta (valores extraídos del código, sin agregar colores nuevos).
