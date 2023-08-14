from . import FDMA, FDMI, FDF, FDN
from .nouns import Noun

from .categories import (
    ANIMAL,
    PROFESSION,
    PLACE,
    PERSON,
    FOOD,
    THING,
    VEHICLE,
)


# TEN
fdma_nouns = [
    Noun("doktor", "doctor", FDMA, PROFESSION),
    Noun("pan", "old man", FDMA, PERSON),
    Noun("muž", "young man", FDMA, PERSON),
    Noun("pes", "dog", FDMA, ANIMAL),
]


# TEN
fdmi_nouns = [
    Noun("obchod", "shop", FDMI, PLACE),
    Noun("telefon", "telephone", FDMI, THING),
    Noun("obývák", "living room", FDMI, PLACE),
    Noun("stůl", "table", FDMI, THING),
    Noun("dům", "house", FDMI, PLACE),
    Noun("sešit", "notebook", FDMI, THING),
    Noun("most", "bridge", FDMI, PLACE),
    Noun("hrad", "castle", FDMI, PLACE),
]


# TA
fdf_nouns = [
    Noun("žena", "woman", FDF, PERSON),
    Noun("škola", "school", FDF, PLACE),
    Noun("sušenka", "biscuit", FDF, FOOD),
    Noun("tužka", "pencil", FDF, THING),
    Noun("cesta", "road", FDF, PLACE),
    Noun("lampa", "lamp", FDF, THING),
    Noun("maminka", "mother", FDF, PERSON)
]


# TO
fdn_nouns = [
    Noun("auto", "car", FDN, VEHICLE),
    Noun("kino", "cinema", FDN, PLACE),
    Noun("křeslo", "chair", FDN, THING),
    Noun("radio", "radio", FDN, THING),
    Noun("město", "city", FDN, PLACE),
]
