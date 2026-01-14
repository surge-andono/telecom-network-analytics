from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parents[1]

# Data paths
DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
REFERENCE_DATA_DIR = DATA_DIR / "reference"
CURATED_DATA_DIR = DATA_DIR / "curated"

# Files
FACT_NETWORK_KPI_FILE = RAW_DATA_DIR / "fact_network_kpi.csv"
FACT_INCIDENT_FILE = RAW_DATA_DIR / "fact_incident.csv"

CURATED_KPI_FILE = CURATED_DATA_DIR / "network_kpi_curated.csv"

# Incremental configuration
INCREMENTAL_COLUMN = "year_month"

# Validation thresholds
LATENCY_MAX_MS = 200
PACKET_LOSS_MAX_PCT = 5.0
