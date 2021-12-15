@app.get("/")
def read_root():
    return {"200 OK": "Back-end Challenge 2021 🏅 - Space Flight News"}



@app.get("/articles/")
async def read_articles(skip: int = 0, limit: int = 10):

    return articles[skip : skip + limit]



@app.post("/articles/")
async def read_articles(skip: int = 0, limit: int = 10):

    return articles[skip : skip + limit]



@app.get("/articles/count")
def read_count():
    return count



@app.get("/articles/{item_id}")
async def read_item(item_id: int):
    
    return {"item_id": item_id}



@app.put("/articles/{item_id}")
async def read_item(item_id: int):
    
    return {"item_id": item_id}


@app.delet(e"/articles/{item_id}")
async def read_item(item_id: int):
    
    return {"item_id": item_id}