---
name: organizar
description: >
  Estructura la información para que las personas puedan encontrar lo que necesitan, entender dónde están
  y navegar con confianza. Abarca el diseño de patrones de navegación, taxonomía, sistemas de etiquetado,
  estrategia de búsqueda y exploración, wayfinding y métodos de investigación de IA. Activa cuando diseñes
  estructuras de navegación, esquemas de categorización, mapas del sitio, taxonomías, sistemas de etiquetado,
  experiencias de búsqueda, o cuando pregunten "¿cómo deberíamos organizar esto?" También activa para card sorting,
  tree testing, problemas de findability de información, o cuando los usuarios reporten que no encuentran cosas.
  Usa esta habilidad siempre que la organización estructural de la información sea el problema — no el
  flujo a través de ella, no las palabras en ella, no la presentación visual de ella.
---

# Organizar — Estructurar la Información

## Visión general

La arquitectura de información es el diseño estructural de entornos compartidos de información. Determina si las personas pueden encontrar lo que necesitan, entender dónde están y navegar con confianza. Una buena IA es invisible: los usuarios simplemente "lo entienden". Una mala IA vuelve todo más difícil: más tickets de soporte, más rebote, más confusión, más tiempo perdido.

La IA no es diseño de navegación (eso es una salida de la IA). No es estrategia de contenido (eso es lo que llena la estructura). No es diseño visual (eso es cómo se ve la estructura). La IA es la organización subyacente: categorías, jerarquías, relaciones y etiquetas que hacen que la información de un producto sea localizable y comprensible.

**Activa esta habilidad cuando pregunten sobre:**
- Diseñar o reestructurar navegación (nivel superior, secundaria, contextual)
- Organizar contenido en categorías, secciones o taxonomías
- Mapas del sitio, inventarios de contenido o auditorías estructurales
- Convenciones de etiquetado y nombrado para navegación, categorías o funcionalidades
- Estrategia de búsqueda, filtrado o experiencias de exploración
- Usuarios que reportan que "no encuentran cosas" o se sienten perdidos
- Card sorting, tree testing u otra investigación de IA
- "¿Cómo deberíamos organizar esto?" o "¿Dónde debería vivir esto?"
- Fusionar o reestructurar áreas de producto después de crecimiento o adquisición

## Familia de habilidades

Trabajas junto a habilidades complementarias que gestionan preocupaciones interconectadas:

- **`$strategy`** — Su definición de audiencia y ajuste de solución informan tus decisiones de IA. ¿Para quién organizas y cómo piensan? Sus cinco preguntas fundacionales te dicen si el alcance del producto es lo suficientemente estable para construir una estructura duradera, o si es probable que cambie.
- **`$research`** — Los card sorts, tree tests y entrevistas de usuario revelan cómo los usuarios realmente categorizan y encuentran información. Sin su investigación, tu IA se basa en suposiciones internas sobre cómo piensan las personas — y esas suposiciones casi siempre son incorrectas.
- **`$journey`** — Tu IA proporciona la estructura a través de la cual navegan sus flujos. Ellos diseñan la secuencia de pasos; tú diseñas el espacio a través del que se mueven esos pasos. Cuando un flujo sigue llegando a callejones sin salida, el problema suele ser estructural, no secuencial.
- **`$articular`** — Las etiquetas son donde la IA y la estrategia de contenido se encuentran. La claridad del nombrado es crítica — una taxonomía perfectamente estructurada con etiquetas poco claras falla igual que un volcado plano de ítems claramente nombrados. Colabora estrechamente en las decisiones de nombrado.
- **`$blueprint`** — La arquitectura del sistema limita y habilita las posibilidades de IA. El modelo de datos, la estructura de API y el sistema de gestión de contenido determinan qué estructuras organizativas son técnicamente factibles. Una taxonomía hermosa que el CMS no puede representar es inútil.
- **`$evaluar`** — Prueba si los usuarios realmente pueden encontrar cosas en tu estructura. Su evaluación heurística detecta problemas de IA que los tree tests pierden — patrones inconsistentes, agrupaciones engañosas, contenido huérfano.
- **`$localizar`** — Las decisiones de IA que funcionan en un idioma o cultura pueden fallar en otro. Los límites de categoría, los significados de las etiquetas y las convenciones de navegación varían entre mercados.
- **`$idear`** — Un modo cognitivo transversal para cuando las categorías parecen naturales pero los usuarios siguen perdiéndose. Entra cuando: la estructura refleja el organigrama en lugar de los modelos mentales del usuario, los supuestos heredados de IA necesitan cuestionarse, o sospechas que el esquema de categorización en sí mismo es el problema. Idear te ayuda a preguntarte si el principio de organización es correcto, no solo si la organización es ordenada.

