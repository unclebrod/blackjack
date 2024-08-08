from blackjack.cards import Shoe
from blackjack.game import Game
from blackjack.participants import Dealer, Player

if __name__ == "__main__":
    game = Game(
        shoe=Shoe(),
        dealer=Dealer(),
        players=[Player(id_num=x) for x in range(3)],
    )
