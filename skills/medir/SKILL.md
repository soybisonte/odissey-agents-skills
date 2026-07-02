---
name: medir
description: >
  Define y realiza seguimiento del éxito UX mediante métricas, marcos de medición
  y experimentación. Parte del sistema de estrategia de diseño Odissey.
  Conecta las decisiones de diseño con evidencia observable — ¿lo que construimos
  realmente ayudó? Protege contra que la medición se convierta en manipulación.
  Activa cuando: defines criterios de éxito, diseñas A/B tests, construyes
  marcos de medición, analizas funnels, revisas dashboards de métricas,
  cuestionas si se están midiendo las cosas correctas, o cuando alguien dice
  "¿cómo sabemos si esto funcionó?", "¿qué deberíamos medir?",
  "lancemos un test" o "los números se ven bien pero algo no cuadra".
  También activa para revisiones de medición ética y definición de contra-métricas.
version: 1.5.0
user-invocable: true
---

# Medir — Definir y Seguir el Éxito

## Visión general

Si no puedes definir el éxito, no puedes diseñar para él. Y si mides la cosa equivocada, optimizarás el resultado equivocado.

La medición UX conecta las decisiones de diseño con evidencia observable: ¿lo que construimos realmente ayudó? Esta habilidad define qué medir, cómo medirlo y cómo tomar decisiones a partir de lo que aprendes. Cierra la brecha entre "lo lanzamos" y "funcionó".

Pero la medición no es neutral. Cada métrica que eliges moldea lo que se optimiza. Mide tiempo en el sitio y obtendrás scroll infinito. Mide clics y obtendrás clickbait. Mide conversión y obtendrás dark patterns, a menos que también midas lo que esas métricas le cuestan al usuario. Esta habilidad evita que la medición se convierta en manipulación y asegura que las métricas incentiven valor genuino, no engagement fabricado.

**Activa esta habilidad cuando haya:** definición de criterios de éxito para una nueva funcionalidad, diseño de experimentos, construcción de marcos de medición, análisis de funnels, revisión de dashboards de métricas, cuestionamiento de si se está midiendo lo correcto o cualquier momento en que "los números se ven bien" pero la experiencia se siente mal.

---

## Familia de habilidades

Medir trabaja junto al sistema completo de habilidades Odissey:

- **`/strategy`**: Sus hipótesis necesitan criterios de éxito medibles. Cada apuesta estratégica debe conectarse a una métrica que indique si la apuesta dio resultado. `/strategy` define "creemos que X"; `/medir` define "sabremos que X es cierto cuando Y." Cuando las métricas contradicen un supuesto estratégico, medir vuelve a abrir strategy — con salvaguardas (ver "Cuando la medición apunta de vuelta a la estrategia" a continuación).
- **`/research`**: La investigación cualitativa complementa la medición cuantitativa. Cuando los números muestran una caída en el paso 3, research te dice por qué. Cuando los scores de satisfacción caen tras un rediseño, research entrevista a usuarios para entender la experiencia detrás del número. Nunca tomes decisiones de diseño importantes solo a partir de métricas.
- **`/evaluar`**: La evaluación UX produce scores y hallazgos que informan qué medir. La evaluación identifica problemas de usabilidad; la medición rastrea si las correcciones realmente los resolvieron.
- **`/spec`**: Los planes de prueba y los criterios de éxito van en los specs de handoff. Cada spec de funcionalidad debería incluir cómo se ve el éxito y cómo medirlo, para que ingeniería pueda instrumentar en consecuencia.
- **`/idear`**: Un modo cognitivo transversal para cuestionar tus métricas antes de que se conviertan en objetivos. Activa cuando: una métrica parece demasiado fácil de manipular, el dashboard luce verde pero los usuarios se están quejando, no estás seguro de si estás midiendo el éxito del usuario o la extracción del negocio, o necesitas la pregunta: "¿Qué pasa si medir esto cambia el comportamiento que intentamos medir?"

---

## Capacidades principales

### 1. Selección de métricas: marco HEART

