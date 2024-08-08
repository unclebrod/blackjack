from abc import ABC
from dataclasses import dataclass, field

from blackjack.cards import Card, Deck


@dataclass
class Hand:
    """Hand class for a collection of cards.

    Attributes
    ----------
    cards : list[Card]
        Collection of cards.

    """

    cards: list[Card] = field(default_factory=list)

    def value(self):
        return sum(self.cards)


@dataclass
class Participant(ABC):
    """Participant base class for someone playing Blackjack.

    Attributes
    ----------
    id_num : int
        Unique identifier for the participant.
    hands : list[Card]
        Hands held by the participant.

    """

    id_num: int
    hands: list[Hand] = field(default_factory=list)  # TODO: hands class for splitting
    # TODO: maybe a strategy class that determines when to draw/stand/split/etc.

    def draw(self, hand: Hand, deck: Deck):
        hand.cards.append(deck.cards.pop())

    def stand(self):
        pass


@dataclass
class Player(Participant):
    """Player class for someone playing Blackjack."""

    def __str__(self):
        return f"Player {self.id_num}"

    def __repr__(self):
        return f"Player {self.id_num}"

    def double(self):
        pass

    def split(self):
        pass


@dataclass
class Dealer(Participant):
    """Class for the Blackjack dealer."""

    id_num: int = 1

    def __str__(self):
        return "Dealer"

    def __repr__(self):
        return "Dealer"
