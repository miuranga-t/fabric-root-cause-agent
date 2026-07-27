class InvestigationEngine:

    def compare_totals(self, dashboard_total, source_total):

        difference = source_total - dashboard_total

        return {
            "dashboard_total": dashboard_total,
            "source_total": source_total,
            "difference": difference
        }

    def detect_missing_records(
        self,
        dashboard_records,
        source_records
    ):

        missing = []

        for record in source_records:
            if record not in dashboard_records:
                missing.append(record)

        return missing

    def detect_duplicates(self, records):

        seen = []
        duplicates = []

        for record in records:

            if record in seen and record not in duplicates:
                duplicates.append(record)

            seen.append(record)

        return duplicates

    def analyze_root_cause(
        self,
        missing_records,
        duplicate_records
    ):

        causes = []

        if len(missing_records) > 0:
            causes.append("Missing transactions detected.")

        if len(duplicate_records) > 0:
            causes.append("Duplicate transactions detected.")

        if len(causes) == 0:
            causes.append("No obvious root cause detected.")

        return causes

    def calculate_impact(
        self,
        missing_records,
        duplicate_records
    ):

        return {
            "missing_count": len(missing_records),
            "duplicate_count": len(duplicate_records)
        }

    def calculate_financial_impact(
        self,
        source_df,
        missing_records
    ):

        impact = source_df[
            source_df["invoice_id"].isin(missing_records)
        ]["amount"].sum()

        return impact

    def calculate_confidence_score(
        self,
        missing_records,
        duplicate_records
    ):

        score = 100

        if len(missing_records) > 0:
            score -= 5

        if len(duplicate_records) > 0:
            score -= 5

        if score < 0:
            score = 0

        return score

    def generate_report(
        self,
        total_result,
        causes,
        impact,
        financial_impact,
        confidence
    ):

        report = f"""
====================================
INVESTIGATION REPORT
====================================

Dashboard Total      : {total_result['dashboard_total']}
Source Total         : {total_result['source_total']}
Difference           : {total_result['difference']}

Missing Count        : {impact['missing_count']}
Duplicate Count      : {impact['duplicate_count']}

Financial Impact     : {financial_impact}

Root Causes:
"""

        for cause in causes:
            report += f"\n- {cause}"

        report += f"""

Confidence Score     : {confidence}%

Recommendation:
Review missing invoices and duplicate transactions.

====================================
"""

        return report