El marco HEART de Google proporciona un enfoque estructurado para seleccionar métricas UX. Aplícalo por funcionalidad, no globalmente — diferentes funcionalidades necesitan diferentes métricas.

**Happiness (Satisfacción subjetiva):**
- NPS (Net Promoter Score): probabilidad de recomendar, escala 0-10. Contundente pero útil para tendencias.
- CSAT (Satisfacción del cliente): satisfacción con una interacción específica, habitualmente escala 1-5. Más accionable que NPS para decisiones a nivel de funcionalidad.
- SUS (System Usability Scale): cuestionario estandarizado de usabilidad de 10 preguntas. Bueno para benchmarking entre versiones.
- Encuestas personalizadas: preguntas específicas vinculadas a funcionalidades específicas. "¿Qué tan fácil fue encontrar lo que buscabas?" es más útil que "¿Qué tan satisfecho estás?"

**Engagement (Profundidad de uso):**
- Frecuencia: con qué frecuencia regresan los usuarios (usuarios activos diarios, semanales, mensuales)
- Intensidad: profundidad de uso por sesión (funcionalidades usadas, contenido consumido, acciones realizadas)
- Amplitud: cuántas funcionalidades toca un usuario (amplitud de adopción, no solo profundidad)
- Recencia: cuándo fue la última interacción (señal temprana de churn)

**Adoption (Nuevo uso):**
- Activación de nuevos usuarios: porcentaje que completa hitos clave de onboarding
- Adopción de funcionalidades: porcentaje de usuarios elegibles que prueban una nueva funcionalidad
- Completitud del onboarding: funnel a través de la experiencia de primer uso
- Tiempo hasta el valor: con qué rapidez los nuevos usuarios alcanzan su primer resultado significativo

**Retention (Uso continuado):**
- Tasa de retorno: retención D1, D7, D30 (porcentaje que regresa tras 1, 7, 30 días)
- Tasa de churn: porcentaje de usuarios que dejan de usar el producto en un período
- Reactivación: usuarios que se fueron y volvieron (¿qué los trajo de vuelta?)
- Retención por cohorte: curvas de retención por cohorte de registro (¿los usuarios más recientes retienen mejor?)

**Task success (Efectividad):**
- Tasa de completitud: porcentaje de usuarios que terminan la tarea que iniciaron
- Tasa de error: porcentaje de intentos que resultan en errores
- Tiempo en tarea: cuánto tarda la tarea (menos es generalmente mejor, pero no siempre)
- Eficiencia: completitud de tarea relativa a la longitud del camino óptimo

**No toda funcionalidad necesita las cinco dimensiones.** Selecciona las 2-3 dimensiones que más importan para el odissey de la funcionalidad. Un flujo de checkout se preocupa principalmente por el task success y la satisfacción. Un feed de contenido se preocupa principalmente por el engagement y la retención. El lanzamiento de una nueva funcionalidad se preocupa principalmente por la adopción.

**Contra-métricas:** Para cada métrica que optimizas, nombra la métrica que podría sufrir. Si el engagement sube pero la satisfacción baja, eso es una señal de alerta. Si la conversión mejora pero los tickets de soporte aumentan, algo está mal. Las contra-métricas son tu canario en la mina de carbón.

### 2. Mapeo Goal-Signal-Metric

El marco GSM evita que saltes directamente a métricas sin entender qué estás intentando realmente aprender.

**Goal (Objetivo):** ¿Qué resultado del usuario o del negocio intentas lograr? Sé específico. "Mejorar la experiencia de usuario" no es un objetivo. "Los usuarios pueden encontrar contenido relevante rápidamente sin explorar en exceso" es un objetivo.

**Signal (Señal):** ¿Qué comportamiento observable del usuario indicaría progreso hacia el objetivo? Este es el puente entre el odissey y los datos. "Los usuarios navegan directamente al contenido relevante" es una señal. "Los usuarios pasan más tiempo en el sitio" no es necesariamente una señal de éxito — podría significar que están perdidos.

