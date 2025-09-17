def evaluate_with_llm(row):
    # Stubbed for now — replace with OpenAI/LLM later
    if row.get('paid_amount_aed', 0) > 10000:
        return {"reason": "High amount needs review", "action": "Request pre-approval confirmation"}
    return {"reason": "Amount is within range", "action": "Approve claim"}
