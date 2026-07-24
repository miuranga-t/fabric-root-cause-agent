from investigation_engine import InvestigationEngine

engine = InvestigationEngine()

result = engine.compare_totals(
    dashboard_total=1000000,
    source_total=1200000
)

print(result)
