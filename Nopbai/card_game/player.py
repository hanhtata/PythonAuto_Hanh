class Player:
    count = 1
    auto = 1

    def __init__(self, name):
        if not name:
            name = f'Chơi thôi... {Player.auto} 🦊'
            Player.auto += 1

        self._id = Player.count
        self._name = name
        self._cards = []

        Player.count += 1

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        return self._cards

    @property
    def info(self):
        return '{:2} {}'.format(self.id, self.name)

    @property
    def point(self):
        total = sum([int(c) for c in self.cards])

        total %= 10
        return 10 if total == 0 else total

    @property
    def biggest_card(self):
        return max(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def remove_cards(self):
        self.cards.clear()

    def flip_cards(self):
        return ' '.join([str(c) for c in self.cards])

    def __gt__(self, other):
        return self.point > other.point or (self.point == other.point and self.biggest_card > other.biggest_card)
