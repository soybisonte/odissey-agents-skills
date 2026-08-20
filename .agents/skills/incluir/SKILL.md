---
name: incluir
description: >-
  Usa cuando una experiencia deba ser accesible e inclusiva para personas con distintas capacidades: WCAG, teclado, lector de pantalla, foco, contraste, texto alternativo, objetivos táctiles, accesibilidad cognitiva o motora. Se centra en barreras de acceso y uso; no en adaptar el producto a otra cultura.
---

# Incluir — Diseñar para Todas las Personas

## Visión general

La accesibilidad no es una característica. No es una fase. No es algo que "añades" después de que el diseño esté "terminado". Es una disciplina de diseño que asegura que cada persona, sin importar su capacidad, dispositivo, situación o contexto, pueda usar lo que construyes.

Mil millones de personas en el mundo tienen alguna discapacidad. Solo ese dato debería cerrar el debate sobre si la accesibilidad importa. Pero la accesibilidad no trata solo de discapacidad permanente. Trata del rango completo de la experiencia humana: el padre o madre que sostiene a un bebé con un brazo y usa el teléfono con el otro. La persona que lee una pantalla bajo sol directo. El usuario en una cafetería ruidosa que no puede reproducir audio. La persona recuperándose de una cirugía ocular. La ejecutiva mayor cuya vista ya no es la de hace cinco años. La persona con TDAH intentando concentrarse en un formulario de varios pasos.

Todas las personas experimentan limitaciones situacionales o temporales. Diseñar para accesibilidad mejora la experiencia de todas ellas, no solo de quienes estás "acomodando". Las rampas se diseñaron para usuarios de silla de ruedas. Hoy las usan también personas con cochecito, maleta, carrito de reparto o bicicleta. El buen diseño accesible funciona igual.

Esta habilidad trata la accesibilidad como una cualidad de diseño, no como una carga de cumplimiento. Pero no evade la realidad legal: el cumplimiento de WCAG es obligatorio en muchas jurisdicciones (ADA en EE. UU., European Accessibility Act, Section 508 para gobierno y leyes similares en todo el mundo). Ignorar la accesibilidad es tanto un fallo de diseño como un riesgo legal.

**Cuándo activar esta habilidad:** auditorías de accesibilidad, revisiones de diseño inclusivo, comprobaciones de cumplimiento WCAG, guía de pruebas con lector de pantalla, diseño de navegación por teclado, evaluación de contraste de color, revisión de objetivos táctiles o cualquier momento en que la pregunta sea "¿puede usar esto todo el mundo?"

---

## Familia de habilidades

Incluir trabaja junto al sistema completo de habilidades de Odissey. La accesibilidad toca todo — cada habilidad produce trabajo que debe ser accesible.

- **`$journey`** — Los flows deben funcionar para usuarios solo-teclado, usuarios de lector de pantalla, usuarios de acceso por switch y usuarios de control por voz — no solo ratón y táctil. Cada flow que diseña `$journey` debe revisarse para independencia del método de entrada. Cuando diseñan una interacción de arrastrar y soltar, tú aseguras que haya una alternativa de teclado. Cuando diseñan un flow móvil basado en gestos, tú aseguras que haya un fallback de un solo puntero.

- **`$articular`** — La escritura clara ES escritura accesible. Lenguaje sencillo, oraciones cortas, texto de enlace significativo ("Lee el informe de accesibilidad" en lugar de "Haz clic aquí"), encabezados descriptivos y etiquetas que comuniquen lo que un campo espera. `$articular` es dueño del copy; tú asesoras sobre lo que lo hace accesible.

- **`$organizar`** — La estructura de navegación debe ser interpretable por la tecnología asistiva. Los landmarks (header, nav, main, footer), la jerarquía de encabezados (H1 hasta H6 sin saltar niveles), los skip links y los breadcrumbs son decisiones de arquitectura de información con implicaciones directas de accesibilidad. Cuando `$organizar` diseña la IA, tú aseguras que se traduzca en una experiencia de lector de pantalla que tenga sentido.

- **`$robustecer`** — El hardening de casos límite se solapa con la accesibilidad. Diseñar para conexiones lentas, pantallas pequeñas, uso con una sola mano y contenido extremo es tanto trabajo de resiliencia como diseño inclusivo. Coordina para evitar duplicación — tú eres dueño de la metodología de accesibilidad; ellos son dueños de la metodología de pruebas de estado y estrés.

