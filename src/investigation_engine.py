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

    def generate_report(
        self,
        total_result,
        missing_records,
        duplicate_records
    ):

        report = f"""
Investigation Report

Dashboard Total : {total_result['dashboard_total']}
Source Total    : {total_result['source_total']}
Difference      : {total_result['difference']}

Missing Records :
{missing_records}

Duplicate Records :
{duplicate_records}
"""

        return report

    def analyze_root_cause(
        self,
        missing_records,
        duplicate_records
    ):

        causes = []

        if len(missing_records) > 0:
            causes.append(
                "Missing transactions detected."
            )

        if len(duplicate_records) > 0:
            causes.append(
                "Duplicate transactions detected."
            )

        if len(causes) == 0:
            causes.append(
                "No obvious root cause detected."
            )

        return causes