# api/main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class WalletQuery(BaseModel):
    command: str
    user_id: str

@app.post("/assistant")
async def respond_to_query(query: WalletQuery):
    if "balance" in query.command.lower():
        return {"response": "You have 1,250 FDAK. Market’s up today 🚀"}
    elif "swap" in query.command.lower():
        return {"response": "Swapped 100 FDAK for 92 FX. 💱"}
    elif "smart contract" in query.command.lower():
        return {"response": "A smart contract enforces rules autonomously. Want to write one?"}
    else:
        return {"response": "I'm not sure yet, Kubu! Want to try another question?"}
