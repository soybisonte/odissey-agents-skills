# Diseño de servicios

## Índice

- [Metodología de blueprint de servicio](#metodología-de-blueprint-de-servicio)
- [Análisis de momentos de la verdad](#análisis-de-momentos-de-la-verdad)
- [Mapeo de puntos de contacto](#mapeo-de-puntos-de-contacto)
- [Identificación de puntos de fallo y diseño de recuperación](#identificación-de-puntos-de-fallo-y-diseño-de-recuperación)
- [Orquestación de canales](#orquestación-de-canales)

## Metodología de blueprint de servicio

Un blueprint de servicio es un diagrama que representa el proceso completo de prestación: lo que ve el cliente, lo que hace la organización entre bastidores y cómo los sistemas técnicos sostienen el conjunto. Lynn Shostack introdujo el concepto en 1984 para abordar un problema fundamental: los servicios son invisibles y no se puede mejorar lo que no se ve.

### Modelo original de Shostack

El blueprint original de Shostack era deliberadamente sencillo: una línea temporal horizontal del proceso de servicio y una «línea de visibilidad» que separaba lo que el cliente ve de lo que no ve. Por encima de la línea: la experiencia del cliente. Por debajo: los procesos entre bastidores que la hacen posible.

**Por qué fue importante:** Antes de Shostack, los servicios se diseñaban a partir de la intuición y las anécdotas. El blueprint hizo visible lo invisible: mostró dónde era frágil el servicio, dónde dependía de personas concretas y dónde fallaba de manera predecible.

### Capas de un blueprint moderno

Los blueprints de servicio contemporáneos amplían el modelo de Shostack a cinco capas, cada una con una capacidad analítica distinta.

**Capa 1: Acciones del cliente**

Lo que hace el cliente en cada etapa del servicio: sus decisiones, interacciones y movimientos entre canales. Es el recorrido del usuario, pero en un blueprint constituye una capa de un panorama mayor, no el panorama completo.

Documenta qué intenta conseguir el cliente, qué hace físicamente y qué canales utiliza. Registra estados emocionales cuando tengas evidencia, pero evita proyectar emociones que no hayas investigado.

**Capa 2: Acciones en la parte visible (frontstage)**

Lo que hacen las partes de la organización orientadas al cliente y que este puede ver: el sitio web, la aplicación, la tienda, el agente del centro de atención o el correo electrónico. Es la superficie visible del servicio.

Documenta cada punto de contacto con el que interactúa el cliente y cada acción del personal que presencia. En el frontstage se forma la percepción de marca; también es donde muchas organizaciones concentran su esfuerzo de diseño, a veces excluyendo todo lo que ocurre debajo.

**Capa 3: Acciones entre bastidores (backstage)**

Lo que hace la organización sin que el cliente lo vea, pero que respalda directamente el frontstage. La persona del almacén que prepara el pedido. El algoritmo que genera recomendaciones. El agente de soporte que revisa una transacción señalada. El diseñador que crea la plantilla de correo.

Documenta cada acción interna que sostiene una interacción visible. Aquí se determinan la eficiencia, la coherencia y la calidad, y aquí se originan la mayoría de los fallos del servicio.

**Capa 4: Procesos de apoyo**

Los sistemas, herramientas y procesos organizativos que permiten las acciones entre bastidores: CRM, gestión de inventario, procesamiento de pagos, verificación de identidad y herramientas de comunicación interna. Suelen pertenecer a equipos y departamentos distintos, y en ocasiones a empresas diferentes.

Documenta los sistemas técnicos y los procesos organizativos de los que dependen quienes trabajan entre bastidores. Aquí viven las dependencias entre funciones y aquí una mejora en el proceso de un equipo puede romper el flujo de trabajo de otro.

**Capa 5: Evidencia física**

Los elementos tangibles que encuentra el cliente en cada etapa: el embalaje, el recibo, la notificación de la aplicación, el correo de confirmación o el propio producto físico. La evidencia física configura expectativas y crea recuerdos.

Documenta cada elemento que el cliente recibe, ve o conserva. La evidencia física perdura después de que termine la interacción: es lo que el cliente se lleva consigo.

### Las líneas

Los blueprints de servicio se dividen mediante tres líneas horizontales:

**Línea de interacción** — Entre las acciones del cliente y el frontstage. Es donde el cliente y quien presta el servicio interactúan directamente. Cada cruce de esta línea es un momento de la verdad.

**Línea de visibilidad** — Entre el frontstage y el backstage. Separa lo que el cliente puede ver de lo que no. La pregunta estratégica es: ¿deberíamos hacer visible una mayor parte del backstage para generar confianza mediante transparencia o mantenerlo oculto para reducir complejidad?

**Línea de interacción interna** — Entre el backstage y los procesos de apoyo. Es donde las personas que actúan entre bastidores interactúan con los sistemas técnicos y los procesos organizativos. Esta línea revela dependencias tecnológicas y cuellos de botella del proceso.

---

## Análisis de momentos de la verdad

No todos los puntos de contacto tienen el mismo peso. Los momentos de la verdad —término acuñado en 1987 por Jan Carlzon, entonces director ejecutivo de SAS Airlines— son las interacciones críticas que influyen de forma desproporcionada en la percepción global del servicio.

### Cómo identificar los momentos de la verdad

Un momento de la verdad tiene tres características:

1. **Gran carga emocional** — Al cliente le importa el resultado: la ansiedad ante una prueba médica, la expectativa de una entrega o la frustración por un pago fallido.
2. **Formación de la percepción** — La interacción condiciona cómo percibe el servicio completo. Un onboarding fluido crea un efecto halo. Una recuperación de errores deficiente empaña todo lo demás.
3. **Influencia en la decisión** — La interacción afecta a si el cliente continúa, recomienda o abandona.

**Las primeras impresiones** siempre son momentos de la verdad. La primera interacción con el servicio —primera visita, primera transacción o primer contacto con soporte— establece las expectativas para lo que sigue.

**Los fallos** siempre son momentos de la verdad. La manera en que el servicio responde cuando algo sale mal revela su verdadero carácter. Un servicio que se recupera con elegancia genera más confianza que uno que nunca falla, pero carece de un mecanismo de recuperación.

**Pico y final** (regla del pico y el final de Kahneman): Las personas juzgan las experiencias principalmente por su punto de mayor intensidad y por el final. Un servicio mediocre durante todo el recorrido que termina bien se recuerda mejor que otro uniformemente bueno que acaba mal.

### Categorías de momentos de la verdad

**Momentos de la verdad positivos** — Interacciones en las que el servicio supera las expectativas: una facilidad sorprendente, un agrado inesperado o la prevención proactiva de problemas. Generan lealtad y recomendaciones.

**Momentos de la verdad negativos** — Interacciones en las que el servicio no cumple las expectativas: fricción, confusión, demoras, descortesía o falta de información. Generan abandono y comentarios negativos, que se propagan con mayor rapidez.

**Momento cero de la verdad (concepto de Google)** — El momento en que un cliente potencial investiga el servicio antes de interactuar con él: reseñas, redes sociales y sitios de comparación. La experiencia comienza antes que el servicio.

### Cómo diseñar los momentos de la verdad

1. **Identifica** — Utiliza investigación del recorrido del cliente, análisis de incidencias de soporte, comentarios abiertos de NPS y análisis de redes sociales para descubrir qué interacciones importan más.
2. **Invierte de manera desproporcionada** — Estos momentos merecen más atención de diseño, pruebas, pulido y monitorización que las interacciones rutinarias.
3. **Prepárate para el fallo** — Cada momento debe tener un modo de fallo diseñado. ¿Qué ocurre si no se procesa el pago? ¿Si la entrega se retrasa? ¿Si el agente no resuelve el problema? La respuesta nunca debe ser «No lo sé».
4. **Mide por separado** — Sigue las métricas de satisfacción y resultados de estos momentos de forma independiente de las métricas globales. Un servicio con satisfacción media alta, pero satisfacción baja en los momentos de la verdad, tiene un problema oculto.

---

## Mapeo de puntos de contacto

Un punto de contacto es cualquier interacción entre el cliente y el servicio. El mapeo cataloga todos los puntos de contacto de todos los canales y evalúa su calidad, coherencia e importancia estratégica.

### Inventario de puntos de contacto

**Digitales:** Sitio web, aplicación móvil, correo electrónico, SMS, notificaciones push, chatbot, redes sociales, publicidad, resultados de búsqueda, ficha en la tienda de aplicaciones y mensajes dentro de la aplicación.

**Humanos:** Centro de atención telefónica, personal presencial, agentes de chat en vivo, gestores de cuenta, personal de reparto y técnicos de instalación.

**Físicos:** Embalaje, producto, tienda física, materiales impresos, señalización, recibos y tarjetas de visita.

**Ambientales:** Distribución de la tienda, entorno de la oficina, sala de espera, aparcamiento y accesibilidad física.

### Matriz de evaluación de puntos de contacto

Evalúa cada punto de contacto:

| Dimensión | Pregunta |
|-----------|----------|
| **Frecuencia** | ¿Con qué frecuencia ocurre: a diario, cada semana o una sola vez? |
| **Criticidad** | Si falla, ¿cuál es la consecuencia: una molestia menor o la interrupción completa del servicio? |
| **Impacto emocional** | ¿En qué estado emocional está el cliente cuando llega a este punto? |
| **Coherencia** | ¿Ofrece la misma calidad cada vez? |
| **Alineación con la marca** | ¿Refleja los valores y la voz de la marca? |
| **Calidad de la transferencia** | ¿Cómo conecta con los puntos de contacto anterior y posterior? |

### Coherencia entre canales

El fallo más habitual no es un punto de contacto malo, sino la incoherencia entre varios. El sitio web dice una cosa, la aplicación otra y el agente telefónico una tercera. El cliente comienza un proceso en línea y no puede continuarlo en la tienda. Las funciones de la aplicación móvil no coinciden con las de escritorio.

**Diseña la coherencia entre canales mediante:**

- Un modelo de contenido compartido: la información se crea una vez y se muestra en todos los canales.
- Un registro unificado del cliente: cada canal ve el mismo historial.
- Terminología coherente: la misma acción recibe el mismo nombre en todas partes.
- Una identidad visual congruente: adaptada a cada canal, pero reconocible como la misma marca.
- Transiciones fluidas: empezar en un canal y continuar en otro sin perder el progreso.

---

## Identificación de puntos de fallo y diseño de recuperación

Todos los servicios fallan. La pregunta es si el fallo se anticipó y se diseñó una respuesta, o si sorprende tanto al cliente como a la organización.

### Categorías de puntos de fallo

**Fallos de proceso** — El proceso definido no produce el resultado esperado. El pedido se realizó, pero no se preparó. El paso de verificación agotó el tiempo. El pago se cobró dos veces. Son predecibles y se puede diseñar para ellos.

**Fallos humanos** — Una persona de la cadena de servicio comete un error o actúa mal. Un agente proporciona información incorrecta. Una persona de reparto es descortés. Un colega olvida transferir una tarea. Pueden gestionarse mediante formación, herramientas y diseño de procesos.

**Fallos del sistema** — La tecnología se avería. La API deja de responder. La base de datos pierde un registro. El correo no se envía. Son inevitables y es necesario diseñar respuestas.

**Fallos del cliente** — El cliente hace algo inesperado: introduce datos incorrectos, no entiende un paso o utiliza otro canal. En realidad no son fallos, sino comportamientos humanos normales que el servicio debe admitir.

**Fallos externos** — Fuerzas fuera del control del servicio: clima, interrupciones de la cadena de suministro, caídas de terceros o cambios normativos. No se pueden impedir; solo cabe prepararse.

### Principios de diseño de recuperación

**Detecta pronto.** Cuanto antes detectes el fallo, más opciones tendrás para recuperarte. La monitorización, las alertas y los ciclos de retroalimentación del cliente deben sacar a la luz los problemas antes de que el cliente tenga que notificarlos.

**Comunica de forma proactiva.** Si sabes que algo salió mal, avisa antes de que el cliente lo descubra. «Tu pedido se ha retrasado por el clima; la nueva entrega estimada es el jueves» es mucho mejor que dejar que consulte el seguimiento el miércoles y no encuentre ninguna actualización.

**Ofrece una solución, no solo una explicación.** Los clientes quieren saber qué vas a hacer, no recibir una explicación minuciosa del fallo. «Esto es lo que ocurrió» debe ir seguido de inmediato por «Esto es lo que haremos para resolverlo».

**Da capacidad de decisión al personal de primera línea.** Si la persona con la que habla el cliente no puede resolver el problema, la recuperación ya ha fallado. El diseño debe darle autoridad y herramientas para solucionar los fallos habituales sin escalar el caso.

**Corrige primero y mejora después.** Resuelve el problema inmediato (reembolsa, reenvía o corrige el error). Después, añade algo inesperado: un descuento, una mejora o un seguimiento personal. Una buena recuperación genera más lealtad que la ausencia de fallos —la «paradoja de recuperación del servicio», documentada por McCollough y Bharadwaj en 1992—.

---

## Orquestación de canales

Los servicios modernos operan en múltiples canales. La orquestación diseña cómo fluye la experiencia entre ellos, no como silos independientes, sino como un servicio coordinado.

### Patrones de orquestación

**Nativo por canal:** Cada canal ofrece la experiencia completa, adaptada a sus fortalezas. El sitio web, la aplicación y la tienda física prestan el servicio completo. Exige muchos recursos, pero maximiza la capacidad de elección.

**Canales complementarios:** Distintos canales cubren partes diferentes del recorrido. Se investiga en el sitio web, se compra en la tienda y se recibe soporte en la aplicación. Cada canal hace lo que mejor sabe hacer. Es eficiente, pero exige transferencias claras.

**Canal principal con alternativa:** Un canal contiene la experiencia principal y los demás sirven como alternativa en situaciones concretas. «Usa la app para todo; llámanos si necesitas ayuda». Es habitual en servicios nativos digitales.

**Canales secuenciales:** El servicio mueve al cliente por una secuencia definida. Registro en línea, verificación telefónica y activación en la aplicación. Es común en servicios regulados, como banca y seguros, donde cada canal satisface necesidades de cumplimiento distintas.

### Principios de diseño de la orquestación

**No impongas canales.** Deja que los clientes elijan el que prefieran. Si alguien quiere llamar en vez de usar el chatbot, permíteselo. Obligar a usar un canal genera frustración, incluso cuando objetivamente sea más rápido.

**Conserva el contexto entre canales.** Si el cliente comienza un proceso en el sitio web y llama a soporte, el agente debe ver qué estaba haciendo. Si añade artículos al carrito desde el móvil, el carrito debe aparecer en el escritorio. Perder el contexto entre canales es uno de los fallos más comunes del diseño de servicios.

**Diseña las transiciones.** El cambio de canal conlleva un riesgo alto de confusión y pérdida de contexto. Diseña transferencias explícitas: «Continúa en la app; hemos guardado tu progreso», con una ruta clara para retomar el proceso.

**Haz que los canales se conozcan entre sí.** El personal de tienda debe conocer lo que ofrece el sitio web. El chatbot debe saber cuál es el teléfono de soporte. La aplicación debe conocer el horario de la tienda física. Los canales que se ignoran producen una experiencia fragmentada.

**Mide entre canales, no dentro de cada uno.** El cliente que empieza en la web y termina por teléfono completó con éxito el recorrido. Sin embargo, las métricas aisladas registrarían un «rebote» en la web y una conversión sin atribuir por teléfono. La medición entre canales revela la experiencia real.