- **`$evaluar`** — La evaluación de accesibilidad es parte de toda evaluación de UX. Cuando `$evaluar` realiza una revisión heurística, las violaciones de accesibilidad emergen a través de múltiples heurísticas. Tu metodología detallada de accesibilidad alimenta su marco de evaluación. Sus hallazgos en categorías de accesibilidad se enrutan a ti.

- **`$spec`** — Los requisitos de accesibilidad deben estar en todo spec de handoff. Roles ARIA, patrones de interacción por teclado, comportamiento de gestión del foco, anuncios del lector de pantalla — no son anotaciones "nice to have". Son requisitos centrales del spec. Cuando `$spec` escribe el handoff, tú aseguras que la accesibilidad no sea una sección separada sino que esté integrada en todo.

- **`$blueprint`** — La arquitectura del sistema afecta la accesibilidad. Los sistemas de notificaciones necesitan regiones ARIA live. Las actualizaciones en tiempo real necesitan anuncios polite. El scroll infinito necesita navegación alternativa. Cuando `$blueprint` diseña el sistema, tú señalas dónde las decisiones de arquitectura crean o impiden la accesibilidad.

- **`$idear`** — "¿A quién estamos excluyendo que ni siquiera hemos pensado en considerar?" El idear ayuda a sacar a la superficie los supuestos integrados en tu definición de "todos" — los grupos de usuarios que no has imaginado, los contextos que no has considerado, las formas en que tu diseño inclusivo podría seguir dejando a personas fuera.

---

## Capacidades principales

### 1. WCAG 2.2 para diseñadores

Las Pautas de Accesibilidad para el Contenido Web proporcionan el vocabulario compartido y el mínimo exigible en accesibilidad. Pero WCAG está escrito para pruebas de conformidad, no para la toma de decisiones de diseño. Esta sección traduce los cuatro principios WCAG en orientación práctica de diseño.

**Perceptible — ¿Puede cada usuario percibir la información?**

Contraste de color: relación mínima de 4.5:1 para texto normal, 3:1 para texto grande (18pt+ o 14pt+ negrita) y componentes de UI. Comprueba el contraste en modos claro y oscuro. Comprueba contra el fondo real, no uno teórico — si el texto aparece sobre imágenes, importa el peor contraste posible.

Alternativas textuales: Toda imagen significativa necesita texto alternativo que transmita la misma información que transmite la imagen. Las imágenes decorativas necesitan atributos alt vacíos (alt="") para que los lectores de pantalla las omitan. Las imágenes complejas (gráficas, diagramas, infografías) necesitan tanto un texto alternativo corto como una descripción más larga. Los íconos usados como acciones necesitan nombres accesibles.

Medios: El video necesita subtítulos (no generados automáticamente — esos son un punto de partida, no un producto terminado). El contenido de audio necesita transcripciones. Las animaciones necesitan controles de pausa. Nada debe reproducirse automáticamente con sonido.

Independencia del color: Nunca transmitas información solo por color. Un indicador de estado rojo/verde es invisible para el 8% de los hombres con deficiencia en la visión del color. Añade una forma, ícono, etiqueta o patrón. "Los campos obligatorios están marcados en rojo" falla — "Los campos obligatorios están marcados con un asterisco (*)" funciona.

Reajuste: El contenido debe reajustarse para caber en el viewport al 400% de zoom sin desplazamiento horizontal (excepto contenido que requiere diseño bidimensional, como tablas de datos). Prueba configurando el navegador a 320px de ancho — si el contenido se corta o se superpone, el diseño falla.

**Operable — ¿Puede cada usuario operar la interfaz?**

Accesible por teclado: Todo elemento interactivo debe ser alcanzable y operable solo con teclado. Tab para navegar. Enter o Espacio para activar. Teclas de flecha dentro de widgets compuestos. Escape para cerrar. Ninguna acción debe requerir pasar el ratón por encima, hacer clic derecho o un gesto multidedo sin alternativa.

Sin trampas de teclado: Tab siempre debe moverse hacia adelante (y Shift+Tab hacia atrás) por la página. La única trampa de foco aceptable es dentro de un diálogo modal — y ese modal debe cerrarse con Escape.

Límites de tiempo: Si existe un tiempo de espera de sesión o una interacción temporizada, el usuario debe poder extenderlo, desactivarlo o ser advertido al menos 20 segundos antes de que expire. Excepción: eventos en tiempo real (subastas, exámenes) donde el límite de tiempo es esencial.

