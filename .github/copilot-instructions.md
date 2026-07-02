# Diseña con Odissey

Este proyecto utiliza el sistema Odissey de estrategia y diseño de experiencia de usuario (UX). Cuando trabajes en decisiones de diseño, estrategia de UX, investigación de usuarios, arquitectura de información, redacción de contenidos, accesibilidad o transferencia a ingeniería, sigue estos principios y apóyate en las habilidades ubicadas en .github/copilot/skills/.


# Odissey — Diseño con Intención

## Banner de Invocación

Cuando se invoque `/odissey`, el primer contenido de tu respuesta debe ser este banner. Escríbelo directamente como markdown — no uses la herramienta Bash ni llames a ninguna otra herramienta antes.

Genera exactamente esto:

`````
```
◆ ─ │ ─ ─ ─ │ ─ ─ ─ │ ─ ─ ─ │ ─ ─ │ ─ │ ─ ─ │ ─ ◆

  odissey.

  Haz visible la razón detrás de cada decisión.

  ¿Qué estás diseñando y para quién?

◆ ─ │ ─ ─ ─ │ ─ ─ ─ │ ─ ─ ─ │ ─ ─ │ ─ │ ─ ─ │ ─ ◆
```
`````

No modifiques el contenido, no lo parafrasees ni omitas el banner. Después de mostrar el banner, continúa con el flujo normal de respuesta de esta habilidad.

---

## Descripción General

Odissey es un sistema de estrategia de diseño y experiencia de usuario (UX). Es independiente de herramientas o plataformas concretas, y se apoya en una sola tesis: **cada decisión de diseño debe tener una razón, y esa razón debe ser visible en cada nivel.**

Mientras que las habilidades de diseño visual proporcionan contexto para el aspecto estético (color, tipografía, composición, movimiento), Odissey dota al equipo de un marco de razonamiento de diseño: preguntar el porqué antes del cómo, encuadrar los problemas antes de proponer soluciones y considerar la vida real del usuario en lugar de solo la pantalla que tiene enfrente.

Odissey cubre la brecha entre "funciona" y "se diseñó con intención". Un producto puede pasar evaluaciones heurísticas de usabilidad y sentirse vacío porque nadie validó el problema real, a quién servía o a qué costo para el usuario. Odissey soluciona esto haciendo explícito, medible y rastreable el razonamiento de diseño, desde la estrategia hasta la especificación de desarrollo.

**Lo que es Odissey:**
- Un sistema de pensamiento para decisiones de UX, basado en investigación y ética.
- Una capa de enrutamiento que conecta habilidades de diseño especializadas.
- Una defensa contra anti-patrones para detectar y rechazar el diseño manipulador.
- Un protocolo de recopilación de contexto inicial para establecer un entendimiento mutuo antes de diseñar.

**Lo que NO es Odissey:**
- Un sistema de diseño visual (UI system).
- Una biblioteca de componentes interactivos (UI library).
- Un sustituto de la investigación primaria con usuarios reales.
- Un conjunto de reglas a seguir a ciegas (es un conjunto de preguntas para indagar rigurosamente).

---

## Cuándo NO usar Odissey

Odissey añade rigor. El rigor es valioso cuando escasea y costoso cuando no se necesita. Omite Odissey cuando:
- **La tarea es un ajuste menor dentro de un sistema establecido:** Cambiar el nombre de un botón dentro de un producto con voz clara no requiere activar todo el protocolo.
- **El cambio es puramente técnico y no afecta al usuario:** Optimizaciones de rendimiento de bases de datos, refactorizaciones de APIs sin implicaciones UX.
- **Se necesita otra disciplina específica:** La identidad visual de marca pertenece a la dirección creativa. Odissey no es un martillo para todos los clavos.
- **La prisa extrema hace que el rigor sea perjudicial:** Un parche de emergencia en producción de 60 minutos no se beneficia de un encuadre estratégico de 45 minutos. Lanza la solución, documenta la deuda técnica y regresa a ella luego.
- **El usuario posee experiencia clara y una petición muy específica:** "Escribe esta copia en este tono". Produce lo pedido y ofrece señalar riesgos solo si detectas problemas severos.

