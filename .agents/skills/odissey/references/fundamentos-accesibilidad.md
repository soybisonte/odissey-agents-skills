# Fundamentos de accesibilidad

Esta guía traduce los estándares de accesibilidad en decisiones prácticas de diseño. No sustituye una auditoría técnica ni determina por sí sola las obligaciones legales de un producto.

## Índice

- [WCAG 2.2 para diseño](#wcag-22-para-diseño)
- [Panorama de tecnologías de asistencia](#panorama-de-tecnologías-de-asistencia)
- [Diseño del flujo para lectores de pantalla](#diseño-del-flujo-para-lectores-de-pantalla)
- [Diseño de navegación por teclado](#diseño-de-navegación-por-teclado)
- [Accesibilidad cognitiva](#accesibilidad-cognitiva)
- [Diseño inclusivo más allá de la discapacidad](#diseño-inclusivo-más-allá-de-la-discapacidad)

## WCAG 2.2 para diseño

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) es una Recomendación del W3C. Organiza la accesibilidad web alrededor de cuatro principios: perceptible, operable, comprensible y robusto (POUR, por sus siglas en inglés). Conviene leerla como una especificación verificable que orienta lo que el diseño debe lograr para un espectro amplio de capacidades humanas, no como una mera lista de control.

WCAG define tres niveles de conformidad —A, AA y AAA—, pero el nivel objetivo y la obligación legal aplicable dependen del producto, el contrato, el sector y la jurisdicción. WCAG no es por sí misma la ley en todos los países. Confirma con especialistas en accesibilidad y asesoría jurídica qué versión, nivel, alcance y normativa corresponden a cada lanzamiento.

### Perceptible

La información y los componentes de la interfaz deben presentarse de formas que las personas puedan percibir. No todo el mundo ve, oye o procesa información de la misma manera.

**Alternativas textuales (1.1):** Todo elemento no textual que comunique información necesita un equivalente en texto. Las imágenes requieren texto alternativo; los iconos, una etiqueta; los gráficos, una tabla de datos o un resumen; y el video, subtítulos y audiodescripción. La pregunta de diseño es: si desapareciera este elemento visual, ¿se perdería información?

**Errores frecuentes de diseño:** Añadir descripciones extensas a imágenes decorativas —un lector de pantalla tendría que repetir en cada página «fotografía de archivo de un equipo diverso colaborando en una oficina moderna»—; dejar vacío el texto alternativo de imágenes informativas; describir un gráfico solo como «gráfico» sin explicar los datos; o usar iconos sin nombre accesible. La solución es un texto alternativo intencional: describe lo que la imagen comunica, no solo lo que representa.

**Medios temporales (1.2):** El video necesita subtítulos —texto sincronizado del contenido hablado— y audiodescripción —narración del contenido visual—. El audio necesita transcripción y el contenido en directo, subtitulado en tiempo real. Esto no beneficia solo a personas sordas: los subtítulos ayudan a cualquiera que esté en un entorno ruidoso o que necesite silencio.

**Adaptable (1.3):** La estructura de la información debe ser programática, no solo visual. Un encabezado grande y en negrita implementado como `<div>` es invisible como encabezado para un lector de pantalla. Una tabla de datos creada con elementos posicionados en lugar de `<table>` pierde las relaciones entre filas y columnas. Las decisiones de jerarquía, agrupación y secuencia deben poder implementarse con estructura semántica.

**Distinguible (1.4):** Los mínimos de contraste son 4.5:1 para texto normal y 3:1 para texto grande —al menos 18 pt, aproximadamente 24 px CSS, o 14 pt, aproximadamente 18.66 px CSS, en negrita—. WCAG 1.4.11 establece 3:1 para la información visual necesaria de componentes de interfaz y objetos gráficos, con sus excepciones. Para cuerpo de texto, procura superar el mínimo. El color no debe ser el único medio para comunicar información: un borde rojo de error también necesita icono o texto. El texto debe poder ampliarse al 200 % sin perder contenido ni funcionalidad.

**Novedad de 2.2 — Movimientos de arrastre (2.5.7):** Toda función que dependa de arrastrar debe ofrecer una alternativa sin arrastre. Por ejemplo, reordenar mediante arrastre también debe admitir botones para subir o bajar, u otro método de entrada.

### Principio operable

La interfaz debe poder manejarse con varios métodos de entrada, no solo con ratón o pantalla táctil.

**Accesible por teclado (2.1):** Todo debe funcionar con teclado. Cada elemento interactivo debe recibir foco y poder activarse. No debe haber trampas de teclado: la persona tiene que poder salir de cualquier componente. Los atajos personalizados no deben entrar en conflicto con el navegador ni con las tecnologías de asistencia.

**Tiempo suficiente (2.2):** Si el contenido tiene límite de tiempo, debe poder desactivarse, ajustarse o ampliarse. Los cierres de sesión requieren aviso y opción de extensión. El contenido que se actualiza automáticamente necesita controles para pausar o detener. Cualquier contenido en movimiento o reproducción automática debe poder detenerse.

**Convulsiones y reacciones físicas (2.3):** Evita contenido que parpadee más de tres veces por segundo. No es un riesgo teórico: puede provocar convulsiones fotosensibles. Permite reducir las animaciones de movimiento y respeta `prefers-reduced-motion`.

**Navegable (2.4):** Incluye un enlace para saltar al contenido principal como primer elemento enfocable. Usa títulos de página descriptivos. El orden del foco debe ser lógico y predecible, normalmente igual al orden visual de lectura. El texto de los enlaces debe comprenderse en contexto: «Más información» resulta ambiguo; «Lee nuestra política de accesibilidad» comunica el destino. Los encabezados y etiquetas también deben ser descriptivos.

**Novedad de 2.2 — Foco no oculto, mínimo (2.4.11):** Cuando un componente recibe foco de teclado, otros contenidos —cabeceras fijas, modales o avisos— no deben ocultarlo por completo. Al menos una parte debe permanecer visible.

**Novedad de 2.2 — Tamaño del objetivo, mínimo (2.5.8):** Los objetivos interactivos deben medir al menos 24 × 24 píxeles CSS, con las excepciones previstas por el criterio, como ciertos enlaces en línea o controles nativos. Esto ayuda a personas con discapacidad motriz y a cualquiera que use una pantalla pequeña.

### Comprensible

El contenido y el comportamiento de la interfaz deben poder entenderse.

**Legible (3.1):** Declara el idioma de la página con el atributo `lang` e identifica los cambios de idioma dentro de ella. Define palabras inusuales, abreviaturas y jerga. Aunque su implementación sea técnica, la elección y explicación de términos es una decisión de diseño.

**Predecible (3.2):** Los componentes que se ven iguales deben funcionar igual en todo el producto. La navegación debe ser consistente entre páginas. Los cambios de contexto —abrir otra ventana, enviar un formulario o mover el foco— solo deben suceder cuando se esperan, nunca al recibir foco ni al introducir datos sin aviso.

**Ayuda para la entrada (3.3):** Identifica y describe los errores con texto. Proporciona etiquetas e instrucciones para cada entrada y, cuando sea posible, sugiere cómo corregirla. En envíos importantes —financieros, jurídicos o de modificación de datos— permite revertir, comprobar o confirmar la operación según el criterio aplicable.

**Novedad de 2.2 — Entrada redundante (3.3.7):** No solicites de nuevo información que la persona ya proporcionó durante el mismo proceso, salvo las excepciones del criterio. Si las direcciones de envío y facturación coinciden, ofrece una opción para reutilizarlas.

**Novedad de 2.2 — Autenticación accesible, mínimo (3.3.8):** La autenticación no debe exigir pruebas de función cognitiva —acertijos o tareas de memoria— sin una alternativa adecuada. Admite gestores de contraseñas, llaves de acceso y copiar y pegar códigos de verificación.

### Robusto

El contenido debe poder interpretarse de manera fiable por una amplia variedad de agentes de usuario, incluidas las tecnologías de asistencia. Es principalmente una cuestión de implementación, pero el diseño influye mediante la elección de componentes y la claridad de las especificaciones.

---

## Panorama de tecnologías de asistencia

Diseñar con accesibilidad exige entender cómo se usan realmente las tecnologías de asistencia, no solo marcar casillas.

### Lectores de pantalla

Son programas que convierten el contenido visual en voz o braille. Entre los principales están JAWS —Windows, frecuente en contextos profesionales—, NVDA —Windows, gratuito y de código abierto—, VoiceOver —integrado en macOS e iOS—, TalkBack —integrado en Android— y Narrator —integrado en Windows—.

**Cómo se utilizan:** Las personas con experiencia no escuchan necesariamente cada palabra. Navegan por encabezados —tecla H—, regiones —tecla D en JAWS—, enlaces —Tab— y controles de formulario. Primero recorren la estructura y después profundizan en el contenido. Una página sin encabezados ni regiones apropiadas es como una hoja impresa sin formato: técnicamente legible, pero poco utilizable.

**Idea equivocada común:** «Quien usa un lector de pantalla es ciego». Muchas personas tienen visión parcial y combinan el lector con ampliación o alto contraste. Diseña para esa combinación, no para una suposición única.

### Acceso mediante conmutadores

Quienes no pueden usar ratón, pantalla táctil o teclado convencional pueden utilizar conmutadores: botones físicos, dispositivos de soplido y succión, seguimiento ocular o movimientos de cabeza. La navegación avanza de forma secuencial por los elementos interactivos.

**Implicación de diseño:** La cantidad de elementos interactivos afecta de forma directa. Llegar al último de 50 controles puede requerir 50 activaciones. Agrupa acciones relacionadas, proporciona mecanismos de salto y coloca primero las acciones más habituales.

### Control por voz

Permite navegar e interactuar mediante comandos hablados. Algunos ejemplos son Dragon NaturallySpeaking, Voice Control de macOS/iOS y Voice Access de Android.

**Implicación de diseño:** Las personas dicen lo que ven: «pulsa Enviar» o «pulsa el botón de búsqueda». Si la etiqueta visible no coincide con el nombre accesible, el comando puede fallar. Haz que ambos coincidan.

### Ampliación

El software o las funciones del sistema operativo amplían partes de la pantalla para personas con baja visión.

**Implicación de diseño:** Con un zoom del 200 % se ve aproximadamente una cuarta parte del área original; al 400 %, cerca de una dieciseisava parte. El diseño debe refluir: exigir desplazamiento horizontal al ampliar hasta el 400 % incumple WCAG 1.4.10 en los supuestos del criterio. Piensa en la ampliación como un viewport muy estrecho, no como una versión agrandada de la pantalla completa.

---

## Diseño del flujo para lectores de pantalla

### Orden de lectura

Los lectores de pantalla procesan el DOM en el orden de origen. La posición visual definida con CSS puede diferir y generar una desconexión entre lo que ve una persona y lo que escucha otra.

**Regla:** El orden visual y el de origen deben coincidir. Si una tarjeta muestra título, imagen y descripción, el origen debe seguir título → imagen → descripción, no imagen → título → descripción con reposicionamiento CSS.

**Fallo común:** CSS Grid y Flexbox facilitan reordenar visualmente el contenido sin modificar el origen. Esto confunde tanto a quienes usan lector de pantalla como a quienes navegan con teclado, porque Tab sigue por defecto el orden de origen.

### Regiones

Las regiones ARIA definen las grandes áreas de una página: `banner`, `navigation`, `main`, `complementary`, `contentinfo`, `search` y `form`. Los lectores de pantalla permiten saltar entre ellas para recorrer la estructura.

**Regiones mínimas:** Cada página necesita una región `<main>`, una `<nav>` para la navegación principal y `<header>` / `<footer>`. Si existen varias regiones de navegación, cada una requiere una etiqueta única, por ejemplo «Navegación principal» y «Navegación del pie».

### Regiones activas

El contenido que cambia de forma dinámica —notificaciones, mensajes de chat, estados o datos en tiempo real— debe anunciarse con regiones activas ARIA.

**`aria-live="polite"`:** Anuncia cuando el lector queda libre. Úsalo para actualizaciones no urgentes, como estados o recuentos de resultados.

**`aria-live="assertive"`:** Interrumpe la voz actual. Resérvalo para información urgente, como alertas de error o avisos con límite de tiempo. Las interrupciones frecuentes vuelven inutilizable la interfaz.

**`role="alert"`:** Es implícitamente asertivo. Úsalo para errores y avisos críticos. Se anuncia de inmediato cuando cambia o se incorpora al DOM.

**`role="status"`:** Es implícitamente cortés. Úsalo para estados y actualizaciones no críticas. «El archivo se guardó correctamente» es un estado, no una alerta.

---

## Diseño de navegación por teclado

### Gestión del foco

**El foco debe ser visible.** El indicador predeterminado del navegador puede no encajar con la estética, pero funciona. Si lo sustituyes, el estilo nuevo debe ser igual o más perceptible, por ejemplo un contorno sólido de 2 px con contraste suficiente. Quitar `outline` sin alternativa es un fallo de accesibilidad.

**El foco debe ser lógico.** El orden de Tab debe seguir el orden visual de lectura: de izquierda a derecha y de arriba abajo en idiomas LTR. Forzar otro orden con valores de `tabindex` mayores que 0 genera confusión para teclado y lector de pantalla.

**El foco debe gestionarse ante cambios de interfaz.** Al abrir un modal, pasa el foco al modal; al cerrarlo, devuélvelo al control que lo abrió. Tras eliminar contenido, muévelo al siguiente elemento lógico. Al terminar una edición en línea, llévalo al contenido guardado. Cada cambio dinámico necesita un plan de foco.

### Orden de tabulación

**Elementos enfocables:** Enlaces, botones, entradas de formulario, áreas de texto, selectores y elementos con `tabindex="0"`. Solo los controles interactivos deben estar en el orden de Tab. No hagas enfocables encabezados, párrafos o `div` salvo que implementen un componente interactivo personalizado.

**Enlaces de salto:** El primer elemento enfocable debe ser «Saltar al contenido principal». Evita recorrer toda la navegación en cada página. Puede permanecer visualmente oculto hasta recibir foco: visible cuando hace falta, discreto el resto del tiempo.

### Patrones de teclado para componentes personalizados

Los elementos HTML nativos —botones, enlaces y entradas— incorporan comportamiento de teclado. Los componentes personalizados deben implementarlo de acuerdo con WAI-ARIA Authoring Practices.

**Pestañas:** Las flechas se desplazan entre pestañas; Tab lleva al panel; Inicio/Fin mueve a la primera o última.

**Menús:** Las flechas recorren elementos; Enter/Espacio activa; Escape cierra; la escritura anticipada selecciona por las primeras letras.

**Modales y diálogos:** Mientras están abiertos, el foco permanece dentro; Escape cierra; al cerrar, el foco regresa al control de origen. El contenido de fondo queda inerte mediante el atributo `inert` o una técnica apropiada.

**Vistas de árbol:** Las flechas navegan; derecha expande un nodo; izquierda lo contrae o va al padre; Enter activa.

---

## Accesibilidad cognitiva

La accesibilidad no se limita a capacidades sensoriales o motrices. Las discapacidades cognitivas y de aprendizaje también condicionan el uso del producto.

### Lenguaje claro

Usa lenguaje directo, frases breves, palabras frecuentes y terminología consistente. Define los términos técnicos en contexto. Esto beneficia a todo el mundo y es esencial para personas con discapacidades cognitivas o de aprendizaje, alfabetización limitada o menor dominio del idioma.

### Patrones consistentes

Haz lo mismo de la misma manera en todo el producto. Si una acción se llama «Eliminar» en un lugar, no la llames «Quitar» en otro. Si la acción principal está a la derecha en un diálogo, mantén esa convención. La consistencia reduce la carga de aprendizaje y de recordar cómo funciona la interfaz.

### Prevención de errores

Prevén antes de informar. Restringe entradas —por ejemplo, un selector de fecha en lugar de texto libre—, proporciona valores predeterminados útiles, muestra ejemplos de formato en contexto y desactiva combinaciones inválidas. Para acciones con consecuencias, ofrece una vista previa antes de confirmar.

### Simplificación de procesos

Divide los procesos largos en etapas claras y con nombre, acompañadas de indicadores de progreso. Permite guardar y continuar después. No obligues a retener información en la memoria entre pasos. Muestra un resumen antes del envío final.

---

## Diseño inclusivo más allá de la discapacidad

Los estándares cubren muchas barreras asociadas con discapacidades permanentes. El diseño inclusivo amplía la mirada a la diversidad humana, incluidas las limitaciones situacionales y temporales.

### Limitaciones situacionales

- **Uso con una mano:** Cargar a un bebé, sujetarse en el transporte o llevar un brazo en cabestrillo. Objetivos táctiles y gestos deben funcionar con una sola mano.
- **Luz solar intensa:** El texto con poco contraste desaparece en exteriores. Un contraste suficiente también ayuda una tarde cualquiera en un parque.
- **Entornos ruidosos:** El audio no sirve en una obra o un bar lleno. Subtítulos e indicadores visuales ayudan en esos contextos.
- **Atención dividida:** Cocinar o cuidar menores reduce la atención disponible. Las interfaces usadas en estas situaciones deben requerir la mínima atención visual posible. No diseñes para fomentar el uso durante la conducción.

### Alfabetización limitada

Diseñar para distintos niveles de alfabetización implica usar frases breves, palabras comunes, apoyos visuales junto al texto, pasos numerados y párrafos poco densos. No presupongas un nivel de lectura a partir del país, la profesión o la edad; valida con la audiencia real.

### Dispositivos antiguos y ancho de banda limitado

No todo el mundo dispone de un teléfono reciente ni de una conexión rápida. La accesibilidad también implica páginas ligeras, mejora progresiva, estados sin conexión funcionales e interfaces que, cuando sea viable, mantengan las tareas esenciales sin JavaScript.

### Envejecimiento

La edad puede modificar la visión —presbicia y menor sensibilidad al contraste—, la audición —pérdida de frecuencias altas—, el control motor —menor precisión y respuesta más lenta— y la cognición —procesamiento más lento y menor memoria de trabajo—. Diseña para la persona en la que se convertirá la audiencia, no solo para la que es hoy. Texto mayor, contraste alto, objetivos táctiles amplios, navegación sencilla y errores fáciles de corregir mejoran el producto para todo el mundo.
