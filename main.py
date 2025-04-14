from blackjack.deck import Shoe
from blackjack.game import Game
from blackjack.participants import Dealer, Player

if __name__ == "__main__":
    game = Game(
        deck=Shoe(),
        dealer=Dealer(),
        players=[Player(id_num=x) for x in range(3)],
    )
    game.play_a_hand()
