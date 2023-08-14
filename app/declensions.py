from .constants import CASES, VOWELS

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


class ThirdDeclensionMasculineAnimate(Gender):
    @property
    def endings(self):
       return {1: "", 2: "y", 3: "ovi", 4: "u", 5: "o", 6: "ovi", 7: "ou"}


class ThirdDeclensionFeminine(Gender):
    @property
    def endings(self):
        return {1: "", 2: "i", 3: "i", 4: "", 5: "", 6: "i", 7: "í"}


class ThirdDeclensionNeuter(Gender):
    @property
    def endings(self):
        return {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "m"}
