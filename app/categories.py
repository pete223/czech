class Category():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


ANIMAL     = Category("animal")
EMOTION    = Category("emotion")
PROFESSION = Category("profession")
PLACE      = Category("place")
FOOD       = Category("food")
PERSON     = Category("people")
VEHICLE    = Category("vehicle")
THING      = Category("uncategorized")
CLOTHES    = Category("clothes")
HOUSEHOLD  = Category("household")
