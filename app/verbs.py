
class Verb():
    def __init__(self, czech, english):
        self.czech = czech
        self.english = english
        # Remove infinite suffix
        self.root = self.czech[:-2]

    def conjugate(self, add_prefix=False):
        for k, v in self.endings().items():
            if add_prefix:
                print(f"{self.prefix()[k]} {self.root}{v}")
            else:
                print(f"{self.root}{v}")

    def prefix(self):
        return { 1: "já", 2: "ty", 3: "on/ona/ono", 4: "my", 5: "vy", 6: "oni" }


    def endings(self):
        return { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "" }



class FirstDeclensionVerb(Verb):
    def endings(self):
        return { 1: "ám", 2: "ás", 3: "á", 4: "áme", 5: "áte", 6: "ají" }


class SecondDeclensionVerb(Verb):
    pass


class FDV(FirstDeclensionVerb):
    pass


VERBS = [
    FDV("vstávat", "to get up"),
    FDV("mít", "to have"),
    FDV("snídat", "to have breakfast"),
    FDV("odpočivat", "to rest"),
    FDV("čekat", "to wait"),
    FDV("obědvat", "to have lunch")
]