**Metric (Métrica):** ¿Cómo cuantificas esa señal? Fórmula específica, fuente de datos, frecuencia de medición y umbral de éxito. "Mediana de clics hasta el contenido inferior a 3 para el percentil 80 de las sesiones, medido semanalmente a través de analytics" es una métrica.

**Ejemplo de cadena GSM:**
- Objetivo: los usuarios pueden completar el checkout sin fricción
- Señal: los usuarios avanzan por los pasos del checkout sin abandonar ni retroceder
- Métrica: tasa de completitud del checkout > 75% para usuarios que añaden artículos al carrito; tiempo mediano de checkout inferior a 90 segundos; tasa de navegación hacia atrás durante el checkout < 10%

**Construye cadenas GSM para cada funcionalidad importante antes del lanzamiento.** Si no puedes articular el objetivo, no sabes cómo se ve el éxito. Si no puedes identificar la señal, estás adivinando qué medir. Si no puedes definir la métrica, no puedes aprender de lo que lanzas.

### 3. Diseño de A/B tests

La experimentación es cómo aprendes si un cambio de diseño realmente ayuda. Pero los experimentos mal diseñados producen falsa confianza.

**Estructura de hipótesis:**
"Si [cambio específico], entonces [métrica específica] [dirección del cambio] en [magnitud estimada] porque [razonamiento causal]."

Ejemplo: "Si movemos la barra de búsqueda del encabezado a la sección hero, entonces el uso de búsqueda aumentará un 15% porque los usuarios la encontrarán antes en su patrón de escaneo, reduciendo la fricción de tener que desplazarse hacia arriba para buscar."

**Efecto mínimo detectable (MDE):**
¿Cuál es el cambio más pequeño que vale la pena detectar? Una mejora del 0,1% en la conversión puede no justificar el esfuerzo de ingeniería. Una mejora del 5% sí lo haría. Establece el MDE antes del test, no después. Esto determina el tamaño de muestra requerido.

**Cálculo del tamaño de muestra:**
Depende de: tasa de conversión base, MDE, poder estadístico (típicamente 80%), nivel de significancia (típicamente 95% / alpha = 0,05). No adivines — usa la fórmula o una calculadora.

**Referencia rápida para escenarios comunes** (test bilateral, 80% de poder, 95% de significancia, dos variantes):

| Tasa base | MDE (relativo) | Tamaño de muestra por variante |
|---|---|---|
| 5% | 20% (5% → 6%) | ~25.000 |
| 10% | 10% (10% → 11%) | ~14.500 |
| 10% | 20% (10% → 12%) | ~3.800 |
| 25% | 10% (25% → 27,5%) | ~4.800 |
| 50% | 5% (50% → 52,5%) | ~6.000 |

Las tasas base más bajas y los MDE más pequeños requieren dramáticamente más tráfico. Si el tamaño de muestra requerido supera tu tráfico mensual, aumenta el MDE (detecta solo efectos mayores), extiende la duración del test, o acepta que un A/B test no es el método correcto — usa investigación cualitativa en su lugar. Los tests con poco poder producen resultados no concluyentes que desperdician tiempo.

**Duración:**
Ejecuta durante al menos 1-2 ciclos semanales completos para tener en cuenta los efectos del día de la semana. Más tiempo para negocios estacionales. Nunca ejecutes menos de una semana aunque alcances el tamaño de muestra antes — los patrones de comportamiento varían por día.

**Segmentación:**
Verifica efectos diferenciales entre segmentos de usuarios: usuarios nuevos vs. recurrentes, móvil vs. escritorio, geografía, tipo de plan. Un resultado global neutro puede ocultar un efecto positivo fuerte para un segmento y uno negativo fuerte para otro.

**Métricas de salvaguarda:**
Define qué NO debe empeorar. Si pruebas un nuevo flujo de checkout, las métricas de salvaguarda podrían incluir: ingresos por usuario, volumen de tickets de soporte, tasa de devoluciones. Si la variante del test mejora la conversión pero aumenta las devoluciones, el test ha fallado.

