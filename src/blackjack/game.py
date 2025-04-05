from blackjack import logger

from blackjack.deck import Deck
from participants import Dealer, Player


class Game:

    def __init__(self, deck: Deck, dealer: Dealer, players: list[Player]):
        self.deck = deck
        self.dealer = dealer
        self.players = players

    def play_a_hand(self):
        logger.info("New hand commencing!")
        for _ in range(2):
            self.dealer.hand.draw(self.deck)
            for player in self.players:
                for hand in player.hands:
                    hand.draw(self.deck)