from blackjack.card import Card
from blackjack.deck import Deck


class Hand:
    """Hand class for a collection of cards.

    Attributes
    ----------
    cards : list[Card]
        Collection of cards.

    """

    def __init__(self, cards: list[Card] | None = None):
        self.cards = cards or []

    def low_value(self, visible: bool = False) -> int:
        cards = self.visible_cards() if visible else self.cards
        return sum(cards)

    def high_value(self, visible: bool = False) -> int:
        cards = self.visible_cards() if visible else self.cards
        return sum([card.convert() for card in cards])

    def visible_cards(self) -> list[Card]:
        return self.cards[1:]

    def draw(self, deck: Deck):
        self.cards.append(deck.cards.pop())
