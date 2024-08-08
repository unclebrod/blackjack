from dataclasses import dataclass

from cards import Shoe
from participants import Dealer, Player


@dataclass
class Game:
    shoe: Shoe
    dealer: Dealer
    players: list[Player]

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
