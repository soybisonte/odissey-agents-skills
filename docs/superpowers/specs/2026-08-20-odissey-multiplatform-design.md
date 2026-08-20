# Odissey multiplataforma: diseño técnico

Fecha: 2026-08-20  
Estado: aprobado para implementación

## Objetivo

Convertir el repositorio en una distribución reproducible de Odissey que funcione de forma nativa en:

1. Codex CLI y ChatGPT desktop app.
2. La extensión oficial de Codex para Visual Studio Code.
3. GitHub Copilot Agent Mode para Visual Studio Code.

El resultado debe conservar las 16 disciplinas y los 6 roles de misión, eliminar formatos obsoletos o ambiguos y evitar mantener manualmente copias equivalentes.

## Decisiones aprobadas

- Usar `.agents/skills/<nombre>/SKILL.md` como fuente canónica de las 16 skills. Codex y Copilot descubren esta ruta a nivel de proyecto.
- Mantener `agents/*.md` como fuente semántica de los 6 roles durante esta migración para no invalidar el formato existente de Claude Code.
- Generar agentes nativos de Codex en `.codex/agents/*.toml`.
- Generar agentes de GitHub Copilot en `.github/agents/*.agent.md`.
- Generar wrappers de los roles como skills instalables en `generated-skills/*-skill/`; el plugin los incluirá porque los plugins no distribuyen agentes personalizados de proyecto.
- Empaquetar Desktop/CLI en `plugins/bbva-odissey/` y registrar el marketplace del repositorio en `.agents/plugins/marketplace.json`.
- Mantener Cursor y Claude Code como salidas de compatibilidad, sin tratarlos como fuente de verdad.
- Usar `$nombre-skill` en instrucciones dirigidas a Codex. Las barras `/...` quedan reservadas para comandos reales de cada cliente y no representan skills.

## Arquitectura de fuentes y salidas

```text
.agents/skills/                 fuente canónica de 16 skills
agents/                         fuente semántica de 6 roles
.codex-plugin/plugin.json       metadatos canónicos del plugin
AGENTS.md                       contrato operativo del repositorio
scripts/                        build, validación y release
tests/                          contratos y pruebas de regresión
        │
        └── build determinista
            ├── .codex/agents/*.toml
            ├── .github/agents/*.agent.md
            ├── .github/copilot-instructions.md
            ├── generated-skills/*-skill/
            ├── plugins/bbva-odissey/
            └── .cursor/rules/*.mdc
```

No se borrará `.github/` para reconstruirla. Cada generador será dueño únicamente de sus archivos de salida declarados.

## Contratos por superficie

### Codex CLI, Desktop y extensión de VS Code

- Las 16 skills serán visibles directamente desde `.agents/skills` sin instalar el plugin.
- La invocación explícita documentada será `$strategy`, `$journey`, etc.
- Los 6 roles se declararán en `.codex/agents` con `name`, `description` y `developer_instructions`.
- Los agentes heredarán modelo, esfuerzo y permisos del padre; no se fijarán modelos o permisos salvo que el rol realmente los necesite.
- El `AGENTS.md` raíz explicará fuentes canónicas, comandos de desarrollo, condiciones de delegación y verificación.
- El plugin será una vía instalable adicional para Desktop/CLI y no un requisito de funcionamiento en la extensión IDE.

### GitHub Copilot en Visual Studio Code

- Las mismas 16 skills se descubrirán desde `.agents/skills`.
- Los 6 perfiles se generarán en `.github/agents/*.agent.md` con frontmatter YAML y herramientas mediante alias portables (`read`, `search`, `edit`, `web`, `agent`).
- `.github/copilot-instructions.md` contendrá únicamente principios globales y navegación; no duplicará el cuerpo completo de `$odissey`.
- No se generará `.github/copilot/skills`, porque no es una ruta de Agent Skills soportada.

### Plugin Codex

- `plugins/bbva-odissey/.codex-plugin/plugin.json` será una copia validada de los metadatos canónicos.
- `plugins/bbva-odissey/skills/` incluirá las 16 skills disciplinares y los 6 wrappers de roles.
- El manifiesto incluirá `interface.capabilities`, rutas relativas válidas y solo campos soportados.
- `.agents/plugins/marketplace.json` apuntará a `./plugins/bbva-odissey` e incluirá política de instalación, autenticación y categoría.
- Cada build deberá producir exactamente el mismo árbol a partir de las mismas fuentes.

## Modernización de skills

Cada skill cumplirá lo siguiente:

- Frontmatter con solo `name` y `description`.
- Nombre de carpeta idéntico a `name`, en minúsculas y kebab-case.
- Descripción orientada a descubrimiento: qué hace y cuándo activarla, preferentemente por debajo de 500 caracteres y siempre por debajo de 1024.
- Cuerpo en español, conciso y con instrucciones accionables.
- Referencias pesadas fuera del cuerpo y enlazadas directamente desde `SKILL.md`.
- Referencias a otras skills mediante su nombre y sintaxis `$skill` cuando la invocación sea explícita.
- Herramientas descritas por capacidad, no mediante nombres MCP inexistentes o específicos de Claude.
- Ninguna afirmación legal o regulatoria presentada como vigente sin fecha, jurisdicción y fuente verificable; los ejemplos históricos se identificarán como tales.
- Corrección de tokens corruptos, anglicismos accidentales y enlaces rotos.

La edición semántica de cada skill se validará de forma individual antes de pasar a la siguiente. Las transformaciones puramente mecánicas podrán ejecutarse en lote cuando estén cubiertas por pruebas.

## Tooling

