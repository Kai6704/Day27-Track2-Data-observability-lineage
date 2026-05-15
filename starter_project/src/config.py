from __future__ import annotations

import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Tự động nạp các biến từ file .env vào môi trường (nếu có)
env_file = PROJECT_ROOT / ".env"
if env_file.exists():
    with env_file.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#") and "=" in line:
                key, val = line.strip().split("=", 1)
                os.environ.setdefault(key.strip(), val.strip())

DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"

PASSED_DATASET = DATA_DIR / "orders_passed.csv"
FAILED_DATASET = DATA_DIR / "orders_failed.csv"
SUMMARY_FILE = OUTPUT_DIR / "validation_summary.json"

VALID_STATUSES = {"completed", "pending", "cancelled"}

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")
AIRFLOW_INPUT_FILE = os.getenv("AIRFLOW_INPUT_FILE", str(PASSED_DATASET))
