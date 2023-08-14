class Noun():
    def __init__(self, czech, english, gender, category) -> None:
        self.czech = czech
        self.english = english
        self.gender = gender(self.czech)
        self.case = self.gender.case
        self.endings = self.gender.endings
        self.category = category

    def __repr__(self):
        return self.czech

    def declinate(self):
        return self.gender.all_cases()
