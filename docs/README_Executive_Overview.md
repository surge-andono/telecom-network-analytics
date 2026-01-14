# 📡 Telecom Network Analytics – Repository Structure

This repository is organized to support end-to-end telecom network analytics, from raw data ingestion and ETL processing to BI dashboards and executive storytelling.

---
Please refer to the repository structure in [REPOSITORY_STRUCTURE.md](../docs/REPOSITORY_STRUCTURE.md)
## 📘 Core Documentation
- [README.md](../README.md)
- [Project Overview](../docs/PROJECT_OVERVIEW.md)
- [Architecture Decisions Record (ADR)](../docs/architecture/Architecture_Decisions_Record.md)
- [Data Lineage](../docs/architecture/data-lineage.md)
- [Failure & Recovery Playbook](../docs/architecture/failure-recovery-playbook.md)

---

## ⚙️ Configuration
Centralized configuration for paths, logging, SLA, and data quality thresholds.
- [config/__init__.py](../config/__init__.py)
- [settings.py](../config/settings.py)
- [logging_config.py](../config/logging_config.py)

---

## 🛠 Utility Scripts
One-time or helper scripts.
- [generate_sample_data.py](../scripts/generate_sample_data.py)  
  _Generate realistic sample CSV data_

---

## 📊 Data Layer

### Raw Data (Source Inputs)
- [fact_network_kpi.csv](../data/raw/fact_network_kpi.csv)  
  _Site-level network KPIs_
- [fact_incident.csv](../data/raw/fact_incident.csv)  
  _Operational incident data_

### Reference / Dimension Data
- [dim_date.csv](../data/reference/dim_date.csv)
- [dim_region.csv](../data/reference/dim_region.csv)
- [dim_service.csv](../data/reference/dim_service.csv)
- [dim_vendor.csv](../data/reference/dim_vendor.csv)

### Curated Data (BI-Ready)
- [network_kpi_curated.csv](../data/curated/network_kpi_curated.csv)  
  _Executive-ready KPI dataset_

---

## 🔄 ETL Layer
Modular ETL logic covering extraction, validation, transformation, and loading.
- [extract.py](../etl/extract.py)  
  _Load raw and reference data_
- [validate.py](../etl/validate.py)  
  _Data quality checks_
- [transform.py](../etl/transform.py)  
  _KPI calculation and aggregation_
- [load.py](../etl/load.py)  
  _Publish curated datasets_

---

## ⏱ Orchestration
Pipeline execution and scheduling entry point.
- [main.py](../orchestration/main.py)

---

## 📈 Observability & Logging
- [etl.log](../logs/etl.log)  
  _ETL execution logs for monitoring and troubleshooting_

---

## 🧪 Testing
Unit tests to ensure data quality and KPI correctness.
- [test_validation.py](../tests/test_validation.py)
- [test_transform.py](../tests/test_transform.py)

---

## 📊 Dashboard & BI Artefacts

### Power BI
- [telecom-network-analytics.pbix](../dashboard/powerbi/telecom-network-analytics.pbix)

### Dashboard Screenshots
- [Executive Overview](../dashboard/screenshots/EXECUTIVE_OVERVIEW.jpg)
- [Operational Analysis](../dashboard/screenshots/OPERATIONAL_ANALYSIS.jpg)
- [SLA Risk Analysis](../dashboard/screenshots/SLA_RISK_ANALYSIS.jpg)

---

## 🧠 Architecture & Storytelling

### Architecture Documentation
- [ETL & Analytics Architecture](../docs/architecture/architecture.md)
- [Data Lineage Diagram](../docs/architecture/data-lineage.md)
- [Dashboard Wireframe](../docs/architecture/dashboard_wireframe1.md)

### Executive Storytelling
- [Storytelling Summary](../docs/storytelling/STORYTELLING_SUMMARY.md)

---

## 🚀 CI/CD
- [CI Pipeline](../.github/workflows/ci.yml)  
  _GitHub Actions pipeline for automated testing and validation_
