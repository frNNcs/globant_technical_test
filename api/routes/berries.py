import asyncio
import collections

import httpx
from fastapi import APIRouter

from api.constants import ERRORS, POKEAPI_URL
from api.models.berry import BerryStats
from api.utils.api_utils import fetch_berry_growth_time
from api.utils.helpers import convert_hour_to_human_redable as _

router = APIRouter()


@router.get(
    "/allBerryStats",
    response_model=BerryStats,
    tags=["berries"],
    description="Get all berries stats! 🎉",
)
async def read_root():
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
