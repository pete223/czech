class Verb():
    def __init__(self, czech, english, transitive):
        self.czech = czech
        self.english = english
        # Remove infinite suffix
        self.root = self.czech[:-2]
        self.transitive = transitive

    def __repr__(self):
        return self.czech

    def case(self, case, add_prefix=False):
        if add_prefix:
            return self.prefix[case] + " " + self.root + self.endings[case]
        return self.root + self.endings[case]

    def conjugate(self, add_prefix=False):
        for k, v in self.endings.items():
            if add_prefix:
                print(f"{self.prefix[k]} {self.root}{v}")
            else:
                print(f"{self.root}{v}")

    @property
    def prefix(self):
        return { 1: "já", 2: "ty", 3: "on/ona/ono", 4: "my", 5: "vy", 6: "oni" }


    @property
    def endings(self):
        return { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "" }



class FirstDeclensionVerb(Verb):

    @property
    def endings(self):
        return { 1: "ám", 2: "ás", 3: "á", 4: "áme", 5: "áte", 6: "ají" }


class SecondDeclensionVerb(Verb):
    pass


class ThirdDeclensionVerb(Verb):
    pass


class FourthDeclensionVerb(Verb):
    pass


class FDV(FirstDeclensionVerb):
    pass


class SDV(SecondDeclensionVerb):
    pass


class TDV(ThirdDeclensionVerb):
    pass


class FourDV(FourthDeclensionVerb):
    pass
