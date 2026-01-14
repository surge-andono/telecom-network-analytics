# Data Model & Sample Data

## Telecom Network Analytics

**Implementation Foundation for Analytics & Automation**

## 1. Purpose

This document defines the **data foundation** for the analytics solution described in Step 1.

The objectives of this step are to:

* Translate the logical design into a **clear data model**
* Define **explicit schemas** for fact and dimension tables
* Provide **realistic sample datasets** that can be used directly for ETL and BI development
* Ensure the data structure supports automation, KPI accuracy, and scalability

This step intentionally focuses on  **data structure** , not on code.

---

## 2. Data Modeling Approach

### 2.1 Modeling Style

The solution uses a **star schema** optimized for BI and executive reporting.

* Fact tables store measurable events and metrics
* Dimension tables store descriptive attributes
* Grain is explicitly defined and consistently enforced

This approach ensures:

* Simple joins
* Predictable KPI calculations
* High performance in BI tools

### 2.2 Reporting Grain (Confirmed)

> **Year-Month × Region × Service × Vendor**

All fact tables are designed to align with this grain unless explicitly stated otherwise.

---

## 3. Dimension Tables

Dimension tables act as **master reference data** and are maintained independently from fact data.

### 3.1 dim_date

**Purpose:**

Provides a consistent time reference for reporting and aggregation.

| Column Name | Data Type | Description                |
| ----------- | --------- | -------------------------- |
| date_key    | INTEGER   | Surrogate key (YYYYMM)     |
| year        | INTEGER   | Calendar year              |
| month       | INTEGER   | Month number (1–12)       |
| year_month  | STRING    | Year-month label (YYYY-MM) |

**Notes:**

* `date_key` is used for joins
* Granularity is monthly to match executive reporting

### 3.2 dim_region

**Purpose:**

Defines geographical regions where network services operate.

| Column Name | Data Type | Description   |
| ----------- | --------- | ------------- |
| region_key  | INTEGER   | Surrogate key |
| region      | STRING    | Region name   |

Example values:
West, Central, East

### 3.3 dim_service

**Purpose:**

Defines types of network services.

| Column Name | Data Type | Description   |
| ----------- | --------- | ------------- |
| service_key | INTEGER   | Surrogate key |
| service     | STRING    | Service name  |

Example values:
4G, 5G, Fiber

### 3.4 Dim Vendor

**Purpose:**

Identifies network equipment vendors.

| Column Name | Data Type | Description   |
| ----------- | --------- | ------------- |
| vendor_key  | INTEGER   | Surrogate key |
| vendor      | STRING    | Vendor name   |

**Example values:**

`Vendor A`, `Vendor B`, `Vendor C`

---

## 4. Fact Tables

### 4.1 fact_network_kpi

**Purpose:**

Stores aggregated network performance metrics at the defined reporting grain.

**Grain**

> **One row per Year-Month × Region × Service × Vendor**

**Schema**

| Column Name      | Data Type | Description            |
| ---------------- | --------- | ---------------------- |
| date_key         | INTEGER   | FK to `dim_date`     |
| region_key       | INTEGER   | FK to `dim_region`   |
| service_key      | INTEGER   | FK to `dim_service`  |
| vendor_key       | INTEGER   | FK to `dim_vendor`   |
| uptime_minutes   | INTEGER   | Total uptime minutes   |
| downtime_minutes | INTEGER   | Total downtime minutes |
| avg_latency_ms   | FLOAT     | Average latency        |
| packet_loss_pct  | FLOAT     | Packet loss percentage |

**Notes:**

* Uptime and downtime are stored separately to support accurate availability calculation
* Latency and packet loss are already aggregated at monthly level

### 4.2 fact_incident

**Purpose:**

Stores aggregated incident counts to provide operational context.

**Grain**

> **One row per Year-Month × Region × Service**

| Column Name    | Data Type | Description           |
| -------------- | --------- | --------------------- |
| date_key       | INTEGER   | FK to `dim_date`    |
| region_key     | INTEGER   | FK to `dim_region`  |
| service_key    | INTEGER   | FK to `dim_service` |
| incident_count | INTEGER   | Number of incidents   |

---

## 5. KPI Definitions (Data-Level)

These definitions are enforced  **outside the BI layer** .

### 5.1 Availability (%)

> **Availability = uptime_minutes / (uptime_minutes + downtime_minutes)**

### 5.2 SLA Risk Indicator (Conceptual)

* SLA risk is flagged if availability falls below a predefined threshold
* Threshold values are configurable outside the data model

---

## 6. Sample Data Strategy

### 6.1 Time Coverage

* Period: **January 2024 – December 2025**
* Total: **24 months**

### 6.2 Data Characteristics

* Values follow realistic telecom ranges
* Seasonal variations included
* Incidents correlate with performance degradation

### 6.3 Data Format

* All sample data is provided as **CSV**
* UTF-8 encoding
* Header included

(Refer to diagrams in `/docs/architecture/`)

---

## 7. Sample Dataset Structure (Repository)

data/
├── README.md                     # Penjelasan dataset & aturan penggunaan
│
├── reference/                    # Master / dimension data (static & low-change)
│   ├── dim_date.csv
│   ├── dim_region.csv
│   ├── dim_service.csv
│   └── dim_vendor.csv
│
├── raw/                          # Raw fact data (source-aligned, no transformation)
│   ├── fact_network_kpi.csv
│   └── fact_incident.csv
│
├── curated/                      # Output ETL (analytics-ready, BI-consumable)
│   ├── fact_network_kpi_monthly.csv
│   └── fact_incident_monthly.csv
│
└── _archive/                     # Optional: deprecated / historical samples
    └── README.md

---

## 8. Validation Rules (Data Foundation)

Before any ETL logic is applied, the following assumptions hold:

* No NULL keys in fact tables
* All foreign keys must exist in dimension tables
* Numeric metrics must fall within valid ranges
* No duplicate rows at the defined grain

These rules are enforced later in  **Step 3 (ETL implementation)** .

---

## 9. Relationship to Other Steps

* **Step 1** defines *why* and *what* the solution is
* **Step 2** defines *how data is structured*
* **Step 3** implements automation, ETL, and governance
* **Step 4** validates readiness for job application

---

### 10. Final Assessment (Step 2)

This data model:

* Is simple, explicit, and BI-optimized
* Supports automation and incremental processing
* Aligns fully with the design decisions in Step 1
* Can be directly consumed by ETL pipelines and BI tools

---
