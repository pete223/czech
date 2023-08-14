from . import (TDMA, TDF, TDN)
from .nouns import Noun
from .categories import (
    EMOTION,
    PERSON,
    PLACE,
    PROFESSION,
    THING,
)


# TEN
tdma_nouns = [
    Noun("kolega", "colleague", TDMA, PERSON),
]


# TA
tdf_nouns = [
    Noun("místnost", "room", TDF, PLACE),
    Noun("radost", "joy", TDF, EMOTION),
]


# TO
tdn_nouns = [
    Noun("nádraží", "station", TDN, PLACE),
    Noun("náměstí", "square", TDN, PLACE),
]
