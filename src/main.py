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

# Convert sale_date to datetime
dashboard_df["sale_date"] = pd.to_datetime(
    dashboard_df["sale_date"]
)

source_df["sale_date"] = pd.to_datetime(
    source_df["sale_date"]
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

# Missing Records
missing = engine.detect_missing_records(
    dashboard_records,
    source_records
)

# Duplicate Records
duplicates = engine.detect_duplicates(
    dashboard_records
)

# Financial Impact
financial_impact = engine.calculate_financial_impact(
    source_df,
    missing
)

# Date Validation
date_validation = engine.validate_date_range(
    dashboard_df,
    source_df
)

# Refresh Validation
refresh_validation = engine.validate_refresh_status(
    dashboard_df,
    source_df
)

# Root Cause Analysis
root_cause_analysis = engine.analyze_root_cause(
    missing,
    duplicates,
    financial_impact
)

# Impact Analysis
impact = engine.calculate_impact(
    missing,
    duplicates
)

# Confidence Score
confidence = engine.calculate_confidence_score(
    missing,
    duplicates
)

# Report
report = engine.generate_report(
    result,
    root_cause_analysis,
    impact,
    financial_impact,
    confidence,
    date_validation
)

print(report)

print("\nREFRESH VALIDATION")
print("-------------------")
print(
    "Dashboard Last Date:",
    refresh_validation["dashboard_last_date"]
)
print(
    "Source Last Date:",
    refresh_validation["source_last_date"]
)
print(
    "Issue:",
    refresh_validation["issue"]
)