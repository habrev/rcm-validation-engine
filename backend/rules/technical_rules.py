def apply_technical_rules(row):
    errors = []
    if not row.get('approval_number'):
        errors.append("Missing approval number")
    if row.get('paid_amount_aed', 0) > 5000:
        errors.append("Paid amount exceeds technical threshold (5000)")
    return "; ".join(errors) if errors else None
