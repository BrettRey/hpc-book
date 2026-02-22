#!/bin/bash
# HPC Book Quick Status - Zero-token overview
# Run from anywhere; resolves repo root from script location

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}" || {
    echo "Failed to locate repository root from script directory."
    exit 1
}

if [ ! -f "hpc-book.tex" ]; then
    echo "hpc-book.tex not found in ${PWD}."
    exit 1
fi

# Colors
BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo ""
echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}  HPC BOOK STATUS${NC}"
echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"

# ─────────────────────────────────────────────────────────────────
# CHAPTER STATUS (from PROJECT_STATUS.md)
# ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${BLUE}▶ CHAPTER STATUS${NC}"
echo "─────────────────────────────────────────────────────────────────"

# Extract Part/Chapter status from the Completed and In Progress sections
echo "  Part I (Ch 1-3):  Complete"
echo "  Part II (Ch 4-8): Complete"
echo ""
echo "  Part III:"
grep -E "^- (✅|🔄).*\*\*Ch (9|10|11|12)\*\*" PROJECT_STATUS.md 2>/dev/null | sed 's/^- /    /' | head -4
echo ""
echo "  Part IV:"
grep -E "^- 🔄.*Ch (13|14|15)" PROJECT_STATUS.md 2>/dev/null | sed 's/^- /    /' | head -3

# ─────────────────────────────────────────────────────────────────
# CURRENTLY ACTIVE (uncommented in hpc-book.tex)
# ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}▶ ACTIVE CHAPTERS (uncommented in hpc-book.tex)${NC}"
echo "─────────────────────────────────────────────────────────────────"

grep -E "^\\\\(include|input)\{chapters/chapter" hpc-book.tex 2>/dev/null \
    | sed -E 's/^\\(include|input)\{chapters\//  /' \
    | sed 's/}//' \
    || echo "  None uncommented"

echo ""
echo -e "${YELLOW}  Commented out:${NC}"
grep -E "^%.*\\\\(include|input)\{chapters/chapter" hpc-book.tex 2>/dev/null \
    | wc -l \
    | xargs -I {} echo "  {} chapters"

# ─────────────────────────────────────────────────────────────────
# NEXT ACTIONS (from PROJECT_STATUS.md)
# ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${YELLOW}▶ NEXT ACTIONS${NC}"
echo "─────────────────────────────────────────────────────────────────"

# Extract Immediate section
sed -n '/^### Immediate/,/^### /p' PROJECT_STATUS.md 2>/dev/null | grep -E "^[0-9]+\." | sed 's/^/  /' | head -5

# ─────────────────────────────────────────────────────────────────
# LAST BUILD
# ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${BLUE}▶ LAST BUILD${NC}"
echo "─────────────────────────────────────────────────────────────────"

if [ -f "build/hpc-book.pdf" ]; then
    LAST_BUILD=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "build/hpc-book.pdf" 2>/dev/null)
    PAGES=$(pdfinfo "build/hpc-book.pdf" 2>/dev/null | grep "Pages" | awk '{print $2}')
    echo "  Last built: ${LAST_BUILD}"
    echo "  Pages: ${PAGES:-unknown}"
else
    echo "  No build found in build/"
fi

# ─────────────────────────────────────────────────────────────────
# RECENT SESSION LOGS
# ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}▶ RECENT SESSIONS${NC}"
echo "─────────────────────────────────────────────────────────────────"

ls -t .agent/logs/*.md 2>/dev/null | head -3 | while read f; do
    DATE=$(basename "$f" .md | sed 's/session-//')
    LINES=$(wc -l < "$f" | xargs)
    echo "  ${DATE} (${LINES} lines)"
done

# ─────────────────────────────────────────────────────────────────
# GIT STATUS
# ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${BLUE}▶ GIT STATUS${NC}"
echo "─────────────────────────────────────────────────────────────────"

BRANCH=$(git branch --show-current 2>/dev/null)
UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | xargs)
echo "  Branch: ${BRANCH:-unknown}"
echo "  Uncommitted changes: ${UNCOMMITTED}"

echo ""
echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
echo "  Build: latexmk hpc-book.tex"
echo "  Full status: cat PROJECT_STATUS.md"
echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
echo ""
