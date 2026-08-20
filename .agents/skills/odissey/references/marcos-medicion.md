# Marcos de medición

## Índice

- [Marco HEART](#marco-heart)
- [Mapeo Goal-Signal-Metric](#mapeo-goal-signal-metric)
- [Cultura estadística para diseño](#cultura-estadística-para-diseño)
- [Diseño de pruebas A/B](#diseño-de-pruebas-ab)
- [Medición ética](#medición-ética)

## Marco HEART

Desarrollado en Google por Kerry Rodden, Hilary Hutchinson y Xin Fu, el marco HEART proporciona una forma estructurada de definir métricas centradas en las personas a cualquier escala, desde una función hasta un producto completo.

### Las cinco dimensiones

**Happiness — Satisfacción.** Satisfacción subjetiva, actitudes y facilidad de uso percibida. Se mide mediante encuestas —CSAT, SUS, NPS—, preguntas de satisfacción dentro del producto y comentarios cualitativos.

Lo que detecta y otras métricas omiten: un producto puede registrar muchas tareas completadas y aun así generar poca satisfacción si el proceso resulta tedioso, condescendiente o estresante. Esta dimensión captura la calidad emocional de la experiencia.

Lo que no detecta: una persona satisfecha no siempre logra su objetivo. Un producto puede ser agradable y no aportar valor. La satisfacción sin éxito de la tarea es entretenimiento, no utilidad.

**Engagement — Interacción.** Profundidad y frecuencia con que se usa el producto. Se mide con frecuencia y duración de sesiones, uso de funciones, acciones por sesión y consumo de contenido.

Lo que detecta: si el producto aporta valor suficiente para volver e invertir tiempo. Distingue «se registró y no regresó» de «lo usa a diario».

Qué vigilar: la interacción puede inflarse mediante patrones adictivos —desplazamiento infinito, exceso de notificaciones o refuerzo de razón variable—. Una cifra alta basada en manipulación no es éxito, sino explotación. Combínala siempre con satisfacción y éxito de tareas para distinguir interacción saludable de consumo compulsivo.

**Adoption — Adopción.** Personas que empiezan a usar un producto o una función. Se mide con registros, activación —primer uso significativo, no solo crear la cuenta—, conversiones de plan y descubrimiento de funciones nuevas.

Lo que detecta: si el crecimiento ocurre y si las funciones nuevas se descubren y utilizan. Responde: ¿llegamos a nuevas personas y encuentran valor?

Lo que no detecta: adopción sin retención es un recipiente con fugas. Muchos registros y poca retención al día 7 indican que la adquisición funciona, pero el producto no.

**Retention — Retención.** Personas que vuelven a lo largo del tiempo. Se mide mediante curvas de retención en los días 1, 7 y 30, abandono, reactivación y renovación de suscripciones.

Lo que detecta: si el producto mantiene su valor. La retención es un indicador fuerte del ajuste producto-mercado: quien vuelve encontró un motivo para hacerlo.

Qué vigilar: costes de cambio, dependencia de los datos o dificultad para cancelar pueden inflarla sin aportar valor genuino. Una persona que conserva una suscripción porque no logra cancelarla está retenida, pero no satisfecha. Combina retención y satisfacción para diferenciar retención saludable de cautividad.

**Task Success — Éxito de la tarea.** Capacidad para completar de manera correcta y eficiente el objetivo previsto. Se mide con tasa de finalización, tiempo por tarea, errores, abandono y volumen de solicitudes de soporte.

Lo que detecta: si el producto sirve para lo que las personas necesitan. Es la medida más directa de calidad UX: responde «¿pueden usar esto para alcanzar sus objetivos?».

Lo que no detecta: eficiencia sin satisfacción. Completar una tarea con frustración, confusión o falta de respeto no equivale a completarla con fluidez.

### Aplicar HEART según el tipo de función

| Tipo de función | Dimensión principal | Dimensiones secundarias |
|-----------------|---------------------|-------------------------|
| Flujo principal —pago, creación de archivos, mensajería— | Éxito de la tarea | Satisfacción, Interacción |
| Incorporación | Adopción | Éxito de la tarea, Retención —día 1— |
| Funciones sociales | Interacción | Retención, Satisfacción |
| Contenido / descubrimiento | Interacción | Satisfacción, Adopción —nuevas áreas— |
| Ajustes / configuración | Éxito de la tarea | Satisfacción |
| Monetización | Adopción —conversión— | Retención —renovación—, Satisfacción |
| Soporte / ayuda | Éxito de la tarea —resolución— | Satisfacción |

---

## Mapeo Goal-Signal-Metric

HEART indica qué dimensiones medir. Goal-Signal-Metric (GSM) explica cómo convertir cada dimensión en métricas concretas y observables. Se desarrolló como parte de HEART en Google.

### Las tres capas

**Goal — Objetivo:** ¿Qué se quiere conseguir? Exprésalo como resultado para las personas, no como resultado de negocio. «Las personas encuentran contenido relevante con rapidez», no «aumentar las páginas vistas».

**Signal — Señal:** ¿Qué comportamiento indicaría que el objetivo se cumple o no? Una señal es observable y se relaciona con el resultado. «La persona encuentra lo que busca en el primer intento» es una señal. Puede ser positiva —indica éxito— o negativa —indica fallo—.

**Metric — Métrica:** ¿Cómo se cuantifica la señal a escala? Es la medida específica que la representa: «Porcentaje de sesiones de búsqueda en las que se selecciona un resultado de la primera página».

### Ejemplo GSM: función de búsqueda

| Capa | Contenido |
|------|-----------|
| **Objetivo** | Las personas encuentran contenido relevante con rapidez |
| **Señales positivas** | Seleccionan un resultado, continúan la sesión tras buscar, no reformulan varias veces la misma consulta |
| **Señales negativas** | Abandonan sin seleccionar, buscan de inmediato con otros términos, contactan con soporte después de buscar |
| **Métricas** | Tasa de éxito —% de búsquedas con selección—, tasa de reformulación, tiempo hasta la primera selección, solicitudes de soporte que mencionan «no encuentro» |

### Errores frecuentes con GSM

**Empezar por las métricas, no por los objetivos.** «Debemos registrar usuarios activos diarios» no es un objetivo. Pregunta por qué interesa DAU y qué resultado para la persona reflejaría un cambio. Parte del objetivo y deriva la métrica.

**Señales que no representan el objetivo.** Mucho tiempo en una página puede indicar interés o desorientación. Muchos clics pueden significar curiosidad o una búsqueda frustrada del enlace correcto. Pregunta siempre qué explicaciones alternativas admite cada señal.

**Métricas sin línea de base.** «Mejoramos el éxito de búsqueda al 73 %» dice poco si no se conoce el valor anterior. «Pasó del 58 % al 73 % en seis semanas» permite interpretar el cambio.

**Métricas de vanidad.** Total de cuentas, páginas vistas o descargas: números que suelen crecer aunque la calidad no lo haga. Prefiere tasas —finalización, retención, error— y medidas por persona —sesiones por semana, acciones por sesión— que reflejen la experiencia.

---

## Cultura estadística para diseño

No hace falta ser especialista en estadística. Sí hace falta saber plantear preguntas, detectar errores evidentes y conversar con profesionales de datos y analítica.

### Tamaño de muestra

**Por qué importa:** Con muy pocas observaciones, una prueba no puede detectar diferencias reales; si se prolonga más de lo necesario, consume tiempo sin aportar información. El tamaño condiciona la fiabilidad de las conclusiones.

**Referencias prácticas para investigación cualitativa:**
- Pruebas de usabilidad: 5 personas por ronda —Nielsen—. Es preferible ejecutar varias rondas e iterar a aumentar una sola ronda.
- Entrevistas: 12–20 para buscar saturación temática en un grupo homogéneo —Guest et al., 2006—. Más segmentos requieren más entrevistas.
- Clasificación de tarjetas: 15–20 para ejercicios abiertos; 30 o más para cerrados con análisis cuantitativo.

Estas cifras son puntos de partida, no garantías universales. Ajusta según diversidad de segmentos, riesgo, complejidad de tareas y variación observada.

**Referencias prácticas para investigación cuantitativa:**
- Encuestas: 30 como mínimo para estadísticas básicas, más de 100 para segmentación y más de 400 para ciertas estimaciones poblacionales.
- Pruebas A/B: usa una calculadora de tamaño. Introduce conversión de base, efecto mínimo detectable, nivel de significación y potencia. No adivines.

### Significación estadística

**Qué significa:** Bajo un modelo y unos supuestos determinados, el valor p expresa qué tan compatibles son los datos observados con la hipótesis nula. Se usa de forma convencional `p < 0.05`, pero el umbral debe definirse antes del análisis y no equivale literalmente a «menos de 5 % de probabilidad de que la diferencia sea azar».

**Qué no significa:** Que el resultado sea importante, grande o útil. Una mejora de 0.1 % en clics puede ser estadísticamente significativa con una muestra enorme y, aun así, no justificar una decisión.

**Error frecuente:** Mirar resultados repetidamente y detener la prueba al ver significación, sin un método secuencial previsto. Esto aumenta los falsos positivos. Define tamaño y criterio de parada antes de empezar; espera a cumplirlos y después analiza.

### Intervalos de confianza

**Qué son:** Un intervalo calculado por un procedimiento que, al repetirse el muestreo, cubre el parámetro real con una frecuencia determinada. «Conversión: 4.2 %, IC del 95 % [3.8 %, 4.6 %]» comunica un rango compatible con los datos y el método, no una certeza absoluta sobre ese caso único.

**Por qué importan en diseño:** Expresan incertidumbre. «4.2 %» parece exacto; «entre 3.8 % y 4.6 %» recuerda que existen varios valores plausibles. Para comparar variantes, analiza directamente el intervalo de la diferencia o el método estadístico definido; el simple solapamiento de dos intervalos no es una prueba universal.

**Implicación:** Al presentar datos, incluye intervalos o una expresión explícita de incertidumbre. «Estimamos que el diseño mejora la conversión entre 1 y 3 puntos porcentuales» es más honesto y útil que «mejora 2.1 %» sin contexto.

### Tamaño del efecto

**Qué es:** Magnitud de una diferencia, separada conceptualmente del tamaño de muestra. Con suficientes observaciones se detectan diferencias diminutas; el tamaño del efecto indica si son suficientemente grandes para importar.

**Para diseño:** Una mejora estadísticamente detectable que nadie percibiría puede ser técnicamente real y prácticamente irrelevante. Pregunta si cambia la experiencia y si compensa el coste de implementación.

---

## Diseño de pruebas A/B

### Estructura de la hipótesis

Cada prueba debe comenzar con una hipótesis escrita, no con «probemos y veamos».

**Formato:** «Creemos que [cambio] provocará [efecto] porque [razonamiento]. Lo mediremos con [métrica] y lo consideraremos exitoso si [umbral]».

**Ejemplo:** «Creemos que reducir el pago de cinco pasos a tres aumentará la tasa de finalización, porque las pruebas de usabilidad mostraron abandonos en los pasos 3 y 4 por fatiga de formulario. Mediremos la finalización y consideraremos significativo para el producto un aumento de cinco puntos porcentuales, del 62 % al 67 %».

**Por qué importa:** Sin hipótesis no se distingue «la prueba no mostró diferencia» de «no sabíamos qué buscábamos». También evita justificar a posteriori que otra métrica era la importante.

### Efecto mínimo detectable (MDE)

Antes de ejecutar, decide cuál es la mejora mínima que justificaría implementar la variante.

Si la conversión base es 5 % y solo actuarías ante una mejora relativa de 10 % —de 5.0 % a 5.5 %—, el MDE es 0.5 puntos porcentuales. Esto determina el tamaño necesario: efectos menores requieren muestras mayores.

**Error frecuente:** Diseñar pruebas para detectar diferencias demasiado pequeñas. Si implementarías cualquiera de las variantes ante una diferencia de 0.1 %, no tiene sentido requerir 500,000 personas por variante. Define primero qué resultado permite actuar y después calcula la prueba.

### Duración de la prueba

Se calcula a partir de tasa base, MDE, nivel de significación —a menudo 0.05—, potencia —a menudo 0.80— y tráfico diario.

**Duración mínima:** Cubre al menos un ciclo de comportamiento relevante, con frecuencia una semana completa, aunque la muestra se alcance antes. El comportamiento varía por día y una prueba de lunes a miércoles puede no representar el fin de semana.

**Duración máxima:** No uses cuatro o seis semanas como regla universal para declarar que un efecto «no existe». Si la prueba no alcanza el tamaño previsto o el intervalo sigue siendo demasiado amplio, registra la incertidumbre, revisa viabilidad y decide según el criterio de parada acordado.

### Lo que una prueba A/B no puede explicar

- **Por qué** ganó una variante. Muestra qué ocurrió, no la causa percibida; combínala con investigación cualitativa.
- **Si el cambio es bueno para las personas.** Una variante manipuladora puede aumentar compras. Las métricas no tienen valores; el equipo sí.
- **Efectos a largo plazo.** Una mejora esta semana puede erosionar confianza durante meses.
- **Resultados no medidos.** Optimizar clics puede empeorar satisfacción, carga de soporte o retención sin que aparezca en la métrica principal.

---

## Medición ética

Las métricas no son neutrales. Elegir qué medir influye en lo que se construye y puede incentivar un diseño dañino.

### Ley de Goodhart

«Cuando una medida se convierte en objetivo, deja de ser una buena medida». — Charles Goodhart, formulación popularizada por Marilyn Strathern.

**En la práctica:** Si «tiempo en página» es un KPI, el equipo puede maximizarlo mediante contenido más largo, pasos innecesarios o reproducción automática. El número sube mientras la experiencia empeora. La métrica deja de aproximar interés y pasa a registrar la fricción incentivada.

**Corrección:** Usa conjuntos de métricas. Combina cada medida de interacción con satisfacción o éxito de tarea. Si el tiempo sube y la satisfacción cae, la optimización probablemente trabaja contra las personas.

### Interacción frente a bienestar

La interacción, métrica predeterminada de buena parte de la industria tecnológica, puede entrar en conflicto con el bienestar según la categoría del producto.

**Cuando se alinean:** Herramientas de productividad —más uso puede representar más trabajo completado—, aprendizaje —más uso puede acompañar más práctica— o seguimiento de salud —más uso puede indicar mayor atención—. Incluso aquí, valida la relación en lugar de asumirla.

**Cuando pueden entrar en conflicto:** Redes sociales, entretenimiento, noticias o juegos, donde el consumo compulsivo no equivale necesariamente a disfrute o beneficio. La duración de sesión aislada no distingue valor de dificultad para detenerse.

**Alternativas orientadas al bienestar:**
- Satisfacción al terminar: «¿Valió la pena este tiempo?».
- Retorno intencional: personas que deciden entrar frente a quienes vuelven por una notificación.
- Objetivo completado: ¿lograron lo que venían a hacer?
- Desconexión consciente: ¿pudieron salir cuando quisieron?

### Cuando las métricas incentivan una mala UX

**Conversión sin salvaguardas:** La optimización agresiva puede favorecer botones dominantes, rechazos ocultos y urgencia artificial. Añade tasas de quejas, devoluciones y contactos con soporte como controles junto a la conversión.

**Interacción sin límites:** Si los incentivos del equipo dependen de DAU, diseñará para DAU incluso a costa del bienestar. Haz explícita la tensión: interacción más satisfacción, no interacción aislada.

**Crecimiento sin retención:** Medir altas nuevas sin saber si se obtiene valor incentiva la parte superior del embudo y descuida el producto. Combina adquisición con activación y retención.

**Desvío de soporte como éxito:** Reducir solicitudes puede significar que las personas resolvieron su problema o que no encontraron ayuda. Combina la reducción con satisfacción de resolución.

### Principios de medición ética

1. **Mide resultados, no solo productos.** Un alta es un producto; completar una tarea es un resultado. Una página vista es un producto; encontrar la respuesta, un resultado.
2. **Combina cada optimización con una métrica de control.** Conversión con devoluciones; interacción con satisfacción; crecimiento con retención.
3. **Incluye la perspectiva humana.** Al menos una métrica debe reflejar cómo se vive la experiencia, no solo qué conducta se registra.
4. **Pregunta quién se beneficia.** Si una subida beneficia al negocio pero no a la persona, es una métrica de negocio, no de UX. Ambas pueden ser válidas; no las confundas.
5. **Haz visibles los incentivos.** Si los objetivos del equipo dependen de una métrica, documenta los comportamientos perversos que podría estimular.
6. **Revisa las métricas periódicamente.** Lo adecuado al lanzar puede no servir en la madurez. Actualiza el marco conforme evoluciona el producto.
