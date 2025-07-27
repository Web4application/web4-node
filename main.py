from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/status")
def status():
    return {
        "block_height": 10234,
        "peers": 5,
        "faucet_supply": "945,000"
    }

class TxRequest(BaseModel):
    from_: str
    to: str
    amount: str
    gas: str
    private_key: str

@app.post("/sign")
def sign_tx(req: TxRequest):
    return { "signed_tx": f"signed({req.from_}→{req.to})" }
