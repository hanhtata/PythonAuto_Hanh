class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self, name):  # dễ
       self.wins = 0
       self.card = None
       self.name = name

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        pass

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        pass

    def add_card(self):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        pass

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
