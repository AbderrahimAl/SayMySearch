from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .es_connection import client


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"))

templates = Jinja2Templates(directory=".")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


@app.get("/search", status_code=status.HTTP_200_OK)
def search(query: str):

    search_params =  { 
            "query": {
                "multi_match": {
                "query": query,
                "operator": "and", 
                "type": "bool_prefix", 
                "fuzziness": "auto", 
                "fields": [
                    "club_name"
                    ]
                }
            }
            }
    
    response = client.search(index="clubs_index", **search_params)
    return [res["_source"]["club_name"] for res in response["hits"]["hits"]]