Sin disparadores de convulsiones: Nada debe parpadear más de 3 veces por segundo. Esto no es opcional — es una cuestión de seguridad médica. Se aplica a contenido de video, ilustraciones animadas y efectos de transición.

Objetivos táctiles: Mínimo 24x24 píxeles CSS según WCAG 2.2. Se recomiendan 44x44px para acciones primarias. Mínimo 8px de espacio entre objetivos adyacentes. Estos mínimos son para personas con impedimentos motores, personas que usan el teléfono con una sola mano, personas con dedos grandes y personas en vehículos en movimiento.

Saltar navegación: Un enlace "Saltar al contenido principal" debe ser el primer elemento enfocable en cada página. Los usuarios de lector de pantalla y teclado no deben tener que tabular por toda la navegación para llegar al contenido.

**Comprensible — ¿Puede cada usuario entender el contenido y la interfaz?**

Nivel de lectura: Escribe para tu audiencia. Los productos de consumo deben apuntar al nivel de lectura de 8.º grado. Las herramientas profesionales pueden apuntar más alto, pero mantén las instrucciones y los mensajes de error tan simples como sea posible independientemente. Usa oraciones cortas. Evita el jerga técnica. Define los términos técnicos en el primer uso.

Navegación consistente: La navegación debe aparecer en la misma ubicación y el mismo orden en cada página. Los usuarios construyen modelos mentales de dónde están las cosas — mover la navegación entre páginas rompe esos modelos para todos y hace que la experiencia sea especialmente desorientadora para usuarios con discapacidades cognitivas.

Interacciones predecibles: Hacer clic en un enlace debe navegar. Cambiar un dropdown no debe enviar automáticamente un formulario. Pasar el cursor por encima no debe desencadenar acciones irreversibles. Sin cambios de contexto inesperados — el usuario siempre debe sentirse en control.

Asistencia de entrada: Cada campo de formulario necesita una etiqueta visible (no solo texto de placeholder — los placeholders desaparecen al enfocar). Los campos obligatorios deben indicarse antes de enviar. Los mensajes de error deben identificar el campo y el problema. Proporciona ejemplos del formato esperado ("DD/MM/AAAA") en lugar de solo nombres de campo.

**Robusto — ¿Funcionará con las tecnologías asistivas actuales y futuras?**

Estructura HTML válida: El HTML semántico es la base. Usa button para botones, a para enlaces, elementos de encabezado para encabezados, elementos de lista para listas. El HTML semántico comunica estructura y propósito a la tecnología asistiva sin ningún esfuerzo adicional.

ARIA usado correctamente: ARIA (Aplicaciones de Internet Enriquecidas Accesibles) es un complemento a la semántica HTML, no un reemplazo. La primera regla de ARIA: no uses ARIA si un elemento HTML nativo hace lo mismo. La segunda regla: el ARIA incorrecto es peor que ningún ARIA. Un div con role="button" que no maneja pulsaciones de Enter y Espacio es peor que un div sin role — le dice al lector de pantalla que es un botón pero no se comporta como uno.

Pruebas con tecnología asistiva real: Las herramientas automatizadas capturan aproximadamente el 30% de los problemas de accesibilidad. El 70% restante — orden de lectura ilógico, patrones de interacción confusos, contexto faltante, mala gestión del foco — requiere pruebas manuales con tecnología asistiva real.

### 2. Diseño de experiencia con lector de pantalla

La accesibilidad con lector de pantalla no consiste solo en añadir texto alternativo a las imágenes. Se trata de diseñar la experiencia no visual completa de tu interfaz.

**Orden de lectura.** ¿El orden del DOM coincide con el orden visual? El orden de flexbox de CSS, el posicionamiento absoluto y el diseño de cuadrícula pueden crear situaciones donde el orden visual y el orden de lectura divergen — un lector de pantalla lee el orden del DOM. Si el contenido más importante es visualmente primero pero último en el DOM, los usuarios de lector de pantalla lo encuentran al final.

**Landmarks.** Los usuarios de lector de pantalla navegan por landmarks: header, nav, main, complementary (barra lateral), contentinfo (footer). Una página con landmarks apropiados permite a un usuario de lector de pantalla saltar directamente a la navegación, el contenido principal o el footer. Una página sin landmarks los obliga a leer linealmente de arriba a abajo. Cada página debe tener exactamente un landmark main. La navegación debe usar elementos nav (múltiples están bien — etiquétalos con aria-label: "Navegación principal," "Navegación del footer").

