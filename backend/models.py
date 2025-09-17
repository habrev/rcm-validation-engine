from sqlalchemy import Column, Integer, String, Float, Date, Text
from database import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    claim_id = Column(String)
    encounter_type = Column(String)
    service_date = Column(String)
    national_id = Column(String)
    member_id = Column(String)
    facility_id = Column(String)
    unique_id = Column(String)
    diagnosis_codes = Column(Text)
    service_code = Column(String)
    paid_amount_aed = Column(Float)
    approval_number = Column(String)
    status = Column(String)
    error_type = Column(String)
    error_explanation = Column(Text)
    recommended_action = Column(Text)
