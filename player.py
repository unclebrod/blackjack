from deck import Deck


class Player:
    def __init__(self, deck: Deck):
        self.deck = deck
        self.hand = []

    def hit(self):
        card = self.deck.cards.pop()
        self.hand.append(card)
        print(f"Player drew a {card}.")

    def pass(self):
        print("Player passses.")
        pass