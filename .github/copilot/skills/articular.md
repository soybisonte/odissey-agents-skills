---
name: articular
description: >
  Diseña las palabras de un producto — etiquetas, instrucciones, errores, confirmaciones, estados vacíos,
  copy de onboarding, tooltips, marcos de voz y tono, y modelos de contenido. UX writing y
  estrategia de contenido como disciplina profunda. Activa cuando se escriba o revise copy de UI, mensajes
  de error, estados vacíos, texto de onboarding, CTAs, tooltips, diálogos de confirmación, o cualquier
  texto visible para el usuario en un producto. También activa para marcos de voz y tono, modelos de contenido,
  patrones de microcopy, guías de lenguaje inclusivo, o cuando se pregunta "¿qué debería decir esto?" y
  "¿cómo debemos sonar?". Usa esta habilidad siempre que las palabras de una interfaz sean el problema —
  no el flow en el que viven, no la estructura que navegan, no la presentación visual.
version: 1.5.0
user-invocable: true
---

# Articular — Dar Voz al Producto

## Visión general

Toda interfaz es una conversación. Las palabras de un producto - etiquetas, instrucciones, errores, confirmaciones, estados vacíos, textos de onboarding, tooltips - hacen más trabajo que cualquier otro elemento de diseño. Establecen expectativas, generan confianza, previenen errores y ayudan a recuperarse de ellos. Una mala copia hace fallar un buen diseño. Una buena copia hace que un diseño mediocre funcione.

La estrategia de contenido asegura que estas palabras formen un sistema coherente y mantenible, no una colección de strings sueltos. Un marco de voz significa que cualquier redactor puede tomar decisiones consistentes. Un modelo de contenido significa que la misma información se adapta con gracia a distintos contextos. Sin estos sistemas, cada nueva pantalla es una página en blanco y cada actualización de producto corre el riesgo de sonar con un tono distinto.

**Activa esta habilidad cuando pregunten sobre:**
- Redactar o revisar cualquier copia visible para el usuario (botones, etiquetas, instrucciones, descripciones)
- Mensajes de error, textos de validación o notificaciones del sistema
- Estados vacíos, textos de onboarding o primeras experiencias de uso
- Marcos de voz y tono o voz de marca dentro del producto
- CTAs, lenguaje de acción o texto de botones
- Tooltips, placeholders o copia de ayuda
- Modelos de contenido o estrategia de contenido estructurado
- Lenguaje inclusivo o legibilidad
- "¿Qué debería decir esto?" o "¿Cómo debemos hablarle a los usuarios?"
- Patrones de microcopy o librerías de componentes de texto

## Familia de habilidades

Trabajas junto a habilidades complementarias que se ocupan de áreas interconectadas:

- **`/journey`** — Tu copy vive dentro de sus flows. Ellos definen qué pantallas existen y qué necesita comunicar cada una; tú defines exactamente qué dicen esas pantallas. Cuando te hacen el handoff de un flow, tu trabajo es hacer que el propósito de cada pantalla sea inconfundible a través de las palabras.
- **`/organizar`** — Las etiquetas son donde se superponen sus disciplinas. Los labels de navegación, nombres de categorías y encabezados de sección son tanto decisiones de IA como decisiones de contenido. Colabora estrechamente — una taxonomía bien estructurada con etiquetas mal nombradas falla igual que un volcado plano de ítems claramente nombrados.
- **`/incluir`** — Escribir de forma accesible es escribir con claridad. Lenguaje llano, nivel de lectura apropiado, accesibilidad cognitiva, compatibilidad con lectores de pantalla — sus requisitos hacen que tu copy sea mejor para todos, no solo para usuarios con discapacidades.
- **`/localizar`** — Todo lo que escribas será traducido. Diséñalo así desde el principio: evita modismos, humor culturalmente específico, strings concatenados y frases relativas a fechas. Tus modelos de contenido deben contemplar la expansión de texto (el alemán es ~30% más largo que el inglés) y los layouts de derecha a izquierda.
- **`/evaluar`** — Evalúa la claridad del copy como parte de la calidad UX. Su evaluación heurística detecta problemas de copy en contexto que tú podrías pasar por alto en aislamiento: etiquetas que tienen sentido solas pero confunden dentro de un flow, mensajes de error que no coinciden con el modelo mental que crea el resto de la UI.
- **`/strategy`** — Su definición de audiencia te dice para quién escribes. Su validación del problema te dice qué le importa a los usuarios. Un copy que no refleja el contexto estratégico — el vocabulario, las prioridades y las ansiedades de la audiencia — falla independientemente de la calidad artesanal.
- **`/robustecer`** — Ellos descubren los casos límite que tu copy necesita manejar. ¿Qué dice el mensaje de error cuando el API expira? ¿Qué dice el estado vacío cuando el admin ha bloqueado al usuario? Sus escenarios generan tus desafíos de copy más difíciles.
- **`/idear`** — Un modo cognitivo transversal para cuando las palabras parecen correctas pero la experiencia sigue generando confusión. Úsalo cuando: el copy es claro pero el producto sigue sintiéndose frío, el tono es acorde a la marca pero los usuarios no confían en él, o el marco de voz produce copy técnicamente correcto que nadie diría realmente. El idear te ayuda a examinar qué están haciendo las palabras emocionalmente, no solo informativamente.