Colabora explícitamente con cada una cuando su dominio importa. Señala qué *no* estás decidiendo.

## Visualización

Cuando el usuario invoca `$organizar`, decide si el entregable debe
incluir un mapa del sitio / diagrama de IA, y si es así, en qué formato. Pregunta al usuario
de antemano — antes de producir el entregable en markdown.

### Pregunta primero

Abre la respuesta con esta pregunta, con HTML como opción por defecto:

> ¿Te gustaría una visualización de esta IA?
>
> - **HTML** (por defecto) — bloque de código autocontenido, abre en cualquier navegador
> - **Herramienta de diseño** — creado en el archivo de diseño disponible
> - **Herramienta de diagramación** — creado en el archivo de diagramación disponible
> - **No** — solo markdown

Omite la pregunta si la solicitud ya indica una preferencia — "con un
diagrama", "en una herramienta de diseño", "en una herramienta de diagramación",
"sin diagrama", "solo html" omiten
el prompt. Por defecto, HTML si el usuario dice sí sin nombrar un formato.

### Salida HTML

Emite un único archivo HTML autocontenido como un bloque de código delimitado. Sin
CSS externo, sin fuentes externas, sin JS. El usuario copia el código en un archivo `.html`
y lo abre en un navegador. Incluye siempre el bloque de tokens completo + CSS por patrón
a continuación en una etiqueta `<style>` en línea.

**Bloque de estilos requerido** — pega textualmente en `<style>`:

```css
:root {
  --bg: #fafafc; --surface: #ffffff; --fg: #18182b; --fg-muted: #65657a;
  --border: #d8d8e4; --accent: #4338ca;
  --sans: "Hanken Grotesk", Inter, system-ui, -apple-system, sans-serif;
  --mono: ui-monospace, "SF Mono", Menlo, monospace;
  --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px;
  --s5: 20px; --s6: 24px; --s7: 32px; --s8: 48px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #18182b; --surface: #1f1f36; --fg: #f0f0f8; --fg-muted: #8888a8;
    --border: #2a2a44; --accent: #7c6ff0;
  }
}
* { box-sizing: border-box; }
body {
  font-family: var(--sans); background: var(--bg); color: var(--fg);
  padding: var(--s7); line-height: 1.5; margin: 0;
}
.visual-diagram {
  margin: 0; padding: var(--s5);
  background: var(--surface); border-radius: 8px;
  border: 1px solid var(--border); overflow-x: auto;
}
.visual-label {
  font-family: var(--mono); font-size: 10px; font-weight: 600;
  color: var(--fg-muted); letter-spacing: 0.06em;
  margin-bottom: var(--s4); text-transform: uppercase;
}
.sitemap-tabbar {
  display: flex; align-items: center; justify-content: space-around;
  padding: var(--s2) var(--s3);
  background: var(--bg); border: 1px solid var(--border);
  border-radius: 8px; margin-bottom: var(--s4);
}
.sitemap-tab {
  display: flex; flex-direction: column; align-items: center;
  gap: 2px; font-size: 10px; color: var(--fg-muted);
  padding: var(--s1) var(--s2);
}
.sitemap-tab svg { color: var(--fg-muted); }
.sitemap-tab-active { color: var(--accent); }
.sitemap-tab-active svg { color: var(--accent); }
.sitemap-tab-post {
  background: var(--accent); border-radius: 50%;
  width: 32px; height: 32px;
  display: flex; align-items: center; justify-content: center; padding: 0;
}
.sitemap-tab-post svg { color: white; }
.sitemap-tree { padding: var(--s2) 0; }
.sitemap-root { margin-bottom: var(--s3); }
.sitemap-root .sitemap-node-label {
  font-family: var(--mono); font-size: 11px; font-weight: 700; color: var(--fg);
}
.sitemap-branches { display: flex; gap: var(--s2); flex-wrap: wrap; }
.sitemap-branch { flex: 1; min-width: 85px; }
.sitemap-node {
  padding: var(--s2); background: var(--bg);
  border: 1px solid var(--border); border-radius: 4px;
  font-size: 11px; font-weight: 600; color: var(--fg);
  margin-bottom: var(--s2);
  display: flex; align-items: center; gap: var(--s1);
}
.sitemap-node-primary { border-color: var(--accent); border-width: 2px; }
.sitemap-node-action {
  background: var(--accent); color: white; border-color: var(--accent);
}
.sitemap-node-tag {
  font-family: var(--mono); font-size: 9px;
  color: var(--fg-muted); font-weight: 400; margin-left: auto;
}
.sitemap-node-action .sitemap-node-tag { color: rgba(255,255,255,0.7); }
.sitemap-children {
  padding-left: var(--s3); border-left: 1px dashed var(--border);
}
.sitemap-leaf {
  font-size: 10.5px; color: var(--fg-muted);
  padding: 2px 0; line-height: 1.4;
}
```

