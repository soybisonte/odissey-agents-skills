# Patrones de interacción

## Índice

- [Principios de diseño de formularios](#principios-de-diseño-de-formularios)
- [Máquinas de estados para interfaces](#máquinas-de-estados-para-interfaces)
- [Patrones de validación](#patrones-de-validación)
- [Bucles de retroalimentación](#bucles-de-retroalimentación)
- [Divulgación progresiva](#divulgación-progresiva)
- [Patrones de deshacer y rehacer](#patrones-de-deshacer-y-rehacer)
- [Salvaguardas para acciones destructivas](#salvaguardas-para-acciones-destructivas)

## Principios de diseño de formularios

Los formularios son el lugar donde las personas intercambian valor con un producto. Cada campo innecesario, etiqueta ambigua o error poco útil añade fricción entre la persona y su objetivo. La investigación sobre formularios es extensa y notablemente consistente.

### Una cosa por página

El patrón de Government Digital Service (GDS), utilizado en millones de trámites, propone que cada pantalla solicite una pregunta o unidad conceptual. No significa necesariamente un único campo.

**Por qué funciona:** Reduce la carga cognitiva, da un propósito claro a cada página y simplifica la recuperación de errores: el problema está aquí y trata de esta cuestión. El avance se percibe, el rendimiento móvil puede mejorar y la analítica localiza con precisión el abandono.

**Cuándo flexibilizarlo:** Campos estrechamente relacionados que se entienden como un concepto —nombre y apellidos; ciudad, estado y código postal—; edición que necesita contexto simultáneo; o herramientas expertas donde prima la velocidad.

**Cuándo no flexibilizarlo sin evidencia:** Pago, registro y otros flujos con riesgo de abandono, especialmente en móvil. Prueba el diseño con la audiencia real antes de condensar.

### Momento de la validación en línea

Cuándo validar importa tanto como cómo hacerlo. Un momento incorrecto convierte la ayuda en acoso.

**Valida al salir del campo, no con cada tecla.** Mostrar un error mientras todavía se escribe puede resultar hostil: la entrada aún no está terminada. La investigación de Luke Wroblewski —2009— mostró mejoras con validación en línea cuando la respuesta llegaba en el momento adecuado. Para la mayoría de campos, valida en `blur`.

**Excepción: fortaleza de contraseña.** La retroalimentación en tiempo real ayuda a construir una entrada que cumpla criterios visibles.

**Excepción: recuento de caracteres.** Si existe límite, muestra el espacio restante mientras se escribe. No esperes a que se redacte un párrafo para revelar que el máximo era 140.

**Después del primer error, valida al cambiar.** Una vez visible el error, vuelve a validar con cada cambio para retirarlo en cuanto la entrada sea válida. No obligues a enviar otra vez para descubrir que ya se corrigió.

### Agrupación de campos

Los campos relacionados deben agruparse visual y semánticamente. Un formulario sin grupos parece más largo de lo que es.

**Usa `fieldset` para grupos conceptuales:** Información personal, datos de pago y dirección de envío son grupos. `<fieldset>` y `<legend>` aportan agrupación visual y estructura accesible.

**Limita los campos visibles.** Si hay 20 pero solo seis corresponden según respuestas previas, muestra seis. La visibilidad condicional reduce complejidad percibida sin eliminar opciones: el formulario se adapta al contexto.

**Diseño en una columna.** Los estudios de seguimiento ocular de Matteo Penzo —2006— y de Baymard Institute suelen favorecer formularios de una columna. Las personas recorren verticalmente; varias columnas pueden volver ambiguo el orden y aumentar el tiempo. Valida la excepción en interfaces densas o expertas.

### Valores predeterminados inteligentes

Los valores iniciales deben servir a la intención más probable de la persona, no al resultado preferido del negocio.

**Buenos valores:** País sugerido por geolocalización de IP con posibilidad de corregirlo; fecha de hoy; cantidad 1; opción para copiar la dirección de facturación a envío.

**Malos valores:** Plan prémium preseleccionado, consentimiento de marketing marcado, opción más cara por defecto o privacidad en «compartir con todo el mundo».

**Prueba:** Si la gran mayoría elegiría el valor y cambiarlo es sencillo, puede ser útil. Si beneficia sobre todo al negocio o oculta una decisión, es manipulación.

---

## Máquinas de estados para interfaces

Todo componente interactivo existe en varios estados. Enumerarlos antes de construir previene una clase frecuente de errores: los estados que nadie diseñó.

### Estados universales de un componente

**Predeterminado / reposo:** Antes de interactuar. Debe comunicar qué es y qué se puede hacer.

**Hover:** El puntero está encima. Debe señalar que es interactivo y anticipar una acción. No existe de la misma forma en táctil; nunca escondas información esencial solo en `hover`.

**Foco:** El componente tiene foco de teclado. Debe distinguirse de `hover` y del estado base. Es un requisito de accesibilidad para saber dónde se está.

**Activo / pulsado:** La activación está en curso —`mousedown` o inicio táctil—. Necesita respuesta inmediata que confirme el registro de la acción.

**Deshabilitado:** Existe, pero no puede activarse. Debe comunicar la indisponibilidad y, cuando sea útil, su causa. Un control deshabilitado sin explicación genera frustración.

**Carga:** Está procesando. Debe confirmar que recibió la acción, que continúa trabajando y cuánto podría tardar si se conoce.

**Éxito:** La acción terminó. Debe comunicar que funcionó y cuál fue el resultado.

**Error:** Falló. Debe explicar qué ocurrió, por qué si se conoce y cómo continuar.

**Vacío:** No hay contenido. Debe explicar qué aparecerá y cómo crear el primer elemento. Es uno de los estados más olvidados.

### Estados de los campos de formulario

Los campos añaden estados propios:

**Placeholder:** Sugerencia visible mientras está vacío. Úsala para ejemplos de formato —«DD/MM/AAAA»—, no como etiqueta. Desaparece al escribir; si la información debe consultarse durante la entrada, colócala en una etiqueta o ayuda persistente.

**Relleno:** Contiene información introducida. Debe distinguirse del placeholder para no confundir datos y sugerencias.

**Solo lectura:** Muestra un valor no editable. No equivale a deshabilitado: el primero informa; el segundo representa indisponibilidad temporal.

**Válido:** Supera la validación. Mostrar confirmación positiva es opcional; una marca verde tras cada campo puede resultar condescendiente. Resérvala para casos donde el éxito no es evidente —fortaleza de contraseña o disponibilidad de nombre—.

**Inválido:** No supera la validación. Debe indicar qué falla y cómo corregirlo. «Entrada no válida» no ayuda; «El correo debe incluir @» sí.

### Estados de los botones

**Acción principal:** La tarea central de la pantalla. Visualmente prominente. Procura una por pantalla, o una por sección en formularios largos.

**Acción secundaria:** Alternativas como Cancelar, Guardar borrador o Restablecer. Subordinadas visualmente y sin confundirse con la principal.

**Acción destructiva:** No puede deshacerse —Eliminar, Revocar—. Debe distinguirse, pero el color rojo no basta. Requiere confirmación proporcional a la consecuencia.

---

## Patrones de validación

### Cuándo validar

| Momento | Cuándo usarlo | Ejemplo |
|---------|---------------|---------|
| **Al salir (`blur`)** | En la mayoría de campos, tras completar la entrada. | Formato de correo, campos obligatorios |
| **Al cambiar, después del error** | Una vez visible, para retirarlo inmediatamente al corregir. | Requisitos de contraseña |
| **Al enviar** | Validación compleja que relaciona varios campos. | «La fecha final debe ser posterior a la inicial» |
| **En tiempo real** | Cuando se construye hacia un objetivo visible. | Fortaleza de contraseña, recuento de caracteres |
| **En servidor / asíncrona** | Cuando hace falta una llamada de red. | Disponibilidad de nombre, validación de dirección |

### Diseño de mensajes de error

**Estructura:** Qué ocurrió + cómo resolverlo. Incluye siempre ambas partes.

- Mal: «Entrada no válida».
- Mal: «Error en el campo 3».
- Bien: «El correo debe incluir @; por ejemplo, nombre@empresa.com».
- Bien: «Este nombre ya está ocupado. Añade números o prueba maria_diseno o maria.d».

**Posición:** Junto al campo, no solo en la parte superior. Si hace falta desplazarse para encontrar el origen, el mensaje no cumple su función. En formularios largos, un resumen superior puede complementar los mensajes locales.

**Momento:** Aparece al detectar el error y desaparece al corregirlo. No esperes al siguiente envío para retirar errores resueltos.

**Tono:** Neutral y útil. Evita culpar. «Introdujiste un correo incorrecto» señala a la persona; «Introduce un correo con el formato nombre@ejemplo.com» centra la solución.

**Accesibilidad:** Asocia programáticamente el mensaje con su campo mediante `aria-describedby` o la técnica semántica apropiada. Los lectores deben anunciar los errores al aparecer; utiliza regiones `aria-live` o `role="alert"` para resúmenes según la urgencia, sin interrumpir en exceso.

---

## Bucles de retroalimentación

Las personas necesitan saber que el sistema recibió su acción y responde. El silencio destruye confianza.

### Interfaz optimista

Actualiza de inmediato como si la acción hubiera funcionado y después reconcilia con el servidor. Si el servidor la rechaza, revierte de manera comprensible.

**Cuándo usarla:** Acciones de bajo riesgo y alta probabilidad de éxito: marcar favorito, enviar un chat o reordenar. El retraso de 200 ms para confirmar puede sentirse innecesario.

**Cuándo no usarla:** Transacciones financieras, acciones que afectan a otras personas o situaciones en las que la reversión resulte dañina. Si «en realidad no funcionó» tendría consecuencias, espera confirmación.

**Diseño de reversión:** Explica la corrección: «No se pudo enviar el mensaje; pulsa para reintentar». Eliminar en silencio algo que parecía enviado no es aceptable.

### Pantallas esqueleto

Muestran la estructura antes de que llegue el contenido mediante formas provisionales en su posición futura.

**Por qué funcionan:** Investigaciones y práctica de Luke Wroblewski y Google indican que pueden reducir el tiempo de espera percibido frente a indicadores aislados. La página parece llenarse en lugar de saltar de vacía a completa.

**Cuándo usarlas:** Páginas de contenido, feeds y paneles con estructura predecible y datos dinámicos. No siempre resultan apropiadas en formularios o transacciones donde la propia estructura depende de la respuesta.

**Detalle de implementación:** Las formas deben corresponder a la disposición final. Un esqueleto sin relación con el contenido produce una transición más brusca que no mostrarlo.

### Indicadores de progreso

**Determinado:** Si se conoce la duración o avance, usa una barra con porcentaje o unidades. Muestra cuánto se completó y, si puede estimarse con fiabilidad, cuánto queda.

**Indeterminado:** Si se desconoce, usa un spinner o pulso. No inventes un porcentaje. Aporta contexto: «Subiendo tu archivo…» comunica más que una animación sola.

**De varios pasos:** Muestra las etapas y destaca la actual. Hay que entender cuántas faltan, cuál está activa, si se puede volver y si es posible guardar para continuar.

---

## Divulgación progresiva

Muestra lo necesario ahora, revela lo siguiente cuando corresponde y oculta lo poco frecuente sin volverlo imposible de encontrar.

### Patrones

**Flujos por etapas:** Divide tareas complejas en pasos. Cada uno se centra en una decisión o tipo de información, mientras un indicador mantiene visible el proceso general.

**Secciones expandibles:** Coloca información avanzada u opcional tras controles de expandir/contraer. La etiqueta debe anticipar el contenido. «Opciones avanzadas» comunica más que «Más».

**Ayuda contextual:** Tooltips, iconos de información y ayuda en línea explican bajo demanda. Sirven para conceptos técnicos o campos poco habituales; no sustituyen etiquetas claras.

**Descubrimiento gradual de funciones:** En herramientas complejas, muestra lo esencial y presenta funciones avanzadas conforme aumenta el dominio. No equivale a esconderlas: la ruta de descubrimiento debe ser visible.

### Antipatrones de divulgación progresiva

**Navegación de contenido misterioso:** Iconos o etiquetas tan abstractos que no permiten predecir el destino. La divulgación necesita señales claras sobre lo oculto.

**Información obligatoria escondida:** Si hace falta para completar la tarea, no debe estar tras «Mostrar más». Reserva la divulgación para información opcional o contextual.

**Profundidad inconsistente:** Una sección revela un elemento y otra quince. Las personas construyen expectativas sobre estos controles; la consistencia reduce sorpresa y exploración innecesaria.

---

## Patrones de deshacer y rehacer

Deshacer no es solo una función: es una red de seguridad que reduce el estrés del resto de interacciones.

### Estrategias de implementación

**Deshacer inmediato —toast o snackbar—:** Para acciones rápidas y de bajo riesgo. «Mensaje archivado — Deshacer». La ventana suele durar 5–10 segundos; después, la acción se consolida. Undo Send de Gmail es un ejemplo conocido.

**Historial de acciones:** Para edición y herramientas creativas. Conserva una pila para deshacer con `Ctrl+Z` o recorrer el historial. Nombra los estados de forma descriptiva: «Cambió la fuente a Helvetica», no «Acción 47».

**Historial de versiones:** Para documentos duraderos y colaboración. Guarda instantáneas con fecha y autoría; permite comparar y restaurar. El historial de Google Docs funciona bien porque identifica las versiones por momento y persona, no por números arbitrarios.

**Papelera / archivo:** Para eliminación. Mueve a un lugar recuperable antes de borrar de forma permanente. Comunica el plazo: «La papelera se vacía después de 30 días».

### Principios para deshacer

- Hazlo descubrible. Si nadie sabe que existe, no protege.
- Explica la ventana. Si caduca, indica cuándo.
- Define el alcance. ¿Revierte la última acción, varias o todo desde el último guardado?
- En colaboración, debería afectar solo a las acciones propias, no a las de otras personas, salvo que el modelo explique claramente otra cosa.

---

## Salvaguardas para acciones destructivas

Las acciones irreversibles necesitan fricción proporcional a sus consecuencias.

### Jerarquía de fricción

**Nivel 1 — Distinción visual:** Diferencia el control destructivo de las acciones seguras. El rojo es convencional, pero no suficiente ni universal. Es el mínimo para consecuencias pequeñas.

**Nivel 2 — Diálogo de confirmación:** «¿Quieres eliminar este proyecto? Se perderán sus 47 archivos y no podrás recuperarlos». Incluye la consecuencia; «¿Seguro?» no informa.

**Nivel 3 — Acción deliberada:** Pide escribir una frase: «Escribe ELIMINAR para borrar definitivamente este repositorio». GitHub utiliza este patrón al eliminar repositorios. Resérvalo para consecuencias graves.

**Nivel 4 — Periodo de espera:** En acciones de máxima consecuencia —como eliminar una cuenta— puede ofrecerse una ventana de cancelación: «Se eliminará en 14 días; puedes cancelar antes». Confirma con las personas responsables de privacidad y cumplimiento si el plazo es compatible con las obligaciones aplicables; no asumas que una norma lo permite en todos los casos.

### Principios de las salvaguardas

- Nombra la consecuencia. «Eliminar el proyecto y sus 47 archivos» es más claro que «Eliminar proyecto».
- Muestra lo que se perderá. Una vista previa vuelve concreta la decisión.
- Ofrece alternativas. «También puedes archivar el proyecto, lo que lo oculta sin borrarlo».
- No confirmes acciones reversibles. Preguntar «¿Seguro?» siempre enseña a avanzar sin leer. Reserva la confirmación para lo realmente destructivo; en lo demás, ofrece deshacer.
