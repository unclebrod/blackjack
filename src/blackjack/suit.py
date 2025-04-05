from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
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


SUITS = [
    ClubSuit,
    SpadeSuit,
    DiamondSuit,
    HeartSuit,
]