**Plantilla de estructura** — rellena con la IA real:

```html
<div class="visual-diagram">
  <div class="visual-label">Information Architecture: [PRODUCT NAME]</div>

  <!-- Optional tab bar mockup (skip if the IA isn't a tabbed mobile shell). -->
  <div class="sitemap-tabbar">
    <div class="sitemap-tab sitemap-tab-active">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2" stroke-linecap="round"
           stroke-linejoin="round"><!-- icon path --></svg>
      <span>[TAB 1 — ACTIVE]</span>
    </div>
    <div class="sitemap-tab">
      <svg ...><!-- icon --></svg>
      <span>[TAB 2]</span>
    </div>
    <!-- Centered accent action tab (e.g., Post, Pay, +) — round indigo button -->
    <div class="sitemap-tab sitemap-tab-post">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2.5" stroke-linecap="round"
           stroke-linejoin="round">
        <line x1="12" y1="5" x2="12" y2="19"/>
        <line x1="5" y1="12" x2="19" y2="12"/>
      </svg>
    </div>
    <div class="sitemap-tab">
      <svg ...><!-- icon --></svg>
      <span>[TAB 4]</span>
    </div>
    <div class="sitemap-tab">
      <svg ...><!-- icon --></svg>
      <span>[TAB 5]</span>
    </div>
  </div>

  <!-- Site map tree -->
  <div class="sitemap-tree">
    <div class="sitemap-root">
      <span class="sitemap-node-label">[PRODUCT]</span>
    </div>

    <div class="sitemap-branches">
      <!-- Primary / default branch — accent 2px border, "default" tag -->
      <div class="sitemap-branch">
        <div class="sitemap-node sitemap-node-primary">
          <span>[SECTION]</span>
          <span class="sitemap-node-tag">default</span>
        </div>
        <div class="sitemap-children">
          <div class="sitemap-leaf">[CHILD SCREEN]</div>
          <div class="sitemap-leaf">[CHILD SCREEN]</div>
          <!-- 2–4 leaves per branch -->
        </div>
      </div>

      <!-- Default branch -->
      <div class="sitemap-branch">
        <div class="sitemap-node">
          <span>[SECTION]</span>
          <span class="sitemap-node-tag">toggle</span>
        </div>
        <div class="sitemap-children">
          <div class="sitemap-leaf">[CHILD]</div>
        </div>
      </div>

      <!-- Action branch — solid accent fill, white text -->
      <div class="sitemap-branch">
        <div class="sitemap-node sitemap-node-action">
          <span>[ACTION] (+)</span>
        </div>
        <div class="sitemap-children">
          <div class="sitemap-leaf">[CHILD]</div>
        </div>
      </div>
    </div>
  </div>
</div>
```

**Reglas:**

- Envuelve siempre en `.visual-diagram` con un título `.visual-label`.
- Tres estados de nodo:
  - `sitemap-node` — borde por defecto de 1px (la mayoría de las ramas)
  - `sitemap-node-primary` — borde de acento de 2px (la rama "por defecto" / "inicio" / "principal" en la que aterrizan los usuarios)
  - `sitemap-node-action` — fondo de acento sólido + texto blanco (acciones de creación como Post, Pay, New)
- Los hijos se sitúan bajo cada nodo con un borde izquierdo discontinuo (`.sitemap-children`), sangría de 12px.
- La barra de tabs (opcional) muestra la shell de navegación. El tab activo usa `sitemap-tab-active` (color índigo). La acción centrada usa `sitemap-tab-post` (círculo índigo de 32×32, icono blanco, sin etiqueta).
- Los iconos SVG para tabs usan `stroke-width="2"` para tabs regulares, `2.5` para el icono de más de la acción centrada.
- Usa etiquetas mono (`default`, `toggle`, `requires auth`, etc.) con moderación — anotan el comportamiento de la rama, no su nombre.
- No inventes nombres de clase — cópialos textualmente. La consistencia de clases es cómo las habilidades permanecen alineadas.
- Los temas claro + oscuro se incluyen juntos. No elimines el modo oscuro.
- Autocontenido: sin `<link>` externo a fuentes o CSS, sin JS.

### Salida en una herramienta de diseño

Cuando el usuario elige una herramienta de diseño, crea o abre un archivo de diseño y
traduce los patrones del sitemap a equivalentes visuales:

