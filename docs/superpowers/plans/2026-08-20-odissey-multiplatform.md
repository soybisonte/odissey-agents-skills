# Odissey multiplataforma — Plan de implementación

> **Required skill:** Use `superpowers:executing-plans` to implement this plan task by task. Use `superpowers:test-driven-development` for tooling and behavior changes, and `superpowers:writing-skills` for every skill edit.

**Goal:** Hacer que las 16 skills y los 6 agentes de Odissey funcionen nativamente en Codex CLI/Desktop, la extensión oficial de Codex para VS Code y GitHub Copilot Agent Mode, con una sola fuente de verdad y salidas reproducibles.

**Architecture:** `.agents/skills` será la fuente canónica de skills y `agents/*.md` seguirá siendo la fuente semántica de roles. Un generador Python sin dependencias externas producirá agentes Codex y Copilot, wrappers de roles, plugin Codex y compatibilidad Cursor. Un validador común aplicará contratos antes y después del build.

**Tech stack:** Python 3 estándar (`unittest`, `json`, `tomllib`, `pathlib`, `tempfile`), Bash POSIX para wrappers, Markdown/YAML restringido, TOML y GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-20-odissey-multiplatform-design.md`

**Global constraints:** Preservar `.codex-plugin/`, `generated-skills/` y `plugins/` existentes hasta validar equivalencia. No borrar `.github/`. No descargar dependencias. No fijar modelos o permisos de agentes. No hacer push ni publicar plugins.

---

## Task 1: Congelar la línea base y crear el núcleo de parsing

**Files:**

- Create: `tests/__init__.py`
- Create: `tests/test_tooling.py`
- Create: `scripts/__init__.py`
- Create: `scripts/odissey_tooling.py`

### Step 1: Escribir pruebas RED del frontmatter

Añadir pruebas con directorios temporales que demuestren:

- Se extraen `name`, `description` y cuerpo de un `SKILL.md` válido.
- Se rechaza frontmatter sin delimitador final.
- Se rechazan campos distintos de `name` y `description`.
- Se soporta una descripción escalar o plegada `>`.
- Se resuelven enlaces Markdown relativos y se reportan enlaces rotos.

### Step 2: Verificar RED

Run: `python3 -m unittest tests.test_tooling.FrontmatterTests -v`

Expected: `ImportError` o fallos porque `scripts.odissey_tooling` aún no existe.

### Step 3: Implementar el parser mínimo

Crear funciones puras para:

- `parse_frontmatter(path)`
- `render_frontmatter(metadata, body)`
- `relative_markdown_links(path, body)`
- `validate_relative_links(path, body)`

El parser aceptará únicamente el subconjunto YAML usado por el repositorio y producirá errores con ruta y línea.

### Step 4: Verificar GREEN

Run: `python3 -m unittest tests.test_tooling.FrontmatterTests -v`

Expected: todas las pruebas pasan.

### Step 5: Refactorizar sin ampliar alcance

Extraer `ValidationIssue` como dataclass y mantener las pruebas verdes.

## Task 2: Construir el validador del catálogo

**Files:**

- Modify: `tests/test_tooling.py`
- Modify: `scripts/odissey_tooling.py`
- Create: `scripts/validate.py`

### Step 1: Escribir pruebas RED de contratos

Cubrir de forma observable:

- Carpeta y `name` coinciden.
- Los nombres usan minúsculas, dígitos y guiones.
- La descripción no está vacía ni supera 1024 caracteres; advertir por encima de 500.
- Solo existen `name` y `description` en frontmatter.
- Los links relativos existen.
- Las fuentes canónicas no contienen `.github/copilot/skills`, nombres MCP `mcp__claude`/`mcp__figma`/`mcp__pencil` ni invocaciones `/strategy`, `/research`, `/blueprint`, `/journey`, `/organizar`, `/articular`, `/evaluar`, `/robustecer`, `/incluir`, `/trasponer`, `/localizar`, `/medir`, `/idear`, `/spec`, `/storytelling` u `/odissey`.
- El presupuesto agregado de descripciones se informa.

### Step 2: Verificar RED

Run: `python3 -m unittest tests.test_tooling.CatalogValidationTests -v`

Expected: fallos por funciones ausentes.

### Step 3: Implementar validación mínima y CLI

Implementar `validate_skill`, `validate_catalog` y salida humana/JSON en `scripts/validate.py`. La CLI aceptará `--root`, `--format text|json` y `--warnings-as-errors`.

### Step 4: Verificar GREEN

Run: `python3 -m unittest tests.test_tooling.CatalogValidationTests -v`

Expected: todas las pruebas pasan.

## Task 3: Crear un build seguro e idempotente

**Files:**

- Modify: `tests/test_tooling.py`
- Modify: `scripts/odissey_tooling.py`
- Create: `scripts/build.py`
- Modify: `build.sh`

### Step 1: Escribir pruebas RED del generador

En un repositorio temporal mínimo, comprobar que:

- Se conserva `.github/workflows/ci.yml` y `.github/keep.md`.
- Se crean `.codex/agents`, `.github/agents`, `generated-skills`, `plugins/bbva-odissey/skills` y `.cursor/rules`.
- Dos ejecuciones producen bytes idénticos.
- Un fallo de validación no modifica salidas existentes.
- El generador solo elimina archivos que incluyan su cabecera de propiedad o estén dentro de un subárbol completamente gestionado.

### Step 2: Verificar RED

Run: `python3 -m unittest tests.test_tooling.BuildTests -v`

Expected: fallos por generador ausente.

### Step 3: Implementar el generador mínimo

Implementar escrituras atómicas, orden estable, normalización de saltos de línea y propietarios de salida. Reemplazar `build.sh` por un wrapper que ejecute `python3 scripts/build.py`.

### Step 4: Verificar GREEN

Run: `python3 -m unittest tests.test_tooling.BuildTests -v`

Expected: todas las pruebas pasan.

## Task 4: Migrar las 16 skills a la fuente canónica

**Files:**

- Move: `skills/` → `.agents/skills/`
- Modify: `.agents/skills/*/SKILL.md`
- Modify: `.agents/skills/odissey/references/*.md`

### Step 1: Mover el árbol sin cambiar contenido

Run: `mkdir -p .agents && mv skills .agents/skills`

Comprobar que siguen existiendo exactamente 16 `SKILL.md` y 8 referencias.

### Step 2: Aplicar la migración mecánica cubierta

En cada skill:

- Eliminar `version` y `user-invocable`.
- Convertir invocaciones de skills `/nombre` a `$nombre`.
- Reemplazar rutas internas antiguas por `.agents/skills` o referencias relativas.
- Conservar contenido y headings.

Run: `python3 scripts/validate.py --root .`

Expected: ya no hay errores mecánicos; pueden quedar advertencias de longitud y contenido.

### Step 3: Acortar descripciones individualmente

Editar y validar, en este orden:

1. `odissey`
2. `strategy`
3. `research`
4. `blueprint`
5. `journey`
6. `organizar`
7. `articular`
8. `evaluar`
9. `robustecer`
10. `incluir`
11. `trasponer`
12. `localizar`
13. `medir`
14. `idear`
15. `storytelling`
16. `spec`

Para cada una: escribir primero un escenario de activación y uno de no activación en `tests/evals/skill-routing.json`, comprobar la línea base, editar solo esa skill, validar y registrar el resultado esperado.

### Step 4: Corregir referencias

Corregir tokens corruptos, traducir los segmentos ingleses que impidan uso consistente en español, añadir índice a referencias de más de 100 líneas y convertir afirmaciones regulatorias volátiles en referencias fechadas con jurisdicción.

Run: `python3 scripts/validate.py --root . --warnings-as-errors`

Expected: 16 skills válidas, 0 errores y 0 advertencias.

## Task 5: Generar agentes Codex, Copilot y wrappers instalables

**Files:**

- Modify: `tests/test_tooling.py`
- Modify: `scripts/odissey_tooling.py`
- Modify: `scripts/build.py`
- Modify: `agents/*.md`
- Generate: `.codex/agents/*.toml`
- Generate: `.github/agents/*.agent.md`
- Generate: `generated-skills/*-skill/`

### Step 1: Escribir pruebas RED de transformación

Para los seis roles, comprobar:

- TOML válido con `name`, `description` y `developer_instructions`.
- Ningún TOML fija modelo, esfuerzo o sandbox.
- Perfil Copilot válido con `name`, `description`, `tools` y cuerpo inferior a 30.000 caracteres.
- Herramientas Copilot usan alias portables.
- Wrapper skill tiene frontmatter válido, nombre `<rol>-skill` y una invocación predeterminada que menciona `$<rol>-skill`.

### Step 2: Verificar RED

Run: `python3 -m unittest tests.test_tooling.AgentGenerationTests -v`

Expected: fallos por transformadores ausentes.

### Step 3: Normalizar fuentes y generar

Mantener en `agents/*.md` solo metadata semántica compatible y contenido del rol. El generador mapeará herramientas por capacidad y enlazará las skills especializadas con sintaxis `$skill`.

### Step 4: Verificar GREEN

Run: `python3 -m unittest tests.test_tooling.AgentGenerationTests -v && python3 scripts/build.py`

Expected: 6 TOML, 6 perfiles Copilot y 6 wrappers.

## Task 6: Rehacer el plugin y marketplace Codex

**Files:**

- Modify: `.codex-plugin/plugin.json`
- Create: `.agents/plugins/marketplace.json`
- Generate: `plugins/bbva-odissey/.codex-plugin/plugin.json`
- Generate: `plugins/bbva-odissey/skills/**`
- Modify: `tests/test_tooling.py`

### Step 1: Escribir pruebas RED del paquete

Comprobar:

- Manifiesto con semver, autor y campos `interface` requeridos, incluido `capabilities`.
- Todos los paths declarados existen dentro del plugin.
- Marketplace con `policy.installation`, `policy.authentication` y `category`.
- Source relativo `./plugins/bbva-odissey`.
- Plugin contiene exactamente 22 skills válidas.

### Step 2: Verificar RED

Run: `python3 -m unittest tests.test_tooling.PluginTests -v`

Expected: fallos del manifiesto y marketplace actuales.

### Step 3: Implementar paquete mínimo

Actualizar el manifiesto canónico, generar el paquete y crear el marketplace del repositorio. No instalar ni actualizar el marketplace personal del usuario.

### Step 4: Verificar GREEN

Run: `python3 -m unittest tests.test_tooling.PluginTests -v && python3 scripts/validate.py --root .`

Expected: 22 skills y manifiestos válidos.

## Task 7: Crear instrucciones y experiencia de instalación correctas

**Files:**

- Create: `AGENTS.md`
- Modify: `.github/copilot-instructions.md`
- Modify: `.github/AGENTS.md`
- Modify: `README.md`
- Modify: `HOW-TO-USE.md`
- Modify: `install.sh`

### Step 1: Escribir pruebas RED de documentación operativa

Comprobar que README e instalador:

- Distinguen Codex Desktop/CLI, extensión Codex VS Code y Copilot VS Code.
- No presentan `claude plugin add` como comando Codex.
- Explican que la extensión Codex usa `.agents/skills` y no plugins.
- Documentan `$skill` y selección/delegación de agentes.
- Enlazan solo archivos existentes.

### Step 2: Verificar RED

Run: `python3 -m unittest tests.test_tooling.DocumentationTests -v`

Expected: fallos sobre rutas y comandos actuales.

### Step 3: Reescribir la documentación

Crear un `AGENTS.md` raíz corto con comandos y fuente de verdad. Reducir `copilot-instructions.md` a principios globales. Actualizar README/HOW-TO-USE e instalador con instrucciones separadas por superficie.

### Step 4: Verificar GREEN

Run: `python3 -m unittest tests.test_tooling.DocumentationTests -v`

Expected: todas las pruebas pasan.

## Task 8: Modernizar release y CI

**Files:**

- Create: `scripts/release.py`
- Modify: `release.sh`
- Create: `.github/workflows/validate.yml`
- Modify: `tests/test_tooling.py`

### Step 1: Escribir pruebas RED de release

Comprobar que:

- Una versión no semver se rechaza sin escribir.
- Se actualizan los dos manifiestos y marketplace, no SKILL.md.
- No se ejecutan commit, tag o push.
- El comando `--check` informa drift sin escribir.

### Step 2: Verificar RED

Run: `python3 -m unittest tests.test_tooling.ReleaseTests -v`

Expected: fallos porque el release portable no existe.

### Step 3: Implementar release portable y CI

Crear `scripts/release.py`, usar `release.sh` solo como wrapper y configurar CI con pruebas, validate, build doble y diff de artefactos.

### Step 4: Verificar GREEN

Run: `python3 -m unittest tests.test_tooling.ReleaseTests -v`

Expected: todas las pruebas pasan.

## Task 9: Forward-tests de skills y agentes

**Files:**

- Create: `tests/evals/skill-routing.json`
- Create: `tests/evals/agent-scenarios.json`
- Create: `tests/evals/README.md`
- Modify: skills individuales solo si el escenario descubre una brecha.

### Step 1: Ejecutar controles sin la skill o agente objetivo

Usar contextos frescos y prompts realistas para observar enrutamiento, omisiones y racionalizaciones. Guardar únicamente prompt, criterio y resultado resumido; no guardar razonamiento privado.

### Step 2: Ejecutar el mismo escenario con el artefacto objetivo

Validar al menos:

- `$odissey` enruta correctamente.
- Houston reúne contexto y delega solo cuando conviene.
- Pathfinder distingue estrategia de investigación.
- Orion separa journey, arquitectura y copy.
- Sentinel cubre heurística, resiliencia y accesibilidad.
- Atlas conserva intención y criterios verificables en el handoff.
- Galileo expande antes de converger.

### Step 3: Refactorizar una skill a la vez

Cuando un escenario falle, editar únicamente el artefacto implicado y repetir control/variante hasta cumplir.

## Task 10: Verificación completa y entrega

**Files:** all changed files

### Step 1: Ejecutar suite completa

Run: `python3 -m unittest discover -s tests -v`

Expected: 0 fallos.

### Step 2: Validar catálogo y plugin

Run: `python3 scripts/validate.py --root . --warnings-as-errors`

Expected: 0 errores y 0 advertencias.

### Step 3: Verificar build idempotente

Run: `python3 scripts/build.py && python3 scripts/build.py && git diff --check`

Expected: segunda ejecución no cambia archivos y no hay errores de whitespace.

### Step 4: Ejecutar validadores oficiales disponibles

Run one by one for all 16 canonical skills with `quick_validate.py`; run `validate_plugin.py plugins/bbva-odissey`.

Expected: todos válidos. Si el entorno carece de una dependencia del validador oficial, documentar la limitación y conservar la validación equivalente local.

### Step 5: Revisar el diff y el estado

Run: `git status --short && git diff --stat && git diff --check`

Confirmar que no se modificaron archivos fuera del alcance y que los tres árboles inicialmente no rastreados quedaron integrados sin pérdida.

### Step 6: Solicitar code review

Use `superpowers:requesting-code-review`, corregir hallazgos confirmados y volver a ejecutar los pasos 1–5.

