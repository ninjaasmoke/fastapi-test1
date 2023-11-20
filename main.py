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

class Ticket(BaseModel):
    workflow_id: str
    data: Optional[Any]

@app.post("/create", response_model=Dict)
async def create(
    ticket: Ticket,
    x_sero_api_token: str = Header(None),
) -> Dict:
    if isinstance(ticket.data, str):
        data_dict = json.loads(ticket.data)
        return {"workflow_id": data_dict.workflow_id, "data": data_dict.data}
    return {"workflow_id": ticket.workflow_id, "data": ticket.data}
