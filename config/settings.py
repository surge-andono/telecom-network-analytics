# Purpose: Centralized configuration for paths, SLA, and data quality rules

"""
Central configuration file.
All paths, thresholds, and SLA rules are defined here
to avoid hard-coded values inside ETL logic.
"""

# =========================
# DATA PATHS
# =========================

# Raw input data (as received from source systems)
RAW_PATH = "data/raw/"

# Reference / master data (dimensions)
REF_PATH = "data/reference/"

# Curated output data (BI-ready layer)
CURATED_PATH = "data/curated/"

# =========================
# BUSINESS RULES
# =========================

# SLA threshold for network availability (%)
AVAILABILITY_SLA = 99.5

# =========================
# DATA QUALITY THRESHOLDS
# =========================

# Maximum allowed NULL percentage in critical columns
MAX_NULL_RATE = 0.01   # 1%

# Maximum allowed duplicate rate based on logical primary key
MAX_DUPLICATE_RATE = 0.005  # 0.5%
