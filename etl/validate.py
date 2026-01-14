from typing import Dict, Any, List
import pandas as pd
from config.app_config import LATENCY_MAX_MS, PACKET_LOSS_MAX_PCT


def validate_network_kpi(
    df: pd.DataFrame,
    grain_columns: List[str]
) -> Dict[str, Any]:
    """
    Data Quality validation with rule severity.
    """

    rules = []
    violations = []

    def add_violation(rule_id, severity, message):
        violations.append({
            "rule_id": rule_id,
            "severity": severity,
            "message": message
        })

    # RULE 1 — CRITICAL
    rules.append(("no_null_grain_keys", "CRITICAL"))
    if df[grain_columns].isnull().any().any():
        add_violation(
            "no_null_grain_keys",
            "CRITICAL",
            "Null values detected in grain columns."
        )

    # RULE 2 — CRITICAL
    rules.append(("no_duplicate_grain", "CRITICAL"))
    if df.duplicated(subset=grain_columns).any():
        add_violation(
            "no_duplicate_grain",
            "CRITICAL",
            f"Duplicate records at grain {grain_columns}"
        )

    # RULE 3 — WARNING
    rules.append(("latency_range", "WARNING"))
    if (
        (df["avg_latency_ms"] < 0).any()
        or (df["avg_latency_ms"] > LATENCY_MAX_MS).any()
    ):
        add_violation(
            "latency_range",
            "WARNING",
            f"Latency out of range (0–{LATENCY_MAX_MS} ms)."
        )

    # RULE 4 — WARNING
    rules.append(("packet_loss_range", "WARNING"))
    if (
        (df["packet_loss_pct"] < 0).any()
        or (df["packet_loss_pct"] > PACKET_LOSS_MAX_PCT).any()
    ):
        add_violation(
            "packet_loss_range",
            "WARNING",
            f"Packet loss out of range (0–{PACKET_LOSS_MAX_PCT}%)."
        )

    total_rules = len(rules)
    failed_rules = len(violations)

    critical_failures = [
        v for v in violations if v["severity"] == "CRITICAL"
    ]

    coverage_pct = round(
        ((total_rules - failed_rules) / total_rules) * 100, 2
    )

    return {
        "passed": len(critical_failures) == 0,
        "total_rules": total_rules,
        "failed_rules": failed_rules,
        "critical_failures": len(critical_failures),
        "warning_failures": failed_rules - len(critical_failures),
        "coverage_pct": coverage_pct,
        "violations": violations
    }
