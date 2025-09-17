import pandas as pd
from database import SessionLocal
from models import Claim
from rules.technical_rules import apply_technical_rules
from rules.medical_rules import apply_medical_rules
from llm_validator import evaluate_with_llm

def process_claims(file_path):
    df = pd.read_excel(file_path)
    db = SessionLocal()

    for _, row in df.iterrows():
        row = row.to_dict()
        tech_err = apply_technical_rules(row)
        med_err = apply_medical_rules(row)
        llm_eval = evaluate_with_llm(row)

        error_type = []
        explanation = []
        if tech_err:
            error_type.append("Technical error")
            explanation.append(tech_err)
        if med_err:
            error_type.append("Medical error")
            explanation.append(med_err)
        if not error_type:
            error_type.append("No error")

        claim = Claim(
            claim_id=row.get('claim_id'),
            encounter_type=row.get('encounter_type'),
            service_date=row.get('service_date'),
            national_id=row.get('national_id'),
            member_id=row.get('member_id'),
            facility_id=row.get('facility_id'),
            unique_id=row.get('unique_id'),
            diagnosis_codes=row.get('diagnosis_codes'),
            service_code=row.get('service_code'),
            paid_amount_aed=row.get('paid_amount_aed'),
            approval_number=row.get('approval_number'),
            status="Validated" if not tech_err and not med_err else "Not validated",
            error_type=" / ".join(error_type),
            error_explanation="; ".join(explanation + [llm_eval.get('reason', '')]),
            recommended_action=llm_eval.get('action', 'Check claim details')
        )
        db.add(claim)
    db.commit()
    db.close()
