CASES = {
    1: {
        'name': 'NOMANITIVE',
        'meaning': 'Used as the subject of the sentence',
        'prepositions': []
    },
    2: {
        'name': 'GENITIVE',
        'meaning': 'Expresses possessive or partitive meaning the students book/ the piece of banana',
        'prepositions': []
    },
    3: {
        'name': 'DATIVE',
        'meaning': 'Is used for the indirect object Ill give the coffee to the student',
        'prepositions': []
    },
    4: {
        'name': 'ACCUSATIVE',
        'meaning': 'Is used for the direct object',
        'prepositions': []
    }, 
    5: {
        'name': 'VOCATIVE',
        'meaning': 'Used to address people and animals',
        'prepositions': []
    },
    6: {
        'name': 'LOCATIVE',
        'meaning': 'Used to express location',
        'prepositions': []
    },
    7: {
        'name': 'INSTRUMENTAL',
        'meaning': 'Express the means by which an activity is carried out',
        'prepositions': []
    }
}

SIMPLE_CONSONANTS = [
    'b', 'c', 'd', 'f', 'g',
    'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'r', 's', 't',
    'v', 'w', 'x', 'y', 'z'
]

VOWELS = ['a', 'e', 'o']

class Gender():

    def __init__(self, word=''):
        'Peter'
        last_letter = word[-1:]
        if last_letter in VOWELS:
            self.root = word[:-1]
        else:
            self.root = word
        self.endings = self.get_endings()

    def case(self, case=1, explain=True):
        if case in [1, 'nom', 'nomanitive', 'NOM', 'NOMANITIVE']:
            case = 1
        elif case in [2, 'gen', 'genitive', 'GEN', 'GENITIVE']:
            case = 2
        elif case in [3, 'dat', 'dative', 'DAT', 'DATIVE']:
            case = 3
        elif case in [4, 'acc', 'accusative', 'ACC', 'ACCUSATIVE']:
            case = 4
        elif case in [5, 'voc', 'vocative', 'VOC', 'VOCATIVE']:
            case = 5
        elif case in [6, 'loc', 'locative', 'LOC', 'LOCATIVE']:
            case = 6
        elif case in [7, 'ins', 'inst', 'instrumental', 'INS', 'INST', 'INSTRUMENTAL']:
            case = 7
        else:
            raise Exception('No case identified, invalid selection')

        if explain == True:
            print(f"Case: {CASES[case]['name']}")
            print(f"Case Meaning: {CASES[case]['meaning']}")
            print(f"Prepositions: {CASES[case]['prepositions']}")
            return self.root + self.endings[case]

        else:
            return self.root + self.endings[case] 

    @property
    def nouns(self):
        return { '_': '_', }

    @property
    def nouns_en(self):
        cz = self.nouns().items()
        en = {}

        for k,v in cz:
            en[v] = k
        return en

    def get_endings(self):
        return {
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
            7: ''
        }


class FirstDeclensionMasculineAnimate(Gender):
    @property
    def nouns(self):
        return {
            'doktor': 'doctor',
            'pan': 'old man',
            'muž': 'young man',
        }

    def get_endings(self):
        return {
            1: '',
            2: 'a',
            3: 'ovi',
            4: 'a',
            5: 'e',
            6: 'ovi',
            7: 'em'
        }


class FirstDeclensionMasculineInanimate(Gender):
    @property
    def nouns(self):
        return {
            'obchod': 'shop',
        }

    def get_endings(self):
        return {
            1: '',
            2: 'u',
            3: 'u',
            4: '',
            5: '',
            6: 'ě',
            7: 'em'
        }


class FirstDeclensionFeminine(Gender):

    @property
    def nouns(self):
        return {
            'žena': 'woman',
            'škola': 'school',
        }

    def get_endings(self):
        return {
            1: 'a',
            2: 'y',
            3: 'e',
            4: 'u',
            5: 'o',
            6: 'e',
            7: 'ou'
        }


class FirstDeclensionNeuter(Gender):

    @property
    def nouns(self):
        return {
            'auto': 'car',
            'kino': 'cinema',
        }

    def get_endings(self):
        return {
            1: 'o',
            2: 'a',
            3: 'u',
            4: 'o',
            5: '',
            6: 'ě',
            7: 'em'
        }
