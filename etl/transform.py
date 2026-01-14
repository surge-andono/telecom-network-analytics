"""
Transform Layer

Responsibilities:
- KPI calculation
- Aggregation
- BI-ready schema
"""

import pandas as pd

def transform_network_kpi(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Availability KPI
    df["availability"] = (
        df["uptime_minutes"] /
        (df["uptime_minutes"] + df["downtime_minutes"])
    )

    # Aggregate to executive grain
    agg_df = (
        df.groupby(
            ["date_key", "region_key", "service_key", "vendor_key"],
            as_index=False
        )
        .agg({
            "uptime_minutes": "sum",
            "downtime_minutes": "sum",
            "availability": "mean",
            "avg_latency_ms": "mean",
            "packet_loss_pct": "mean"
        })
    )

    return agg_df