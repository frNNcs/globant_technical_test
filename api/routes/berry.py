import collections

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from api.constants import ERRORS
from api.models.berry import Berry, BerryStats
from api.utils.helpers import convert_hour_to_human_redable as _

router = APIRouter()


@router.get(
    "/allBerryStats",
    tags=["berries"],
    response_model=BerryStats,
    summary="Get all berries stats! 🎉",
)
async def get_all_berry_stats() -> JSONResponse:
    """
    Get all berries stats from the PokeAPI and calculate some statistics.

    - **berries_names**: list of all berries names.
    - **min_growth_time**: minimum growth time of all berries.
    - **median_growth_time**: median growth time of all berries.
    - **max_growth_time**: maximum growth time of all berries.
    - **variance_growth_time**: variance growth time of all berries.
    - **mean_growth_time**: mean growth time of all berries.
    - **frequency_growth_time**: frequency of growth time of all berries.

    """
    berries_names_list : list[str] = []

    try:
        all_berries = await Berry.get_all()

    except Exception:
        return JSONResponse(
            content=jsonable_encoder({
                'error': ERRORS.COULD_NOT_RETRIEVE_DATA
            }),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    berries_names_list : list[str] = [berry.name for berry in all_berries]

    berry_growth_times : list[int] = [berry.growth_time for berry in all_berries]

    berries_stats = BerryStats(
        berries_names=berries_names_list,
        min_growth_time=_(min(berry_growth_times)),
        median_growth_time=_(sum(berry_growth_times) / len(berry_growth_times)),
        max_growth_time=_(max(berry_growth_times)),
        variance_growth_time=_(max(berry_growth_times) - min(berry_growth_times)),
        mean_growth_time=_(sum(berry_growth_times) / len(berry_growth_times)),
        frequency_growth_time=dict(collections.OrderedDict({
            time: berry_growth_times.count(time)
            for time in berry_growth_times
        }))
    )

    return JSONResponse(
        content=jsonable_encoder(berries_stats),
        status_code=status.HTTP_200_OK
    )


@router.get(
    "/berry/{id}",
    tags=["berries"],
    response_model=Berry,
    summary="Get a berry by its id! 🍓"
)
async def get_berry_by_id(id: int) -> JSONResponse:
    """
    Get a berry by its id from redis cache.

    - **id**: The id of the berry.

    """
    try:
        berry = await Berry.cache_get_by_id(id)

    except Exception:
        return JSONResponse(
            content=jsonable_encoder({
                'error': ERRORS.COULD_NOT_RETRIEVE_DATA
            }),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return JSONResponse(
        content=jsonable_encoder(berry),
        status_code=status.HTTP_200_OK
    )