- Barra de tabs → frame horizontal, 64px de alto, radio de 8px, trazo de 1px `#d8d8e4`, relleno `#fafafc`. Tabs distribuidos uniformemente. Icono + etiqueta del tab activo en azul índigo de acento.
- Tab de acción centrado → círculo de 32×32 relleno `#4338ca` con glifo `+` blanco (o icono equivalente al dominio).
- `.sitemap-node` → frame ~160×40, radio de 4px, trazo de 1px `#d8d8e4`, etiqueta (Sans 11/600/primer plano) a la izquierda, etiqueta mono opcional (Mono 9/regular/atenuado) a la derecha.
- `.sitemap-node-primary` → mismo frame, trazo de acento de 2px.
- `.sitemap-node-action` → mismo frame, relleno `#4338ca`, texto blanco.
- `.sitemap-children` → columna sangrada, línea izquierda discontinua de 1px `#d8d8e4`, hojas como líneas Sans 10.5/regular/atenuado.

### Salida en una herramienta de diagramación

Cuando el usuario elige una herramienta de diagramación, crea un nuevo archivo y
establece los tokens del diagrama Odissey. Inserta la barra de tabs mockup (si aplica),
la etiqueta raíz y una fila de frames de rama con sus hojas hijas debajo.

## Capacidades principales

### 1. Diseño de patrones de navegación

La navegación es cómo los usuarios se mueven a través de tu IA. El patrón que eliges da forma a todo — qué pueden descubrir los usuarios, con qué rapidez se orientan y si se sienten en control o perdidos. Cada patrón tiene compensaciones genuinas, y la elección correcta depende de la estructura del contenido, las tareas del usuario y la escala.

**Jerárquico (estructura de árbol)** — Funciona cuando el contenido tiene relaciones padre-hijo claras con mínima superposición. Las categorías se anidan lógicamente: Ajustes > Cuenta > Contraseña. Escala bien con la profundidad si cada nivel es significativo. Falla cuando los ítems pertenecen legítimamente a múltiples categorías — forzar un único hogar crea problemas de "¿Dónde encontraré...?". La mayoría de los productos usan por defecto el jerárquico porque refleja los organigramas; eso es una señal de alerta, no una recomendación.

**Hub-and-spoke** — Funciona para apps orientadas a tareas con modos distintos (una app bancaria: cuentas, transferencias, pagos, ajustes). Cada spoke es autocontenido; el hub es la base de inicio. Falla cuando las tareas se superponen significativamente o los usuarios necesitan moverse entre spokes sin regresar al hub.

**Plano** — Funciona para conjuntos de contenido pequeños donde todo tiene aproximadamente la misma prioridad. Una página de ajustes con 6 opciones. Una app utilitaria con 4 herramientas. Se derrumba con más de 7-10 ítems — los usuarios no pueden escanear, priorizar o recordar dónde están las cosas. Si tienes la tentación de usar navegación plana con 15+ ítems, necesitas jerarquía.

**Facetado** — Funciona para contenido grande y rico en atributos: catálogos de e-commerce, bases de datos, directorios, cualquier colección donde los ítems tienen múltiples propiedades independientes. Los usuarios filtran combinando facetas (talla + color + precio). Falla cuando las facetas no son verdaderamente independientes (filtrar por "principiante" y "avanzado" simultáneamente no tiene sentido) o cuando el conjunto de datos es demasiado pequeño para beneficiarse del filtrado.

**Dashboard** — Funciona para monitoreo, vista general y verificación de estado. Los usuarios necesitan una vista de resumen con capacidad de drill-down. Falla como navegación principal para la completitud de tareas — los dashboards muestran estado pero no guían bien la acción.

**Secuencial (wizard)** — Funciona para procesos lineales con dependencias: configuración de cuenta, formularios de solicitud, flujos de configuración. Cada paso requiere el anterior. Falla cuando los usuarios necesitan saltar, revisar decisiones anteriores, o el proceso no es realmente lineal.

**Navegación global + local** — La mayoría de los productos de cualquier escala necesitan ambas. La navegación global proporciona orientación persistente (secciones de nivel superior). La navegación local proporciona opciones específicas al contexto dentro de una sección. La pregunta de diseño es cómo se relacionan: ¿la navegación local reemplaza a la global, se anida dentro de ella, o existe junto a ella?

Cuando recomiendes un patrón, muestra las compensaciones para este producto específico, no solo las fortalezas generales del patrón. "La navegación jerárquica funciona para tu sitio de documentación porque el contenido tiene relaciones padre-hijo claras, pero tu sección de 'Integraciones' necesitará polihieraquía ya que las integraciones abarcan múltiples áreas de producto."

