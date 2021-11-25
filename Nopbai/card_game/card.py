class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return 1 if self._rank == 'A' else self._rank

    @property
    def suit(self):
        points = {'S': 0, 'C': 1, 'D': 2, 'H': 3}
        return points.get(self._suit)

    def __str__(self):
        symbol = {'S': '♠', 'C': '♣', 'D': '♦', 'H': '♥'}
        return f"{self._rank}{symbol[self._suit]}"

    def __int__(self):
        return self.rank

    def __gt__(self, other):
        return self.suit > other.suit or (self.suit == other.suit and self.rank > other.rank)