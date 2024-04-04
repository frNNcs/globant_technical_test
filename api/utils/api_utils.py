import httpx

from api.constants import POKEAPI_URL
from api.models.berry import Berry


async def fetch_berry(id: int) -> Berry:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{POKEAPI_URL}/berry/{id}/")
        response.raise_for_status()

        try:
            berry = Berry(**response.json())
        except Exception:
            raise ValueError(f"Could not parse berry with id {id}")
        return berry


async def fetch_berry_growth_time(id: int) -> int:
    berry = await fetch_berry(id)
    return berry.growth_time
