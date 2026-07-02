# Diseña con Odissey

Un sistema integral de estrategia y diseño de experiencia de usuario (UX) para herramientas de IA. Contiene 16 habilidades especializadas y 6 agentes que cubren todo el espectro del diseño de productos, desde la estrategia y validación temprana hasta el diseño interactivo, accesibilidad, calidad y la transferencia a ingeniería.

Odissey dota a la inteligencia artificial del contexto de diseño necesario para abordar decisiones con profundidad. Mientras que otras herramientas se enfocan en la estética, Odissey se centra en la razón de ser del producto.

## La Tripulación (Agentes)

Seis agentes que combinan múltiples habilidades en roles especializados con temática de exploración espacial:

| Rol de Misión | Agente | Comandos y habilidades que combina |
|---------------|--------|------------------------------------|
| Control de Misión | **Houston** | `/odissey` — Orienta la misión, establece el contexto del proyecto y enruta a la tripulación. |
| Estrategia e Investigación | **Pathfinder** | `/strategy` + `/research` — Encuentra el problema real, exige evidencia de usuario y define la estrategia. |
| Diseño de Experiencia | **Orion** | `/journey` + `/organizar` + `/articular` — Diseña flujos, estructura la información y redacta el copy. |
| Calidad y Resiliencia | **Sentinel** | `/evaluar` + `/robustecer` + `/incluir` — Audita la usabilidad heurística, previene fallos y asegura accesibilidad. |
| Transferencia a Ingeniería | **Atlas** | `/spec` — Documenta especificaciones técnicas detalladas y prepara la transferencia técnica a código. |
| Pensamiento Lateral | **Galileo** | `/idear` — Cuestiona suposiciones profundas, busca analogías laterales y destraba el proceso. |

---

## Las Habilidades (Skills)

16 habilidades disciplinares y el punto de entrada principal:

### Odissey (Bases del Sistema)
- `odissey/skills/odissey/SKILL.md` — Principios fundamentales de UX, el catálogo de anti-patrones manipuladores y el protocolo de contexto.
- `odissey/skills/odissey/references/` — 8 guías de referencia en profundidad sobre investigación, arquitectura, formularios, redacción, accesibilidad, servicios, métricas y ética.

### Estrategia e Investigación
- `/strategy` — Encuadre estratégico mediante las 5 preguntas fundamentales (validación de problema, audiencia, ajuste de solución, características y competidores).
- `/research` — Planificación de investigación cualitativa/cuantitativa y síntesis de hallazgos.
- `/blueprint` — Mapeo del plano del servicio (Service Blueprint) y procesos internos.

### Diseño de Experiencia
- `/journey` — Mapeo de flujos e interacción pantalla a pantalla.
- `/organizar` — Estructuración de la arquitectura de información y navegación.
- `/articular` — Redacción UX, microcopia y matrices de voz y tono.

### Calidad y Evaluación
- `/evaluar` — Análisis heurístico de usabilidad y detección de patrones oscuros.
- `/robustecer` — Resiliencia ante casos de borde, fallos de red y estados del sistema.
- `/incluir` — Diseño inclusivo y conformidad de accesibilidad WCAG 2.2.

### Adaptación y Contexto
- `/trasponer` — Adaptación del diseño a múltiples soportes físicos y digitales.
- `/localizar` — Adaptación a idiomas, sentidos de lectura (RTL) y dinámicas culturales.

### Medición
- `/medir` — Modelado de métricas UX y diseño de pruebas estadísticas A/B.

### Habilidades Transversales
- `/idear` — Sesión de pensamiento lateral y cuestionamiento estructurado.
- `/storytelling` — Redacción de arcos narrativos persuasivos y veraces.

### Entrega
- `/spec` — Preparación del paquete de handoff técnico de ingeniería.

---

## Instalación

**Como plugin de Claude Code / Codex:**
```
/plugin marketplace add ghaida/odissey
```
Luego instálalo desde el menú `/plugin` para registrar las 16 habilidades como comandos y los 6 agentes como subagentes.
