import httpx

from api.constants import POKEAPI_URL


async def fetch_berry_growth_time(id: int):
    async with httpx.AsyncClient() as client:
        berry = await client.get(f"{POKEAPI_URL}/berry/{id}/")
        berry.raise_for_status()
        return berry.json()['growth_time']