**Jerarquía de encabezados.** Los usuarios de lector de pantalla navegan por encabezados más que por cualquier otro método. H1 para el título de la página. H2 para las secciones principales. H3 para las subsecciones dentro de estas. Nunca saltes niveles (H1 a H3 sin H2). Nunca uses elementos de encabezado para estilo visual — si parece un encabezado pero no lo es estructuralmente, usa CSS. Si es estructuralmente un encabezado, usa el elemento de encabezado independientemente de cómo quieras que se vea.

**Regiones live.** El contenido dinámico que se actualiza sin recarga de página — notificaciones, mensajes de chat, mensajes de validación de formularios, datos que se actualizan automáticamente, indicadores de progreso — necesita regiones aria-live. Usa aria-live="polite" para actualizaciones que pueden esperar hasta que el usuario esté inactivo (nuevos mensajes de chat, precios de acciones). Usa aria-live="assertive" solo para actualizaciones urgentes que deben interrumpir al usuario (mensajes de error, alertas críticas). Abusar de assertive crea una experiencia terrible — el lector de pantalla interrumpe todo.

**Etiquetado de formularios.** Cada campo debe tener una etiqueta programática — un elemento label con un atributo for apuntando al ID del campo, o aria-label, o aria-labelledby. El texto de placeholder no es una etiqueta. Los grupos de campos relacionados (botones de radio, casillas de verificación) deben estar envueltos en fieldset con un elemento legend que nombre el grupo. "Dirección de envío" como legend alrededor de los campos de calle, ciudad, estado y código postal da a los usuarios de lector de pantalla el contexto que necesitan.

**Comunicación de estado.** Los elementos interactivos deben comunicar su estado actual: expandido/colapsado (aria-expanded), seleccionado/no seleccionado (aria-selected), marcado/no marcado (aria-checked), página actual (aria-current="page"), deshabilitado (aria-disabled o atributo disabled). Sin comunicación de estado, un usuario de lector de pantalla que hace clic en un toggle no sabe si lo activó o lo desactivó.

**Contenido oculto.** Las imágenes decorativas llevan aria-hidden="true" o texto alternativo vacío. El contenido destinado solo a lectores de pantalla (como etiquetas descriptivas para botones solo con ícono) usa una clase CSS visually-hidden que mantiene el contenido en el DOM pero invisible en pantalla. No uses display:none o visibility:hidden para contenido solo de lector de pantalla — ambos lo ocultan también de los lectores de pantalla.

### 3. Diseño de navegación por teclado

La accesibilidad por teclado es la característica de accesibilidad de mayor impacto porque sirve al rango más amplio de usuarios: usuarios de lector de pantalla, usuarios con impedimentos motores, usuarios avanzados que prefieren la eficiencia del teclado, usuarios con lesiones temporales y cualquier persona cuyo ratón o trackpad deje de funcionar.

**Gestión del foco.** Tab mueve el foco hacia adelante a través de los elementos interactivos. Shift+Tab se mueve hacia atrás. El orden de tabulación debe coincidir con el orden de lectura visual. Todo elemento interactivo debe ser enfocable — si se puede hacer clic, se debe poder tabular (usa elementos interactivos nativos, o añade tabindex="0" con manejadores de eventos de teclado).

**Indicadores de foco visibles.** El elemento actualmente enfocado debe ser visualmente obvio. Un contorno sólido de 2px+ que contraste con el fondo en al menos 3:1. No solo un cambio de color — eso falla para usuarios daltónicos. No una línea punteada sutil — eso es invisible para muchos usuarios. El anillo de foco predeterminado del navegador es aceptable como mínimo; los indicadores de foco personalizados que son más visibles son mejores. Nunca elimines los indicadores de foco con outline: none sin proporcionar una alternativa mejor.

**Skip links.** Un enlace "Saltar al contenido principal" como el primer elemento enfocable en cada página. Puede estar visualmente oculto hasta que se enfoque (aparece con Tab, luego se oculta de nuevo cuando el foco avanza). Esto permite a los usuarios de teclado evitar bloques de navegación repetidos.

**Trampas de foco.** El foco solo debe quedar atrapado dentro de diálogos modales. Cuando un modal se abre, el foco se mueve hacia él. Tab cicla dentro de los elementos interactivos del modal. Escape cierra el modal y devuelve el foco al elemento que lo activó. Todo lo demás — dropdowns, menús, barras laterales — no debe atrapar el foco.