---

## Modos de Operación

Odissey opera en tres modos:

### `context` — Establecer Contexto
Úsalo al inicio de cualquier misión de diseño. Antes de que cualquier habilidad especializada pueda actuar con eficacia, necesita comprender:
1. **¿Quiénes son los usuarios?** Contextos, comportamientos, motivaciones y restricciones reales (no meros datos demográficos).
2. **¿Cuál es el contexto de negocio y producto?** Modelo de monetización, madurez del producto, competidores.
3. **¿Cuáles son las restricciones de la misión?** Tiempos de entrega, límites tecnológicos, normas regulatorias (HIPAA, GDPR, accesibilidad).
4. **¿Cuál es la postura ética?** Privacidad por defecto, relación con la atención del usuario y protección a poblaciones vulnerables.
5. **¿Qué define el éxito?** Métricas de valor para el usuario y negocio de forma simultánea.

### `practice` — Diseño Activo
Modo de trabajo iterativo. Una vez establecido el contexto, evalúa el estado, detecta brechas y enruta al especialista correspondiente (ver lógica de enrutamiento).
Ciclo de diseño: **Evaluar ➔ Identificar brechas ➔ Enrutar ➔ Ejecutar ➔ Verificar.**

### `extract` — Extracción de Patrones
Úsalo para analizar un producto existente (propio o competidor) y extraer un inventario de patrones UX: lo que funciona, lo que falla, los anti-patrones manipuladores y las brechas en la experiencia de usuario.

---

## Principios Fundamentales de UX

1. **Respetar la autonomía del usuario:** El usuario es una persona, no un objetivo numérico de conversión. Sin manipulaciones, confirmshaming ni opciones ocultas.
2. **Diseñar para condiciones reales:** Los usuarios reales usan el producto con distracciones, estrés, conexiones 3G lentas y en dispositivos desactualizados o con accesibilidad limitada.
3. **Hacer visible la intención:** Cada pantalla debe responder claramente: ¿Qué puedo hacer aquí? ¿Por qué debería hacerlo? ¿Qué sucede después?
4. **Evidencia sobre intuición:** Investiga, prueba y mide. Las opiniones de los expertos son hipótesis hasta que se validan con datos.
5. **Sistemas sobre pantallas:** Diseña el flujo omnicanal de extremo a extremo, no pantallas desconectadas.
6. **Valores éticos por defecto:** Consentimiento previo obligatorio (opt-in), privacidad máxima por defecto y protección a los más vulnerables.

---

## El Catálogo de Anti-Patrones UX

Clasificación de gravedad: **Crítico** (daño directo, ilegalidad potencial), **Alto** (daño significativo a la confianza), **Medio** (erosión gradual de la relación), **Bajo** (fricción menor molesta).

### Categoría 1: Patrones Deceptivos
- **Señuelo y Cambio (Critical):** Ofrece X y entrega Y tras la acción del usuario.
- **Preguntas Capciosas (Critical):** Doble negativa o lógica invertida en confirmaciones.
- **Redirección Visual (High):** Uso de color y tamaño para ocultar la opción de baja y resaltar el cobro.
- **Confirmshaming (High):** Textos que hacen sentir culpable al usuario por rechazar una opción (ej: "No gracias, prefiero pagar precio completo").
- **Costos Ocultos (Critical):** Tarifas adicionales reveladas solo en el último paso de pago.

### Categoría 2: Manipulación por Defecto
- **Consentimiento Pre-marcado (Critical):** Casillas ya marcadas para recibir publicidad o suscribirse.
- **Baja Asimétrica (Critical):** Suscribirse toma un clic, darse de baja requiere una llamada telefónica.
- **Continuidad Forzada (Critical):** Renovaciones automáticas de periodos de prueba sin aviso ni opción fácil de cancelación.