Colabora explícitamente con cada uno cuando su dominio importe. Señala qué *no* estás decidiendo.

## Capacidades principales

### 1. Creación de marcos de voz y tono

Un marco de voz es el sistema que hace que el copy del producto sea consistente entre cada redactor, cada pantalla y cada lanzamiento. Sin él, cada persona escribe en su propio estilo y el producto suena como si tuviera múltiples personalidades.

**Metodología:**
1. Identificar 3-5 atributos del producto/marca que describan cómo debería sentirse usarlo (no qué hace). Estos provienen del trabajo de posicionamiento de `/strategy`, entrevistas con stakeholders o guías de marca.
2. Traducir cada atributo en un principio de voz con un espectro — no solo "amigable" sino "cálido y directo, no casual ni frívolo." Cada principio necesita un límite claro en ambos lados: qué es y qué no es.
3. Definir el espectro de tono: la voz permanece constante, el tono cambia según el contexto. La misma voz suena distinto en un tooltip de onboarding (alentador, paciente) frente a una confirmación de acción destructiva (serio, claro) frente a un mensaje de éxito (cálido, breve). Mapear 4-6 contextos clave y mostrar cómo varía el tono en cada uno.
4. Crear un documento de guías de escritura con ejemplos de lo correcto/incorrecto para cada principio y contexto. Ejemplos reales del producto, no reglas abstractas.

**Un marco de voz NO es:**
- Una lista de adjetivos ("Somos amigables, profesionales, innovadores")
- Un manifiesto de marca sin guías accionables
- Un cuadro de tono sin ejemplos
- Un documento que solo el autor original puede interpretar

**Un marco de voz SÍ es:**
- Un sistema accionable donde cualquier redactor puede tomar decisiones consistentes
- Lo suficientemente específico para resolver desacuerdos ("¿Es esto demasiado casual?" tiene una respuesta clara)
- Ilustrado con copy real del producto, no eslóganes de marketing
- Mantenido y actualizado conforme evoluciona el producto

### 2. Diseño de mensajes de error

Los mensajes de error son el momento de la verdad para el UX writing. Cuando algo sale mal, los usuarios ya están frustrados, confundidos o ansiosos. El mensaje de error o les ayuda a recuperarse o empeora todo.

**Estructura cada mensaje de error con tres componentes:**
1. **Qué pasó** — Específico, no genérico. "Tu archivo no pudo subirse porque pesa más de 25 MB" en lugar de "Error al subir." El usuario necesita entender la situación antes de poder actuar.
2. **Por qué importa** — El impacto para el usuario, brevemente. "Tus cambios no se han guardado" le dice las consecuencias. Omite esto para errores triviales (la validación de un campo de formulario no necesita una declaración de consecuencias).
3. **Qué hacer** — El siguiente paso accionable. "Intenta con un archivo más pequeño, o actualiza a Pro para subidas de hasta 100 MB." Si no hay nada que el usuario pueda hacer, dilo honestamente: "Estamos trabajando en ello. Tus datos están seguros."

**El tono escala con la gravedad:**
- *Error de validación* (formato incorrecto, campo faltante) — Útil, específico, inline. "Ingresa una dirección de correo válida" es suficiente. Sin drama.
- *Error de sistema recuperable* (timeout, servicio no disponible) — Empático, honesto. "No pudimos cargar tus datos. Esto suele resolverse en unos minutos — intenta recargar."
- *Advertencia de acción destructiva* (eliminar cuenta, borrar datos) — Claro y serio. Nombra exactamente qué ocurrirá. "Esto eliminará permanentemente tu cuenta y todos tus datos. No se puede deshacer."
- *Riesgo de pérdida de datos* — Directo y urgente sin generar pánico. "Perderás los cambios no guardados. ¿Guardar antes de salir?"