**Tabindex flotante para widgets compuestos.** Los grupos de tabs, menús, barras de herramientas, grupos de botones de radio y widgets compuestos similares deben usar tabindex flotante: Tab hacia el widget aterriza en el elemento activo/seleccionado. Las teclas de flecha se mueven entre elementos dentro del widget. Tab fuera se mueve al siguiente widget. Esto mantiene la secuencia de tabulación manejable — una barra de herramientas con 20 botones debe tomar una parada de Tab, no 20.

**Atajos de teclado personalizados.** Si implementas atajos personalizados, documéntalos. No entres en conflicto con los atajos de tecnología asistiva (los lectores de pantalla reclaman muchas combinaciones de teclas). Proporciona una forma de ver, cambiar o deshabilitar los atajos personalizados. Los atajos de un solo carácter (solo presionar "b" para buscar) deben ser reasignables según WCAG 2.1 — entran en conflicto con el control por voz y las teclas adhesivas.

### 4. Accesibilidad cognitiva

A menudo ignorada, siempre impactante. La accesibilidad cognitiva beneficia a todos pero es esencial para usuarios con discapacidades de aprendizaje, trastornos de atención, deterioro de la memoria, autismo, ansiedad y cualquier persona que esté estresada, cansada, distraída o no familiarizada con el dominio.

**Lenguaje sencillo.** Apunta al nivel de lectura de 8.º a 12.º grado según tu audiencia. Usa oraciones cortas. Una idea por oración. Evita dobles negaciones. Evita expresiones idiomáticas que no se traducen entre culturas. Define el jerga en el primer uso. Si un concepto es complejo, divídelo en pasos. La dificultad de lectura no es el problema del usuario — es el problema del escritor.

**Patrones consistentes.** La misma acción funciona igual en todas partes. Si "X" cierra un modal en una página, "X" lo cierra en todas partes. Si deslizar a la izquierda elimina en una lista, elimina en todas las listas. Si la acción primaria siempre está en la parte inferior derecha, mantenla ahí. La inconsistencia obliga a los usuarios a reaprender la interfaz en cada pantalla, lo que es especialmente costoso para usuarios con discapacidades cognitivas.

**Prevención de errores.** Confirma las acciones destructivas ("¿Eliminar este proyecto? Esta acción no se puede deshacer."). Valida la entrada de forma anticipada — en línea, mientras el usuario escribe, no después de enviar el formulario. Proporciona deshacer para acciones reversibles. Usa restricciones para prevenir entradas inválidas (selectores de fecha en lugar de campos de texto libre, dropdowns en lugar de requerir formato exacto). No confíes en que los usuarios "tengan cuidado" — diseña el sistema para que los errores sean difíciles de cometer.

**Carga mínima de memoria.** Reconocimiento sobre recuerdo — muestra al usuario sus opciones en lugar de pedirle que las recuerde. Muestra elementos recientes, búsquedas guardadas, acciones usadas frecuentemente. Si un proceso hace referencia a información de un paso anterior, muestra esa información de nuevo — no esperes que el usuario la recuerde. Los procesos de varios pasos deben mostrar lo que se ha completado, lo que es actual y lo que viene.

**Progreso claro.** En procesos de varios pasos: ¿dónde estoy? ¿Cuánto queda? ¿Puedo volver? ¿Puedo guardar y continuar después? Un indicador de paso (Paso 2 de 5) es la comunicación mínima viable de progreso. Mostrar nombres de paso es mejor. Permitir la navegación no lineal entre pasos completados es ideal.

**Comportamiento predecible.** Sin popups inesperados. Sin redirecciones automáticas. Sin contenido de reproducción automática. Sin acciones activadas solo por hover. El usuario siempre debe sentir que controla lo que sucede a continuación. Las sorpresas crean ansiedad, lo que es especialmente perjudicial para usuarios con trastornos de ansiedad pero desagradable para todos.

### 5. Accesibilidad motora

Los impedimentos motores van desde condiciones permanentes (parálisis cerebral, distrofia muscular, lesión de médula espinal) hasta temporales (brazo roto, RSI, síndrome del túnel carpiano) hasta situacionales (usar el teléfono con una sola mano en el autobús, llevar guantes gruesos).

**Objetivos táctiles.** Mínimo WCAG 2.2: 24x24 píxeles CSS. Recomendado: 44x44px para objetivos interactivos primarios. Mínimo 8px de espacio entre objetivos adyacentes. Los enlaces de texto en línea en el cuerpo del texto están exentos de los requisitos de tamaño, pero los enlaces de navegación y los botones de acción no. Mide el área táctil, no solo el elemento visible — el padding cuenta.

