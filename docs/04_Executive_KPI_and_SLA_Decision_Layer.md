# Executive KPI & SLA Decision Layer

## 1. Purpose

Step 4 translates the technical data pipeline (Step 1–3) into business-ready insights and executive decision support.

This step focuses on:

- Executive KPIs
- SLA governance
- Risk and compliance visibility
- Apply-ready business storytelling

This layer is intentionally separated from ETL to keep the pipeline
flexible, auditable, and contract-aware.

---

## 2. Executive KPI Scope

The KPI set is intentionally minimal but complete, following telecom
industry best practices.

### 2.1 Core Executive KPIs

| KPI                | Description                 | Business Purpose             |
| ------------------ | --------------------------- | ---------------------------- |
| Availability (%)   | Network uptime ratio        | SLA compliance & reliability |
| Downtime (minutes) | Total service downtime      | Impact assessment            |
| Incident Count     | Number of service incidents | Operational stability        |
| Avg Latency (ms)   | Network response delay      | Customer experience          |
| Packet Loss (%)    | Data transmission loss      | Quality of service           |

These KPIs are calculated from raw fact tables created in Step 2 and processed through Step 3.

---

## 3. SLA Governance Model

### 3.1 SLA Target Dimension (`dim_sla_target`)

SLA targets are treated as business rules rather than hard-coded logic.

This enables:

- Contract-driven analytics
- Flexible SLA updates
- Historical accuracy

#### Conceptual Structure

| Column                  | Description                |
| ----------------------- | -------------------------- |
| sla_target_key          | Surrogate key              |
| service_key             | Related service            |
| availability_target_pct | SLA availability threshold |
| max_downtime_minutes    | Maximum allowed downtime   |
| max_latency_ms          | Latency threshold          |
| max_packet_loss_pct     | Packet loss threshold      |
| effective_start_date    | SLA validity start         |
| effective_end_date      | SLA validity end           |

This table belongs to the decision layer and is not required for ETL execution.

---

## 4. SLA Risk & Compliance Logic

### 4.1 SLA Status Definition

SLA status is derived dynamically based on KPI performance against SLA targets.

#### Conceptual Logic

```text
IF Availability < Availability_Target
   OR Downtime > Max_Downtime
   OR Avg_Latency > Max_Latency
THEN SLA_Status = "AT RISK"
ELSE SLA_Status = "ON TRACK"
```

---

## 5. Executive Dashboard Consumption

### 5.1 Primary Dashboard View

The executive dashboard is designed for quick decision-making:

**Top KPI Cards**

* Availability (%)
* SLA Status
* Downtime (minutes)
* Incident Count

**Trend Analysis**

* Availability trend (monthly)
* SLA risk trend

**Risk Breakdown**

* Top risk services
* Top risk regions
* Incident vs availability correlation

This layout ensures insights are readable within minutes.

---

## 6. Business Insight Narrative

Example executive insight:

> Network availability remains above SLA targets for most services.
>
> However, mobile services show increasing SLA risk driven by rising
>
> incident frequency, indicating a need for proactive capacity and
>
> vendor performance review.

This narrative bridges technical metrics and business action.

## 7. Step 4 Completion Status

| Area                     | Status    |
| ------------------------ | --------- |
| Executive KPI definition | Completed |
| SLA governance model     | Completed |
| Decision KPI logic       | Completed |
| Business storytelling    | Completed |

---

## 9. Final Notes

Step 4 intentionally avoids over-engineering. Its goal is to clearly demonstrate decision-making capability, not to replicate a full enterprise BI implementation.