### 2. Diseño de taxonomía

Una taxonomía es el sistema de clasificación detrás de tu navegación — las categorías, subcategorías y relaciones que organizan tu contenido. La navegación es lo que ven los usuarios; la taxonomía es la lógica subyacente.

**Principio MECE** — Las categorías deben ser mutuamente exclusivas (los ítems pertenecen a una categoría, no a tres) y colectivamente exhaustivas (todo tiene un hogar, nada cae en las grietas). MECE perfecto es raro en la práctica — el objetivo es minimizar la superposición y eliminar los huérfanos, no lograr pureza teórica.

**Top-down vs. bottom-up** — Las taxonomías top-down son diseñadas por expertos que entienden el dominio: lógicas, exhaustivas, potencialmente desconectadas de cómo piensan realmente los usuarios. Las taxonomías bottom-up emergen de la investigación de usuarios (card sorts, análisis de logs de búsqueda): arraigadas en la realidad, potencialmente desordenadas o inconsistentes. Las mejores taxonomías usan ambos: estructura experta validada y ajustada por datos de usuarios.

**Polihieraquía** — A veces un ítem pertenece genuinamente a múltiples categorías. Una receta puede ser tanto "Comidas rápidas" como "Vegetariana". Una funcionalidad de software puede ser tanto "Seguridad" como "Configuración de cuenta". La polihieraquía maneja esto permitiendo múltiples padres. Úsala deliberadamente, no como muleta para categorías poco claras. Si todo necesita polihieraquía, tus categorías probablemente están equivocadas.

**Escalabilidad** — Diseña taxonomías que puedan crecer. Si tienes 3 categorías de producto hoy y tendrás 30 en dos años, diseña la lógica estructural para 30 ahora — incluso si solo poblas 3. Añadir una categoría debería ser extender un patrón, no reestructurar todo el sistema.

**Pruebas** — Los tree tests validan si los usuarios pueden encontrar ítems dentro de tu taxonomía. Los tests de primer clic validan si las categorías de nivel superior comunican sus contenidos. Los card sorts inversos validan si tus categorías coinciden con los modelos mentales del usuario. Ejecuta estos con 50+ participantes para fiabilidad estadística.

### 3. Sistemas de etiquetado

Las etiquetas son la decisión de IA más importante. Una taxonomía perfectamente organizada con etiquetas confusas falla completamente, porque las etiquetas son la única parte de tu IA con la que los usuarios interactúan directamente. Todas las demás decisiones estructurales son invisibles — las etiquetas son la interfaz.

**Las etiquetas deben comunicar el destino, no solo la categoría.** "Recursos" no te dice nada. "Documentación de ayuda, tutoriales y referencia de API" te dice exactamente lo que encontrarás. "Cuenta" es ambiguo — ¿significa facturación, perfil, ajustes o los tres? Nómbralo por lo que el usuario encontrará o hará allí.

**Pruebas de etiquetas:**
- **Test de 5 segundos**: Muestra a los usuarios una barra de navegación durante 5 segundos, luego pregunta qué encontrarían bajo cada etiqueta. Si no pueden predecir los contenidos, la etiqueta falla.
- **Test Cloze**: Elimina una etiqueta y muestra los contenidos debajo — ¿pueden los usuarios adivinar la etiqueta? Si no, la etiqueta no coincide con el modelo mental.
- **A/B testing de variantes de etiquetas**: En producción, prueba si cambiar una etiqueta afecta el click-through, la completitud de tareas o los tickets de soporte.

**Fallos de etiquetado comunes:**
- **Jerga interna** — Tu equipo lo llama "Espacio de trabajo" pero los usuarios lo llaman "Mis proyectos." Usa su lenguaje.
- **Etiquetas ambiguas** — "Dashboard", "Resumen", "Inicio" — ¿cuál es la diferencia? Si tu equipo no puede articularlo en una oración, los usuarios no pueden navegarlo.
- **Categorías superpuestas** — "Herramientas", "Funcionalidades" y "Productos" — ¿dónde busca un usuario lo que quiere? La superposición crea vacilación y retroceso.
- **Etiquetas de formato** — "Recursos", "Biblioteca", "Hub" describen contenedores, no contenidos. Obligan a los usuarios a hacer clic y verificar en lugar de navegar con confianza.

### 4. Diseño de búsqueda y exploración

Los usuarios encuentran información de dos maneras fundamentalmente diferentes, y la mayoría de los productos necesitan soportar ambas.

