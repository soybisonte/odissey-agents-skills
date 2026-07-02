#!/bin/bash
# BBVA Odissey — Instalador Local para Codex / Claude Code
#
# Este script ayuda a instalar BBVA Odissey como un plugin local en tu CLI de Codex o Claude Code.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}◆ ─ │ BBVA Odissey — Instalador Local │ ─ ◆${NC}"
echo ""

# 1. Compilar distribuciones
echo -e "${GREEN}[1/3] Compilando archivos del sistema...${NC}"
chmod +x "$SCRIPT_DIR/build.sh"
"$SCRIPT_DIR/build.sh"

# 2. Intentar validar manifiestos si claude está instalado
echo ""
echo -e "${GREEN}[2/3] Validando manifiestos del plugin...${NC}"
if command -v claude >/dev/null 2>&1; then
    claude plugin validate "$SCRIPT_DIR/.claude-plugin/plugin.json"
    echo -e "  ${GREEN}✓ Manifiesto validado correctamente.${NC}"
else
    echo -e "  ${YELLOW}⚠ 'claude' CLI no detectado en el PATH global (se validará al añadir en el chat).${NC}"
fi

# 3. Instrucciones de instalación
echo ""
echo -e "${GREEN}[3/3] Instrucciones de Instalación en Codex / Claude Code:${NC}"
echo ""
echo -e "Para activar BBVA Odissey en tu CLI de Codex o Claude Code, ejecuta el siguiente comando:"
echo ""
echo -e "  ${YELLOW}claude plugin add \"$SCRIPT_DIR\"${NC}"
echo ""
echo -e "O, si ya estás dentro de una sesión activa de Codex / Claude Code, simplemente escribe:"
echo ""
echo -e "  ${YELLOW}/plugin add \"$SCRIPT_DIR\"${NC}"
echo ""
echo -e "Una vez instalado, podrás:"
echo -e "  - Llamar a los agentes con ${BLUE}@houston${NC}, ${BLUE}@pathfinder${NC}, ${BLUE}@orion${NC}, ${BLUE}@sentinel${NC}, ${BLUE}@atlas${NC} o ${BLUE}@galileo${NC}."
echo -e "  - Usar comandos rápidos como ${BLUE}/strategy${NC}, ${BLUE}/journey${NC}, ${BLUE}/evaluar${NC}, ${BLUE}/robustecer${NC}, etc."
echo ""
echo -e "${GREEN}¡Listo para iniciar el viaje!${NC}"