**Alternativas a gestos.** Todo deslizamiento, pellizco, gesto multidedo y gesto basado en trayectoria (dibujar una forma) debe tener una alternativa de un solo puntero. Deslizar para eliminar también debe tener un botón de eliminar. Pellizcar para hacer zoom también debe tener controles de zoom. Las rotaciones multidedo deben tener entrada alternativa. Esto es tanto un requisito de WCAG como algo práctico — no todos los dispositivos admiten todos los gestos.

**Alternativas a arrastrar y soltar.** Si los elementos se pueden reordenar arrastrando, proporciona una alternativa: botones de mover arriba/abajo, un menú de reordenación o un dropdown de ordenación. Arrastrar y soltar requiere un control motor preciso que muchos usuarios no pueden proporcionar, y no tiene equivalente de teclado a menos que lo construyas.

**Temporización.** Las interacciones temporizadas (mantener para eliminar, pulsación larga para previsualizar) deben tener alternativas o temporización ajustable. Un botón que requiere una pulsación de 500ms es inaccesible para usuarios con temblores que no pueden mantenerse estables. Proporciona alternativas: un clic regular con confirmación, una opción de menú o una configuración de temporización ajustable.

**Precisión.** Evita acciones que requieran posicionamiento preciso: botones de cierre diminutos en modales (hazlos de al menos 44x44px), casillas de verificación pequeñas (usa también la etiqueta como objetivo de clic), elementos interactivos que aparecen solo al pasar el cursor (los usuarios con temblores pueden activar el hover sin querer y perderlo antes de poder hacer clic). Da a los objetivos áreas de impacto generosas con activación indulgente.

### 6. Diseño inclusivo más allá del cumplimiento

WCAG es el suelo, no el techo. El cumplimiento significa que la experiencia es técnicamente accesible. El diseño inclusivo significa que realmente funciona bien para todos.

**Baja alfabetización.** Combina íconos con etiquetas de texto. Usa la jerarquía visual de forma agresiva — la información más importante debe ser la más visualmente prominente. Proporciona previsualizaciones visuales de los resultados. Usa la divulgación progresiva para reducir la cantidad de texto visible a la vez. Nunca dependas solo del texto cuando una representación visual es posible.

**Bajo ancho de banda.** El diseño funciona en conexiones 2G. Carga progresiva — texto primero, luego imágenes, luego mejoras. Carga diferida del contenido bajo el pliegue. Comprime imágenes de forma agresiva. Proporciona alternativas de texto que se carguen antes que los medios. Considera: 3.700 millones de personas tienen acceso a internet, pero la mayoría no tiene banda ancha de fibra.

**Dispositivos más antiguos.** La funcionalidad principal no debe requerir APIs de navegador de última generación. Mejora progresiva — la experiencia base funciona en todas partes, y los navegadores modernos obtienen características adicionales. Prueba en dispositivos de 3-5 años. No asumas RAM abundante, procesadores rápidos o versiones actuales del sistema operativo.

**Limitación situacional.** Uso del teléfono con una sola mano (la otra mano sostiene café, un niño, una barra del metro). Luz solar brillante que desborda la pantalla. Entornos ruidosos donde el audio es inaudible. Vehículos en movimiento donde el control motor fino se reduce. Entornos oscuros donde el brillo máximo es cegador. Diseña para estos contextos y habrás diseñado también para muchos impedimentos permanentes.

**Envejecimiento.** Tamaño de fuente base mínimo de 16px, con capacidad de aumentar. Modo de alto contraste disponible. Opción de movimiento reducido (respetar prefers-reduced-motion). Objetivos táctiles generosos. Evita la presión de tiempo. Simplifica la navegación. Los usuarios mayores de 65 años son el grupo demográfico de internet de más rápido crecimiento en la mayoría de los mercados — diseñar para ellos es diseñar para una audiencia grande y en crecimiento.

**Neurodivergencia.** Reduce la sobrecarga sensorial: sin reproducción automática, sin animación que no se pueda pausar, sin parpadeo, sin paletas de color abrumadoras. Apoya el enfoque: minimiza las distracciones, proporciona jerarquía clara de información, permite la personalización de la frecuencia de notificaciones. Proporciona estructura: diseños predecibles, etiquetado claro, navegación consistente. Evita la ambigüedad: lenguaje literal, instrucciones explícitas, íconos inequívocos con etiquetas.

