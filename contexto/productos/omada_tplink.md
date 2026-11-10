# TP-Link Omada — Redes WiFi Profesionales
> Documento de referencia técnica para guiones y contenido de Aura Hogar.
> Línea de redes instalada en todos los proyectos residenciales y comerciales.

---

## 1. ¿Qué es Omada y por qué lo instala Aura Hogar?

Omada es la línea **profesional** de TP-Link. No es el router que comprás en el súper. Es un **sistema de red completo**, con gestión centralizada, pensado para hoteles, edificios, oficinas y casas premium.

La diferencia principal frente a un router de ISP o doméstico:

| | Router del ISP / doméstico | Omada Profesional |
|-|---------------------------|-------------------|
| Gestión | Pantalla básica, sin control real | App centralizada, todo visible |
| Dispositivos soportados | Se degrada con 20+ | Mantiene rendimiento con 200+ |
| Cobertura | Un solo punto | APs en cada zona de la casa |
| Roaming | Se corta al cambiar de zona | Transparente, sin interrupciones |
| Red de invitados | Básica o inexistente | Aislada realmente de tu red |
| Seguridad | WPA2 estándar | WPA3-Enterprise |
| Garantía | 1 año | 5 años |
| Escalabilidad | Casi ninguna | Ilimitada |

**Para comunicar en contenido:**
> "El WiFi del proveedor de internet lo diseñaron para una familia de 4 con 2 celulares. Una casa inteligente tiene 50+ dispositivos conectados. Ahí es donde Omada hace la diferencia."

---

## 2. Componentes del sistema

### 2.1 Access Points (AP) — Los puntos de WiFi

Son los dispositivos que emiten la señal WiFi en cada zona de la casa. Se instalan en el techo o pared, conectados por cable desde el cuarto técnico.

**Tipos según ubicación:**

| Tipo | Dónde se instala | Para qué |
|------|-----------------|---------|
| **Techo (Ceiling)** | Empotrado en cielorraso | Habitaciones, living, cocina |
| **Pared (Wall plate)** | En caja de pared, como un tomacorriente | Ambientes específicos, departamentos |
| **Exterior (Outdoor)** | Fachada, pérgola, garaje | Jardín, pileta, cochera, quinchos |

**Modelos más usados en instalaciones residenciales:**

| Modelo | WiFi | Velocidad | Cobertura | Uso ideal |
|--------|------|-----------|-----------|-----------|
| **EAP620 HD** | WiFi 6 | 1800 Mbps | ~120 m² | Casa mediana, el más usado |
| **EAP670** | WiFi 6 | 5400 Mbps | ~200 m² | Casas grandes, múltiples pisos |
| **EAP690E HD** | WiFi 6E | 10.800 Mbps | ~250 m² | Villas premium, máxima capacidad |
| **EAP615-Wall** | WiFi 6 | 1800 Mbps | — | Apartamentos, como toma de pared |
| **EAP610-Outdoor** | WiFi 6 | 1800 Mbps | 250 m rango | Jardín, pileta, exterior (IP67) |

**Cobertura estimada por tamaño de casa:**
- Casa pequeña (< 150 m²): 1 AP EAP620
- Casa mediana (150–300 m²): 2 AP EAP620 HD
- Casa grande (300–500 m²): 2–3 AP EAP670
- Casa grande + exterior: APs interiores + 1–2 EAP610-Outdoor

---

### 2.2 Switch PoE — El corazón de la instalación

El switch va en el cuarto técnico y cumple dos funciones al mismo tiempo: distribuir datos **y** dar energía eléctrica a los APs por el mismo cable de red.

**Por qué importa:**
- Un solo cable Cat6A desde el switch al AP → datos + luz
- No necesitás electricista en cada punto del techo
- Instalación limpia, un solo cable visible por AP
- Podés reiniciar cualquier AP de forma remota desde la app

**Modelos más usados:**
- **ES210GMP**: 10 puertos, 8 con PoE+ — suficiente para casas medianas
- **TL-SG2210MP**: 10 puertos Gigabit + 2 SFP — para casas grandes

---

### 2.3 Router / Gateway

El router gestiona la conexión a internet, el firewall, la VPN y toda la seguridad de perímetro.

