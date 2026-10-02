#!/usr/bin/env bash
# start.sh – Start the GFM Bank Core Banking API
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODE_DIR="$SCRIPT_DIR/code"

cd "$CODE_DIR"

echo "Installing Python dependencies…"
pip install -q -r requirements.txt

if [ ! -f corebank.db ]; then
  echo "Seeding database…"
  python seed_db.py
fi

echo ""
echo "Starting GFM Bank API on http://127.0.0.1:8000"
echo "API docs: http://127.0.0.1:8000/docs"
echo ""
uvicorn demo_api:app --reload --host 127.0.0.1 --port 8000
