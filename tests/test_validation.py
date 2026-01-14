import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import pandas as pd
from etl.validate import validate_network_kpi


def test_validation_pass():
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

    is_valid, _ = validate_network_kpi(df)
    assert is_valid is True