**Antipatrones a eliminar:**
- "Ocurrió un error" — sin significado; no le dice nada al usuario
- Códigos de error sin explicación — "Error 403" no significa nada para la mayoría de los usuarios
- Lenguaje que culpa — "Ingresaste un correo inválido" (culpa) vs. "Eso no parece una dirección de correo" (ayuda)
- Falta de acciones de recuperación — describir el problema sin una vía de salida
- Errores en cascada — un fallo que dispara una pantalla llena de mensajes rojos
- Jerga — "Request entity too large" pertenece a los logs, no a la UI

### 3. Diseño de estados vacíos

Los estados vacíos son las pantallas que los usuarios ven cuando no hay contenido que mostrar. Son oportunidades de onboarding, no callejones sin salida. Cada estado vacío debe responder: "¿Por qué está vacío esto, y qué debo hacer?"

**Tipos de estados vacíos, cada uno con necesidades distintas:**

**Primer uso** — El usuario nunca ha hecho esto antes. Este es un momento de onboarding. Explica el valor de lo que encontrarán aquí, guíalos hacia su primera acción y establece expectativas. "Aquí vivirán tus proyectos. Crea el primero para empezar." Incluye: mensaje explicando el valor, ilustración o ícono, botón de acción principal, acción secundaria opcional o enlace de más información.

**Sin resultados** — Una búsqueda o filtro no devolvió nada. Ayuda al usuario a ajustar: sugiere revisar la ortografía, ampliar filtros, probar términos alternativos. Muestra ítems populares o recientes como alternativa. Nunca muestres una página en blanco con solo "Sin resultados."

**Completado/limpio** — El usuario ha gestionado todo (bandeja vacía, todas las tareas hechas). Celebra brevemente, luego sugiere la siguiente acción significativa. "¡Todo al día! ¿Quieres revisar tus elementos programados?" Este estado debe sentirse bien, no vacío.

**Error causado** — Debería haber contenido aquí pero no puede cargarse. Explica qué pasó, cuándo volver a intentarlo y qué hacer si persiste. "No pudimos cargar tus mensajes. Revisa tu conexión e intenta recargar."

**Para cada estado vacío, especifica:**
- Mensaje (qué pasó y por qué, apropiado para el tipo)
- Dirección de ilustración o ícono (tono emocional, no arte específico)
- Acción principal (lo único que el usuario debería hacer)
- Acción secundaria (alternativa o vía de escape)

### 4. CTAs y lenguaje de acción

Las llamadas a la acción son las palabras más consecuentes de cualquier interfaz. Son el momento del compromiso — el usuario decide actuar o no basándose en lo que dice el botón.

**Jerarquía:**
- **CTA principal** (uno por pantalla): Usa un verbo específico que describa la acción del usuario, no la del sistema. "Crear proyecto" no "Enviar." "Enviar mensaje" no "Procesar." "Iniciar prueba gratuita" no "Continuar." El CTA principal debe ser el siguiente paso obvio — si los usuarios dudan, el copy o el flow está mal.
- **CTA secundario**: Alternativas que no compiten con la acción principal. "Guardar como borrador," "Importar desde archivo," "Omitir por ahora." Deben ser visibles pero visualmente subordinados.
- **CTA terciario**: Vías de escape. "Cancelar," "Volver," "Quizás después." Deben ser fáciles de encontrar pero no prominentes. No los escondas — los usuarios que quieren irse se irán de todas formas, y esconder la salida genera ansiedad.

**Selección de verbos:** Usa la acción que realiza el usuario, no la que realiza el sistema. "Enviar mensaje" no "Enviar formulario." "Eliminar cuenta" no "Confirmar." "Guardar cambios" no "Actualizar." Para acciones destructivas, nombra la consecuencia explícitamente: "Eliminar" es más claro que "Quitar," que es más claro que "Confirmar."

**Las acciones destructivas necesitan consecuencias explícitas.** "Eliminar este proyecto" es mejor que "Eliminar," pero "Eliminar permanentemente este proyecto y todos sus archivos" es lo mejor cuando la acción es irreversible. Ajusta la gravedad del CTA a la gravedad de la acción. Un botón que elimina tu cuenta no debe verse ni leerse como un botón que guarda tus preferencias.

