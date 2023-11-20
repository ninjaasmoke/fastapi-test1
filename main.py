from typing import Dict, Annotated, Optional

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/create", response_model=Dict)
async def create(
    workflow_id: str,
    ticket: Dict,
    x_sero_api_token: Annotated[str, Header()] = None,
) -> Dict:
    return ticket
