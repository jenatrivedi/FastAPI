import uvicorn
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app=FastAPI(debug = True)

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000), # Path Parameter
    q: str = None, # Query Paramter
    item: Item = None, # Request Body
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
