from .nouns import (SDMA, SDMI, SDF, SDN)
from .categories import (
    PROFESSION,
    PLACE,
    THING,
)


# TEN
sdma_nouns = [
    SDMA("lékař", "healer", PROFESSION),
    SDMA("herec", "actor", PROFESSION),
]


# TEN
sdmi_nouns = [
    SDMI("počitač", "computer", THING),
    SDMI("taliř", "plate", THING),
]


# TA
sdf_nouns = [
    SDF("restaurace", "restaurant", PLACE),
    SDF("slívovice", "horrible liquor", THING),
    SDF("kancelář", "office", PLACE),
    SDF("kuchyň", "kitchen", PLACE),
    SDF("ulice", "street", PLACE),
    SDF("píseň", "song", THING),
    SDF("židle", "chair", THING),
]


# TO
sdn_nouns = [
    SDN("letistě", "airport", PLACE),
    SDN("hřiště", "sportground", PLACE),
]
