from .nouns import (FDMA, FDMI, FDF, FDN)

from .categories import (
    ANIMAL,
    CLOTHES,
    PROFESSION,
    PLACE,
    PERSON,
    FOOD,
    THING,
    VEHICLE,
)


# TEN
fdma_nouns = [
    FDMA("doktor", "doctor", PROFESSION),
    FDMA("pan", "old man", PERSON),
    FDMA("muž", "young man", PERSON),
    FDMA("pes", "dog", ANIMAL),
]


# TEN
fdmi_nouns = [
    FDMI("obchod", "shop", PLACE),
    FDMI("telefon", "telephone", THING),
    FDMI("obývák", "living room", PLACE),
    FDMI("stůl", "table", THING),
    FDMI("dům", "house", PLACE),
    FDMI("sešit", "notebook", THING),
    FDMI("most", "bridge", PLACE),
    FDMI("hrad", "castle", PLACE),
    FDMI("kostel", "church", PLACE),
]


# TA
fdf_nouns = [
    FDF("žena", "woman", PERSON),
    FDF("škola", "school", PLACE),
    FDF("sušenka", "biscuit", FOOD),
    FDF("tužka", "pencil", THING),
    FDF("cesta", "road", PLACE),
    FDF("lampa", "lamp", THING),
    FDF("maminka", "mother", PERSON),
    FDF("tiskárna", "printer", THING),
    FDF("koruna", "money", THING),
    FDF("kopírka", "copier", THING),
    FDF("jídelna", "dining room", PLACE),
    FDF("budova", "building", PLACE),
]


# TO
fdn_nouns = [
    FDN("auto", "car", VEHICLE),
    FDN("kino", "cinema", PLACE),
    FDN("křeslo", "chair", THING),
    FDN("radio", "radio", THING),
    FDN("město", "city", PLACE),
    FDN("tričko", "t-shirt", CLOTHES),
]


"""
HW 14-08-2023
8
    ta jedna jídelna
    to velko divadlo
    to malo snídaně
    ten velky hrad
    to malo pivo
    to velko letiště
    ten maly obchod
    ten velky hotel
    ta malá vesnice
    to velko město
    ten maly kostel
    ta velka budova

9
    jedna dobrá zmrzlina
    jedna špatna přítelkyně
    jeden dobry čišník
    jeden špatny pomeranč
    jedno dobro jídlo
    jedna špatna hospoda
    jeden dobry kamarád
    jedno špatno jablko
    jedna dobrá kobliha
    jeden špatnz přitel
    jedna dobrá studentka
"""