| Modelo | Para quién | Capacidad |
|--------|-----------|-----------|
| **ER605** | Residencias y oficinas pequeñas | ~200 dispositivos |
| **ER7206** | Casas grandes, edificios | ~700 dispositivos |

**Para la mayoría de los proyectos residenciales de Aura Hogar:** ER605 o ER7206 según el tamaño.

---

### 2.4 Omada Controller — El "cerebro" del sistema

Es el software que centraliza la gestión de todos los componentes. Se puede usar de dos formas:

- **Cloud (gratuito):** Servidor de TP-Link. Controlás todo desde la app sin hardware extra. Ideal para residencias.
- **OC300 (hardware local):** Un dispositivo físico en el cuarto técnico. Gestión local para quienes prefieren total privacidad.

---

## 3. Tecnologías clave explicadas simple

### WiFi 6 — El estándar actual para casas inteligentes

**Por qué importa para una casa inteligente:**

Una casa con domótica tiene: celulares, laptops, smart TVs, cámaras, luces inteligentes, termostatos, cerraduras, sistema de audio, sensores → **50+ dispositivos conectados al mismo tiempo.**

WiFi 5 (el estándar anterior) se degrada mucho con tantos dispositivos.
WiFi 6 fue diseñado exactamente para este escenario.

| | WiFi 5 | WiFi 6 |
|-|--------|--------|
| Velocidad real en casa | 200–500 Mbps | 400–1.200 Mbps |
| Dispositivos simultáneos sin degradar | ~20 | 100+ |
| Latencia | 50–100 ms | 20–40 ms |
| Eficiencia energética | — | 30% más eficiente |
| Streaming 4K simultáneo | Se puede saturar | Sin problema |

**WiFi 6E** suma la banda de 6 GHz: canal nuevo, sin interferencias de vecinos, máxima velocidad para casas ultra conectadas.

---

### Seamless Roaming — Sin cortes al moverte

**El problema con WiFi doméstico:**
Caminás por la casa con el celular haciendo una videollamada → cuando pasás de una zona de cobertura a otra, la llamada se corta un segundo o se lagguea.

**Cómo lo resuelve Omada:**
Los APs se comunican entre sí y con el controlador. Cuando tu celular se aleja de un AP, el sistema ya preparó la transición al siguiente. El cambio es invisible, en menos de 100 ms.

**Resultado:**
- Videollamadas sin cortes moviéndote por toda la casa
- Música streaming sin pausas del living al jardín
- Gaming sin lag yendo de habitación a habitación

---

### PoE — Un cable para todo

**¿Qué es?**
Power over Ethernet. El cable de red Cat6A transporta datos **y** electricidad al mismo tiempo.

**Por qué es un diferencial en la instalación:**
- El AP en el techo necesita solo un cable → el de red
- No hay toma de electricidad en el techo ni cables eléctricos adicionales
- Instalación más limpia y más barata
- Si un AP se cuelga, se reinicia remotamente desde la app, sin subir al techo

---

### VLAN — Tu red dividida en zonas seguras

**¿Qué es?**
Crear múltiples redes dentro de la misma instalación física. Como tener varias WiFi separadas pero usando la misma infraestructura.

**Ejemplo de cómo lo configura Aura Hogar:**

| Red | Dispositivos | Acceso |
|-----|-------------|--------|
| **Red principal** | Celulares, laptops del propietario | Total |
| **Red IoT** | Luces, termostatos, cerraduras, Sophia | Aislada |
| **Red cámaras** | Hikvision NVR y cámaras | Aislada, sin acceso a otros |
| **Red invitados** | Visitas temporales | Internet solo, no ve nada tuyo |

**Para comunicar:**
> "Tus invitados tienen WiFi pero no pueden ver tus cámaras, ni tu NAS, ni los dispositivos de tu casa. Eso es segmentación de red profesional."

---

### Band Steering — Siempre en la mejor frecuencia

El sistema elige automáticamente si tu dispositivo va a 2.4 GHz o 5 GHz según la distancia y la congestión. No necesitás elegir manualmente ni tener dos redes distintas.

- Cerca del AP → 5 GHz (más rápido)
- Lejos del AP o detrás de muros → 2.4 GHz (más alcance)