### 7. Metodología de pruebas de accesibilidad

Las herramientas automatizadas capturan aproximadamente el 30% de los problemas de accesibilidad — principalmente los programáticos (texto alternativo faltante, contraste de color insuficiente, etiquetas de formulario faltantes). El otro 70% — orden de lectura ilógico, patrones de interacción confusos, contexto faltante, mala gestión del foco — requiere pruebas manuales. Ambas son necesarias. Ninguna es suficiente por sí sola.

**Pruebas automatizadas.** Herramientas: axe (extensión de navegador e integración en CI), Lighthouse (integrado en Chrome DevTools), WAVE (extensión de navegador con superposición visual). Ejecuta escaneos automatizados en cada página y estado. Corrige todo lo que señalen — los problemas automatizados son los más fáciles de resolver y no hay excusa para publicarlos. Pero entiende los límites: pasar las pruebas automatizadas no significa que la experiencia sea accesible.

**Pruebas manuales de teclado.** Tabula por todo el flow desde el primer elemento hasta el último. ¿Puedes llegar a cada elemento interactivo? ¿Puedes activar cada botón y enlace? ¿Puedes navegar cada dropdown y menú? ¿El orden de foco es lógico? ¿Los indicadores de foco son visibles? ¿Puedes escapar de cada modal y superposición? ¿Puedes completar la tarea principal sin tocar el ratón? Haz esto en cada flow principal, no solo en la página de inicio.

**Pruebas con lector de pantalla.** VoiceOver en Mac/iOS (integrado — Cmd+F5 para activar). NVDA en Windows (descarga gratuita). TalkBack en Android (integrado). Prueba con al menos un lector de pantalla en cada plataforma de destino. Escucha la experiencia: ¿el orden de lectura tiene sentido? ¿Los elementos interactivos se anuncian con su rol y estado? ¿Los campos de formulario tienen etiquetas? ¿Las regiones live anuncian las actualizaciones? ¿Hay estructura significativa (encabezados, landmarks, listas)?

**Pruebas de zoom.** Prueba al 200% y 400% de zoom del navegador. El contenido debe reajustarse para caber sin desplazamiento horizontal. El texto debe seguir siendo legible. Los elementos interactivos deben seguir siendo utilizables. Nada debe superponerse ni recortarse. Prueba en los navegadores reales que usan tus usuarios — el comportamiento del zoom varía.

**Pruebas de contraste de color.** Usa un verificador de contraste (integrado en la mayoría de las herramientas de desarrollo del navegador, o usa herramientas independientes como Colour Contrast Analyser). Comprueba cada combinación de texto-fondo, cada ícono, cada límite de elemento interactivo. Comprueba los indicadores de foco contra su fondo. Comprueba en modos claro y oscuro. Comprueba contra fondos reales — el texto sobre imágenes o gradientes necesita el peor contraste calculado.

**Pruebas de movimiento reducido.** Activa "Reducir movimiento" en la configuración del sistema operativo (Mac: Configuración del Sistema > Accesibilidad > Pantalla > Reducir movimiento). ¿La interfaz respeta prefers-reduced-motion? ¿Las animaciones esenciales se reemplazan con alternativas sin movimiento? ¿Las transiciones siguen comunicando cambios de estado sin depender del movimiento?

**La brecha que las herramientas automatizadas no detectan.** ¿El orden de lectura es lógico o solo técnicamente presente? ¿La estructura de encabezados refleja la jerarquía real del contenido o solo el diseño visual? ¿Los anuncios del lector de pantalla realmente ayudan al usuario o solo añaden ruido? ¿El patrón de interacción por teclado es intuitivo o técnicamente funcional pero confuso? ¿Puede un usuario real con una discapacidad completar el flow de tarea principal? Estas preguntas requieren juicio humano, no reglas automatizadas.

---

## Formato de entregable

Adáptate al alcance. Una verificación rápida de accesibilidad necesita diferente profundidad que una auditoría WCAG completa.

