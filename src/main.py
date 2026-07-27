import pandas as pd
from investigation_engine import InvestigationEngine

engine = InvestigationEngine()

# Read CSV files
dashboard_df = pd.read_csv("data/dashboard.csv")
source_df = pd.read_csv("data/source.csv")

# Convert invoice_id column to lists
dashboard_records = dashboard_df["invoice_id"].tolist()
source_records = source_df["invoice_id"].tolist()

# Compare totals
result = engine.compare_totals(
    dashboard_total=len(dashboard_records),
    source_total=len(source_records)
)

print(result)

# Missing Records
missing = engine.detect_missing_records(
    dashboard_records,
    source_records
)

print("Missing:", missing)

# Duplicate Records
duplicates = engine.detect_duplicates(
    dashboard_records
)

print("Duplicates:", duplicates)

# Root Cause Analysis
causes = engine.analyze_root_cause(
    missing,
    duplicates
)

print("Root Causes:")
print(causes)

# Impact Analysis
impact = engine.calculate_impact(
    missing,
    duplicates
)

print("Impact Analysis:")
print(impact)

# Financial Impact
financial_impact = engine.calculate_financial_impact(
    source_df,
    missing
)

print("Financial Impact:")
print(financial_impact)

# Confidence Score
confidence = engine.calculate_confidence_score(
    missing,
    duplicates
)

print("Confidence Score:")
print(f"{confidence}%")

# Professional Investigation Report
report = engine.generate_report(
    result,
    causes,
    impact,
    financial_impact,
    confidence
)

print(report)