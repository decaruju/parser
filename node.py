from dataclasses import dataclass

@dataclass
class Node:
    tokens: list

    @staticmethod
    def is_root():
        return False
