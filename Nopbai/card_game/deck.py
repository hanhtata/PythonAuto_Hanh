from card import Card
from random import shuffle


class Deck:
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9]
    suits = ['S', 'C', 'D', 'H']

    def build(self):
        self.cards = [Card(rank, suit)
                      for rank in Deck.ranks for suit in Deck.suits]

    def shuffle_cards(self):
        shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