**Búsqueda (búsqueda de ítem conocido)** — El usuario sabe lo que quiere y está intentando llegar rápidamente. Tiene vocabulario específico, un objetivo claro y poca tolerancia al ruido. Patrones de búsqueda: autocompletado (reduce la escritura, sugiere correcciones, muestra consultas populares), filtros (acotar resultados por atributos), búsqueda facetada (combinar múltiples filtros), recuperación de cero resultados (sugerir alternativas, verificar ortografía, ampliar alcance, mostrar ítems populares).

**Exploración (búsqueda exploratoria)** — El usuario no sabe exactamente lo que quiere, o no tiene vocabulario para ello. Quiere explorar, comparar y descubrir. Patrones de exploración: categorías y subcategorías, tags y etiquetas, colecciones curadas ("Selección del equipo", "Popular esta semana"), vistos recientemente, ítems relacionados.

**El equilibrio cambia según la experiencia del usuario.** Los usuarios nuevos exploran porque no saben qué está disponible ni cómo llamarlo. Los usuarios expertos buscan porque saben exactamente lo que quieren. Un producto que solo soporta búsqueda penaliza a los usuarios nuevos; uno que solo soporta exploración frustra a los expertos.

**Interacción búsqueda-exploración** — Las mejores experiencias mezclan ambas. Un usuario explora hasta una categoría, luego busca dentro de ella. O busca, ve resultados con filtros facetados y explora el conjunto filtrado. Diseña para estos patrones combinados, no solo para búsqueda o exploración pura.

**Cero resultados es un problema de diseño, no un caso extremo.** Todo producto tiene estados de cero resultados, y son donde los usuarios se sienten más abandonados. Diseña caminos de recuperación: sugerencias de ¿quisiste decir?, corrección ortográfica, sugerencias de categorías más amplias, ítems populares y un camino claro para explorar en su lugar. Una experiencia de búsqueda es solo tan buena como su peor resultado.

### 5. Diseño de wayfinding

El wayfinding es el arte de ayudar a las personas a orientarse y navegar a través de un entorno. Los principios provienen de la investigación de wayfinding del mundo real (Passini, Arthur, Mollerup) y se traducen directamente a productos digitales.

**Las cuatro preguntas de wayfinding que los usuarios siempre se hacen:**
1. **¿Dónde estoy?** (Orientación) — Breadcrumbs, estados de navegación activos, títulos de página, encabezados de sección. Los usuarios necesitan confirmación constante y ambiental de su ubicación. Si tienen que pensar en dónde están, el wayfinding está fallando.
2. **¿A dónde puedo ir?** (Decisión de ruta) — Menús de navegación, enlaces, CTAs, contenido relacionado. Los usuarios necesitan ver sus opciones sin sobrecargarse. La divulgación progresiva ayuda: muestra siempre las rutas primarias, las secundarias bajo demanda.
3. **¿Estoy en el camino correcto?** (Monitoreo de ruta) — Indicadores de progreso, mensajes de confirmación, patrones consistentes. Cuando un usuario hace clic en "Facturación", la página en la que aterriza debe confirmar inmediatamente que está en el lugar correcto — a través del encabezado, el contenido y el contexto visual.
4. **¿He llegado?** (Reconocimiento del destino) — El contenido que encuentra el usuario debe coincidir con lo que prometía la etiqueta. Si hicieron clic en "Precios" y aterrizan en una página que comienza con una comparación de funcionalidades, se preguntarán si están en el lugar correcto.

**Cuando los usuarios se sienten perdidos:**
- Demasiadas opciones a la vez (más de 7-9 ítems de nivel superior tensiona el escaneo)
- Patrones inconsistentes (la navegación funciona diferente en distintas secciones)
- Falta de puntos de referencia (sin elementos persistentes para anclar la orientación)
- Sin "inicio" claro (ningún lugar seguro al que retirarse y empezar de nuevo)
- Anidamiento profundo sin breadcrumbs (perdido en la jerarquía)
- Etiquetas que no coinciden con el contenido (el mapa no coincide con el territorio)

Diseña las señales de wayfinding como un sistema: breadcrumbs, estados activos, títulos de página, indicadores de sección y navegación contextual deben reforzar todos el mismo mensaje sobre dónde está el usuario y qué está disponible.

### 6. Métodos de investigación de IA

Las decisiones de IA deben probarse, no asumirse. Estos son los principales métodos de investigación para validar la arquitectura de información:

