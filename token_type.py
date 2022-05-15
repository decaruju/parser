from dataclasses import dataclass
import re


@dataclass
class Token:
    text: str
    pos: int

    @classmethod
    def match(cls, text):
        return re.match(f'^{cls.rule}$', text)

