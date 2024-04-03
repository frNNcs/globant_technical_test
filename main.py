import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/allBerryStats")
async def read_root():
    results = httpx.get("https://pokeapi.co/api/v2/berry/")
    if results.status_code != 200:
        return {
            'error': 'Could not retrieve data'
        }
    return {
        'berries_names': [
            result['name']
            for result
            in results.json()['results']
        ]
    }
