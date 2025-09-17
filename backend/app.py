from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from models import Claim
from pipeline import process_claims
import shutil
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/api/upload")
def upload(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    process_claims(temp_path)
    os.remove(temp_path)
    return {"message": "File processed"}

@app.get("/api/claims")
def get_claims():
    db = SessionLocal()
    claims = db.query(Claim).all()
    db.close()
    return [c.__dict__ for c in claims]

@app.get("/api/metrics")
def get_metrics():
    db = SessionLocal()
    rows = db.query(Claim).all()
    db.close()
    # Aggregate error_type counts and amounts
    result = {}
    for r in rows:
        cat = r.error_type
        if cat not in result:
            result[cat] = {"count": 0, "amount": 0}
        result[cat]["count"] += 1
        result[cat]["amount"] += r.paid_amount_aed or 0
    labels = list(result.keys())
    counts = [v["count"] for v in result.values()]
    amounts = [v["amount"] for v in result.values()]
    return {"labels": labels, "counts": counts, "amounts": amounts}
