from .nouns import (TDMA, TDF, TDN)
from .categories import (
    EMOTION,
    PERSON,
    PLACE,
    PROFESSION,
    THING,
)


# TEN
tdma_nouns = [
    TDMA("kolega", "colleague", PERSON),
    TDMA("klavírista", "pianist", PROFESSION),
]


# TA
tdf_nouns = [
    TDF("místnost", "room", PLACE),
    TDF("radost", "joy", EMOTION),
]


# TO
tdn_nouns = [
    TDN("nádraží", "station", PLACE),
    TDN("náměstí", "square", PLACE),
    TDN("topení", "heater", THING),
]
