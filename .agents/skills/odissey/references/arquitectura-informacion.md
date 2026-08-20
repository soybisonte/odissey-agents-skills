# Arquitectura de información

## Índice

- [Patrones de navegación](#patrones-de-navegación)
- [Diseño de taxonomías](#diseño-de-taxonomías)
- [Modelos mentales](#modelos-mentales)
- [Orientación espacial](#orientación-espacial)
- [Modelos de comportamiento de búsqueda](#modelos-de-comportamiento-de-búsqueda)
- [Metodología de clasificación de tarjetas y prueba de árbol](#metodología-de-clasificación-de-tarjetas-y-prueba-de-árbol)

## Patrones de navegación

Cada patrón de navegación implica un equilibrio entre facilidad para encontrar contenido, escalabilidad y carga cognitiva. No existe un patrón correcto para todos los casos: existe el patrón adecuado para tu contenido, tus usuarios y tu contexto.

### Jerárquico (árbol)

Es el patrón más común. El contenido se organiza en categorías anidadas: nivel superior → subcategoría → elemento.

**Cuándo funciona:** Conjuntos grandes de contenido con relaciones categóricas claras. Los usuarios tienen una idea general de la categoría a la que pertenece lo que buscan. Quienes crean contenido pueden mantener una categorización coherente.

**Cuándo falla:** Cuando las categorías se solapan de forma significativa (¿un «ratón inalámbrico» pertenece a Accesorios, Ordenadores o Periféricos?). Cuando la jerarquía supera los tres o cuatro niveles: los usuarios pierden rápidamente la orientación. Cuando refleja la estructura de la organización en lugar de los modelos mentales de los usuarios («Productos» → «Unidad de negocio A» → «División 2» → «Resultado del equipo Alpha»).

**Presta atención a:** El cajón de «varios». Si tienes una categoría llamada «Otros» o «General» que no deja de crecer, la jerarquía no funciona. También a los nombres de categorías que significan algo para la organización, pero nada para los usuarios.

### Central y radial (hub-and-spoke)

Un núcleo central conecta secciones independientes. Cada sección es, en gran medida, autónoma. Los usuarios vuelven al núcleo para navegar entre secciones.

**Cuándo funciona:** Aplicaciones móviles con áreas funcionales diferenciadas (Mensajes, Cámara, Perfil). Productos cuyas tareas son independientes; por ejemplo, no es necesario combinar los resultados de búsqueda con el carrito. Interfaces de quiosco y decodificadores en las que el modelo de entrada favorece una navegación enfocada.

**Cuándo falla:** Cuando los usuarios necesitan moverse con fluidez entre secciones. Cuando las tareas abarcan varias secciones. Cuando el «núcleo» se convierte en un cajón de sastre para todo lo que no cabe en una sección radial.

**Presta atención a:** El deseo de añadir enlaces cruzados entre secciones radiales. Cuando estas empiezan a enlazarse ampliamente entre sí, el modelo central y radial se opone al flujo de trabajo real del usuario. Considera cambiar de patrón.

### Plano

Todo el contenido está al mismo nivel, sin jerarquía. Suele combinarse con funciones potentes de búsqueda y filtrado.

**Cuándo funciona:** Conjuntos de contenido homogéneo (una galería de fotos, una lista de transacciones o un feed de publicaciones). Contenido sin categorías naturales. Productos con una infraestructura de búsqueda excelente.

**Cuándo falla:** Con tipos de contenido diversos. Con conjuntos grandes sin búsqueda ni filtrado sólidos. Con usuarios que exploran en lugar de buscar.

**Presta atención a:** La ilusión de una estructura plana. Muchas arquitecturas «planas» son en realidad jerarquías filtradas: el usuario selecciona filtros que crean categorías ad hoc. No hay problema, pero entonces el diseño de filtros es el diseño de navegación.

### Por facetas

Varias dimensiones independientes permiten filtrar el mismo conjunto de contenido. Los usuarios combinan las facetas libremente (color + talla + precio + marca).

**Cuándo funciona:** Comercio electrónico, resultados de búsqueda y bases de datos grandes con múltiples atributos. Cuando distintos usuarios quieren segmentar el mismo contenido de maneras diferentes. Cuando el contenido tiene atributos naturales e independientes.

**Cuándo falla:** Cuando las facetas no son independientes (seleccionar «rojo» y «pequeño» deja cero resultados porque los artículos pequeños no existen en rojo). Cuando hay demasiadas: quince dimensiones de filtrado abruman en vez de ayudar. Cuando el vocabulario no es coherente entre facetas.

**Presta atención a:** Los estados vacíos. La navegación por facetas produce una explosión combinatoria: muchas combinaciones devolverán cero resultados. Diseña una degradación elegante; muestra el número de resultados por faceta antes de seleccionarla y desactiva las que devolverían cero.

### Panel de control

Muestra simultáneamente varios tipos de contenido, normalmente mediante vistas resumidas que enlazan a información detallada.

**Cuándo funciona:** Productos de monitorización y analítica. Vistas ejecutivas. Productos en los que los usuarios deben examinar rápidamente varios flujos de información. Productos de uso recurrente en los que se quiere consultar una instantánea del estado.

**Cuándo falla:** Cuando el panel se convierte en todo el producto: un panel que obliga a recorrer quince widgets se ha convertido accidentalmente en una arquitectura plana. Cuando cada parte interesada exige incluir su métrica y genera sobrecarga informativa. Cuando muestra datos, pero no permite actuar.

**Presta atención a:** El diseño impulsado por el panel, donde cada funcionalidad nueva obtiene un widget en vez de una ubicación adecuada. También a los paneles que muestran los mismos datos a todo el mundo aunque cada rol necesite una vista distinta.

---

## Diseño de taxonomías

La taxonomía es el arte de nombrar y agrupar elementos para que los usuarios puedan encontrarlos. Si la taxonomía es incorrecta, ningún diseño visual salvará la navegación.

### De arriba abajo frente a de abajo arriba

El enfoque **de arriba abajo** comienza con la lógica organizativa: ¿cuáles son las categorías principales?, ¿cómo se subdividen? Funciona cuando los expertos del dominio comprenden bien la estructura y los usuarios comparten esa comprensión. Riesgo: imponer una estructura que tiene sentido internamente, pero no para los usuarios.

El enfoque **de abajo arriba** comienza con los elementos de contenido: ¿qué tenemos?, ¿cómo agrupan los usuarios estos elementos?, ¿qué etiquetas utilizan? La clasificación de tarjetas es el método principal. Este enfoque descubre la taxonomía que los usuarios realmente esperan. Riesgo: producir demasiadas categorías o categorías demasiado específicas para funcionar como navegación.

**Buena práctica:** Empieza de abajo arriba (clasificación de tarjetas para comprender los modelos mentales) y después perfecciona de arriba abajo (con conocimiento del dominio para completar vacíos y resolver casos límite). Ningún enfoque produce por sí solo una buena taxonomía.

### Principio MECE

Mutuamente excluyentes y colectivamente exhaustivas. Cada elemento pertenece exactamente a una categoría y existe una categoría para cada elemento.

**Mutuamente excluyentes:** Si un usuario podría colocar razonablemente un elemento en dos categorías, estas se solapan. Para corregirlo, hazlas más específicas, combina las que se solapan o adopta una navegación por facetas en la que los elementos puedan existir en varias dimensiones.

**Colectivamente exhaustivas:** Si hay elementos que no caben en ninguna categoría, la taxonomía tiene vacíos. Prueba cincuenta elementos de contenido al azar e intenta clasificar cada uno. Si dudas en más del 10 %, la taxonomía necesita trabajo.

**Realidad:** Lograr un MECE estricto suele ser imposible en dominios complejos. Cuando los elementos pertenecen de verdad a varias categorías, considera las referencias cruzadas (el elemento vive en un lugar y recibe enlaces desde otros) o la polijerarquía.

### Polijerarquía

Un elemento puede aparecer en varios puntos de la jerarquía. «Ratón inalámbrico» aparece tanto en «Accesorios para ordenador» como en «Dispositivos inalámbricos».

**Cuándo usarla:** Cuando la clasificación de tarjetas muestra de forma consistente que distintos usuarios colocan elementos en varias categorías. Cuando el coste de no encontrar un elemento es mayor que el coste de duplicarlo.

**Riesgos:** Complejidad de mantenimiento (actualizar en un lugar y olvidar el otro). Confusión si el mismo elemento tiene metadatos o comportamientos distintos según la ubicación. Una navegación que parece poco fiable: «Lo vi en otro sitio, ¿cuál es el auténtico?».

**Mitigación:** Define una ubicación canónica. Marca claramente las demás apariciones como referencias cruzadas. Mantenlas mediante automatización, no por duplicación manual.

---

## Modelos mentales

Un modelo mental es la representación interna que tiene el usuario sobre el funcionamiento de un sistema. No necesita coincidir con el modelo real del sistema, pero la interfaz sí debe corresponderse con el modelo mental del usuario o este fracasará.

### Teoría aplicada de modelos mentales

**The Design of Everyday Things (1988)** distingue tres modelos:

1. **Modelo de diseño** — Cómo cree el diseñador que funciona el sistema.
2. **Modelo del sistema** — Cómo funciona realmente el sistema.
3. **Modelo del usuario** — Cómo cree el usuario que funciona el sistema.

La interfaz conecta el modelo de diseño con el del usuario. Cuando coinciden, el producto parece intuitivo. Cuando no, parece averiado, aunque técnicamente funcione a la perfección.

**Desajustes comunes:**

- Los usuarios creen que «eliminar» borra algo para siempre; el sistema lo mueve a la papelera. (Leve: el sistema perdona más de lo esperado).
- Los usuarios creen que «guardar» conserva su trabajo; el sistema guarda automáticamente y «guardar» no produce ningún efecto visible. (Confuso: la acción no tiene efecto perceptible).
- Los usuarios creen que cada pestaña del navegador es independiente; el sistema comparte el estado de sesión entre pestañas. (Peligroso: los cambios de una afectan silenciosamente a otra).

**Implicación de diseño:** Investiga los modelos mentales antes de diseñar la navegación, la nomenclatura o los patrones de interacción. La clasificación de tarjetas revela modelos mentales categóricos. Las pruebas de usabilidad con pensamiento en voz alta revelan modelos procedimentales. Ambos son necesarios.

---

## Orientación espacial

El libro de Romedi Passini y Paul Arthur, **Wayfinding: People, Signs, and Architecture** (1992), estableció principios de navegación espacial que se trasladan directamente a los entornos digitales.

### Principios fundamentales de orientación

**Orientación:** Los usuarios siempre deben saber dónde están. En el espacio físico: mapas de «Usted está aquí», puntos de referencia visibles y números de planta. En el espacio digital: migas de pan, elementos de navegación resaltados, títulos de página y estructura de URL. Quien no sabe dónde está no puede decidir adónde ir después.

**Decisión de ruta:** En cada punto de decisión, los usuarios necesitan información suficiente para elegir correctamente. En el espacio físico: señales direccionales en las intersecciones. En el digital: etiquetas de navegación, textos de vista previa y descripciones. Si alguien debe hacer clic para saber si un enlace conduce a algo útil, la orientación ha fallado.

**Cierre:** Los usuarios necesitan confirmación de que han llegado. En el espacio físico: números de habitación, rótulos en puertas y mostradores de recepción. En el digital: encabezados que coinciden con el enlace pulsado y contenido que cumple lo prometido por la etiqueta. Hacer clic en «Ajustes de privacidad» y llegar a una página titulada «Gestión de la cuenta» produce un fallo de cierre y desorienta.

**Revelación progresiva del entorno:** No muestres todo el mapa a la vez. Muestra lo relevante en cada punto de decisión. En el espacio físico, los directorios de edificios muestran plantas, no habitaciones individuales. En el digital, la navegación de nivel superior muestra categorías, no subcategorías. Revela la profundidad conforme el usuario avanza.

### Elementos espaciales de Lynch

En **The Image of the City** (1960), Kevin Lynch identificó cinco elementos que las personas utilizan para orientarse en el espacio físico. Los cinco se aplican a productos digitales:

1. **Sendas** — Rutas a través del entorno. En digital: flujos de navegación, migas de pan y procesos secuenciales.
2. **Bordes** — Límites entre regiones. En digital: separadores de sección, límites de grupos de navegación y bordes de barras laterales.
3. **Distritos** — Áreas con un carácter identificable. En digital: secciones de producto diferenciadas con un tratamiento visual coherente (el área de «ajustes» se ve distinta del área de «contenido»).
4. **Nodos** — Puntos estratégicos de concentración. En digital: páginas de destino, paneles y páginas de resultados de búsqueda; lugares por los que los usuarios pasan para llegar a sus destinos.
5. **Hitos** — Puntos de referencia para orientarse. En digital: logotipos, encabezados persistentes y composiciones de página distintivas que los usuarios recuerdan y usan para navegar.

---

## Modelos de comportamiento de búsqueda

No todas las búsquedas son iguales. La investigación de Marcia Bates y el marco de Gary Marchionini identifican comportamientos de búsqueda fundamentalmente distintos que exigen respuestas de diseño diferentes.

### Búsqueda de un elemento conocido

El usuario sabe qué quiere y cómo se llama. Introduce una consulta concreta y espera un resultado específico. Ejemplo: buscar «AirPods Pro» en un sitio de electrónica.

**Diseña para:** Velocidad. Autocompletado. Priorización de coincidencias exactas. Tolerancia a errores tipográficos. La métrica de éxito es: ¿encontré rápidamente el elemento exacto?

### Búsqueda exploratoria

El usuario tiene una necesidad, pero no conoce la solución exacta. Explora, compara y aprende. Ejemplo: buscar «auriculares inalámbricos» para conocer las opciones disponibles.

**Diseña para:** Exploración. Filtrado por facetas. Comparación. Vistas previas ricas de resultados. Elementos relacionados. La métrica de éxito es: ¿aprendí lo suficiente para tomar una decisión?

### Reencuentro

El usuario encontró algo antes y quiere volver a encontrarlo. Ejemplo: «La semana pasada vi unos auriculares que costaban unos 150 dólares; creo que eran Sony…».

**Diseña para:** Historial. Vistos recientemente. Favoritos o marcadores. Búsqueda difusa que admita recuerdos parciales. La métrica de éxito es: ¿encontré aquello que había visto?

### No sé lo que no sé

El usuario no conoce el dominio lo suficiente para formular una consulta útil. Ejemplo: alguien que invierte por primera vez busca en una plataforma financiera sin conocer la terminología.

**Diseña para:** Descubrimiento guiado. Búsquedas populares. Exploración por categorías. Interpretación en lenguaje claro. Sugerencias del tipo «¿Querías decir…?» que enseñen, no solo corrijan.

---

## Metodología de clasificación de tarjetas y prueba de árbol

### Cómo realizar una clasificación de tarjetas

**Preparación:**

1. Selecciona entre 30 y 60 elementos que representen toda la amplitud del contenido. Con muy pocos se omiten distinciones importantes; demasiados fatigan a los participantes.
2. Escribe cada elemento en una tarjeta (física o digital; herramientas como OptimalSort, Maze o UXtweak funcionan bien en remoto).
3. Usa etiquetas de contenido reales, no jerga interna. Si la clasificación revela que los usuarios no entienden una etiqueta, eso es un hallazgo.

**Protocolo de clasificación abierta:**

1. Pide a los participantes que agrupen las tarjetas del modo que les resulte más lógico. No hay una respuesta correcta.
2. Después, pídeles que nombren cada grupo.
3. Pregunta qué tarjetas les resultaron difíciles de colocar.
4. Ten en cuenta que algunos crearán muchos grupos pequeños y otros pocos grupos grandes. Ambos patrones aportan información.

**Protocolo de clasificación cerrada:**

1. Proporciona categorías predefinidas.
2. Pide a los participantes que coloquen cada tarjeta donde esperarían encontrarla.
3. Registra la ubicación y el grado de confianza. Una confianza baja señala problemas de taxonomía.

**Análisis:**

- Genera una matriz de similitud que muestre con qué frecuencia se agruparon juntos los elementos.
- Utiliza dendrogramas o análisis de clústeres para identificar agrupaciones naturales.
- Busca elementos que terminen sistemáticamente solos o que oscilen entre grupos: son los casos problemáticos de la taxonomía.
- Compara los resultados con la arquitectura propuesta. Cuando diverjan, el usuario tiene razón y la arquitectura debe adaptarse.

### Cómo realizar una prueba de árbol

**Preparación:**

1. Crea una representación de la jerarquía de navegación únicamente con texto, sin diseño visual, iconos ni color.
2. Redacta entre 8 y 12 tareas que representen objetivos habituales. Ejemplo: «¿Dónde encontrarías información para cambiar tu contraseña?».
3. Cada tarea debe tener exactamente un destino correcto.

**Protocolo:**

1. Muestra el nivel superior del árbol.
2. Presenta una tarea.
3. El participante entra en categorías y profundiza hasta creer que ha encontrado el lugar correcto.
4. Registra el recorrido, éxito o fracaso, directividad (¿tuvo que retroceder?) y tiempo de finalización.

**Métricas clave:**

- **Tasa de éxito:** ¿Qué porcentaje encontró la respuesta correcta? Menos del 70 % en una tarea indica un problema estructural.
- **Directividad:** ¿Qué porcentaje llegó directamente sin retroceder? Una directividad baja con éxito final alto indica que la etiqueta funcionó, pero la ubicación no era intuitiva: llegaron por eliminación.
- **Primer clic:** ¿Dónde hicieron clic primero? Si la mayoría se equivoca, el problema está en las etiquetas o categorías del nivel superior.

**Interpretación de resultados:**

- Éxito alto + directividad alta = la estructura funciona para esta tarea.
- Éxito alto + directividad baja = se puede encontrar, pero no es intuitiva; los usuarios tuvieron que buscar.
- Éxito bajo + recorridos variados = problema estructural; el elemento no está donde los usuarios esperan.
- Éxito bajo + recorrido erróneo consistente = el elemento está en la categoría equivocada y los usuarios coinciden en dónde debería estar, lo que indica adónde moverlo.