**Errores comunes:**
- Mirar los resultados antes de que el test alcance significancia estadística (infla la tasa de falsos positivos)
- Ejecutar demasiadas variantes sin ajustar para comparaciones múltiples
- Ignorar los efectos de novedad (las cosas nuevas reciben más clics simplemente porque son nuevas — espera a que el efecto se estabilice)
- Detener tests demasiado pronto porque los resultados tempranos "parecen decisivos"
- No tener en cuenta los efectos de interacción cuando varios tests se ejecutan simultáneamente
- Probar cambios cosméticos cuando el problema real es estructural

### 4. Análisis de funnels

Los funnels revelan dónde los usuarios abandonan un flujo deseado. Pero el valor no está en los números — está en entender por qué.

**Define los pasos con precisión:**
¿"Añadir al carrito" es el clic en el botón o la adición confirmada? ¿"Checkout" es el inicio del formulario de pago o el envío? Las definiciones imprecisas de pasos producen tasas de conversión engañosas. Define cada paso como un evento específico, observable e inequívoco.

**Mide la conversión entre cada paso:**
Paso 1 → Paso 2: ¿qué porcentaje avanza? ¿Qué porcentaje regresa a un paso anterior? ¿Qué porcentaje se va completamente? Cada transición cuenta una historia diferente.

**Identifica las mayores caídas:**
Enfócate en las transiciones entre pasos con las tasas de conversión más bajas. Una caída del 40% entre "ver producto" y "añadir al carrito" es un problema diferente a una caída del 40% entre "ingresar pago" y "confirmar pedido."

**Segmenta por todo:**
Tipo de usuario (nuevo vs. recurrente), dispositivo, fuente de tráfico, geografía, hora del día, día de la semana. Los funnels agregados ocultan la señal. Un funnel que convierte al 30% en general podría convertir al 50% para usuarios recurrentes en escritorio y al 10% para nuevos usuarios en móvil — dos problemas completamente diferentes.

**Combina con cualitativo:**
Cuando encuentras la caída, sabes DÓNDE luchan los usuarios. Para entender POR QUÉ, combina con `/research` — grabaciones de sesión, pruebas de usabilidad, encuestas en el punto de fricción. Los números sin contexto producen intervenciones incorrectas.

**Benchmarking:**
Compara funnels entre períodos de tiempo (¿la última versión ayudó o perjudicó?), entre segmentos (¿quién lucha más?), y con cautela frente a benchmarks de la industria (útil para verificaciones de orden de magnitud, peligroso para objetivos específicos).

### 5. Triangulación cualitativa y cuantitativa

Los números te dicen QUÉ ocurrió. Lo cualitativo te dice POR QUÉ. Ninguno por sí solo es suficiente para las decisiones de diseño.

**Cuándo triangular:**
- Las métricas muestran una caída pero no sabes por qué → realiza sesiones de usabilidad en el punto de fricción
- Los scores de satisfacción caen tras un rediseño → entrevista a usuarios para entender qué cambió en su experiencia
- El A/B test no muestra diferencia estadística → la investigación cualitativa revela que ambas variantes tenían el mismo problema fundamental de usabilidad
- La adopción de una funcionalidad es baja → ¿es un problema de descubribilidad, de utilidad o de usabilidad? Solo lo cualitativo puede distinguirlos.

**Cómo triangular:**
- Empieza con cuantitativo para identificar QUÉ y DÓNDE
- Usa cualitativo para entender POR QUÉ
- Vuelve al cuantitativo para verificar que tu intervención abordó el POR QUÉ
- Repite

**Nunca tomes decisiones de diseño importantes a partir de un solo tipo de dato.** Una métrica que dice "la conversión mejoró un 5%" no te dice si la mejora vino de una creación de valor genuina o de añadir fricción al camino alternativo. Una prueba de usabilidad donde 5 personas tuvieron dificultades no te dice cuán extendido está el problema. Ambos juntos te dicen algo real.

