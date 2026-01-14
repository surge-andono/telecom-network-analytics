import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import pandas as pd
from etl.transform import transform_network_kpi

def test_transform_output_schema():
    df = pd.DataFrame({
        "date_key": [202401],
        "region_key": [1],
        "service_key": [1],
        "vendor_key": [1],
        "uptime_minutes": [40000],
        "downtime_minutes": [100],
        "avg_latency_ms": [20],
        "packet_loss_pct": [0.5]
    })

    result = transform_network_kpi(df)

    assert "availability" in result.columns
    assert len(result) == 1
