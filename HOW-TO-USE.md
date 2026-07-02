# Diseña con Odissey

Odissey es un sistema integral de estrategia y diseño de experiencia de usuario (UX) compuesto por seis agentes especializados y dieciséis habilidades (skills) de apoyo. Cada agente es una instrucción de sistema autónoma que puedes cargar en proyectos de IA (como Claude Projects, Custom GPTs o Codex). Juntos cubren todo el arco del diseño de productos, desde el planteamiento inicial del problema hasta las especificaciones de entrega de ingeniería.

La tesis central de Odissey: **cada decisión de diseño debe tener una razón, y esa razón debe ser visible en cada nivel.**

---

## La Tripulación (Agentes)

| Agente | Archivo | Cuándo usarlo |
|--------|---------|---------------|
| **Houston** (Control de Misión) | `houston.md` | Iniciar proyectos, definir el contexto inicial y enrutar al equipo hacia los especialistas |
| **Pathfinder** (Estrategia e Investigación) | `pathfinder.md` | Cuando el problema no esté claro, necesites encuadrar retos o sintetizar investigación |
| **Orion** (Diseño de Experiencia) | `orion.md` | Diseñar flujos, estructurar arquitectura de información y redactar el copy de la interfaz |
| **Sentinel** (Calidad, Resiliencia y Accesibilidad) | `sentinel.md` | Evaluar la usabilidad, auditar accesibilidad y robustecer el diseño ante fallos del mundo real |
| **Atlas** (Especificación y Transferencia) | `atlas.md` | Preparar la transferencia del diseño (handoff) y redactar especificaciones para ingeniería |
| **Galileo** (Inmersión e Ideación) | `galileo.md` | Cuando el equipo esté atascado, el enfoque parezca obvio o quieras cuestionar supuestos |

---

## Cómo desplegar Odissey

### Opción 1: Proyectos de Claude o Codex (Recomendado)
1. Crea un nuevo proyecto en tu entorno de IA.
2. Copia el contenido del agente correspondiente en las instrucciones personalizadas (por ejemplo, `houston.md` para el control central).
3. Sube el contexto de tu producto (briefs, constraints, investigaciones, etc.).
4. Empieza a chatear. La IA operará con las directrices de ese agente especializado.

### Opción 2: Plugin para Codex / Claude Code
Si utilizas Codex o Claude Code, puedes instalar Odissey como un plugin local. Esto registrará automáticamente los 6 agentes y las 16 habilidades:
- **Invoca agentes** como subagentes usando `@` — ej: `@pathfinder ayúdame a estructurar este brief`, `@sentinel audita este flujo para accesibilidad`, `@orion diseña el flujo de registro`.
- **Invoca habilidades** como comandos de barra diagonal — ej: `/strategy`, `/journey`, `/evaluar`, `/robustecer`, `/incluir`, `/spec`.

---

## Árbol de Decisiones de la Misión

```
INICIO: Tengo un reto de diseño de producto
│
├── "No sé qué problema real estamos resolviendo"
│   └── Pathfinder
│       Encuadra el problema, analiza el terreno (research) y define el alcance estratégico.
│
├── "Necesito diseñar la interacción, flujos y navegación"
│   └── Orion
│       Estructura flujos, menús, etiquetas y redacta la microcopia de la UI.
│
├── "¿Es este diseño realmente bueno? ¿Es accesible para todos?"
│   └── Sentinel
│       Audita usabilidad, evalúa la accesibilidad (WCAG 2.2) y robustece contra fallos.
│
├── "El diseño está listo y necesitamos pasarlo a desarrollo"
│   └── Atlas
│       Escribe las especificaciones técnicas (/spec) y prepara el paquete de handoff.
│
├── "Estamos atascados / las soluciones son muy obvias"
│   └── Galileo
│       Cuestiona supuestos, explora analogías y abre el campo mental de la misión.
│
└── "Necesito definir las bases del proyecto y el contexto"
    └── Houston
        Control de misión. Reúne el contexto, valida principios éticos y enruta al especialista.
```

---

## Ciclos de Vida del Proyecto

### Ciclo Corto (2 a 4 semanas)
**Houston ➔ Pathfinder ➔ Orion ➔ Atlas**
- **Houston:** Establece el contexto del proyecto y la postura ética.
- **Pathfinder:** Redacta un brief conciso de 1 página validando el problema.
- **Orion:** Diseña los flujos interactivos clave y redacta los textos del botón y estados.
- **Atlas:** Redacta la especificación final (`/spec`) para el desarrollador.

### Ciclo Completo (6 a 12 semanas)
**Houston ➔ Pathfinder ➔ Orion ➔ Sentinel ➔ Atlas**
- **Houston:** Alineación del equipo y análisis de anti-patrones éticos.
- **Pathfinder:** Síntesis completa de investigación previa y delimitación de hipótesis de negocio.
- **Orion:** Diseño de flujos web y móviles, arquitectura de información y microcopia estructurada.
- **Sentinel:** Evaluación heurística rigurosa, robustecimiento de estados y validación de accesibilidad.
- **Atlas:** Especificaciones detalladas con matrices de copy y casos de uso extremo para la transferencia técnica.
- **Galileo:** Disponible en cualquier momento que la tripulación requiera replantear ideas o buscar caminos laterales.
