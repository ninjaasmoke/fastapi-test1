from typing import Dict, Annotated, Optional, Any
from pydantic import BaseModel, Extra
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

class Ticket(BaseModel):
    workflow_id: str
    data: Optional[Dict[str, Optional[str]]]

@app.post("/create", response_model=Dict)
async def create(
    ticket: Ticket,
    x_sero_api_token: str = Header(None),
) -> Dict:
    return {"workflow_id": ticket.workflow_id, "data": ticket.data}
