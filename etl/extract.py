"""
Extract Layer

Responsibilities:
- Read raw datasets
- No business logic
- No validation
- No incremental logic
"""

import pandas as pd
from config.app_config import (
    FACT_NETWORK_KPI_FILE,
    FACT_INCIDENT_FILE
)

from config.logging_config import setup_logger

logger = setup_logger("etl.extract")

# def extract_network_kpi() -> pd.DataFrame:
#     return pd.read_csv(FACT_NETWORK_KPI_FILE)

def extract_network_kpi() -> pd.DataFrame:
    logger.info("Start extract fact_network_kpi")
    df = pd.read_csv(FACT_NETWORK_KPI_FILE)
    logger.info(f"Extract fact_network_kpi success | rows={len(df)}")
    return df

# def extract_incident() -> pd.DataFrame:
#     return pd.read_csv(FACT_INCIDENT_FILE)

def extract_incident() -> pd.DataFrame:
    logger.info("Start extract fact_incident")
    df = pd.read_csv(FACT_INCIDENT_FILE)
    logger.info(f"Extract fact_incident success | rows={len(df)}")
    return df