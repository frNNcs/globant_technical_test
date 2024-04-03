import asyncio
import collections

import httpx
from fastapi import FastAPI

app = FastAPI()


class ERRORS:
    COULD_NOT_RETRIEVE_DATA = 'Could not retrieve data from the API'


POKEAPI_URL = "https://pokeapi.co/api/v2"


@app.get("/allBerryStats")
async def read_root():
    async def fetch_berry_growth_time(id: int):
        async with httpx.AsyncClient() as client:
            berry = await client.get(f"{POKEAPI_URL}/berry/{id}/")
            berry.raise_for_status()
            return berry.json()['growth_time']

    def _(hour: float) -> str:
        if hour > 24:
            return f"{hour // 24} days and {hour % 24} hours"
        else:
            return f"{hour} hours"

    berries_names_list = []
    request_tasks = []

    results = httpx.get(f"{POKEAPI_URL}/berry/?limit=500")

    if results.status_code != 200:
        return {
            'error': ERRORS.COULD_NOT_RETRIEVE_DATA
        }

    for berry_url, berry_name in (
        (r['url'], r['name']) for r in results.json()['results']
    ):
        berry_id = berry_url.split('/')[-2]
        berry_growth_time = fetch_berry_growth_time(berry_id)

        request_tasks.append(berry_growth_time)
        berries_names_list.append(berry_name)

    berry_growth_times = await asyncio.gather(*request_tasks)

    return {
        'berries_names': berries_names_list,
        'min_growth_time': _(min(berry_growth_times)),
        'median_growth_time': _(sum(berry_growth_times) / len(berry_growth_times)),
        'max_growth_time': _(max(berry_growth_times)),
        'variance_growth_time': _(max(berry_growth_times) - min(berry_growth_times)),
        'mean_growth_time': _(sum(berry_growth_times) / len(berry_growth_times)),
        'frequency_growth_time': dict(collections.OrderedDict({
            time: berry_growth_times.count(time)
            for time in berry_growth_times
        }))
    }