**Card sorting** — Los participantes organizan ítems de contenido en grupos que tienen sentido para ellos.
- *Card sort abierto*: Los participantes crean sus propias categorías y las nombran. Revela modelos mentales naturales. Úsalo con mínimo 15 participantes. Analiza con matrices de similitud (qué ítems se agruparon juntos con más frecuencia) y dendrogramas (agrupación jerárquica de agrupaciones).
- *Card sort cerrado*: Los participantes clasifican ítems en categorías predefinidas. Prueba si tus categorías son intuitivas. Úsalo con 30+ participantes para confianza estadística.
- *Card sort híbrido*: Categorías predefinidas con la opción de crear nuevas. Lo mejor de ambos: prueba tus categorías mientras revela brechas.

**Tree testing** — Los participantes navegan por una jerarquía solo de texto para encontrar ítems específicos. Sin diseño visual, sin contenido — solo la estructura. Esto aísla la calidad de la IA de otros factores de diseño. Basado en tareas: "¿Dónde encontrarías X?" Mide la tasa de éxito (¿lo encontraron?) y la directividad (¿fueron directamente o retrocedieron?). Úsalo con 50+ participantes.

**Test de primer clic** — ¿Dónde hacen clic primero los usuarios cuando intentan completar una tarea? Si el primer clic es incorrecto, la tasa de éxito para la tarea completa cae drásticamente. Úsalo para validar si las categorías de navegación de nivel superior comunican sus contenidos.

**Enfoques combinados** — Empieza con card sorts abiertos para descubrir modelos mentales. Usa esos hallazgos para redactar una taxonomía. Valida con card sorts cerrados y tree tests. Refina con tests de primer clic en la navegación implementada. Esta secuencia construye evidencia en cada etapa en lugar de probar un único supuesto.

**Análisis de logs de búsqueda** — ¿Qué buscan los usuarios? Las búsquedas de alto volumen de ítems que deberían ser explorables indican fallos de IA — los usuarios buscan porque no pueden explorar hasta lo que necesitan. Las búsquedas con cero resultados indican desajustes de vocabulario entre tus etiquetas y el lenguaje de los usuarios. Las principales consultas de búsqueda deben mapear limpiamente a la navegación de nivel superior; cuando no lo hacen, tu IA tiene una brecha.

**Análisis de IA competitiva** — Estudia cómo los competidores y productos análogos organizan información similar. No para copiar — su IA puede estar igual de rota — sino para entender las convenciones que los usuarios ya conocen. Cuando los usuarios llegan a tu producto, traen modelos mentales de otros productos que han usado. Coincidir con esos modelos donde tiene sentido reduce el coste de aprendizaje; romperlos intencionadamente requiere un beneficio claro.

## Formato de entregable

Estructura tu entregable de IA según lo necesario para el problema en cuestión. No todas las secciones aplican a todos los proyectos — usa lo que sirve al problema:

1. **Evaluación de IA**
   Qué funciona, qué está roto y por qué. Evidencia de investigación, analytics o datos de soporte.

2. **Mapa del sitio / Estructura de navegación**
   Jerarquía visual que muestra todos los niveles, relaciones y enlaces cruzados. Anota con la justificación de las decisiones estructurales clave.

3. **Especificación de navegación**
   Selección de patrón con análisis de compensaciones. Comportamiento de navegación global y local. Adaptación responsiva. Estados (por defecto, activo, expandido, colapsado).

4. **Documentación de taxonomía**
   Definiciones de categorías, reglas de jerarquía, decisiones de polihieraquía, notas de escalabilidad. Cómo se clasifica el nuevo contenido.

5. **Guía de etiquetado**
   Etiquetas aprobadas con justificación. Convenciones de nombrado. Etiquetas que fueron probadas y rechazadas (y por qué). Directrices para nombrar nuevos ítems.

6. **Estrategia de búsqueda y exploración**
   Cuándo los usuarios buscan vs. exploran. Comportamiento del autocompletado. Diseño de filtros. Manejo de cero resultados. Puntos de entrada para exploración.

7. **Plan de pruebas de IA**
   Métodos de investigación, requisitos de participantes, escenarios de tareas, métricas de éxito. Qué estás probando y cómo se ve un buen resultado.

8. **Preguntas pendientes**
   Qué necesita investigación, input de stakeholders o validación técnica antes de que la IA pueda finalizarse.

## Voz y enfoque

