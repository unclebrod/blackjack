from abc import ABC

from blackjack.hand import Hand


class Participant(ABC):
    """Participant base class for someone playing Blackjack.

    Attributes
    ----------
    id_num : int
        Unique identifier for the participant.
    hands : list[Card]
        Hands held by the participant.

    """

    def __init__(self, id_num: int):
        self.id_num = id_num

    def stand(self):
        pass


class Player(Participant):
    """Player class for someone playing Blackjack."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hands = [Hand()]

    def __str__(self):
        return f"Player {self.id_num}"

    def __repr__(self):
        return f"Player {self.id_num}"

    def double(self):
        pass

    def split(self):
        pass


class Dealer(Participant):
    """Class for the Blackjack dealer."""

    def __init__(self):
        super().__init__(id_num=1)
        self.hand = Hand()

    def __str__(self):
        return "Dealer"

    def __repr__(self):
        return "Dealer"
