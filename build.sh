#!/bin/bash
# Diseña con Odissey
# Script de compilación: genera distribuciones específicas para plataformas a partir de las fuentes.
#
# Codex / Claude Code leen las habilidades en skills/ y agentes en agents/ directamente.
# Este script produce las distribuciones que requieren otras herramientas.
#
# Plataformas soportadas:
#   .cursor/rules/    — Reglas para Cursor (archivos .mdc con frontmatter simplificado)
#   .github/          — VS Code Copilot (copilot-instructions.md + archivos de habilidades)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"

# Colores para la salida
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # Sin color

echo -e "${BLUE}Diseña con Odissey${NC}"
echo "Compilando distribuciones para plataformas..."
echo ""

skill_count=$(ls -d "$SKILLS_DIR"/*/ 2>/dev/null | wc -l | tr -d ' ')
agent_count=$(ls "$SCRIPT_DIR"/agents/*.md 2>/dev/null | wc -l | tr -d ' ')

# =============================================================================
# CURSOR — .cursor/rules/
# Archivos .mdc con frontmatter de Cursor (description, alwaysApply)
# Cada habilidad se convierte en un archivo .mdc plano. Las referencias se
# extraen a sus propios archivos .mdc para evitar saturación de contexto.
# =============================================================================

echo -e "${GREEN}[1/2] Cursor (.cursor/rules/)${NC}"

CURSOR_DIR="$SCRIPT_DIR/.cursor/rules"
rm -rf "$CURSOR_DIR"
mkdir -p "$CURSOR_DIR"

for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    skill_file="$skill_dir/SKILL.md"

    if [ ! -f "$skill_file" ]; then
        continue
    fi

    # Extrae la descripción del frontmatter YAML
    description=$(awk '
        /^---$/ { count++; next }
        count == 1 && /^description:/ {
            sub(/^description: *>? */, "")
            desc = $0
            while ((getline line) > 0) {
                if (line ~ /^  /) {
                    sub(/^  +/, "", line)
                    desc = desc " " line
                } else {
                    break
                }
            }
            print desc
            exit
        }
    ' "$skill_file")

    # Extrae el contenido después del frontmatter
    content=$(awk '
        BEGIN { count = 0; printing = 0 }
        /^---$/ { count++; if (count == 2) { printing = 1; next } }
        printing { print }
    ' "$skill_file")

    # Si la habilidad tiene documentos de referencia, genera archivos mdc para cada uno
    if [ -d "$skill_dir/references" ]; then
        for ref_file in "$skill_dir/references"/*.md; do
            if [ -f "$ref_file" ]; then
                ref_name=$(basename "$ref_file" .md)
                ref_content=$(cat "$ref_file")

                # Genera una descripción de activación en español según el documento de referencia
                case "$ref_name" in
                    fundamentos-accesibilidad)
                        ref_desc="Referencia de Odissey: WCAG 2.2 para diseñadores, diseño para lector de pantalla, navegación por teclado, accesibilidad cognitiva y motriz. Cargar al trabajar en accesibilidad, auditorías a11y o diseño inclusivo." ;;
                    estrategia-contenido)
                        ref_desc="Referencia de Odissey: metodología de voz y tono, UX writing, microcopia, modelado de contenido. Cargar al redactar textos de interfaz, mensajes de error o definir la estrategia de contenido." ;;
                    diseno-etico)
                        ref_desc="Referencia de Odissey: remediación de anti-patrones, alternativas éticas a patrones oscuros, consentimiento, regulaciones (GDPR, CPRA). Cargar al auditar ética de producto o diseñar flujos de consentimiento." ;;
                    arquitectura-informacion)
                        ref_desc="Referencia de Odissey: patrones de navegación, taxonomías, sistemas de etiquetado, buscabilidad. Cargar al estructurar menús, flujos de navegación o jerarquías de contenido." ;;
                    patrones-interaccion)
                        ref_desc="Referencia de Odissey: diseño de formularios, estados de interacción en UI, validaciones, confirmaciones y flujos de deshacer. Cargar al diseñar formularios, inputs o transiciones de estado." ;;
                    marcos-medicion)
                        ref_desc="Referencia de Odissey: framework HEART de Google, mapeo de métricas, diseño de experimentos A/B. Cargar al definir KPIs o planificar mediciones de producto." ;;
                    metodos-investigacion)
                        ref_desc="Referencia de Odissey: matriz de métodos de investigación de usuarios, guías de entrevista, pruebas de usabilidad. Cargar al planificar o procesar investigaciones de UX." ;;
                    diseno-servicios)
                        ref_desc="Referencia de Odissey: metodología de service blueprinting, capas de procesos, puntos de contacto y orquestación. Cargar al mapear ecosistemas y planos de servicio complejos." ;;
                    *)
                        ref_desc="Documento de referencia de Odissey: $ref_name" ;;
                esac

                cat > "$CURSOR_DIR/odissey-ref-$ref_name.mdc" << ENDOFREF
---
description: $ref_desc
alwaysApply: false
---

$ref_content
ENDOFREF
            fi
        done
    fi

    # Determina si debe aplicarse siempre
    # Solo la habilidad principal de odissey se aplica por defecto
    always_apply="false"
    if [ "$skill_name" = "odissey" ]; then
        always_apply="true"
    fi

    # Escribe la regla .mdc
    cat > "$CURSOR_DIR/$skill_name.mdc" << ENDOFMDC
---
description: $description
alwaysApply: $always_apply
---

$content
ENDOFMDC

done

mdc_count=$(ls "$CURSOR_DIR"/*.mdc 2>/dev/null | wc -l | tr -d ' ')
echo "  Se generaron $mdc_count archivos de regla .mdc para Cursor"

# =============================================================================
# VS CODE COPILOT — .github/
# copilot-instructions.md con los principios principales
# Habilidades individuales en .github/copilot/skills/
# =============================================================================

echo -e "${GREEN}[2/2] VS Code Copilot (.github/)${NC}"

GITHUB_DIR="$SCRIPT_DIR/.github"
COPILOT_SKILLS_DIR="$GITHUB_DIR/copilot/skills"

# Preserva workflows si existen
WORKFLOWS_BACKUP=""
if [ -d "$GITHUB_DIR/workflows" ]; then
    WORKFLOWS_BACKUP=$(mktemp -d)
    cp -r "$GITHUB_DIR/workflows" "$WORKFLOWS_BACKUP/workflows"
    trap '[ -n "${WORKFLOWS_BACKUP:-}" ] && [ -d "$WORKFLOWS_BACKUP/workflows" ] && [ ! -d "$GITHUB_DIR/workflows" ] && { mkdir -p "$GITHUB_DIR" 2>/dev/null; mv "$WORKFLOWS_BACKUP/workflows" "$GITHUB_DIR/workflows" 2>/dev/null; } || true' EXIT
fi
rm -rf "$GITHUB_DIR"
mkdir -p "$COPILOT_SKILLS_DIR"
if [ -n "$WORKFLOWS_BACKUP" ] && [ -d "$WORKFLOWS_BACKUP/workflows" ]; then
    mv "$WORKFLOWS_BACKUP/workflows" "$GITHUB_DIR/workflows"
    rmdir "$WORKFLOWS_BACKUP"
fi

# Genera el copilot-instructions.md principal a partir de la habilidad odissey
odissey_content=$(awk '
    BEGIN { count = 0; printing = 0 }
    /^---$/ { count++; if (count == 2) { printing = 1; next } }
    printing { print }
' "$SKILLS_DIR/odissey/SKILL.md")

cat > "$GITHUB_DIR/copilot-instructions.md" << ENDOFCOPILOT
# Diseña con Odissey

Este proyecto utiliza el sistema Odissey de estrategia y diseño de experiencia de usuario (UX). Cuando trabajes en decisiones de diseño, estrategia de UX, investigación de usuarios, arquitectura de información, redacción de contenidos, accesibilidad o transferencia a ingeniería, sigue estos principios y apóyate en las habilidades ubicadas en .github/copilot/skills/.

$odissey_content
ENDOFCOPILOT

# Copia cada habilidad (excepto odissey, que va en el archivo principal)
for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    skill_file="$skill_dir/SKILL.md"

    if [ ! -f "$skill_file" ] || [ "$skill_name" = "odissey" ]; then
        continue
    fi

    # Copia el archivo SKILL.md
    cp "$skill_file" "$COPILOT_SKILLS_DIR/$skill_name.md"

    # Copia documentos de referencia si existen
    if [ -d "$skill_dir/references" ]; then
        mkdir -p "$COPILOT_SKILLS_DIR/$skill_name"
        cp "$skill_dir/references"/*.md "$COPILOT_SKILLS_DIR/$skill_name/"
    fi
done

# También genera AGENTS.md para la descripción de agentes en Copilot
cat > "$GITHUB_DIR/AGENTS.md" << ENDOFAGENTS
# Diseña con Odissey

Este proyecto utiliza el sistema integral de estrategia y diseño UX Odissey.

## Habilidades (Skills)

Las habilidades especializadas de diseño están disponibles en .github/copilot/skills/:

$(for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    desc=$(awk '
        /^---$/ { count++; next }
        count == 1 && /^description:/ {
            sub(/^description: *>? */, "")
            desc = $0
            while ((getline line) > 0) {
                if (line ~ /^  /) {
                    sub(/^  +/, "", line)
                    desc = desc " " line
                } else {
                    break
                }
            }
            match(desc, /\. /)
            if (RSTART > 0) desc = substr(desc, 1, RSTART)
            print desc
            exit
        }
    ' "$skill_dir/SKILL.md" 2>/dev/null)
    echo "- **$skill_name** — $desc"
