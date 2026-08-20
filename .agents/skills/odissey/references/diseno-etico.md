# Diseño ético

**Última verificación: 2026-08-20**

> **Alcance legal:** Esta es una guía UX, no asesoramiento legal. Antes de convertir cualquier patrón en requisito, el equipo debe verificar con asesoría jurídica cualificada la legislación vigente, la cobertura del producto y de la entidad, las fechas de entrada en vigor y la jurisdicción aplicable. Las normas y su interpretación pueden cambiar después de la fecha indicada.

## Índice

- [Guía para corregir antipatrones](#guía-para-corregir-antipatrones)
- [Panorama normativo](#panorama-normativo)
- [Marcos de diseño ético](#marcos-de-diseño-ético)
- [Patrones de diseño del consentimiento](#patrones-de-diseño-del-consentimiento)
- [Fuentes oficiales](#fuentes-oficiales)

## Guía para corregir antipatrones

La habilidad principal cataloga antipatrones. Este documento explica cómo corregirlos y cómo diseñar desde el principio una alternativa respetuosa.

### Patrones engañosos → Alternativas honestas

**Cebo y cambio → Entrega coherente.** Lo que muestras debe ser lo que entregas. Si un botón dice «Descargar», descarga; si un enlace dice «Más información», explica. Prueba el patrón con esta pregunta: si una persona describiera lo que acaba de ocurrir, ¿coincidiría con la etiqueta que pulsó?

**Preguntas capciosas → Opciones en lenguaje claro.** Cada opción debe poder expresarse de forma afirmativa: «Sí, envíame correos» / «No, no me envíes correos». Evita dobles negaciones como «Desmarca para no dejar de recibir…» y no agrupes varios consentimientos en una casilla. Lee la pregunta en voz alta: si confunde a una persona del equipo, también confundirá a la audiencia.

**Desvío visual → Peso visual equivalente.** Al presentar alternativas, «rechazar» o «excluirse» debe ser igual de visible: tamaño, peso y prominencia comparables. La preferencia de la persona, no la del negocio, debe determinar la elección. Una prueba rápida consiste en mirar la página de reojo: ¿se distinguen las dos opciones por igual?

**Costes ocultos → Precio completo desde el principio.** Muestra el coste total disponible —impuestos, comisiones y envío— antes de solicitar información personal. Si algún importe todavía depende de datos posteriores, explica esa dependencia y actualiza el total en cuanto pueda calcularse.

**Culpabilizar al rechazar → Rechazo neutral.** El texto para rechazar debe ser factual, no emocional. «No, gracias» es válido; «No, gracias, odio ahorrar» manipula. La prueba es sencilla: ¿dirías ese texto cara a cara sin avergonzarte?

**Introducción furtiva en la cesta → Adiciones explícitas.** Nada debe entrar en una cesta, plan o pedido sin una acción deliberada. Complementos preseleccionados, seguros incluidos y ventas adicionales automáticas incumplen este principio. Si la persona no eligió «Añadir», no debería aparecer.

### Manipulación de valores predeterminados → Valores respetuosos

**Consentimiento premarcado → Sin marcar por defecto.** Cuando se necesita consentimiento, una selección previa impide que la acción sea inequívoca. Cada casilla opcional debe comenzar sin marcar y cada permiso, sin conceder. La primera interacción debe ser una elección, no la corrección de una decisión ajena.

**Carga para excluirse → Esfuerzo simétrico.** La dificultad de salir debe ser comparable a la de entrar. Si el alta requiere un clic, el diseño no debe esconder la baja tras varios pasos. Esta es una norma ética de diseño incluso cuando la obligación jurídica concreta varía por jurisdicción.

**Continuidad forzada → Fin de prueba transparente.** Antes de terminar una prueba, informa por canales adecuados; en el momento de convertirla en pago, muestra con claridad el importe, la periodicidad y el mecanismo de cancelación. Diseña reembolsos y cancelaciones fáciles según las reglas aplicables. Dificultar la salida no crea lealtad: crea resentimiento.

### Urgencia fabricada → Escasez honesta

**Temporizadores falsos → Solo plazos reales.** Si el plazo existe —un evento empieza a las 20:00 o una oferta termina el domingo—, muéstralo. Si no existe, no lo inventes. Un contador que se reinicia al recargar la página no es un plazo, es engaño.

**Escasez inventada → Inventario real.** Si muestras existencias, deben proceder de datos reales y suficientemente actuales. «Solo quedan 2» cuando hay 2,000 unidades induce una conclusión falsa. Si la demanda fluctúa, explica la actualización; si no puedes respaldar la cifra, no la muestres.

**Prueba social falsa → Actividad real.** «15 personas están viendo esto» debe representar actividad verdadera, no un número aleatorio. Las reseñas verificadas y los recuentos reales construyen confianza; la prueba social fabricada la destruye.

### Diseño adictivo → Interacción respetuosa

**Desplazamiento infinito → Límites naturales.** Paginación, «Cargar más» o resúmenes de sesión crean puntos de parada. No eliminan necesariamente la interacción: la convierten en intencional. «Ya estás al día» es una ayuda parcial; un límite real hace más visible la elección de continuar.

**Refuerzo de razón variable → Valor predecible.** Las notificaciones deben llegar porque ocurrió algo significativo, no solo porque un algoritmo calculó el mejor momento para recuperar atención. El contenido debe estar organizado, no dispensarse al azar. El valor debe residir en el contenido, no en la imprevisibilidad de su entrega.

**Manipulación de rachas → Progreso sin castigo.** Si registras rachas, romper una no debería imponer una pérdida desproporcionada. «Tuviste una racha de 30 días; ¿quieres comenzar otra?» informa. «Perdiste para siempre tu racha de 30 días» fabrica aversión a la pérdida.

---

## Panorama normativo

Esta sección registra implicaciones de diseño verificadas en las fuentes oficiales el 2026-08-20. Cada norma se describe por jurisdicción y alcance; no debe extrapolarse a productos o entidades que queden fuera de su cobertura.

### GDPR — Unión Europea / EEE

El Reglamento General de Protección de Datos debe consultarse en su [texto oficial](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Para diseño, resultan especialmente relevantes:

**Consentimiento — artículo 7 y considerandos 32, 42 y 43, cuando el consentimiento sea la base aplicable:**
- Debe ser libre; no se vincula al acceso al servicio si el tratamiento no es necesario para ese servicio.
- Debe ser específico e informado; propósitos distintos requieren una explicación y una elección adecuadas.
- Debe expresarse mediante una acción afirmativa inequívoca; el silencio, la inactividad y las casillas premarcadas no bastan.
- Retirarlo debe ser tan fácil como otorgarlo.

**Minimización de datos — artículo 5(1)(c):** Solicita solo los datos adecuados, pertinentes y limitados a lo necesario para el propósito declarado. No añadas campos «por si acaso».

**Derecho de supresión — artículo 17:** Diseña un mecanismo de solicitud y cumplimiento que refleje condiciones y excepciones del artículo. «Ocultar» un registro no equivale necesariamente a cumplir una supresión.

**Protección de datos desde el diseño y por defecto — artículo 25:** Incorpora las garantías al sistema y configura por defecto solo el tratamiento necesario para cada propósito. El detalle técnico y jurídico depende del contexto y del riesgo.

### Opciones negativas de la FTC — Estados Unidos

La situación normativa debe describirse con cuidado:

- La enmienda **Click-to-Cancel de 2024 fue anulada** judicialmente y no es un mandato federal o nacional activo para todo Estados Unidos. No reutilices sus requisitos —por ejemplo, una regla universal de cancelación idéntica al alta— como si siguieran vigentes por esa enmienda.
- La [Negative Option Rule actual](https://www.ftc.gov/legal-library/browse/rules/negative-option-rule), promulgada en 1973, sigue vigente y tiene un alcance más estrecho, centrado en planes de opción negativa con notificación previa.
- Pueden seguir siendo aplicables otras normas vigentes según el producto y el canal: la Sección 5 de la FTC Act, ROSCA, la Telemarketing Sales Rule y leyes estatales. Debe analizarse la cobertura concreta de cada una.
- La FTC abrió en 2026 un [Advance Notice of Proposed Rulemaking (ANPRM)](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-seeks-public-comment-response-advance-notice-proposed-rulemaking-regarding-negative-option). El ANPRM solicita información, incluso sobre conservar la regla actual, recuperar disposiciones de la norma anulada de 2024 u otras alternativas; no es una regla final ni crea por sí mismo un nuevo mandato.

**Implicación de diseño:** Presenta términos, precio y periodicidad antes de obtener aceptación; registra una decisión afirmativa cuando corresponda; y ofrece una cancelación visible y comprensible. Después, valida con asesoría jurídica los pasos, avisos y tiempos exigibles en cada jurisdicción.

### COPPA — Estados Unidos

La FTC publicó [enmiendas finales a la COPPA Rule en 2025](https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-312-coppa-final-rule-amendments). Las [preguntas frecuentes vigentes de la FTC](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions) indican que la regla cubre, entre otros supuestos, a operadores comerciales de sitios y servicios dirigidos a menores de 13 años que recopilan, usan o divulgan información personal, y a ciertos servicios de audiencia general con conocimiento efectivo de esa recopilación. No todo producto que «podría tener menores» queda cubierto de manera idéntica.

**Implicaciones de diseño cuando exista cobertura:**
- Aviso de privacidad claro y completo, junto con aviso directo a madres, padres o tutores según corresponda.
- Consentimiento parental verificable antes de ciertas recopilaciones, con las excepciones de la regla.
- Controles para revisar, suprimir y detener recopilaciones posteriores.
- Recopilar solo lo razonablemente necesario para participar en una actividad.
- Retener datos solo durante el tiempo necesario y eliminarlos de forma segura.

Confirma el texto de las enmiendas de 2025, las fechas aplicables y la clasificación concreta del servicio antes de definir el flujo.

### CCPA / CPRA y ADMT — California

Consulta el [centro vigente de leyes y reglamentos de la CPPA](https://cppa.ca.gov/regulations/). Los diseños de avisos, enlaces de exclusión y señales de preferencia deben ajustarse a la cobertura del negocio, el tratamiento y las excepciones aplicables. La [advertencia de cumplimiento de la CPPA sobre patrones oscuros de 2024](https://cppa.ca.gov/pdf/enfadvisory202402.pdf) es una referencia oficial para revisar si la interfaz subvierte o perjudica la elección.

La CPPA adoptó en 2025 regulaciones sobre tecnología automatizada de toma de decisiones (ADMT), entre otros temas, y señaló el **1 de enero de 2026** como fecha de entrada en vigor. La [página oficial de las regulaciones ADMT 2025/2026](https://cppa.ca.gov/regulations/ccpa_updates.html) describe derechos de acceso y exclusión frente a determinados usos cubiertos por la norma. Esto no significa que toda decisión automatizada de cualquier producto permita universalmente la exclusión: hay que verificar definiciones, umbrales, contexto de uso, excepciones y obligaciones específicas.

**Implicación de diseño:** Inventaría dónde interviene ADMT, qué datos usa y qué efecto produce; identifica qué usos están cubiertos; y diseña avisos, acceso y exclusión solo después del análisis jurídico y técnico correspondiente.

### Digital Services Act — Unión Europea

El [texto oficial del Digital Services Act](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) asigna obligaciones distintas según el tipo y tamaño del servicio.

**Diseño de interfaces — artículo 25:** Los proveedores de plataformas en línea cubiertos no deben diseñar, organizar u operar interfaces de modo que engañen o manipulen, o que distorsionen o perjudiquen de forma sustancial la capacidad de tomar decisiones libres e informadas. El artículo y sus actos asociados deben revisarse antes de convertir ejemplos —prominencia, solicitudes repetidas o terminación— en controles de cumplimiento.

**Protección de menores — artículo 28:** Las plataformas en línea accesibles a menores deben aplicar medidas adecuadas y proporcionadas para asegurar un alto nivel de privacidad, seguridad y protección. La prohibición de publicidad basada en perfiles se activa bajo las condiciones de conocimiento razonable descritas en el artículo.

**Sistemas de recomendación — artículos 27 y 38:** El artículo 27 exige explicar en términos claros los parámetros principales de los sistemas de recomendación y las opciones para modificarlos o influir en ellos. La obligación de ofrecer al menos una opción no basada en perfilado del artículo 38 se dirige a plataformas y motores de búsqueda en línea de muy gran tamaño, no a todo servicio digital.

---

## Marcos de diseño ético

### Value Sensitive Design (VSD)

Desarrollado por Batya Friedman y otras personas de la University of Washington, Value Sensitive Design es un enfoque teórico para incorporar valores humanos de manera sistemática durante todo el proceso de diseño tecnológico.

**Tres investigaciones:**
1. **Conceptual:** Identificar partes interesadas directas e indirectas, los valores en juego y sus posibles conflictos.
2. **Empírica:** Estudiar cómo las partes interesadas comprenden y experimentan la tecnología y esos valores.
3. **Técnica:** Analizar cómo propiedades técnicas concretas apoyan o dificultan los valores.

**Valores frecuentes en VSD:** Bienestar humano, propiedad, privacidad, ausencia de sesgo, usabilidad universal, confianza, autonomía, consentimiento informado, rendición de cuentas, cortesía, identidad, calma y sostenibilidad ambiental.

**Aplicación:** Ante una decisión, identifica qué valores están en juego, quién recibe el impacto —incluidas las personas que no usan el producto— y cómo la implementación los respalda o socava. VSD no decide por el equipo; amplía lo que debe considerar.

### Design Justice — Costanza-Chock, 2020

Design Justice replantea el proceso de diseño al centrar a las comunidades más afectadas por las decisiones, en lugar de priorizar a las partes con más poder.

**Principios centrales:**
1. Diseñar para sostener, sanar y empoderar comunidades, priorizando el impacto sobre las más marginadas.
2. Centrar las voces de quienes reciben directamente los resultados.
3. Priorizar el impacto comunitario sobre la intención de quien diseña.
4. Entender el cambio como resultado de procesos responsables, accesibles y colaborativos.
5. Concebir a quien diseña como facilitador, no como autoridad única.

**Aplicación:** Si la investigación no incluye a las personas más vulnerables frente al producto, el diseño tenderá a fallarles. Si el equipo no incluye perspectivas diversas, sus supuestos quedarán sin cuestionar. Quién participa condiciona quién se beneficia.

### Consequence Scanning

Consequence Scanning, creado por Doteveryone —hoy Responsible Technology Institute—, es una práctica ligera para identificar consecuencias potenciales de un producto o una funcionalidad.

**Proceso:**
1. **Describir** el producto en términos claros: qué hace, quién lo usa y qué datos toca.
2. **Explorar consecuencias** en tres dimensiones:
   - Intencionadas: lo que se pretende lograr.
   - No intencionadas pero previsibles: lo que podría suceder aunque no se haya planeado.
   - No intencionadas e imprevisibles: lo que nadie anticipó.
3. **Clasificar** cada consecuencia como positiva, negativa o incierta.
4. **Decidir** ante cada consecuencia negativa: mitigar —rediseñar—, aceptar —documentar y vigilar— o detener —no construir—.

**Cuándo usarlo:** Antes de desarrollar funciones, durante críticas de diseño, al entrar en nuevos mercados o grupos, al recopilar datos nuevos y al cambiar algoritmos o sistemas de recomendación.

---

## Patrones de diseño del consentimiento

El consentimiento no es una casilla; es un sistema de decisiones, información, registro y retirada.

### Principios de un consentimiento significativo

**Informado:** La persona entiende qué acepta. Usa lenguaje claro, propósitos concretos y ejemplos; evita abstracciones jurídicas o permisos generales. «Usaremos tu ubicación para mostrar restaurantes cercanos» informa mejor que «Tratamos datos para mejorar nuestros servicios».

**Específico:** Cada decisión corresponde a un propósito concreto. «Al usar este servicio aceptas X, Y, Z y W» no permite elegir. Separa los propósitos cuando así lo requieran el contexto y la base jurídica.

**Libre:** Rechazar no debe imponer perjuicios indebidos. Cuando un tratamiento sea realmente necesario para prestar lo solicitado, explica esa necesidad en vez de presentarla como una opción ficticia.

**Revocable:** Retirar debe resultar tan fácil como otorgar. Si se concede con un interruptor, procura que pueda retirarse en el mismo lugar y con esfuerzo equivalente.

**Oportuno:** Solicita la decisión cuando se vuelve relevante, no en bloque durante el alta. Pide ubicación al activar una función que la necesita y explica para qué.

### Patrones de interfaz de consentimiento

**Divulgación por capas:** Presenta primero un resumen fiel —«Queremos usar tu ubicación para mostrar restaurantes cercanos»— y un acceso al detalle. El resumen debe bastar para una decisión real; el detalle amplía, no corrige lo anterior.

**Controles granulares:** Separa propósitos. Para cookies, ofrece categorías como analítica, marketing o personalización cuando correspondan, además de acciones claras. En paneles de permisos, muestra cada permiso y su explicación.

**Consentimiento justo a tiempo:** Pide el permiso al encontrar la función que lo necesita y aporta contexto: «Para guardar la ruta necesitamos acceso a tu ubicación» comunica más que un aviso aislado durante el alta.

**Comprobantes de consentimiento:** Muestra qué se aceptó, cuándo y cómo cambiarlo. Un panel de privacidad puede listar decisiones activas, fechas de modificación y una forma directa de revocarlas.

**Nueva decisión ante cambios materiales:** Si cambia de manera material el uso de datos, no lo escondas en una actualización de términos. Determina con asesoría jurídica si hace falta una nueva elección y explica qué cambió y por qué.

### Fallos frecuentes del consentimiento

- Muros que bloquean todo el servicio hasta aceptar tratamientos no esenciales.
- Botones «Aceptar todo» dominantes mientras «Gestionar preferencias» aparece pequeño y tenue.
- Un clic para aceptar y muchos para personalizar o retirar.
- Rutas de retirada ocultas tras varias capas de ajustes.
- Casillas premarcadas cuando se requiere una acción afirmativa.
- Consentimiento agrupado que mezcla términos esenciales y marketing opcional.
- Avisos repetidos en cada visita porque la negativa no se conserva.

---

## Fuentes oficiales

Verificadas el 2026-08-20:

- [FTC: ANPRM de 2026 sobre opciones negativas y referencia a la regla de 2024 anulada](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-seeks-public-comment-response-advance-notice-proposed-rulemaking-regarding-negative-option)
- [FTC: página vigente de la Negative Option Rule](https://www.ftc.gov/legal-library/browse/rules/negative-option-rule)
- [FTC: enmiendas finales de COPPA de 2025](https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-312-coppa-final-rule-amendments)
- [FTC: guía vigente de cumplimiento de COPPA](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions)
- [EUR-Lex: texto oficial del GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [EUR-Lex: texto oficial del Digital Services Act](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)
- [CPPA: centro vigente de leyes y reglamentos](https://cppa.ca.gov/regulations/)
- [CPPA: advertencia de 2024 sobre patrones oscuros](https://cppa.ca.gov/pdf/enfadvisory202402.pdf)
- [CPPA: regulaciones ADMT adoptadas en 2025 y vigentes desde 2026](https://cppa.ca.gov/regulations/ccpa_updates.html)
