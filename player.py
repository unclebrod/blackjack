from deck import Deck


class User:
    def __init__(self):
        self.hand = []
        self.number = None
        self.total = 0

    def hit(self):
        pass

    def stand(self):
        pass

    def _calculate_total(self):
        self.total = sum(self.hand)


class Player(User):
    def __init__(self, number: int):
        super().__init__()
        self.number = number

    def __str__(self):
        return f"Player {self.number}"

    def report_total(self):
        print(f"{self} has a total of {self.total}")

    def evaluate(self, dealers_hand):
        pass


class Dealer(User):
    def __init__(self, deck: Deck):
        super().__init__()
        self.deck = deck
        self.display_total = 0

    def __str__(self):
        return "Dealer"

    def deal(self, player: User):
        card = self.deck.cards.pop()
        player.hand.append(card)
        if (type(player) == Dealer) and (len(player.hand) == 2):
            print("The dealer has placed his second card face down.")
        else:
            print(f"{player} drew a {card}.")
        player._calculate_total()

    def report_total(self):
        print(f"{self} has a visible total of {self.display_total}")

    def _calculate_total(self):
        super()._calculate_total()
        self._calculate_display_total()

    def _calculate_display_total(self):
        visible_cards = self.hand[:1] + self.hand[2:]
        self.display_total = sum(visible_cards)
