from .constants import GENDERS
from .exceptions import WrongGenderException


ENDINGS = {
    "MA": {
        "plural": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: ""},
        "singular": {
            1: "ý",
            2: "",
            3: "",
            4: "eho",
            5: "",
            6: "",
            7: ""
        }
    },
    "MI": {
        "plural": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: ""},
        "singular": {
            1: "ý",
            2: "",
            3: "",
            4: "ý",
            5: "",
            6: "",
            7: ""
        }
    },
    "F": {
        "plural": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: ""},
        "singular": {
            1: "á",
            2: "",
            3: "",
            4: "ou",
            5: "",
            6: "",
            7: ""
        }
    },
    "N": {
        "plural": {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: ""},
        "singular": {
            1: "é",
            2: "",
            3: "",
            4: "é",
            5: "",
            6: "",
            7: ""
        }
    }
}

class Adjective():
    def __init__(self, czech, english):
        self.czech = czech
        self.english = english
        self.root = czech[:-1]

    def case(self, case: int, gender="", plural=False):
        if gender not in GENDERS:
            raise WrongGenderException
           
        return self.root + ENDINGS["gender"]["plural" if plural else "singular"][case]


class Adj(Adjective):
    pass


adjectives = (
    Adj("skvěla", "awesome")
)
