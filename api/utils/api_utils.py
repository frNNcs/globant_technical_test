from api.models.berry import Berry


async def fetch_berry_growth_time(id: int) -> int:
    berry = await Berry.get_by_id(id)
    return berry.growth_time