### 6. Medición ética

Las métricas moldean el comportamiento — de los equipos, de los productos y de los usuarios. Mide con cuidado.

**Ley de Goodhart:**
"Cuando una medida se convierte en un objetivo, deja de ser una buena medida." Esto no es una preocupación teórica. Cuando los equipos tienen incentivos sobre el tiempo en el sitio, construyen scroll infinito y autoplay. Cuando los incentivos son sobre registros, construyen muros de registro engañosos. Cuando los incentivos son sobre engagement, construyen spam de notificaciones. La métrica no falló — la métrica se convirtió en el objetivo en lugar de ser un proxy del objetivo.

**El engagement no equivale a valor:**
El alto engagement puede señalar adicción, no satisfacción. Un usuario que revisa su teléfono 200 veces al día está comprometido. También puede estar ansioso, distraído e infeliz. Incluye métricas de satisfacción junto a las métricas de engagement. Si el engagement sube pero la satisfacción baja, estás construyendo una máquina tragamonedas, no un producto útil.

**Patrones de métricas oscuras a vigilar:**
- Contar registros "exitosos" en newsletters desde casillas premarcadas
- Medir "engagement" de notificaciones molestas que los usuarios hacen clic para descartar
- Celebrar "retención" que en realidad es fricción en la cancelación
- Reportar "conversión" de etiquetas de botones engañosas o temporizadores de urgencia
- Rastrear "tiempo en el sitio" impulsado por navegación confusa

**Conexión con el catálogo de anti-patrones de Odissey:**
Cualquier métrica que mejoraría al implementar un dark pattern está midiendo la cosa equivocada. Antes de celebrar una mejora de métrica, pregunta: ¿podría esta mejora haberse logrado mediante un dark pattern? Si la respuesta es sí, verifica que no fue así.

**Marco de alternativa ética:**
Mide la satisfacción del usuario, la completitud de tareas y el esfuerzo junto a cada métrica de negocio. Construye un dashboard de medición con dos columnas: resultados de negocio y resultados de usuario. Si las métricas de negocio mejoran mientras las métricas de experiencia de usuario declinan, esa es una señal de dark pattern — incluso si nadie lo pretendió.

- Métrica de negocio: tasa de conversión → Métrica de usuario asociada: satisfacción post-compra
- Métrica de negocio: engagement (DAU) → Métrica de usuario asociada: valor percibido por el usuario
- Métrica de negocio: retención → Métrica de usuario asociada: facilidad de cancelación
- Métrica de negocio: ingresos por usuario → Métrica de usuario asociada: valor percibido por el dinero

---

## Cuando la medición apunta de vuelta a la estrategia

La medición no solo fluye después de la estrategia. También puede reabrir la estrategia cuando la evidencia contradice un supuesto estratégico. Los disparadores a continuación son específicos de la medición; las reglas generales de retroalimentación — punto de control humano, presupuesto de ciclos, condición de salida escrita — viven en `/odissey` bajo "Loop-backs and exit conditions."

### Disparadores para reabrir `/strategy` desde las métricas

- **Contradicción de audiencia.** El análisis de segmentos revela que la audiencia principal que usa el producto no es la audiencia que la estrategia asumió.
- **Fallo de validación de funcionalidad.** Las métricas de adopción muestran que una funcionalidad supuestamente central no se usa mientras que una funcionalidad supuestamente periférica se usa intensamente.
- **Fallo de ajuste de solución.** La caída no está en el flujo que optimizaste — está antes del flujo. Los usuarios no están llegando al producto de la manera que la estrategia asumió.
- **Ley de Goodhart activada.** La métrica principal mejoró, la contra-métrica se deterioró, y la investigación cualitativa confirma que los usuarios están peor.
- **Error de conteo de oportunidad.** La disposición a pagar medida, la frecuencia de uso o el alcance son un orden de magnitud por debajo de la estimación estratégica.

### No son disparadores — falsos positivos comunes

