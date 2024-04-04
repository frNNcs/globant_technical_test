from pydantic import BaseModel


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


class BerryStats(BaseModel):
    berries_names: list[str]
    min_growth_time: str
    median_growth_time: str
    max_growth_time: str
    variance_growth_time: str
    mean_growth_time: str
    frequency_growth_time: dict[int, int]