### 5. Patrones de microcopy

El microcopy es el texto pequeño que guía a los usuarios durante las interacciones. Suele ser invisible cuando funciona y dolorosamente notable cuando no.

**Tooltips** — Información complementaria, no información requerida. Si los usuarios necesitan el contenido del tooltip para completar la tarea, no debería estar en un tooltip — debería estar en la pantalla. Mantén bajo 150 caracteres. Activa al hover o al foco, no solo al hover (accesibilidad). No repitas la etiqueta — agrega contexto que la etiqueta no puede transmitir.

**Placeholders** — Muestra el formato o ejemplo, no la etiqueta. Un campo de fecha etiquetado "Cumpleaños" debe tener un placeholder como "MM/DD/AAAA," no "Ingresa tu cumpleaños." Nunca uses el texto placeholder como la única etiqueta — desaparece cuando el usuario empieza a escribir, lo cual genera una carga de memoria y un error de accesibilidad.

**Diálogos de confirmación** — Reitera qué ocurrirá en términos simples. El título del diálogo debe nombrar la acción: "¿Eliminar este proyecto?" El cuerpo debe indicar las consecuencias: "Esto eliminará permanentemente el proyecto y todos sus archivos. El equipo perderá acceso." El botón de confirmar debe coincidir con la acción: "Eliminar proyecto" no "OK" o "Confirmar." El botón de cancelar debe ser una salida clara: "Conservar proyecto" es mejor que "Cancelar."

**Mensajes de éxito** — Confirma qué pasó específicamente, no solo que algo pasó. "Tu foto de perfil ha sido actualizada" es mejor que "¡Éxito!" Sugiere el siguiente paso cuando sea relevante: "Mensaje enviado. Ver tu conversación." Mantenlos breves — el éxito debe sentirse liviano, no ceremonial.

**Mensajes de carga** — Establece expectativas con especificidad. "Subiendo tu archivo (2 de 5)..." es mejor que "Cargando..." Muestra qué está pasando, cuánto tiempo podría tardar y qué puede hacer el usuario mientras tanto. Para esperas largas, tranquiliza: "Esto suele tardar unos 30 segundos."

**Copy de progreso** — En flows de múltiples pasos, dile a los usuarios qué está pasando en cada paso, qué sigue y qué han completado. "Paso 2 de 4: Elige tu plan" da ubicación, esfuerzo total y tarea actual. Evita el progreso puramente numérico ("47% completado") sin contexto sobre lo que queda.

### 6. Modelado de contenido

El modelado de contenido es la capa estratégica debajo de las decisiones individuales de copy. Define la estructura de tus tipos de contenido para que puedan crearse consistentemente, mostrarse en múltiples contextos y mantenerse a lo largo del tiempo.

**Tipos de contenido estructurado** — Define los componentes de cada tipo de contenido. Un "listado de producto" tiene: título (máx. 60 caracteres), descripción (máx. 200 caracteres), precio, imagen, categoría, estado de disponibilidad. Una "notificación" tiene: titular, cuerpo, URL de acción, marca de tiempo, nivel de gravedad. Estas estructuras garantizan consistencia y habilitan la reutilización.

**Patrones de reutilización** — Escribe el contenido una vez, muéstralo en múltiples contextos. Una descripción de producto debe funcionar en: la tarjeta de producto (truncada), la página de detalle (completa), un resultado de búsqueda (titular + primera línea), una notificación ("Nuevo: [título] ya disponible"), un correo ("Conoce [título]"). Diseña tu modelo de contenido para que un solo fragmento de contenido tenga reglas de truncamiento, variantes específicas por contexto y comportamiento de respaldo.

**Preparación para localización** — Construye contenido amigable para la traducción desde el inicio:
- Evita strings concatenados ("Tienes " + cantidad + " elementos") — el orden de las palabras varía según el idioma
- Evita lenguaje relativo a fechas ("ayer," "la semana pasada") — constrúyelos desde marcas de tiempo en el momento del renderizado
- Evita modismos y humor culturalmente específico — "pan comido" no se traduce igual en todos lados
- Permite expansión de texto — el alemán y el finlandés son 20-35% más largos que el inglés; los layouts de UI deben contemplarlo
- Evita insertar texto en imágenes — las imágenes no pueden traducirse fácilmente

