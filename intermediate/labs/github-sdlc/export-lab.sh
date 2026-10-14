#!/usr/bin/env bash
# export-lab.sh
# Creates a clean ZIP of the Github-SDLC lab for workshop participants.
# Usage: ./export-lab.sh [output-dir]
# Output: <output-dir>/github-sdlc-lab-<date>.zip  (default: current directory)

set -euo pipefail

LAB_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="${1:-$LAB_DIR}"
TIMESTAMP="$(date +%Y%m%d)"
ZIP_NAME="github-sdlc-lab-${TIMESTAMP}.zip"
ZIP_PATH="${OUTPUT_DIR}/${ZIP_NAME}"

echo "📦 Exporting Github-SDLC lab to ${ZIP_PATH} ..."

# Convert all Markdown files to PDF if md2pdf is available
if command -v md2pdf &>/dev/null; then
  echo "📄 Converting Markdown files to PDF ..."
  while IFS= read -r -d '' md_file; do
    pdf_file="${md_file%.md}.pdf"
    echo "   ${md_file} → ${pdf_file}"
    md2pdf "$md_file" -o "$pdf_file"
  done < <(find "$LAB_DIR" -name "*.md" -not -path "*/node_modules/*" -print0)
  echo "✅ PDF conversion done."
fi

rm -f "$ZIP_PATH"

# cd one level up so zip entries get a "github-sdlc/" prefix
cd "$LAB_DIR/.."

zip -r "$ZIP_PATH" \
  github-sdlc/WORKSHOP-part1-BUILD.md \
  github-sdlc/WORKSHOP-part1-BUILD.pdf \
  github-sdlc/WORKSHOP-part2-GITHUB-AUTOMATION.md \
  github-sdlc/WORKSHOP-part2-GITHUB-AUTOMATION.pdf \
  github-sdlc/.github \
  github-sdlc/docs \
  github-sdlc/.bob/workshop-hints.md \
  github-sdlc/.bob/rules \
  -x "*.DS_Store"

echo "✅ Done: ${ZIP_PATH}"
echo "   Size: $(du -sh "$ZIP_PATH" | cut -f1)"
