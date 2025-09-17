def apply_medical_rules(row):
    errors = []
    if 'Z99' in str(row.get('diagnosis_codes', '')):
        errors.append("Invalid diagnosis code Z99")
    if not row.get('service_code'):
        errors.append("Missing service code")
    return "; ".join(errors) if errors else None
