from __future__ import annotations

import random

from blackjack.card import Card
from blackjack.rank import RANKS
from blackjack.suit import SUITS


class Deck:
    """Class for a deck of cards.

    Attributes
    ----------
    cards : list[Card]
        Collection of cards.

    """

    def __init__(self, cards: list[Card] | None = None) -> None:
        self.cards = cards or [
            Card(rank=rank(), suit=suit()) for rank in RANKS for suit in SUITS
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


class Shoe(Deck):
    """Class for multiple decks of cards (a shoe).

    Attributes
    ----------
    n : int, default=6
        Number of decks in the shoe.

    """

    def __init__(self, n: int = 6, **kwargs) -> None:
        """Initialize a shoe with n decks of cards."""
        super().__init__(**kwargs)
        self.n = n
        self.cards *= self.n
        self.shuffle()
