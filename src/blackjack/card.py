from __future__ import annotations

from blackjack.rank import AceHighRank, AceLowRank, Rank
from blackjack.suit import Suit


class Card:
    """Playing card class.

    Attributes
    ----------
    rank : blackjack.rank.Rank
        Card rank.
    suit : blackjack.suit.Suit
        Card suit.

    """

    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{repr(self.rank)}{repr(self.suit)}"

    def __lt__(self, other: Card) -> bool:
        return self.rank.value < other.rank.value

    def __le__(self, other: Card) -> bool:
        return self.rank.value <= other.rank.value

    def __gt__(self, other: Card) -> bool:
        return self.rank.value > other.rank.value

    def __ge__(self, other: Card) -> bool:
        return self.rank.value >= other.rank.value

    def __eq__(self, other: Card) -> bool:
        return self.rank.value == other.rank.value

    def __ne__(self, other: Card) -> bool:
        return self.rank.value != other.rank.value

    def __add__(self, other: Card) -> int:
        return self.rank.value + other.rank.value

    def __radd__(self, other: int | float) -> int:
        if isinstance(other, int | float):
            return other + self.rank.value
        return NotImplemented

    def __sub__(self, other: Card) -> int:
        return self.rank.value - other.rank.value

    def __rsub__(self, other: int | float) -> int:
        if isinstance(other, int | float):
            return other - self.rank.value
        return NotImplemented

    def convert(self):
        if isinstance(self.rank, AceLowRank):
            self.rank = AceHighRank
        elif isinstance(self.rank, AceHighRank):
            self.rank = AceLowRank
        return self
