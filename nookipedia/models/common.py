import typing as _t
from pydantic import BaseModel


class Availability(BaseModel):
    months: str
    time: str


class Hemisphere(BaseModel):
    availability_array: _t.List[Availability]
    times_by_month: _t.Dict[str, str]
    months: str
    months_array: _t.List[int]


class CommonCritter(BaseModel):
    url: str
    name: str
    image_url: str
    catchphrases: _t.List[str]
    time: _t.Optional[str]
    location: str
    rarity: str
    total_catch: int
    sell_nook: int
    tank_width: int
    tank_length: int
    north: Hemisphere
    south: Hemisphere
