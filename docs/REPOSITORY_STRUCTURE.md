<pre>
telecom-network-analytics/
│
├── README.md
│   ├── Project Overview
│   ├── Architecture Decisions Record (ADR)
│   ├── Data Lineage
│   ├── Failure & Recovery Playbook
│
├── requirements.txt
│
├── config/                              # Centralized configuration
│   ├── __init__.py                     # Configuration package
│   ├── settings.py                     # Paths, SLA, DQ thresholds
│   └── logging_config.py               # Structured logging setup
│
├── scripts/                             # One-time / utility scripts
│   └── generate_sample_data.py          # Generate realistic sample CSV
│
├── data/
│   ├── raw/                             # Raw source data (input)
│   │   ├── fact_network_kpi.csv         # Site-level metrics
│   │   └── fact_incident.csv            # Operational input
│   │
│   ├── reference/                      # Master / dimension tables
│   │   ├── dim_date.csv
│   │   ├── dim_region.csv
│   │   ├── dim_service.csv
│   │   └── dim_vendor.csv
│   │
│   └── curated/                        # Curated BI-ready output
│       └── network_kpi_curated.csv      # Executive KPI dataset
│
├── etl/                                # ETL core logic (modular)
│   ├── __init__.py
│   ├── extract.py                      # Load raw & reference data
│   ├── validate.py                     # Data quality checks
│   ├── transform.py                    # KPI calculation & aggregation
│   └── load.py                         # Publish curated data
│
├── orchestration/                      # Pipeline orchestration
│   └── main.py                         # ETL entry point (scheduler-ready)
│
├── logs/                               # Observability
│   └── etl.log                         # ETL execution logs
│
├── tests/                              # Unit tests (pytest)
│   ├── test_validation.py              # Data quality rules tests
│   └── test_transform.py               # KPI & aggregation tests
│
├── dashboard/                          # BI artefacts
│   ├── powerbi/
│   │   └── telecom-network-analytics.pbix
│   └── screenshots/                    # Dashboard images
│       ├── EXECUTIVE_OVERVIEW.jpg
│       ├── OPERATIONAL_ANALYSIS.jpg
│       └── SLA_RISK_ANALYSIS.jpg
│
├── docs/                               # Consulting artefacts
│   ├── architecture/
│   │   ├── architecture.md             # ETL & analytics architecture
│   │   ├── data-lineage.md              # End-to-end data lineage
│   │   └── dashboard_wireframe1.md      # Dashboard design
│   │
│   └── storytelling/
│       └── STORYTELLING_SUMMARY.md      # Executive storytelling
│
└── .github/
    └── workflows/
        └── ci.yml                       # GitHub Actions CI pipeline
</pre>