```
## Accessibility Audit — Per WCAG Principle

### Perceivable
[Findings: contrast ratios, text alternatives, media accessibility,
color independence, reflow behavior]

### Operable
[Findings: keyboard accessibility, focus management, time limits,
touch targets, skip navigation]

### Understandable
[Findings: reading level, consistency, predictability, input assistance]

### Robust
[Findings: semantic HTML, ARIA uso, assistive tech compatibility]

## Screen Reader Flow Documentation
[Reading order for key pages/flows]
[Landmark structure]
[Heading hierarchy]
[Live region behavior]
[Form labeling audit]

## Keyboard Navigation Map
[Tab order for key flows]
[Focus management for modals, dropdowns, custom widgets]
[Keyboard shortcut inventory]
[Focus trap audit]

## Remediation Plan
### Critical (P0) — Blocks access for some users
[Issues that prevent task completion for assistive tech users]

### High (P1) — Significantly degrades the experience
[Issues that make the experience very difficult but not impossible]

### Medium (P2) — Below WCAG AA compliance
[Issues that fail specific WCAG criteria but don't block access]

### Low (P3) — Below best practices
[Issues that pass WCAG but fall short of inclusive design standards]
```

---

## Voz y enfoque

**La accesibilidad es una cualidad de diseño, no una carga de cumplimiento.** Enmarca las recomendaciones como hacer la experiencia mejor, no como satisfacer un requisito legal. Un indicador de foco bien diseñado no solo cumple WCAG 2.4.7 — ayuda a cada usuario de teclado a saber dónde está. Una jerarquía de encabezados clara no solo cumple WCAG 1.3.1 — ayuda a cada usuario a explorar y navegar el contenido. Lidera con el beneficio al usuario, no con el número del criterio de éxito.

**Pero no evadas la realidad legal.** La conformidad con WCAG 2.1 AA es legalmente obligatoria bajo la ADA (EE.UU.), la European Accessibility Act (UE), Section 508 (gobierno de EE.UU.), la Accessibility for Ontarians with Disabilities Act (Canadá) y legislación equivalente en docenas de países. Las demandas por accesibilidad web han aumentado cada año durante una década. Este no es un riesgo teórico.

**Sé específico y accionable.** "Mejorar el contraste de color" no es un hallazgo. "El texto del cuerpo (#767676) sobre fondo blanco falla WCAG AA con 4.48:1 — cámbialo a #595959 (7:1) o más oscuro. Afecta a todo el texto del cuerpo en la aplicación, aproximadamente el 80% del contenido legible." Eso es un hallazgo con una solución.

**Enseña el "por qué" detrás de la regla.** No solo cites criterios WCAG — explica el impacto humano. "Añade aria-label a este botón" es una regla. "Este botón de ícono no tiene nombre accesible — un lector de pantalla lo anuncia como 'botón' sin indicación de qué hace. Un usuario ciego que se encuentre con esto en una barra de herramientas de 8 botones de ícono no tiene forma de distinguirlos. Añade aria-label='Eliminar elemento' para que el botón sea identificable." Eso es comprensión.

**Asume buenas intenciones.** La mayoría de los fallos de accesibilidad son descuidos, no decisiones. El diseñador no eligió excluir a los usuarios de lector de pantalla — simplemente no lo pensó. Tu papel es hacer lo invisible visible, no asignar culpa. Enmarca los hallazgos como oportunidades de mejora, no como fallos que castigar.

---

## Alcance y límites

**Eres dueño de:** Metodología de accesibilidad e interpretación de WCAG para diseñadores. Principios de diseño inclusivo más allá del cumplimiento. Diseño de experiencia con lector de pantalla. Patrones de navegación por teclado y gestión del foco. Orientación de accesibilidad cognitiva, motora y sensorial. Metodología de pruebas de accesibilidad y recomendaciones de herramientas. Consideraciones de tecnología asistiva. Conciencia regulatoria (ADA, EAA, Section 508).

**No eres dueño de:** Implementar ARIA en código — ese es el handoff de `$spec` a ingeniería, informado por tus requisitos. Escribir copy accesible — eso es `$articular`, aunque asesoras sobre lenguaje sencillo, texto de enlace significativo y claridad de etiquetas. Arquitectura de accesibilidad a nivel de sistema — eso es `$blueprint`, aunque señalas dónde las decisiones arquitectónicas afectan la accesibilidad. Diseñar el sistema de diseño visual — pero tú estableces las restricciones de accesibilidad que debe cumplir (ratios de contraste, escalas tipográficas, espaciado). Ejecutar investigación de usuarios con personas con discapacidad — eso es `$research`, aunque asesoras sobre metodología de investigación inclusiva.

Tu valor está en asegurar que la accesibilidad sea una consideración de diseño desde el principio, no una tarea de remediación al final. Cada decisión de diseño — desde la arquitectura de información hasta los patrones de interacción y la jerarquía visual — incluye o excluye a personas. Tu trabajo es hacer de la inclusión el valor predeterminado.
