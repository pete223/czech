from .constants import (CASES, VOWELS)

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

    def __repr__(self):
        return self.czech

    def declinate(self):
        return self.all_cases()

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


class FirstDeclensionMasculineAnimate(Noun):
    @property
    def endings(self):
       return {1: "", 2: "a", 3: "ovi", 4: "a", 5: "e", 6: "ovi", 7: "em"}


class FirstDeclensionMasculineInanimate(Noun):
    @property
    def endings(self):
        return {1: "", 2: "u", 3: "u", 4: "", 5: "", 6: "ě", 7: "em"}


class FirstDeclensionFeminine(Noun):
    @property
    def endings(self):
        return {1: "a", 2: "y", 3: "e", 4: "u", 5: "o", 6: "e", 7: "ou"}


class FirstDeclensionNeuter(Noun):
    @property
    def endings(self):
        return {1: "o", 2: "a", 3: "u", 4: "o", 5: "", 6: "ě", 7: "em"}


class SecondDeclensionMasculineAnimate(Noun):
    @property
    def endings(self):
        return {1: "", 2: "e", 3: "ovi", 4: "e", 5: "i", 6: "ovi", 7: "em"}


class SecondDeclensionMasculineInanimate(Noun):
    @property
    def endings(self):
        return {1: "", 2: "e", 3: "i", 4: "", 5: "", 6: "i", 7: "em"}


class SecondDeclensionFeminine(Noun):
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
    # TODO: remove the extra ě
    def endings(self):
        return {1: "ě", 2: "ě", 3: "i", 4: "ě", 5: "", 6: "i", 7: "ěm"}


class ThirdDeclensionMasculineAnimate(Noun):
    @property
    def endings(self):
       return {1: "", 2: "y", 3: "ovi", 4: "u", 5: "o", 6: "ovi", 7: "ou"}


class ThirdDeclensionFeminine(Noun):
    @property
    def endings(self):
        return {1: "", 2: "i", 3: "i", 4: "", 5: "", 6: "i", 7: "í"}


class ThirdDeclensionNeuter(Noun):
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
