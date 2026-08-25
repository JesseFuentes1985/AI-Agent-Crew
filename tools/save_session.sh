#!/usr/bin/env bash
# save_session.sh — Dump current session JSON to a temp file and run session_saver.py
#
# Usage (called by Orbit at end of sessions or on demand):
#   bash tools/save_session.sh <session_json_file> [label] [agent]
#
# Orbit will:
#   1. Use sessions_history tool to get the JSON
#   2. Write it to /tmp/current_session.json
#   3. Call this script

set -euo pipefail

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$WORKSPACE/.venv"

SESSION_FILE="${1:-/tmp/current_session.json}"
LABEL="${2:-session}"
AGENT="${3:-orbit}"

echo "🛸 Orbit Session Saver"
echo "   File:  $SESSION_FILE"
echo "   Label: $LABEL"
echo "   Agent: $AGENT"
echo ""

# Use the Python 3.14 venv where mem0 is installed
if [ -f "$VENV/bin/python3" ]; then
    PYTHON="$VENV/bin/python3"
else
    PYTHON="python3"
fi

"$PYTHON" "$WORKSPACE/tools/session_saver.py" \
    --file "$SESSION_FILE" \
    --agent "$AGENT" \
    --label "$LABEL"
