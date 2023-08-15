class Number():
    def __init__(self, czech, masculine, feminine, neuter, num: int):
        self.czech = czech
        self.masculine = masculine
        self.feminine = feminine
        self.neuter = neuter
        self.num = num


Number("jedna", "jeden", "jedna", "jedno", 1)
