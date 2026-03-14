#!/bin/bash
# check-anthropic-balance.sh
# Reads dashboard/budget.json and prints balance info
# Used by the credit monitor cron job

BUDGET_FILE="/Users/jessefuentes/.openclaw/workspace-main/dashboard/budget.json"

if [ ! -f "$BUDGET_FILE" ]; then
  echo "ERROR: budget.json not found at $BUDGET_FILE"
  exit 1
fi

cat "$BUDGET_FILE"