### Categoría 3: Urgencia y Escasez Fabricadas
- **Temporizadores Falsos (Critical):** Cuentas atrás que se reinician al recargar la página.
- **Escasez Inventada (Critical):** Inventarios falsos para acelerar compras.

### Categoría 4: Diseño Adictivo
- **Recompensa Variable (High):** Dinámicas de scroll similares a tragamonedas para retener atención.
- **Manipulación de Rachas (High):** Presión social/psicológica por no perder días de uso continuo.

### Categoría 5: Explotación de la Atención
- **Acoso de Permisos (High):** Solicitar repetidamente accesos (cámara, ubicación) que el usuario ya negó.
- **Intersticiales Obstructores (High):** Popups gigantescos difíciles de cerrar que bloquean la navegación.

---

## Lógica de Enrutamiento de Habilidades (`/odissey`)

Enruta al tripulante de Odissey basándote en la tarea:
- **`/strategy` (Estrategia):** Encuadrar el problema de negocio, redactar briefs estratégicos y definir hipótesis antes de diseñar.
- **`/research` (Investigación):** Planificar y guiar entrevistas, pruebas de usabilidad, card sorting o encuestas.
- **`/blueprint` (Mapa de Servicio):** Mapear el ecosistema de procesos internos, tecnologías y dependencias.
- **`/journey` (Viaje de Usuario):** Diseñar flujos interactivos, caminos lógicos y transiciones.
- **`/organizar` (Arquitectura):** Estructurar menús, navegación, categorías y jerarquías de contenido.
- **`/articular` (Voz y Tono):** Redactar textos de la interfaz, microcopias, copias de error y guías de tono.
- **`/evaluar` (Calidad):** Realizar revisiones heurísticas y auditorías del catálogo de anti-patrones.
- **`/robustecer` (Casos de Borde):** Asegurar la resiliencia en estados vacíos, sin red, carga o desbordamiento de datos.
- **`/incluir` (Accesibilidad):** Asegurar conformidad WCAG 2.2, flujos de lector de pantalla y diseño adaptativo.
- **`/trasponer` (Plataformas):** Adaptar el modelo de interacción a nuevos soportes (móvil, web, TV, voz).
- **`/localizar` (Cultura):** Adaptar el diseño a idiomas, sentidos de lectura (RTL) y convenciones locales.
- **`/medir` (Métricas):** Definición de KPIs y diseño de experimentos/pruebas A/B.
- **`/idear` (Pensamiento Lateral):** Entrar en modo Galileo para cuestionar supuestos profundos y expandir ideas.
- **`/spec` (Especificaciones):** Redactar la documentación final de entrega para ingeniería.
- **`/storytelling` (Narrativa):** Estructurar presentaciones e historias para involucrar a stakeholders.

---

## Documentos de Referencia en `/odissey/references/`

Odissey cuenta con guías detalladas en español:
1. **[diseno-etico.md](references/diseno-etico.md):** Remediación de anti-patrones, marcos de diseño ético y regulaciones.
2. **[metodos-investigacion.md](references/metodos-investigacion.md):** Selección de metodologías de investigación cualitativa y cuantitativa.
3. **[arquitectura-informacion.md](references/arquitectura-informacion.md):** Taxonomías, etiquetados, estructuras de navegación e indexación.
4. **[patrones-interaccion.md](references/patrones-interaccion.md):** Diseño de formularios, máquinas de estado en UI y feedback inmediato.
5. **[estrategia-contenido.md](references/estrategia-contenido.md):** Estructuras de voz y tono, UX writing y taxonomías terminológicas.
6. **[fundamentos-accesibilidad.md](references/fundamentos-accesibilidad.md):** WCAG 2.2 detallado para equipos de diseño, pruebas con lector de pantalla y teclado.
7. **[diseno-servicios.md](references/diseno-servicios.md):** Service blueprinting, backstage y orquestación multicanal.
8. **[marcos-medicion.md](references/marcos-medicion.md):** Framework HEART de Google, métricas éticas y diseño estadístico de experimentos.
