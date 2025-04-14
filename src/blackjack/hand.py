from blackjack import logger
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

    def low_value(self, *, visible: bool = False) -> int:
        cards = self.visible_cards() if visible else self.cards
        return sum(cards)

    def high_value(self, *, visible: bool = False) -> int:
        cards = self.visible_cards() if visible else self.cards
        return sum([card.convert() for card in cards])

    def visible_cards(self) -> list[Card]:
        return self.cards[1:]

    def draw(self, deck: Deck):
        self.cards.append(deck.cards.pop())

    def has_one_value(self, *, visible: bool = False) -> bool:
        return self.low_value(visible=visible) == self.high_value(visible=visible)

    def log_cards(
        self,
        idx: int | None = None,
        player_meta: str | None = None,
        *,
        visible: bool = False,
    ):
        meta = f"{player_meta} " if player_meta else ""
        num = f" {idx}" if idx is not None else ""
        if visible:
            verb = "is showing"
            cards_in_hand = self.visible_cards()
        else:
            verb = "contains"
            cards_in_hand = self.cards
        logger.info(
            f"{meta}Hand{num} {verb} {', '.join([str(x) for x in cards_in_hand])}"
        )
        low = self.low_value(visible=visible)
        high = self.high_value(visible=visible)
        if self.has_one_value(visible=visible):
            logger.debug(f"{meta}Hand{num} {verb} a value of {low}")
        else:
            logger.debug(f"{meta}Hand{num} has a value of {low} or {high}")


class Hands:
    """Hands class for a collection of hands.

    Attributes
    ----------
    hands : list[Hand]
        Collection of hands.

    """

    def __init__(self, hands: list[Hand] | None = None):
        self.hands = hands or [Hand()]

    def __iter__(self):
        yield from self.hands

    def log_cards(self, *, visible: bool = False, **kwargs):
        for idx, hand in enumerate(self.hands, start=1):
            hand.log_cards(visible=visible, idx=idx, **kwargs)
