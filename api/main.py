from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import openai

app = FastAPI()

# User settings (mocked for now)
user_preferences = {
    "kubu123": {"nickname": "Captain Kubu", "voice_mode": True}
}

class WalletQuery(BaseModel):
    command: str
    user_id: str

def personalize_response(user_id, reply):
    prefs = user_preferences.get(user_id, {})
    if prefs.get("nickname"):
        reply = f"{prefs['nickname']}, {reply}"
    return reply

@app.post("/assistant")
async def respond_to_query(query: WalletQuery):
    prompt = query.command
    # GPT response
    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a helpful wallet assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    response = gpt_response.choices[0].message.content
    final_response = personalize_response(query.user_id, response)
    return {"response": final_response}

@app.post("/sign")
async def sign_tx(request: Request):
    tx_data = await request.json()
    result = requests.post("http://localhost:8545/sign", json=tx_data)
    return result.json()