---

## 4. La app Omada

**Una app para ver y controlar toda la red.**

| Función | Detalle |
|---------|---------|
| **Monitoreo en tiempo real** | Qué dispositivos están conectados, velocidad de cada uno, uso de datos |
| **Estado de cada AP** | Online/offline, clientes conectados, señal |
| **Control remoto** | Reiniciar APs, cambiar configuración, activar/desactivar redes |
| **Red de invitados** | Crear, limitar velocidad, programar horario de acceso, generar QR |
| **Alertas** | Dispositivo desconocido conectado, AP caído, red saturada |
| **Diagnóstico** | Interferencias WiFi, mapa de cobertura, test de velocidad |

**Acceso:** desde cualquier lugar del mundo, con internet.

---

## 5. Por qué Omada es "profesional" y no de consumo

1. **SDN (Software Defined Networking):** Todos los APs actúan como un solo sistema coordinado, no como dispositivos independientes
2. **Escala real:** Soporta 1.000 APs, todos sincronizados. Un router doméstico colapsa con 3 extendedores
3. **Uptime:** Diseñado para 99.5%+ de disponibilidad. Actualizaciones sin cortar la red
4. **Seguridad de verdad:** WPA3-Enterprise, VPN, firewall avanzado, VLAN, aislamiento real
5. **Componentes dedicados:** Router + Switch + AP + Controller, cada uno optimizado para su función. No un solo aparato haciendo todo mal
6. **5 años de garantía** vs 1 año del mercado de consumo
7. **Instalación técnica:** No es plug and play. Requiere planificación, cableado Cat6A y configuración. Por eso lo instala Aura Hogar

---

## 6. Ideas de contenido y ganchos para videos de redes

### Ganchos poderosos:
- *"¿Cuántos metros cuadrados de tu casa tiene WiFi muerto? Esto lo resuelve."*
- *"El WiFi que te dio el proveedor de internet no fue diseñado para una casa inteligente."*
- *"Este cable alimenta de luz y datos al mismo tiempo al AP del techo. Sin electricista."* (mostrar PoE)
- *"Tus invitados tienen WiFi pero no pueden ver tus cámaras. Así funciona."*
- *"Caminé de la cocina al jardín en videollamada. No se cortó. Así es Omada."*
- *"Desde el celular veo qué dispositivos están conectados en la red de mi cliente."* (mostrar app)

### Videos que podés grabar:
1. **Tour de cuarto técnico** — mostrar el rack con router + switch + controller, explicar qué hace cada cosa
2. **AP en el techo** — mostrar la instalación prolija, un solo cable bajando al AP
3. **Demo de la app** — mostrar dispositivos conectados, velocidades, estado de la red
4. **Antes y después de cobertura** — mostrar zonas con señal muerta vs cobertura total
5. **Instalación en obra** — pasando cable Cat6A por cañerías, antes de cerrar las paredes
6. **Prueba de roaming** — llamada activa caminando por toda la casa sin cortes

---

## 7. Argumentos de venta / objeciones frecuentes

| Objeción | Respuesta |
|----------|-----------|
| "El WiFi del proveedor me funciona bien" | Hoy sí, pero una casa con domótica tiene 50+ dispositivos conectados. Cuando instales todo el sistema vas a notar la diferencia |
| "Es muy caro para una red" | Son equipos con 5 años de garantía, diseñados para durar. El router del proveedor lo reemplazás cada 2 años |
| "¿Para qué necesito WiFi en el jardín?" | Para que las cámaras exteriores, el riego inteligente, las luces y el audio del jardín funcionen sin cortes |
| "¿Y si se cuelga un AP?" | Lo reiniciás desde la app en 30 segundos, sin tocar nada físicamente |
| "¿Puedo ver quién está conectado a mi red?" | Sí, desde la app ves cada dispositivo con nombre, velocidad y consumo en tiempo real |
| "¿Es complicado de usar?" | La instalación la hacemos nosotros. Una vez configurado, lo manejás con una app igual de simple que cualquier otra |

---

*Última actualización: abril 2026 | Fuente: tp-link.com / omadanetworks.com + investigación técnica*
