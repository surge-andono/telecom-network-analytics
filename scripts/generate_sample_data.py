"""
Sample Data Generator (Telecom)

Purpose:
- Generate realistic telco analytics datasets
- Support STEP 2 (Data Model & Sample Data)
- Used for portfolio, demo, and BI development
- NOT part of production ETL
"""

import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

# ------------------------------------------------------------------
# Project paths
# ------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
REF_DIR = DATA_DIR / "reference"

RAW_DIR.mkdir(exist_ok=True)
REF_DIR.mkdir(exist_ok=True)

# ------------------------------------------------------------------
# DIMENSION TABLES (REALISTIC)
# ------------------------------------------------------------------

# Date: 24 months
months = pd.period_range("2024-01", "2025-12", freq="M")

dim_date = pd.DataFrame({
    "date_key": [int(p.strftime("%Y%m")) for p in months],
    "year": [p.year for p in months],
    "month": [p.month for p in months],
    "year_month": [p.strftime("%Y-%m") for p in months]
})

# Region (national clusters)
regions = [
    "Sumatra",
    "Jabodetabek",
    "West Java",
    "Central Java",
    "East Java",
    "Kalimantan",
    "Sulawesi"
]

dim_region = pd.DataFrame({
    "region_key": range(1, len(regions) + 1),
    "region": regions
})

# Service (telco-standard with SLA class)
services = [
    ("4G LTE", "Mobile"),
    ("5G", "Mobile"),
    ("FTTH", "Fixed"),
    ("Metro Ethernet", "Core")
]

dim_service = pd.DataFrame({
    "service_key": range(1, len(services) + 1),
    "service": [s[0] for s in services],
    "sla_class": [s[1] for s in services]
})

# Vendor (global vendors)
vendors = [
    "Huawei",
    "Ericsson",
    "Nokia",
    "ZTE"
]

dim_vendor = pd.DataFrame({
    "vendor_key": range(1, len(vendors) + 1),
    "vendor": vendors
})

# Site (BTS / POP)
site_count = 120

dim_site = pd.DataFrame({
    "site_key": range(1, site_count + 1),
    "site_code": [f"SITE-{i:04d}" for i in range(1, site_count + 1)],
    "region_key": np.random.choice(dim_region["region_key"], site_count)
})

# ------------------------------------------------------------------
# FACT: NETWORK KPI
# Grain: date × site × service × vendor
# ------------------------------------------------------------------
kpi_rows = []

for d in dim_date.itertuples():
    for site in dim_site.itertuples():
        for s in dim_service.itertuples():
            for v in dim_vendor.itertuples():

                # Monthly minutes
                total_minutes = 30 * 24 * 60

                # Availability-driven downtime
                availability = np.random.uniform(0.990, 0.9995)
                downtime = int(total_minutes * (1 - availability))
                uptime = total_minutes - downtime

                latency = np.random.uniform(15, 120)
                packet_loss = np.random.uniform(0.05, 1.5)

                kpi_rows.append([
                    d.date_key,
                    site.site_key,
                    site.region_key,
                    s.service_key,
                    v.vendor_key,
                    uptime,
                    downtime,
                    round(latency, 2),
                    round(packet_loss, 3),
                    round(availability * 100, 3)
                ])

fact_network_kpi = pd.DataFrame(
    kpi_rows,
    columns=[
        "date_key",
        "site_key",
        "region_key",
        "service_key",
        "vendor_key",
        "uptime_minutes",
        "downtime_minutes",
        "avg_latency_ms",
        "packet_loss_pct",
        "availability_pct"
    ]
)

# ------------------------------------------------------------------
# FACT: INCIDENT
# Grain: date × region × service
# Incident correlated with downtime
# ------------------------------------------------------------------
incident_rows = []

for d in dim_date.itertuples():
    for r in dim_region.itertuples():
        for s in dim_service.itertuples():

            base_incident = np.random.randint(0, 10)

            # Higher incidents for mobile services
            if s.service in ["4G LTE", "5G"]:
                base_incident += np.random.randint(5, 20)

            incident_rows.append([
                d.date_key,
                r.region_key,
                s.service_key,
                base_incident
            ])

fact_incident = pd.DataFrame(
    incident_rows,
    columns=[
        "date_key",
        "region_key",
        "service_key",
        "incident_count"
    ]
)

# ------------------------------------------------------------------
# SAVE FILES
# ------------------------------------------------------------------
dim_date.to_csv(REF_DIR / "dim_date.csv", index=False)
dim_region.to_csv(REF_DIR / "dim_region.csv", index=False)
dim_service.to_csv(REF_DIR / "dim_service.csv", index=False)
dim_vendor.to_csv(REF_DIR / "dim_vendor.csv", index=False)
dim_site.to_csv(REF_DIR / "dim_site.csv", index=False)

fact_network_kpi.to_csv(RAW_DIR / "fact_network_kpi.csv", index=False)
fact_incident.to_csv(RAW_DIR / "fact_incident.csv", index=False)

print("Telco sample data generated successfully.")
