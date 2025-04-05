from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from emoji import emojize


@dataclass(frozen=True)
class Rank(ABC):
    """Class describing the rank of a card.

    Attributes
    ----------
    name : str
        Name of the rank.
    value : int
        Blackjack value of the rank

    """

    name: str
    value: int

    def __str__(self):
        return self.name

    def __lt__(self, other: Rank) -> bool:
        return self.value < other.value

    def __le__(self, other: Rank) -> bool:
        return self.value <= other.value

    def __gt__(self, other: Rank) -> bool:
        return self.value > other.value

    def __ge__(self, other: Rank) -> bool:
        return self.value >= other.value

    def __eq__(self, other: Rank) -> bool:
        return self.value == other.value

    def __ne__(self, other: Rank) -> bool:
        return self.value != other.value

    def __add__(self, other: Rank) -> int:
        return self.value + other.value

    def __radd__(self, other: int | float) -> int:
        if isinstance(other, int | float):
            return other + self.value
        return NotImplemented

    def __sub__(self, other: Rank) -> int:
        return self.value - other.value

    def __rsub__(self, other: int | float) -> int:
        if isinstance(other, int | float):
            return other - self.value
        return NotImplemented


@dataclass(frozen=True)
class AceLowRank(Rank):
    """Ace low rank class."""

    name: str = "Ace"
    value: int = 1

    def __repr__(self):
        return emojize("\U0001f170")


@dataclass(frozen=True)
class AceHighRank(Rank):
    """Ace high rank class."""

    name: str = "Ace"
    value: int = 11

    def __repr__(self):
        return emojize("\U0001f170")


@dataclass(frozen=True)
class TwoRank(Rank):
    """Two rank class."""

    name: str = "Two"
    value: int = 2

    def __repr__(self):
        return emojize(":keycap_2:")


@dataclass(frozen=True)
class ThreeRank(Rank):
    """Three rank class."""

    name: str = "Three"
    value: int = 3

    def __repr__(self):
        return emojize(":keycap_3:")


@dataclass(frozen=True)
class FourRank(Rank):
    """Four rank class."""

    name: str = "Four"
    value: int = 4

    def __repr__(self):
        return emojize(":keycap_4:")


@dataclass(frozen=True)
class FiveRank(Rank):
    """Five rank class."""

    name: str = "Five"
    value: int = 5

    def __repr__(self):
        return emojize(":keycap_5:")


@dataclass(frozen=True)
class SixRank(Rank):
    """Six rank class."""

    name: str = "Six"
    value: int = 6

    def __repr__(self):
        return emojize(":keycap_6:")


@dataclass(frozen=True)
class SevenRank(Rank):
    """Seven rank class."""

    name: str = "Seven"
    value: int = 7

    def __repr__(self):
        return emojize(":keycap_7:")


@dataclass(frozen=True)
class EightRank(Rank):
    """Eight rank class."""

    name: str = "Eight"
    value: int = 8

    def __repr__(self):
        return emojize(":keycap_8:")


@dataclass(frozen=True)
class NineRank(Rank):
    """Nine rank class."""

    name: str = "Nine"
    value: int = 9

    def __repr__(self):
        return emojize(":keycap_9:")


@dataclass(frozen=True)
class TenRank(Rank):
    """Ten rank class."""

    name: str = "Ten"
    value: int = 10

    def __repr__(self):
        return emojize(":keycap_10:")


@dataclass(frozen=True)
class JackRank(Rank):
    """Jack rank class."""

    name: str = "Jack"
    value: int = 10

    def __repr__(self):
        return emojize(":man:")


@dataclass(frozen=True)
class QueenRank(Rank):
    """Queen rank class."""

    name: str = "Queen"
    value: int = 10

    def __repr__(self):
        return emojize(":princess:")


@dataclass(frozen=True)
class KingRank(Rank):
    """King rank class."""

    name: str = "King"
    value: int = 10

    def __repr__(self):
        return emojize(":prince:")


RANKS = [
    AceLowRank,
    TwoRank,
    ThreeRank,
    FourRank,
    FiveRank,
    SixRank,
    SevenRank,
    EightRank,
    NineRank,
    TenRank,
    JackRank,
    QueenRank,
    KingRank,
]
