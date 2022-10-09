import random


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value_map = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": [1, 11],
        }
        self.value = self.value_map[self.rank]

    def __repr__(self):
        return f"Card(rank={self.rank}, suit={self.suit}, value={self.value})"

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value


class Deck:
    def __init__(self):
        self.suits = ["D", "H", "C", "S"]
        self.ranks = [str(x) for x in range(2, 11)] + ["A", "J", "Q", "K"]
        self.cards = [Card(rank=rank, suit=suit) for rank in self.ranks for suit in self.suits]
        self.shuffle()

    def __add__(self, other):
        return self.cards + other.cards

    def __len__(self):
        return len(self.cards)

    def __mul__(self, other):
        return self.cards * other

    def shuffle(self):
        random.shuffle(self.cards)


class Shoe(Deck):
    def __init__(self, decks=int):
        super().__init__()
        self.decks = decks
        self.cards = Deck() * self.decks
        self.shuffle()
