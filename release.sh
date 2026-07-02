#!/bin/bash
# Diseña con Odissey — Script de Lanzamiento (Release)
#
# Uso: ./release.sh <versión>
# Ejemplo: ./release.sh 1.1.0
#
# Este script:
#   1. Actualiza la versión en todos los archivos de habilidad y manifiestos de plugin.
#   2. Recompila las distribuciones de plataforma (Cursor, Copilot, etc.).
#   3. Hace commit de los cambios.
#   4. Crea una etiqueta git (v<versión>).
#   5. Sube el commit y la etiqueta al repositorio.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# =============================================================================
# Validar entrada
# =============================================================================

if [ $# -ne 1 ]; then
    echo -e "${RED}Uso:${NC} ./release.sh <versión>"
    echo "  Ejemplo: ./release.sh 1.1.0"
    exit 1
fi

VERSION="$1"

# Validar formato semver (X.Y.Z)
if ! echo "$VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
    echo -e "${RED}Error:${NC} La versión debe ser formato semver (ej., 1.1.0)"
    exit 1
fi

TAG="v$VERSION"

# Verificar cambios sin confirmar en git
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo -e "${RED}Error:${NC} Tienes cambios sin confirmar en git. Confírmalos o guárdalos en stash primero."
    exit 1
fi

# Verificar que la etiqueta no exista ya
if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo -e "${RED}Error:${NC} La etiqueta $TAG ya existe."
    exit 1
fi

# Obtener versión actual de plugin.json
CURRENT=$(grep '"version"' "$SCRIPT_DIR/.claude-plugin/plugin.json" | head -1 | sed 's/.*"version": *"\([^"]*\)".*/\1/')

echo -e "${BLUE}Diseña con Odissey — Lanzamiento${NC}"
echo ""
echo "  Versión actual: $CURRENT"
echo "  Nueva versión:  $VERSION"
echo "  Etiqueta:       $TAG"
echo ""

# =============================================================================
# Incrementar versiones
# =============================================================================

echo -e "${GREEN}[1/5] Incrementando versiones${NC}"

# Archivos de habilidad fuente
for skill_file in "$SCRIPT_DIR"/skills/*/SKILL.md; do
    sed -i '' "s/^version: $CURRENT$/version: $VERSION/" "$skill_file"
done
skill_count=$(ls "$SCRIPT_DIR"/skills/*/SKILL.md 2>/dev/null | wc -l | tr -d ' ')
echo "  Se actualizaron $skill_count archivos de habilidad"

# Manifiestos de plugin
sed -i '' "s/\"version\": \"$CURRENT\"/\"version\": \"$VERSION\"/" "$SCRIPT_DIR/.claude-plugin/plugin.json"
sed -i '' "s/\"version\": \"$CURRENT\"/\"version\": \"$VERSION\"/" "$SCRIPT_DIR/.claude-plugin/marketplace.json"
echo "  Se actualizaron plugin.json y marketplace.json"

# =============================================================================
# Recompilar distribuciones
# =============================================================================

echo -e "${GREEN}[2/5] Recompilando distribuciones${NC}"
"$SCRIPT_DIR/build.sh"

# =============================================================================
# Validar manifiestos
# =============================================================================

echo -e "${GREEN}[3/5] Validando plugin${NC}"
if ! command -v claude >/dev/null 2>&1; then
    echo -e "${YELLOW}Advertencia:${NC} No se encontró la herramienta 'claude' CLI para validar el plugin localmente."
else
    claude plugin validate "$SCRIPT_DIR/.claude-plugin/plugin.json"
    claude plugin validate "$SCRIPT_DIR/.claude-plugin/marketplace.json"
fi

# =============================================================================
# Confirmar cambios (Commit)
# =============================================================================

echo -e "${GREEN}[4/5] Confirmando cambios en git${NC}"
git add skills/ agents/ .claude-plugin/ .cursor/ .github/ 2>/dev/null || true
git add build.sh release.sh README.md HOW-TO-USE.md 2>/dev/null || true

git commit -m "Lanzamiento $TAG"

# =============================================================================
# Crear Etiqueta (Tag)
# =============================================================================

echo -e "${GREEN}[5/5] Creando etiqueta git${NC}"
git tag "$TAG"

echo ""
echo -e "${YELLOW}Commit y etiqueta creados localmente.${NC}"
echo "  Commit: $(git log -1 --pretty=format:'%h %s')"
echo "  Etiqueta:    $TAG"
echo ""
read -r -p "¿Subir commit y etiqueta al origen (git push)? [y/N] " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo ""
    echo "Subida cancelada. Para subir manualmente cuando estés listo:"
    echo "  git push && git push origin $TAG"
    exit 0
fi

git push
git push origin "$TAG"

echo ""
echo -e "${BLUE}Lanzamiento $TAG subido con éxito.${NC}"