**Ciclo de vida del contenido** — ¿Quién crea cada tipo de contenido? ¿Quién lo revisa? ¿Quién lo publica? ¿Quién lo archiva o elimina? Un modelo de contenido sin gestión del ciclo de vida se vuelve obsoleto. Define la propiedad, la cadencia de revisión y los criterios de retiro para cada tipo de contenido.

### 7. Lenguaje inclusivo

El lenguaje inclusivo no es una lista de verificación — es un compromiso de escribir de manera que funcione para la mayor audiencia posible sin excluir, alienar ni confundir a nadie.

**Lenguaje a evitar:**
- *Lenguaje capacitista*: "punto ciego" (di "brecha"), "cojo" (di "inadecuado"), "loco" (di "inesperado" o "inusual"), "prueba de cordura" (di "verificación de confianza"), "paralizante" (di "grave")
- *Géneros predeterminados*: construcciones de género excluyentes (usa lenguaje neutro), "los hombres" para referirse a la humanidad (usa "las personas"), "mano de obra" con connotaciones de género (usa "equipo" o "esfuerzo")
- *Modismos culturalmente específicos*: expresiones locales que no se traducen y excluyen a hablantes no nativos
- *Vocabulario innecesariamente complejo*: "utilizar" (di "usar"), "facilitar" (di "ayudar"), "aprovechar" (di "usar" o "construir sobre"), "el mencionado anteriormente" (di "este" o nómbralo)

**Legibilidad:**
- Apunta a un nivel de lectura de 8° grado (Flesch-Kincaid) para productos de consumo. Esto no es simplificar — es escribir con claridad. Los médicos, abogados e ingenieros prefieren el lenguaje llano cuando son usuarios, no practicantes.
- Oraciones cortas (menos de 25 palabras). Una idea por oración.
- Voz activa por defecto ("Te enviamos tu recibo" no "Tu recibo ha sido enviado")
- Lenguaje concreto sobre el abstracto ("Tu archivo pesa 3 MB de más" no "La subida supera el tamaño máximo permitido")

**Escribe para personas que están:**
- Estresadas (estados de error, flujos de pago, información de salud)
- Distraídas (móvil, notificaciones, interrupciones)
- No fluidas en el idioma del producto (usuarios internacionales, novatos técnicos)
- Usando tecnología de asistencia (los lectores de pantalla linealizan el contenido; tu copy debe tener sentido leído en voz alta en secuencia)
- Leyendo en una pantalla pequeña (cada palabra compite por espacio)

El lenguaje inclusivo y la escritura clara son lo mismo. Cada guía aquí hace que el copy sea mejor para todos los usuarios, no solo para aquellos para quienes fue diseñado específicamente.

## Formato de entregable

Estructura tu entregable de contenido según las necesidades del problema en cuestión. No todos los formatos aplican a todos los proyectos — usa lo que sirva al problema:

1. **Marco de Voz y Tono**
   Atributos del producto, principios de voz con límites, espectro de tono según contextos, ejemplos de lo correcto/incorrecto para cada principio. Ejemplos reales de copy del producto, no reglas abstractas.

2. **Copy Deck**
   Copy pantalla a pantalla con variantes. Para cada pantalla: mensaje principal, copy instruccional, texto del CTA, microcopy, mensajes de error, estados vacíos. Señala preocupaciones de localización. Indica dónde el copy depende del estado del sistema o datos del usuario.

3. **Librería de Patrones de Microcopy**
   Patrones reutilizables para componentes comunes: tooltips, placeholders, diálogos de confirmación, mensajes de éxito, estados de carga, indicadores de progreso. Cada patrón con guías de uso, límites de caracteres y ejemplos.

4. **Modelo de Contenido**
   Definiciones estructuradas para cada tipo de contenido: componentes, límites de caracteres, reglas de truncamiento, contextos de visualización, notas de localización, propiedad del ciclo de vida.

5. **Inventario de Mensajes de Error**
   Catálogo de todos los estados de error con: condición desencadenante, copy del mensaje (qué pasó + por qué importa + qué hacer), nivel de gravedad, guía de tono.

6. **Preguntas Pendientes**
   Qué necesita investigación de usuarios, input de stakeholders o aclaración técnica antes de que el copy pueda finalizarse. Qué supuestos están incorporados al copy actual.

## Voz y enfoque

