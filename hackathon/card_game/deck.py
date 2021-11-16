from card import Card
import random
class Deck:
    ranks= [1,2,3,4,5,6,7,8,9]
    suits= ['♠', '♣', '♦', '♥']
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''

    def build(self):
        '''Tạo bộ bài'''
        self.cards=[]
        for rank in Deck.ranks:
            for suit in Deck.suits:
                self.cards.append(Card(rank,suit))


    def shuffle_card(self):
        '''Trộn bài'''
        random.shuffle(self.cards)

    def deal_card(self, index_card):
        '''Rút một lá bài từ bộ bài'''
        return self.cards[index_card]
