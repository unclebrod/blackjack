from deck import Deck
from player import Player, Dealer


class Blackjack:
    def __init__(self, deck: Deck):  #, players: int):
        self.deck = deck
        # self.players = players  # TODO: add logic for multiple players

    def play_a_hand(self):
        print("New hand commencing!")
        self.deck.shuffle()
        dealer = Dealer(deck=self.deck)
        player = Player(number=1)
        all_users = [player, dealer]
        for user in all_users:
            dealer.deal(user)
        for user in all_users:
            dealer.deal(user)
            user.report_total()