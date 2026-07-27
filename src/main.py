from investigation_engine import InvestigationEngine

engine = InvestigationEngine()

# Total Comparison
result = engine.compare_totals(
    dashboard_total=1000000,
    source_total=1200000
)

print(result)

# Missing Records
missing = engine.detect_missing_records(
    dashboard_records=[1001, 1002, 1003],
    source_records=[1001, 1002, 1003, 1004, 1005]
)

print("Missing:", missing)

# Duplicates
duplicates = engine.detect_duplicates(
    [1001, 1002, 1003, 1002, 1004, 1001]
)

print("Duplicates:", duplicates)

# Report
report = engine.generate_report(
    result,
    missing,
    duplicates
)

print(report)