Se implementará tooling sin dependencias de red para que funcione en macOS, Linux y CI:

- `scripts/validate.py`: valida skills, agentes, enlaces, manifiestos, marketplace, referencias obsoletas y presupuesto de metadatos.
- `scripts/build.py`: genera artefactos de plataforma sin borrar directorios ajenos.
- `scripts/release.py`: actualiza únicamente manifiestos versionados, ejecuta build y validación y deja commit/tag/push como acciones explícitas.
- `build.sh`, `install.sh` y `release.sh`: wrappers compatibles y mensajes correctos por plataforma.

La suite usará `unittest` de Python para evitar depender de PyYAML o paquetes npm. El parser de frontmatter soportará únicamente el subconjunto que este repositorio declara; esto reduce ambigüedad y hace fallar temprano entradas no soportadas.

## Estrategia de pruebas

### Pruebas de contrato

- Una skill válida se descubre desde `.agents/skills` y conserva recursos relativos.
- Frontmatter adicional, descripción extensa, carpeta divergente o enlace roto producen errores accionables.
- Un agente fuente produce TOML Codex válido y Markdown Copilot válido.
- El build no altera `.github/workflows` ni archivos ajenos a sus salidas.
- Dos builds consecutivos no producen diferencias.
- El plugin y su marketplace pasan sus esquemas y todos sus paths existen.
- Las salidas no contienen rutas `.github/copilot/skills`, invocaciones de skills con `/` ni nombres MCP de Claude conocidos.

### Evals de comportamiento

Se crearán escenarios representativos para:

- Descubrimiento y enrutamiento desde `$odissey`.
- Selección entre `strategy`, `research`, `journey`, `evaluar`, `robustecer`, `incluir` y `spec`.
- Uso de Houston como entrada, Galileo para divergencia y Atlas para handoff.
- Conservación de autonomía del usuario y rechazo de patrones manipuladores.
- Comportamiento sin Figma, navegador o MCP disponibles.

Las pruebas automáticas verifican estructura; los evals con agentes verifican que las instrucciones cambian el comportamiento observable.

## Migración por fases

1. Crear pruebas RED y tooling mínimo.
2. Mover `skills/` a `.agents/skills/` y corregir frontmatter, invocaciones y enlaces.
3. Generar los seis formatos Codex/Copilot y los wrappers instalables.
4. Rehacer el paquete Codex y el marketplace.
5. Reemplazar build, instalación y release destructivos o específicos de macOS.
6. Modernizar el contenido de las 16 skills una a una con validación.
7. Añadir CI, evals, documentación y verificación de reproducibilidad.

Durante la migración se preservarán los artefactos actualmente no rastreados (`.codex-plugin/`, `generated-skills/` y `plugins/`) y se integrarán de forma explícita; no se eliminarán ni sobrescribirán sin comprobar su equivalencia.

## Manejo de errores

- Todos los scripts usarán códigos de salida distintos de cero y mensajes con archivo, regla y remediación.
- El build validará entradas antes de escribir salidas.
- Las escrituras serán temporales y se reemplazarán por artefacto o subárbol controlado, nunca por la raíz `.github` o por el repositorio completo.
- Si una salida existente contiene archivos desconocidos, el build los conservará y reportará el conflicto cuando impida una generación segura.
- La instalación detectará la herramienta disponible y mostrará comandos distintos para Codex, Copilot/VS Code y Claude; no presentará comandos de Claude como si fueran de Codex.

## CI y release

La CI ejecutará:

1. Pruebas unitarias.
2. Validación completa.
3. Build en un checkout temporal.
4. Segunda ejecución para comprobar idempotencia.
5. `git diff --exit-code` para detectar artefactos generados desactualizados.

El release no hará push por defecto. La actualización de versión, el commit, el tag y el push serán pasos separados y reversibles. La versión vivirá en manifiestos de distribución, no en el frontmatter de cada skill.

## Criterios de aceptación

- Las 16 skills son descubribles por Codex y Copilot desde `.agents/skills`.
- Existen 6 agentes válidos para Codex y 6 para Copilot, generados de las mismas fuentes semánticas.
- El plugin Codex contiene 22 workflows instalables y valida correctamente.
- `AGENTS.md`, README e instalación distinguen claramente las tres superficies objetivo.
- No quedan invocaciones de skills con `/`, rutas Copilot obsoletas, enlaces internos rotos ni nombres MCP de Claude en las fuentes canónicas.
- El build es no destructivo, portable e idempotente.
- Las pruebas, validadores, evals estructurales y CI pasan sin dependencias descargadas.

## Fuera de alcance

- Crear un MCP propio o conectar servicios externos.
- Fijar un modelo concreto para todos los usuarios.
- Publicar el plugin en un marketplace remoto o hacer push al repositorio.
- Cambiar la identidad conceptual de Odissey, el número de disciplinas o los seis roles.
- Eliminar compatibilidad con Claude Code o Cursor durante esta migración.

## Riesgos y mitigaciones

- **Colisión con skills personales del mismo nombre:** conservar nombres por compatibilidad y documentar la precedencia de la copia de proyecto.
- **Deriva entre plataformas:** generar y verificar las salidas en CI.
- **Descripciones demasiado generales:** medir presupuesto y probar escenarios de enrutamiento.
- **Agentes con permisos excesivos:** heredar permisos y omitir restricciones de herramientas salvo necesidad demostrada.
- **Pérdida de archivos existentes:** limitar la propiedad del generador y cubrir preservación con pruebas.
- **Cambios regulatorios:** convertir reglas legales en referencias fechadas y verificables, no en verdades permanentes del prompt.