- **Resultados ligeramente por debajo de la proyección** — la dirección importa más que la magnitud.
- **Métricas tempranas de efectos de novedad o estacionales** — espera 2+ ciclos semanales para estabilizarte.
- **Un segmento de bajo rendimiento** — puede justificar trabajo específico por segmento, no una reapertura completa de la estrategia.

### Cómo reabrir de forma responsable

1. **Nombra el supuesto estratégico que la métrica contradice.** No "los usuarios no están convirtiendo" — "asumimos que [audiencia X con motivación Y] era la principal, pero los datos muestran [Z]."
2. **Trae evidencia, no conclusiones.** Métrica, contra-métrica, señal cualitativa y el supuesto original. Deja que `/strategy` reencuadre — no lo pre-encuadres.
3. **Pide al usuario que autorice la reapertura.** La medición puede revelar que la estrategia puede estar equivocada; solo el humano con contexto de negocio decide si la estrategia debe cambiar.

### Condición de parada

Como máximo una reapertura de estrategia por iteración de proyecto basada en métricas post-lanzamiento. Una segunda reapertura señala problemas de encuadre que el usuario debe resolver — deja de analizar y presenta la tensión directamente.

---

## Formato de entregable

### Marco de medición (mapa GSM)
Cadenas Goal-Signal-Metric para cada funcionalidad o iniciativa importante, incluyendo contra-métricas y consideraciones éticas.

### Plantilla de plan de A/B test
Hipótesis, variantes, métrica principal, métricas de salvaguarda, cálculo de tamaño de muestra, duración, plan de segmentación, criterios de decisión (qué resultado implica qué acción).

### Plantilla de análisis de funnel
Definiciones de pasos, tasas de conversión, dimensiones de segmentación, análisis de caídas, plan de investigación cualitativa para los principales puntos de fricción.

### Especificación del dashboard de métricas
Qué métricas, cómo se muestran, frecuencia de actualización, umbrales de alerta, audiencia (quién lo ve y qué decisiones toma a partir de él).

### Plan de aprendizaje
Cadencia de medición post-lanzamiento: qué medir al día 1, semana 1, mes 1, trimestre 1. Cuándo hacer seguimiento, qué buscar, cuándo declarar éxito o pivotar.

---

## Voz y enfoque

Preciso sobre lo que los datos demuestran y lo que no. "Los datos sugieren" no "los datos prueban." La significancia estadística no significa significancia práctica. Un p-valor por debajo de 0,05 significa que el resultado es improbable que se deba al azar — no significa que el resultado importe.

Transparente sobre las limitaciones. Tamaño de muestra, sesgo de selección, sesgo de supervivencia, variables de confusión — nómbralos. La incertidumbre honesta es más útil que la falsa confianza.

Resistir la falsa certeza. Cuando los datos son ambiguos, dilo. Cuando la muestra es demasiado pequeña, dilo. Cuando necesitas investigación cualitativa para interpretar los números, dilo. La métrica más peligrosa es la que parece concluyente pero no lo es.

Abogar por medir lo que importa a los usuarios, no solo lo que es fácil de rastrear. Los clics son fáciles de contar. La satisfacción es más difícil. La completitud de tareas es significativa. El tiempo en el sitio es ambiguo. Aboga por las métricas que reflejan el éxito del usuario, incluso cuando son más difíciles de instrumentar.

---

## Alcance y límites

### Esta habilidad incluye:
- Selección de métricas y diseño del marco de medición
- Diseño de A/B tests y metodología de experimentación
- Metodología y plantillas de análisis de funnels
- Guía de medición ética y definición de contra-métricas
- Mapeo GSM y creación de planes de aprendizaje

### Esta habilidad NO incluye:
- Implementación de analytics e instrumentación (ingeniería)
- Ejecución de investigación cualitativa (`/research`)
- Encuadre estratégico y generación de hipótesis (`/strategy`)
- Evaluación UX y evaluación heurística (`/evaluar`)
- Diseño visual del dashboard (diseño visual)
- Ejecución de análisis estadístico (ciencia de datos)
