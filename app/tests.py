from .sentences import SimpleSentence
from . import ALL_VERBS, ALL_NOUNS

# Mít -> to have
predicate = ALL_VERBS[1]

direct_object = ALL_NOUNS[13]

sentence = SimpleSentence(predicate, None, direct_object)
