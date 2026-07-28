import pandas as pd
from investigation_engine import InvestigationEngine

engine = InvestigationEngine()

print("====================================")
print("FABRIC ROOT CAUSE AGENT")
print("====================================")

# User Input
dashboard_file = input(
    "Enter Dashboard Excel File Path: "
)

source_file = input(
    "Enter Source Excel File Path: "
)

# Read Excel files
dashboard_df = pd.read_excel(
    dashboard_file,
    engine="openpyxl"
)

source_df = pd.read_excel(
    source_file,
    engine="openpyxl"
)

# Convert dates
dashboard_df["sale_date"] = pd.to_datetime(
    dashboard_df["sale_date"]
)

source_df["sale_date"] = pd.to_datetime(
    source_df["sale_date"]
)

# Convert invoice column to lists
dashboard_records = dashboard_df["invoice_id"].tolist()
source_records = source_df["invoice_id"].tolist()

# Sales totals
dashboard_sales = dashboard_df["amount"].sum()
source_sales = source_df["amount"].sum()

# Compare totals
result = engine.compare_totals(
    dashboard_total=dashboard_sales,
    source_total=source_sales
)

# Missing records
missing = engine.detect_missing_records(
    dashboard_records,
    source_records
)

# Duplicate records
duplicates = engine.detect_duplicates(
    dashboard_records
)

# Financial impact
financial_impact = engine.calculate_financial_impact(
    source_df,
    missing
)

# Date validation
date_validation = engine.validate_date_range(
    dashboard_df,
    source_df
)

# Refresh validation
refresh_validation = engine.validate_refresh_status(
    dashboard_df,
    source_df
)

# Root cause analysis
root_cause_analysis = engine.analyze_root_cause(
    missing,
    duplicates,
    financial_impact
)

# Impact analysis
impact = engine.calculate_impact(
    missing,
    duplicates
)

# Confidence score
confidence = engine.calculate_confidence_score(
    missing,
    duplicates
)

# Investigation summary
summary = engine.generate_summary(
    impact,
    financial_impact,
    confidence,
    date_validation,
    refresh_validation
)

print("\n====================================")
print("INVESTIGATION SUMMARY")
print("====================================")

print(
    "Risk Level       :",
    summary["risk_level"]
)

print(
    "Financial Impact :",
    summary["financial_impact"]
)

print(
    "Confidence Score :",
    f"{summary['confidence']}%"
)

print("\nKey Findings:")

for finding in summary["key_findings"]:
    print("-", finding)

print("\n====================================")

# Detailed Report
report = engine.generate_report(
    result,
    root_cause_analysis,
    impact,
    financial_impact,
    confidence,
    date_validation
)

print(report)

# Export DOCX Report
output_file = engine.export_report_to_docx(
    summary,
    report,
    "output/investigation_report.docx"
)

print()
print("DOCX Report Exported:")
print(output_file)

# Refresh Validation
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