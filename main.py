from fastapi import FastAPI
import uvicorn
from devopslib.logic import search_wiki
from devopslib.logic import wiki as wikilogic
from devopslib.logic import phrase as wikiphrase

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "wikipedia API. call /search or /wiki"}

@app.get("/search/{value}")
async def search(value: str):
    result = search_wiki(value)
    return {"result": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    result = wikilogic(name)
    return {"result":result}

@app.get("/phrase/{name}")
async def phrase(name: str):
    result = wikiphrase(name)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

