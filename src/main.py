import pandas as pd
from investigation_engine import InvestigationEngine

engine = InvestigationEngine()

# Read Excel files
dashboard_df = pd.read_excel(
    "data/dashboard.xlsx",
    engine="openpyxl"
)

source_df = pd.read_excel(
    "data/source.xlsx",
    engine="openpyxl"
)

# Convert invoice_id column to lists
dashboard_records = dashboard_df["invoice_id"].tolist()
source_records = source_df["invoice_id"].tolist()

# Sales Amount Totals
dashboard_sales = dashboard_df["amount"].sum()
source_sales = source_df["amount"].sum()

# Compare Sales Totals
result = engine.compare_totals(
    dashboard_total=dashboard_sales,
    source_total=source_sales
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