done)

## Principios Fundamentales

- Respetar la autonomía del usuario — sin manipulación, opciones claras, fácil reversibilidad.
- Diseñar para condiciones reales — conexiones lentas, distracciones, accesibilidad, estrés.
- Hacer visible la intención — cada pantalla debe indicar qué puedo hacer, por qué y qué sigue.
- Evidencia sobre intuición — investigar, probar, medir.
- Sistemas sobre pantallas — los flujos forman parte de la vida real del usuario.
- Valores éticos por defecto — opt-in obligatorio, privacidad por defecto, honestidad sobre persuasión.

Consulta .github/copilot-instructions.md para ver el sistema Odissey completo y el catálogo de anti-patrones.
ENDOFAGENTS

copilot_count=$(ls "$COPILOT_SKILLS_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "  Se generaron copilot-instructions.md + AGENTS.md + $copilot_count archivos de habilidad para Copilot"

# =============================================================================
# Resumen
# =============================================================================

echo ""
echo -e "${BLUE}Compilación completada con éxito.${NC}"
echo ""
echo "  skills/             — $skill_count habilidades fuente (usadas por Codex/Claude Code)"
echo "  agents/             — $agent_count agentes fuente (usados por Codex/Claude Code)"
echo "  .cursor/rules/      — $mdc_count reglas en formato .mdc para Cursor"
echo "  .github/            — copilot-instructions.md + AGENTS.md + $copilot_count habilidades"
echo ""
echo -e "${YELLOW}Nota:${NC} Haz commit de los directorios .cursor/ y .github/ generados para que"
echo "las configuraciones queden disponibles en Cursor y Copilot."
