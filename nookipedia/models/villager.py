import typing as _t

from pydantic import BaseModel, Field


class NHDetails(BaseModel):
    image_url: str
    photo_url: str
    icon_url: str
    quote: str
    sub_personality: str = Field(alias="sub-personality")
    catchphrase: str
    clothing: str
    clothing_variation: str
    fav_styles: _t.List[str]
    fav_colors: _t.List[str]
    hobby: str
    house_interior_url: str
    house_exterior_url: str
    house_wallpaper: str
    house_flooring: str
    house_music: str
    house_music_note: _t.Optional[str]


class Villager(BaseModel):
    id: _t.Optional[str]
    url: str
    name: str
    alt_name: _t.Optional[str]
    title_color: _t.Optional[str]
    text_color: _t.Optional[str]
    image_url: str
    species: str
    personality: str
    gender: str
    birthday: _t.Optional[str]
    sign: str
    quote: _t.Optional[str]
    phrase: str
    prev_phrases: _t.List[str]
    clothing: str
    islander: bool
    debut: str
    appearances: _t.List[str]
    nh_details: _t.Optional[NHDetails]
