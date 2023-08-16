from .constants import (CASES, VOWELS)


# TODO:
# Create ENDINGS dictionary with all possible endings
# Refactor nouns to query endings from ENDINGS dictionary

class Noun():
    def __init__(self, czech, english, categories) -> None:
        self.czech = czech
        self.english = english
        self.last_letter = czech[-1:]
        self.word = czech
        self.root = self.word
        if self.last_letter in VOWELS:
            self.root = czech[:-1]
        self.categories = categories
        self.subject = self.case(1)
        self.direct_object = self.case(4)

    def __repr__(self):
        return self.czech

    def declinate(self):
        return self.all_cases()

    def get_case(self, case):
        if case in [1, "nom", "nomanitive", "NOM", "NOMANITIVE", "subject"]:
            case = 1
        elif case in [2, "gen", "genitive", "GEN", "GENITIVE"]:
            case = 2
        elif case in [3, "dat", "dative", "DAT", "DATIVE"]:
            case = 3
        elif case in [4, "acc", "accusative", "ACC", "ACCUSATIVE", "object"]:
            case = 4
        elif case in [5, "voc", "vocative", "VOC", "VOCATIVE"]:
            case = 5
        elif case in [6, "loc", "locative", "LOC", "LOCATIVE"]:
            case = 6
        elif case in [7, "ins", "inst", "instrumental", "INS", "INST", "INSTRUMENTAL"]:
            case = 7
        else:
            raise Exception("No case identified, invalid selection")
        return 1


    def case(self, case=1, explain=False):
        case_as_int = self.get_case(case)

        if explain:
            print(f"Case: {CASES[case]['name']}")
            print(f"Case Meaning: {CASES[case]['meaning']}")
            print(f"Prepositions: {CASES[case]['prepositions']}")

        # If second last letter is e then drop it 
        # TODO: check if it is the same for é and ě
        root = self.root
        if root[-2:-1] == "e" and case_as_int != 1:
            # eg the new root for herec becomes herc
            new_root = root[:-2] + root[-1:]
            root = new_root
        return self.root + self.endings[case_as_int]

    @property
    def endings(self):
        return {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""}

    def all_cases(self):
        print(self.case(1))
        print(self.case(2))
        print(self.case(3))
        print(self.case(4))
        print(self.case(5))
        print(self.case(6))
        print(self.case(7))
        return


class FirstDeclensionMasculineAnimate(Noun):
    def case(self, case=1, explain=False):
        case_as_int = self.get_case(case)

        if explain:
            print(f"Case: {CASES[case]['name']}")
            print(f"Case Meaning: {CASES[case]['meaning']}")
            print(f"Prepositions: {CASES[case]['prepositions']}")

        # If second last letter is e then drop it 
        # TODO: check if it is the same for é and ě
        root = self.root
        if root[-2:-1] == "e" and case_as_int != 1:
            # eg the new root for herec becomes herc
            new_root = root[:-2] + root[-1:]
            root = new_root
        return root + self.endings[case_as_int]

    @property
    def gender(self):
        return "MA"

    @property
    def endings(self):
       return {1: "", 2: "a", 3: "ovi", 4: "a", 5: "e", 6: "ovi", 7: "em"}


class FirstDeclensionMasculineInanimate(Noun):
    @property
    def gender(self):
        return "MI"

    @property
    def endings(self):
        return {1: "", 2: "u", 3: "u", 4: "", 5: "", 6: "ě", 7: "em"}


class FirstDeclensionFeminine(Noun):
    @property
    def gender(self):
        return "F"

    @property
    def endings(self):
        return {1: "a", 2: "y", 3: "e", 4: "u", 5: "o", 6: "e", 7: "ou"}


class FirstDeclensionNeuter(Noun):
    @property
    def gender(self):
        return "N"

    @property
    def endings(self):
        return {1: "o", 2: "a", 3: "u", 4: "o", 5: "", 6: "ě", 7: "em"}


class SecondDeclensionMasculineAnimate(FirstDeclensionMasculineAnimate):
    @property
    def gender(self):
        return "MA"

    @property
    def endings(self):
        return {1: "", 2: "e", 3: "ovi", 4: "e", 5: "i", 6: "ovi", 7: "em"}


class SecondDeclensionMasculineInanimate(Noun):
    @property
    def gender(self):
        return "MI"

    @property
    def endings(self):
        return {1: "", 2: "e", 3: "i", 4: "", 5: "", 6: "i", 7: "em"}


class SecondDeclensionFeminine(Noun):
    @property
    def gender(self):
        return "F"

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


class SecondDeclensionNeuter(Noun):
    @property
    def gender(self):
        return "N"

    @property
    # TODO: remove the extra ě
    def endings(self):
        return {1: "ě", 2: "ě", 3: "i", 4: "ě", 5: "", 6: "i", 7: "ěm"}


class ThirdDeclensionMasculineAnimate(Noun):
    @property
    def gender(self):
        return "MA"

    @property
    def endings(self):
       return {1: "", 2: "y", 3: "ovi", 4: "u", 5: "o", 6: "ovi", 7: "ou"}


class ThirdDeclensionFeminine(Noun):
    @property
    def gender(self):
        return "F"

    @property
    def endings(self):
        return {1: "", 2: "i", 3: "i", 4: "", 5: "", 6: "i", 7: "í"}


class ThirdDeclensionNeuter(Noun):
    @property
    def gender(self):
        return "N"

    @property
    def endings(self):
        return {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "m"}


class FDMA(FirstDeclensionMasculineAnimate):
    pass


class FDMI(FirstDeclensionMasculineInanimate):
    pass


class FDF(FirstDeclensionFeminine):
    pass


class FDN(FirstDeclensionNeuter):
    pass


class SDMA(SecondDeclensionMasculineAnimate):
    pass


class SDMI(SecondDeclensionMasculineInanimate):
    pass


class SDF(SecondDeclensionFeminine):
    pass


class SDN(SecondDeclensionNeuter):
    pass


class TDMA(ThirdDeclensionMasculineAnimate):
    pass


class TDF(ThirdDeclensionFeminine):
    pass


class TDN(ThirdDeclensionNeuter):
    pass


# Unknown declension
# ta poezie - poetry
# ta noc - night
# ta moře - sea
# ta chuť - food
# ta labuť - swan
# ta dlaň - palm
# ta tramvaj - tram
# to museum - museum
