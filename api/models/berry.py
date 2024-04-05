import asyncio
import json
from typing import List, Union

import httpx
from pydantic import BaseModel

from api.config import CACHE_TIME, redis_client
from api.constants import POKEAPI_URL


class BaseAttribute(BaseModel):
    name: str
    url: str

    @property
    def id(self) -> int:
        return int(self.url.split("/")[-2])


class BerryItem(BaseAttribute):
    pass


class NaturalGiftType(BaseAttribute):
    pass


class BerryFirmness(BaseAttribute):
    pass


class BerryFlavor(BaseAttribute):
    pass


class BerryFlavorMap(BaseModel):
    flavor: BerryFlavor
    potency: int


class Berry(BaseModel):
    id: int
    firmness: BerryFirmness
    flavors: list[BerryFlavorMap]
    growth_time: int
    item: BerryItem
    max_harvest: int
    name: str
    natural_gift_power: int
    natural_gift_type: NaturalGiftType
    size: int
    smoothness: int
    soil_dryness: int

    def __str__(self):
        return self.name

    @property
    def url(self) -> str:
        return f"{POKEAPI_URL}/berry/{self.id}/"

    @classmethod
    def create_from_str(cls, string: str) -> "Berry":
        """Create a berry object from a string.

        Args:
            string (str): The string to create the berry object from.

        Returns:
            Berry: The berry object.
        """

        return cls(**json.loads(string))

    @classmethod
    async def cache_get_by_id(cls, id: int) -> "Berry":
        """Get a berry by its id from the cache.

        Returns:
            dict: The berry object.
        """
        berry: Union[str, None] = await redis_client.get(f"berry:{id}")  # type: ignore

        if berry is not None:
            return Berry.create_from_str(berry)   # type: ignore
        else:
            berry_aux = await cls.get_by_id(id)

            await redis_client.set(  # type: ignore
                f"berry:{id}",
                berry_aux.json(),
                ex=CACHE_TIME
            )
            return berry_aux

    @classmethod
    async def get_by_id(cls, id: int) -> "Berry":
        """Get a berry by its id.

        Args:
            id (int): The id of the berry.

        Raises:
            ValueError: If the berry could not be parsed.

        Returns:
            Berry: The berry object.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{POKEAPI_URL}/berry/{id}/")
            response.raise_for_status()

            try:
                berry = Berry(**response.json())
            except Exception:
                raise ValueError(f"Could not parse berry with id {id}")
            return berry

    @classmethod
    async def get_by_id__in(cls, id_list: List[int]) -> list["Berry"]:
        """Get a list of berries by their ids.

        Args:
            id_list (List[int]): A list of berry ids.

        Returns:
            list[Berry]: A list of berry objects.
        """
        tasks = [cls.cache_get_by_id(id) for id in id_list]
        return await asyncio.gather(*tasks)

    @classmethod
    async def get_all(cls) -> List["Berry"]:
        """Get all berries from the PokeAPI.

        Raises:
            ValueError: Could not parse berries.

        Returns:
            List[Berry]: A list of berry objects.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{POKEAPI_URL}/berry/?limit=500")
                response.raise_for_status()

                berry_url = [berry['url'] for berry in response.json()["results"]]
                berry_ids = [int(berry_id.split("/")[-2]) for berry_id in berry_url]

                return await cls.get_by_id__in(berry_ids)

        except Exception as e:
            raise ValueError(f"Could not parse berries: {e}")

    @classmethod
    async def clear_cache(cls):
        """Clear the cache of all berries."""
        await redis_client.delete("berry:*")  # type: ignore
        return True


class BerryStats(BaseModel):
    berries_names: list[str]
    min_growth_time: str
    median_growth_time: str
    max_growth_time: str
    variance_growth_time: str
    mean_growth_time: str
    frequency_growth_time: dict[int, int]
