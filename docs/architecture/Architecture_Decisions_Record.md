# Architecture Decision Records (ADR)

## Project: Telecom Network Analytics

**Status:** Accepted

**Owner:** Data Visualization & Automation Engineer

---

## ADR-001 — End-to-End Analytics Architecture (ETL → BI → Dashboard)

### Context

The project aims to deliver a **reliable, scalable, and explainable analytics solution** for telecom network performance, focusing on  **SLA compliance, operational diagnostics, and risk prioritization** .

The solution must support:

* Incremental data processing
* Clear separation of raw, curated, and semantic layers
* Reusable KPI logic
* Executive and operational consumption

### Decision

Adopt a  **layered analytics architecture** :

* **Python-based ETL** for ingestion, validation, and aggregation
* **Star schema (fact & dimension)** for analytics modeling
* **Power BI semantic layer** for KPI calculation and visualization
* **Three-layer dashboard storytelling** (Executive → Ops → Risk)

### Consequences

✅ Clear data lineage and ownership

✅ BI logic is explainable and auditable

✅ Scalable for future data sources and KPIs

⚠️ Slightly higher upfront design effort (intentional)

---

## ADR-002 — Data Modeling Strategy (Star Schema)

### Context

Telecom analytics requires consistent aggregation across  **time, service, region, site, and vendor** . Flat tables introduce ambiguity and duplication.

### Decision

Use a  **Star Schema** :

* **Fact tables** :
* `fact_network_kpi`
* `fact_incident`
* **Dimension tables** :
* `dim_date`
* `dim_service`
* `dim_region`
* `dim_site`
* `dim_vendor`
* `dim_sla_target`

### Consequences

✅ Predictable aggregation behavior

✅ Power BI performs efficiently

✅ KPI definitions remain stable over time

⚠️ Requires disciplined ETL ownership

---

## ADR-003 — Incremental Load Strategy

### Context

Reprocessing full historical telecom data is inefficient and unnecessary.

### Decision

Implement **incremental loading** based on:

* `year_month` for KPI facts
* Append-only logic for incident data
* Idempotent ETL runs

### Consequences

✅ Faster pipeline execution

✅ Reduced compute cost

✅ Safe re-runs without duplication

⚠️ Requires careful watermark management

---

## ADR-004 — Data Quality Gates in ETL

### Context

Incorrect or duplicated data leads to misleading SLA insights.

### Decision

Enforce **data quality validation** in ETL:

* Row count checks
* Null checks on key fields
* Duplicate detection at reporting grain
* Value range validation

Pipeline **fails fast** if validation fails.

### Consequences

✅ Prevents bad data reaching dashboards

✅ Improves trust with stakeholders

⚠️ ETL may fail more often (by design)

---

## ADR-005 — KPI Ownership and Calculation Layer

### Context

KPIs such as Availability, SLA Gap, and Incident Severity must be:

* Transparent
* Reusable
* Consistent across visuals

### Decision

Split KPI logic:

* **Python ETL** → structural aggregations only
* **Power BI DAX** → business logic and KPI definitions

Examples:

* Availability (%)
* SLA Gap (bps)
* Avg Downtime per Incident
* Days Below SLA

### Consequences

✅ Business logic visible to analysts

✅ Easy KPI iteration without ETL changes

⚠️ Requires DAX governance discipline

---

## ADR-006 — Dashboard Storytelling Structure (Page 1–3)

### Context

Different stakeholders require different levels of detail.

### Decision

Adopt a  **three-page storytelling structure** :

| Page   | Purpose                                         |
| ------ | ----------------------------------------------- |
| Page 1 | Executive overview (health & headline risk)     |
| Page 2 | Operational diagnostics & prioritization        |
| Page 3 | SLA compliance, breach duration & risk exposure |

### Consequences

✅ Clear narrative flow (awareness → diagnosis → risk)

✅ Reduced cognitive load

✅ Suitable for both demos and real operations

---

## ADR-007 — Metric Selection per Page

### Context

Some KPIs lose meaning when variance is low (e.g., Availability ≈ 99.48% everywhere).

### Decision

Metrics are  **context-aware** :

* Page 1: headline KPIs (Availability, SLA Status)
* Page 2: severity & frequency (Avg Downtime per Incident)
* Page 3: compliance sensitivity (SLA Gap in bps, Days Below SLA)

Uniform or non-differentiating metrics are **removed from visuals** but kept in the model.

### Consequences

✅ Visuals remain informative

✅ Avoids misleading comparisons

⚠️ Requires explaining metric removal to non-technical users

---

## ADR-008 — Visualization Principles

### Context

Incorrect chart selection leads to misinterpretation.

### Decision

Adopt strict visualization rules:

* Bar charts for categorical comparison
* Line charts for trends
* Scatter charts for multi-dimensional risk
* Tables only for action and investigation
* No pie or donut charts for SLA analytics

### Consequences

✅ Faster insight extraction

✅ Consistent UX across pages

✅ Executive-friendly visuals

---

## ADR-009 — Sorting & Prioritization Logic

### Context

Operational teams need a  **single, consistent prioritization signal** .

### Decision

Use **Avg Downtime per Incident (Minutes)** as the primary sorting metric on Page 2.

### Consequences

✅ Severity-driven prioritization

✅ Avoids bias from volume-only metrics

⚠️ Requires explanation to teams used to incident counts

---

## ADR-010 — Storytelling Documentation Strategy

### Context

Dashboard visuals alone are insufficient for portfolio and knowledge transfer.

### Decision

* **Markdown (`.md`) in GitHub** as source of truth
* **PDF export** for executive consumption
* Clear linking from `README.md`

### Consequences

✅ Versioned, reviewable documentation

Refer to diagrams in ([/docs/storytelling/](../storytelling/STORYTELLING_SUMMARY.md))

---

## ADR-011 — Tooling Choices

### Context

Solution must be practical, widely adoptable, and enterprise-relevant.

### Decision

* Python (ETL & automation)
* Pandas for data processing
* Power BI for semantic modeling & visualization
* GitHub for version control & documentation

### Consequences

✅ Low barrier to adoption

✅ Industry-standard tooling

⚠️ Vendor lock-in at visualization layer (accepted)

---

## ADR-012 — Portfolio Readiness

### Context

The project is intended as a  **professional portfolio artifact** .

### Decision

All components must:

* Be explainable end-to-end
* Follow industry naming conventions
* Include architecture, data, and storytelling documentation

### Consequences

✅ Demo Asset

✅ Demonstrates senior-level thinking

✅ Reusable as real-world blueprint
