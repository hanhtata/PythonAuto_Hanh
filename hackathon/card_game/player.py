
class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self,name):  # dễ
        self.name = name
        self.cards = []
    def __str__(self):
        return self.name
    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        sum = 0
        for card in self.cards :
            sum+=card.rank
        return sum % 10

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        max_card = self.cards[0]
        for card in self.cards :
            if card > max_card : 
                max_card = card
        return max_card

    def add_card(self, card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.cards.append(card)

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.cards = []
    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        print(self.cards)
   