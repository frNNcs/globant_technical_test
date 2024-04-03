import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/allBerryStats")
async def read_root():
    results = httpx.get("https://pokeapi.co/api/v2/berry/?limit=500")
    results_json = results.json()

    if results.status_code != 200:
        return {
            'error': 'Could not retrieve data from the API'
        }

    berries_names_list = []
    berry_growth_times = []

    for berry_url, berry_name in ((r['url'], r['name']) for r in results_json['results']):
        berries_names_list.append(berry_name)
        id = berry_url.split('/')[-2]
        berry = httpx.get(f"https://pokeapi.co/api/v2/berry/{id}")
        berry_json = berry.json()
        berry_growth_times.append(berry_json['growth_time'])

    return {
        'berries_names': berries_names_list,
        'min_growth_time': min(berry_growth_times),
        'median_growth_time': sum(berry_growth_times) / len(berry_growth_times),
        'max_growth_time': max(berry_growth_times),
        'variance_growth_time': max(berry_growth_times) - min(berry_growth_times),
        'mean_growth_time': sum(berry_growth_times) / len(berry_growth_times),
        'frequency_growth_time': {i: berry_growth_times.count(i) for i in berry_growth_times},
    }
