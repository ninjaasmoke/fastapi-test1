from typing import Dict, Annotated, Optional, Any
from pydantic import BaseModel, Extra
from fastapi import FastAPI, Header
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/create", response_model=Dict)
async def create(
    ticket: Optional[Any],
    x_sero_api_token: str = Header(None),
) -> Dict:
    if ticket is not None and isinstance(ticket, str):
        ticket_dict = json.loads(ticket)
        return {"data": data_dict.data}
    return {"data": ticket.data}
