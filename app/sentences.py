from . import ALL_NOUNS, ALL_VERBS
from .constants import PRONOUNS
from .verbs import Verb
from .nouns import Noun
from .exceptions import WrongPronounException
from typing import Union


class SentenceException(BaseException):
    """Raised when an invalid sentence structure is requested"""


class SimpleSentence():
    def __init__(self, predicate: Verb, subject: Union[Noun, None], direct_object: Noun) -> None: # noqa
        self.predicate = predicate
        self.subject = subject
        self.direct_object = direct_object

    def create(self, pronoun=None):
        # TODO: handle plural
        if pronoun:
            pronoun = str(pronoun).lower()
        if pronoun is None and self.subject is None:
            raise SentenceException("Sentence needs either a subject or a pronoun")
        elif pronoun and self.subject:
            raise SentenceException("Sentence cannot have both a subject and a pronoun,") # noqa
        elif pronoun and self.subject is None:
            if pronoun not in PRONOUNS:
                raise WrongPronounException()
            case = PRONOUNS[pronoun]
            return f"{self.predicate.case(case, add_prefix=True)} {self.direct_object.case(4)}" # noqa
        elif self.subject and pronoun is None:
            # Note: we assume the subject is singular 'thing'
            return f"{self.subject.case(1)} {self.predicate.case(3)} {self.direct_object.case(4)}" # noqa
