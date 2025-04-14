from blackjack import logger
from blackjack.deck import Deck
from blackjack.participants import Dealer, Player


class Game:
    def __init__(self, deck: Deck, dealer: Dealer, players: list[Player]):
        self.deck = deck
        self.dealer = dealer
        self.players = players
        self.participants = [dealer] + players

    def play_a_hand(self):
        logger.info("New hand commencing!")
        for idx in range(2):
            for participant in self.participants:
                for hand in participant.hands:
                    hand.draw(self.deck)
                    if idx == 1:
                        participant.log_cards(visible=True)
                        participant.log_cards(visible=False)
