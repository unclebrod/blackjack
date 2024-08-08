from __future__ import annotations

import random
from abc import ABC
from dataclasses import dataclass, field
from typing import Literal

from emoji import emojize

COLOR = Literal["red", "black"]


@dataclass(frozen=True)
class Suit(ABC):
    """Class describing the suit of a card.

    Attributes
    ----------
    name : str
        Name of the suit.
    color : {'red', 'black'}
        Color of the suit.

    """

    name: str
    color: COLOR

    def __str__(self):
        return self.name


@dataclass(frozen=True)
class ClubSuit(Suit):
    """Club suit class."""

    name: str = "Club"
    color: COLOR = "black"

    def __repr__(self):
        return emojize(":club_suit:")


@dataclass(frozen=True)
class SpadeSuit(Suit):
    """Spade suit class."""

    name: str = "Spade"
    color: COLOR = "black"

    def __repr__(self):
        return emojize(":spade_suit:")


@dataclass(frozen=True)
class DiamondSuit(Suit):
    """Diamon suit class."""

    name: str = "Diamond"
    color: COLOR = "red"

    def __repr__(self):
        return emojize(":diamond_suit:")


@dataclass(frozen=True)
class HeartSuit(Suit):
    """Heard suit class."""

    name: str = "Heart"
    color: COLOR = "red"

    def __repr__(self):
        return emojize(":heart_suit:")


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
        else:
            return NotImplemented

    def __sub__(self, other: Rank) -> int:
        return self.value - other.value

    def __rsub__(self, other: int | float) -> int:
        if isinstance(other, int | float):
            return other - self.value
        else:
            return NotImplemented


@dataclass(frozen=True)
class AceRank(Rank):
    """Ace rank class."""

    name: str = "Ace"
    value: int = 11

    def set_low_value(self):
        """Set the value to 1."""
        object.__setattr__(self, "value", 1)

    def set_high_value(self):
        """Set the value to 11."""
        object.__setattr__(self, "value", 11)

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


@dataclass(frozen=True)
class Card:
    """Playing card class.

    Attributes
    ----------
    rank : Rank
        Card rank.
    suit : Suit
        Card suit.

    """

    rank: Rank
    suit: Suit

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
        else:
            return NotImplemented

    def __sub__(self, other: Card) -> int:
        return self.rank.value - other.rank.value

    def __rsub__(self, other: int | float) -> int:
        if isinstance(other, int | float):
            return other - self.rank.value
        else:
            return NotImplemented


@dataclass
class Deck:
    """Class for a deck of cards.

    Attributes
    ----------
    cards : list[Card]
        Collection of cards.

    """

    cards: list[Card] = field(default_factory=list)

    def __post_init__(self):
        ranks = [
            AceRank,
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
        suits = [
            HeartSuit,
            DiamondSuit,
            SpadeSuit,
            ClubSuit,
        ]
        self.cards = [
            Card(rank=rank(), suit=suit()) for rank in ranks for suit in suits
        ]
        self.shuffle()

    def __add__(self, other):
        return self.cards + other.cards

    def __len__(self):
        return len(self.cards)

    def __mul__(self, other):
        return self.cards * other

    def shuffle(self):
        random.shuffle(self.cards)


@dataclass
class Shoe(Deck):
    """Class for multiple decks of cards (a shoe).

    Attributes
    ----------
    n : int, default=6
        Number of decks in the shoe.

    """

    n: int = 6

    def __post_init__(self):
        Deck.__post_init__(self)
        self.cards *= self.n
        self.shuffle()
