from blackjack import Blackjack
from deck import Shoe

if __name__ == "__main__":
    deck = Shoe()
    blackjack = Blackjack(deck=deck)
    blackjack.play_a_hand()
