from fastapi import FastAPI, status
from .es_connection import client


app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def search(query: str):

    search_params = {
    "query": {
        "match": {
            "club_name": {
                "query": query,
                "fuzziness": "AUTO",
                "operator": "and"
                }
            }
        }
    }

    results = client.search(index="clubs_index", **search_params)

    return results