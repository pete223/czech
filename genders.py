CASES = {
    1: {
        "name": "NOMANITIVE",
        "meaning": "Used as the subject of the sentence",
        "prepositions": [],
    },
    2: {
        "name": "GENITIVE",
        "meaning": "Expresses possessive or partitive meaning the students book/ the piece of banana", # noqa
        "prepositions": [],
    },
    3: {
        "name": "DATIVE",
        "meaning": "Is used for the indirect object I'll give the coffee to the student", # noqa
        "prepositions": [],
    },
    4: {
        "name": "ACCUSATIVE",
        "meaning": "Is used for the direct object",
        "prepositions": [],
    },
    5: {
        "name": "VOCATIVE",
        "meaning": "Used to address people and animals",
        "prepositions": [],
    },
    6: {"name": "LOCATIVE", "meaning": "Used to express location", "prepositions": []},
    7: {
        "name": "INSTRUMENTAL",
        "meaning": "Express the means by which an activity is carried out",
        "prepositions": [],
    },
}

SIMPLE_CONSONANTS = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
]

VOWELS = ["a", "e", "o", "ě"]


class Gender:
    def __init__(self, word):
        self.last_letter = word[-1:]
        self.word = word
        self.root = self.word
        if self.last_letter in VOWELS:
            self.root = word[:-1]

    def case(self, case=1, explain=True):
        if case in [1, "nom", "nomanitive", "NOM", "NOMANITIVE"]:
            case = 1
        elif case in [2, "gen", "genitive", "GEN", "GENITIVE"]:
            case = 2
        elif case in [3, "dat", "dative", "DAT", "DATIVE"]:
            case = 3
        elif case in [4, "acc", "accusative", "ACC", "ACCUSATIVE"]:
            case = 4
        elif case in [5, "voc", "vocative", "VOC", "VOCATIVE"]:
            case = 5
        elif case in [6, "loc", "locative", "LOC", "LOCATIVE"]:
            case = 6
        elif case in [7, "ins", "inst", "instrumental", "INS", "INST", "INSTRUMENTAL"]:
            case = 7
        else:
            raise Exception("No case identified, invalid selection")

        if explain:
            print(f"Case: {CASES[case]['name']}")
            print(f"Case Meaning: {CASES[case]['meaning']}")
            print(f"Prepositions: {CASES[case]['prepositions']}")
        return self.root + self.endings[case]

    @property
    def endings(self):
        return {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""}

    def all_cases(self):
        print(self.case(1, False))
        print(self.case(2, False))
        print(self.case(3, False))
        print(self.case(4, False))
        print(self.case(5, False))
        print(self.case(6, False))
        print(self.case(7, False))
        return


class FirstDeclensionMasculineAnimate(Gender):
    @property
    def endings(self):
        return {1: "", 2: "a", 3: "ovi", 4: "a", 5: "e", 6: "ovi", 7: "em"}


class FirstDeclensionMasculineInanimate(Gender):
    @property
    def endings(self):
        return {1: "", 2: "u", 3: "u", 4: "", 5: "", 6: "ě", 7: "em"}


class FirstDeclensionFeminine(Gender):
    @property
    def endings(self):
        return {1: "a", 2: "y", 3: "e", 4: "u", 5: "o", 6: "e", 7: "ou"}


class FirstDeclensionNeuter(Gender):
    @property
    def endings(self):
        return {1: "o", 2: "a", 3: "u", 4: "o", 5: "", 6: "ě", 7: "em"}


class SecondDeclensionMasculineAnimate(Gender):
    @property
    def endings(self):
        return {1: "", 2: "e", 3: "ovi", 4: "e", 5: "i", 6: "ovi", 7: "em"}


class SecondDeclensionMasculineInanimate(Gender):
    @property
    def endings(self):
        return {1: "", 2: "e", 3: "i", 4: "", 5: "", 6: "i", 7: "em"}


class SecondDeclensionFeminine(Gender):
    # @property
    # # Note! some words may end in e already, so we need to drop the vowel
    # # and only then add the ending
    # def case(self, case=1, explain=True):
    #     word_with_case = super().case(case, explain)
    #     if self.last_letter == "e" and case == 1:
    #         return self.word
    #     if self.last_letter == "ř" and case == 4:
    #         return self.word
    #     return word_with_case

    # TODO: fix above
    @property
    def endings(self):
        return {1: "", 2: "e", 3: "i", 4: "i", 5: "", 6: "i", 7: "í"}


class SecondDeclensionNeuter(Gender):
    @property
    # TODO: remove the extra ě
    def endings(self):
        return {1: "ě", 2: "ě", 3: "i", 4: "ě", 5: "", 6: "i", 7: "ěm"}


class Noun():
    def __init__(self, czech, english, gender) -> None:
        self.czech = czech
        self.english = english
        self.gender = gender(self.czech)
        self.case = self.gender.case
        self.endings = self.gender.endings

    def __repr__(self):
        return self.czech

    def declinate(self):
        return self.gender.all_cases()


class FDMA(FirstDeclensionMasculineAnimate):
    pass


class FDMI(FirstDeclensionMasculineInanimate):
    pass


class FDF(FirstDeclensionFeminine):
    pass


class FDN(FirstDeclensionNeuter):
    pass


fdma_nouns = [
    Noun("doktor", "doctor", FDMA),
    Noun("pan", "old man", FDMA),
    Noun("muž", "young man", FDMA),
]


fdmi_nouns = [
    Noun("obchod", "shop", FDMI),
]


fdf_nouns = [
    Noun("žena", "woman", FDF),
    Noun("škola", "school", FDF),
]


fdn_nouns = [
    Noun("auto", "car", FDN),
    Noun("kino", "cinema", FDN),
]


class SDMA(SecondDeclensionMasculineAnimate):
    pass


class SDMI(SecondDeclensionMasculineInanimate):
    pass


class SDF(SecondDeclensionFeminine):
    pass


class SDN(SecondDeclensionNeuter):
    pass


sdma_nouns = [
    Noun("lékař", "", SDMA),
]

sdmi_nouns = [
    Noun("počitač", "computer", SDMI),
]

sdf_nouns = [
    Noun("restaurace", "restaurant", SDF),
    Noun("kancelář", "office", SDF),
]

sdn_nouns = [
    Noun("letistě", "airport", SDN),
]