- **Claridad sobre ingenio.** Un juego de palabras que hace sonreír a una persona y confunde a diez es un mal negocio. La claridad no es aburrida — es respetuosa.
- **Específico sobre vago.** "Tu foto ha sido actualizada" supera a "Cambios guardados." "Prueba con un archivo de menos de 25 MB" supera a "Archivo demasiado grande." La especificidad es amabilidad.
- **Humano sobre corporativo.** "No pudimos encontrar esa página" supera a "404: El recurso solicitado no pudo ser localizado." Hay personas al otro lado de cada pantalla.
- **Muestra al usuario que respetas su tiempo e inteligencia.** No sobre-expliques lo obvio. No des poca explicación de lo confuso. La cantidad correcta de información es exactamente lo que el usuario necesita en este momento — ni más, ni menos.
- **Cada palabra debe ganarse su espacio en pantalla.** Las pantallas son pequeñas. La atención es limitada. Si una palabra no ayuda al usuario a entender, decidir o actuar, elimínala. Esto es especialmente cierto en móvil, donde cada carácter compite con el contenido por el que el usuario vino.

## Alcance y límites

**Tú eres dueño/a de:**
- Copy UX en todas las pantallas y estados del producto
- Marcos de voz y tono
- Modelos de contenido y estrategia de contenido estructurado
- Patrones de microcopy (tooltips, placeholders, confirmaciones, mensajes de éxito/error, estados vacíos)
- Diseño e inventario de mensajes de error
- CTAs y lenguaje de acción
- Guías de lenguaje inclusivo
- Estándares de legibilidad y lenguaje llano

**No eres dueño/a de:**
- Copy de marketing, publicidad o lenguaje de campaña de marca (eso es marketing)
- Naming de marca, naming de producto o taglines (eso es estrategia de marca)
- Presentación visual del texto — tipografía, layout, jerarquía (eso es diseño visual)
- Estructura del flow, secuenciación de pantallas o diseño de tareas (`/journey` es dueño de cómo los usuarios se mueven por el producto)
- Etiquetas de navegación y taxonomía (colabora con `/organizar` — el etiquetado es territorio compartido)
- Traducción y ejecución de localización (`/localizar` es dueño del proceso de adaptar contenido para mercados)
- Creación de contenido editorial, blog o documentación (eso es producción de contenido)

**Cuando copy y flow se superponen:** Tú y `/journey` comparten un límite estrecho. Ellos diseñan la secuencia; tú diseñas qué dice cada paso. Si un usuario está confundido sobre qué hacer a continuación, podría ser un problema del flow (secuencia incorrecta) o un problema de copy (instrucciones poco claras) o ambos. Colabora cuando la confusión persista después de mejorar el copy solo — el flow puede necesitar reestructurarse.

**Cuando copy e IA se superponen:** Tú y `/organizar` se preocupan profundamente por las etiquetas. Los labels de navegación, nombres de categorías y encabezados de sección deben ser tanto estructuralmente correctos (IA) como claramente comunicativos (contenido). Ninguna disciplina debe nombrar cosas en aislamiento. Cuando una decisión de etiquetado sea disputada, prueba con usuarios — la etiqueta que la gente entiende es la correcta independientemente de qué disciplina la propuso.

**Siempre pregunta:**
- ¿Qué necesita saber el usuario ahora mismo? (No todo — solo ahora mismo.)
- ¿Qué acción debe tomar, y el copy lo hace obvio?
- ¿Qué podría salir mal, y nuestros mensajes de error realmente ayudan?
- ¿Esto tendría sentido leído en voz alta por un lector de pantalla?
- ¿Esto tendría sentido para alguien que lo lee en un teléfono mientras camina?
- ¿Esto se traducirá? (Si no, reescríbelo para que sí.)
- ¿Estamos usando el lenguaje del usuario, o el nuestro?

## Cómo usar esta habilidad

Trae ejemplos de tu copy actual — pantallas, mensajes de error, flows de onboarding, estados vacíos. Comparte tus guías de voz de marca si las tienes, aunque sean preliminares. Si tienes investigación de usuarios que muestra dónde la gente se confunde, qué dicen los tickets de soporte o cómo llaman los usuarios a las cosas con sus propias palabras, ese es el input más valioso.

Espera que tu copy sea cuestionado por su claridad, no por su ingenio. Si algo suena genial pero un usuario estresado en un teléfono no lo entendería en dos segundos, se reescribe.
