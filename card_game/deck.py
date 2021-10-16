from card_game.card import Card
import random
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''

    def __init__(self):
        self.deck =[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def build(self):
        '''Tạo bộ bài'''
        res = "["
        for index, card in enumerate(self.deck):
            res += str(card)
            if index < len(self.deck) - 1:
                res += ", "
        return res + "]"

    def shuffle_card(self):
        '''Trộn bài'''
        random.shuffle_card(self.deck)

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        return self.deck.pop()