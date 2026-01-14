"""
Load Layer

Responsibilities:
- Persist curated datasets
- Overwrite only after successful validation
"""

from config.app_config import CURATED_KPI_FILE
import pandas as pd

def load_curated_kpi(df: pd.DataFrame) -> None:
    df.to_csv(CURATED_KPI_FILE, index=False)