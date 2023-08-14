from . import (SDMA, SDMI, SDF, SDN)
from .nouns import Noun
from .categories import (
    PROFESSION,
    PLACE,
    THING,
)


# TEN
sdma_nouns = [
    Noun("lékař", "healer", SDMA, PROFESSION),
]


# TEN
sdmi_nouns = [
    Noun("počitač", "computer", SDMI, THING),
    Noun("taliř", "plate", SDMI, THING),
]


# TA
sdf_nouns = [
    Noun("restaurace", "restaurant", SDF, PLACE),
    Noun("slívovice", "horrible liquor", SDF, THING),
    Noun("kancelář", "office", SDF, PLACE),
    Noun("kuchyň", "kitchen", SDF, PLACE),
    Noun("ulice", "street", SDF, PLACE),
    Noun("píseň", "song", SDF, THING),
    Noun("židle", "chair", SDF, THING),
]


# TO
sdn_nouns = [
    Noun("letistě", "airport", SDN, PLACE),
]
