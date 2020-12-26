import uvicorn
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# max min length and regular expression validation ,default value (put value instead of ... this)and optional parameter(put None instead of ... this)
@app.get("/items/")
async def get_items(item_id: str = Query(..., min_length = 2, max_length = 10, regex="^Item\d{1,6}")):#... means required value
    return {"item": item_id}

@app.get("/items/")
async def get_items(item_id: List[str] = Query(["Pen", "Pencil"], # list as a parameter
                                               title = "Item List", # metadata
                                               description = "List of items to be returned.",# metadata
                                               min_length = 2, max_length = 10, deprecated = True, # depricarting parameters
                                               alias = "item-id")): # Alias name
    results = {"items": item_id}
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
