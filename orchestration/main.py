"""
Main Orchestration Entry Point

Responsibilities:
- Control end-to-end ETL execution
- Apply data quality validation (grain-aware, severity-aware)
- Persist data quality audit artifacts
- Ensure fail-fast and fail-safe behavior

This file is the ONLY execution entry point.
"""

import sys
import json
import logging
from datetime import datetime
from pathlib import Path

# ------------------------------------------------------------------
# Ensure project root is in PYTHONPATH
# ------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

# ------------------------------------------------------------------
# Imports (after path fix)
# ------------------------------------------------------------------
from config.logging_config import setup_logger
from config.app_config import DATA_DIR
from etl.extract import extract_network_kpi
from etl.validate import validate_network_kpi
from etl.transform import transform_network_kpi
from etl.load import load_curated_kpi

# ------------------------------------------------------------------
# Logging configuration
# ------------------------------------------------------------------
logger = setup_logger("etl.main")

# ------------------------------------------------------------------
# Grain definitions
# ------------------------------------------------------------------
RAW_GRAIN = [
    "date_key",
    "site_key",
    "service_key",
    "vendor_key"
]

CURATED_GRAIN = [
    "date_key",
    "region_key",
    "service_key",
    "vendor_key"
]


def main() -> None:
    logger.info("ETL pipeline started")

    # ==============================================================
    # 1. EXTRACT — RAW LAYER (SITE-LEVEL)
    # ==============================================================
    df_raw = extract_network_kpi()
    logger.info(f"Extracted raw rows: {len(df_raw)}")

    # ==============================================================
    # 2. DATA QUALITY CHECK — RAW LAYER
    # ==============================================================
    dq_raw = validate_network_kpi(
        df_raw,
        grain_columns=RAW_GRAIN
    )

    dq_raw_passed = dq_raw["passed"]

    # --------------------------------------------------------------
    # Persist RAW DQ report (runtime audit)
    # --------------------------------------------------------------
    dq_output_dir = DATA_DIR / "quality"
    dq_output_dir.mkdir(parents=True, exist_ok=True)

    report_period = datetime.now().strftime("%Y_%m")
    dq_raw_file = dq_output_dir / f"dq_raw_{report_period}.json"

    with open(dq_raw_file, "w") as f:
        json.dump(dq_raw, f, indent=2)

    logger.info(f"RAW DQ report saved to {dq_raw_file}")

    if not dq_raw_passed:
        logger.error("RAW data quality validation FAILED")
        logger.error(dq_raw)
        logger.error("ETL pipeline aborted due to CRITICAL data quality issues")
        return

    logger.info(
        f"RAW data quality validation PASSED "
        f"(coverage={dq_raw['coverage_pct']}%)"
    )

    # ==============================================================
    # 3. TRANSFORM — AGGREGATE TO EXECUTIVE GRAIN
    # ==============================================================
    df_curated = transform_network_kpi(df_raw)
    logger.info(f"Curated rows after transform: {len(df_curated)}")

    # ==============================================================
    # 4. DATA QUALITY CHECK — CURATED LAYER
    # ==============================================================
    dq_curated = validate_network_kpi(
        df_curated,
        grain_columns=CURATED_GRAIN
    )

    dq_curated_passed = dq_curated["passed"]

    dq_curated_file = dq_output_dir / f"dq_curated_{report_period}.json"
    with open(dq_curated_file, "w") as f:
        json.dump(dq_curated, f, indent=2)

    logger.info(f"CURATED DQ report saved to {dq_curated_file}")

    if not dq_curated_passed:
        logger.error("CURATED data quality validation FAILED")
        logger.error(dq_curated)
        logger.error("ETL pipeline aborted due to CRITICAL data quality issues")
        return

    logger.info(
        f"CURATED data quality validation PASSED "
        f"(coverage={dq_curated['coverage_pct']}%)"
    )

    # ==============================================================
    # 5. LOAD — SAFE PUBLISH (SINGLE SOURCE OF TRUTH)
    # ==============================================================
    load_curated_kpi(df_curated)
    logger.info("Curated dataset successfully published")

    logger.info("ETL pipeline completed successfully")


if __name__ == "__main__":
    main()