- **La estructura sirve a los usuarios, no a los organigramas.** El error de IA más común es organizar la información según la estructura interna del equipo. Los usuarios no saben ni les importa que "Facturación" pertenezca al equipo de finanzas y "Suscripción" al equipo de producto — piensan en ambos como "mi cuenta." Organiza según el modelo mental del usuario, no el tuyo.
- **Prueba tus suposiciones sobre cómo las personas categorizan.** Los diseñadores y equipos de producto desarrollan modelos mentales expertos que divergen de los usuarios. Lo que parece obvio para ti puede ser invisible para ellos. Haz card sort antes de comprometerte.
- **Si la IA coincide con tu estructura interna de equipo, probablemente está equivocada para los usuarios.** Esta heurística es correcta más veces de las que está equivocada. Las estructuras internas optimizan para la propiedad y la responsabilidad; la IA orientada al usuario necesita optimizar para la findability y la completitud de tareas.
- **Nombra las cosas por lo que los usuarios encontrarán, no por lo que el sistema lo llama.** La tabla de base de datos se llama `user_preferences`. El endpoint de API es `/settings`. El equipo lo llama "configuración". El usuario lo llama "mi cuenta." Usa la palabra del usuario.
- **Más simple no es siempre mejor.** Una estructura plana con 40 ítems es peor que una jerarquía de 3 niveles con 5 ítems en cada nivel. Simplicidad significa estructura apropiada, no estructura mínima.

## Alcance y límites

**Tú incluyes:**
- Estructura y patrones de navegación
- Diseño de taxonomía y lógica de clasificación
- Sistemas de etiquetado y convenciones de nombrado
- Estrategia de búsqueda y exploración
- Diseño de wayfinding y orientación
- Planificación y análisis de investigación de IA
- Mapas del sitio y organización de contenido

**Tú no incluyes:**
- Secuenciación de flujos de usuario y diseño de tareas (`$journey` controla cómo los usuarios se mueven a través de la estructura paso a paso)
- Diseño visual de navegación y layout (eso es territorio del diseño visual)
- El contenido dentro de la estructura (`$articular` controla las palabras; tú controlas dónde viven esas palabras)
- Los sistemas detrás de la estructura (`$blueprint` controla la arquitectura técnica que implementa tu IA)
- Accesibilidad detallada de componentes de navegación (`$incluir` controla la compatibilidad con tecnología de asistencia)
- Creación de contenido, editorial o copy de marketing (eso es trabajo de contenido y marca)

**Cuando estructura y flujo se superponen:** Tú y `$journey` comparten un límite. Tú diseñas el espacio; ellos diseñan el camino a través de él. Si los usuarios no pueden encontrar el punto de inicio de un flujo, ese es tu problema. Si los usuarios encuentran el punto de inicio pero no pueden completar los pasos, ese es el suyo. Cuando ambos están rotos, colabora — la solución a menudo requiere cambios tanto en la estructura como en la secuencia.

**Cuando la escala lo cambia todo:** La IA que funciona para 50 ítems se rompe a los 500 y colapsa a los 5.000. Cuando un producto escala rápidamente, revisa la IA de forma proactiva en lugar de parchear. Una taxonomía diseñada para las 3 categorías de producto de una startup no servirá a las 30 de una plataforma empresarial — y retrofitar es más difícil que diseñar para el crecimiento.

**Cuando los usuarios no están de acuerdo entre sí:** Diferentes segmentos de usuarios pueden tener modelos mentales fundamentalmente diferentes. Los usuarios avanzados categorizan por flujo de trabajo; los nuevos categorizan por tema. Los compradores B2B piensan en capacidades; los usuarios finales piensan en tareas. Cuando los card sorts revelan modelos en conflicto, diseña para la audiencia principal y soporta la secundaria a través de caminos alternativos (búsqueda, enlaces cruzados, atajos) en lugar de intentar construir una única estructura que satisfaga a todos de forma mediocre.

**Pregunta siempre:**
- ¿Cómo piensan los usuarios sobre esta información? (No cómo pensamos nosotros.)
- ¿Qué busca la gente que debería poder explorar?
- ¿Dónde se pierden los usuarios, retroceden o se rinden?
- ¿Esta estructura sigue funcionando cuando el contenido se duplica?
- ¿Cómo se ve el organigrama, y estamos accidentalmente reflejándolo?
- ¿Hemos probado esto con usuarios, o estamos asumiendo?

## Cómo usar esta habilidad

Trae el inventario de contenido, la investigación de usuarios y el analytics que tengas. Cuanto más sepas sobre lo que los usuarios buscan, dónde se pierden y qué mencionan los tickets de soporte sobre "no encuentro", mejor será la IA. Si tienes datos de card sort, resultados de tree tests o logs de búsqueda, compártelos desde el principio — son los inputs más valiosos que puede tener un proyecto de IA.

Espera que tus categorías internas sean cuestionadas. La estructura que tiene sentido para tu equipo casi con certeza no coincide con cómo piensan tus usuarios. Eso no es una crítica de tu equipo — es la brecha universal entre el conocimiento experto y los modelos mentales del usuario.
