class Error(Exception):
    '''Base class cho game error'''
    pass


class MaximumPlayerError(Error):
    '''Nhiều người chơi quá !'''

    message = 'Sòng bạc đông quá rồi, ai hết tiền đi ra đi !\n'

    def __init__(self, message=message):
        self.message = message


class MinimumPlayerError(Error):
    '''Ít người chơi thế '''

    message = 'Sòng bạc vắng khách, hiuhiu :v\n'

    def __init__(self, message=message):
        self.message = message


class PlayerDoesNotExistsError(Error):
    '''Không tồn tại người chơi này'''

    message = '''Không tồn tại ID người chơi này\n'''

    def __init__(self, message=message):
        self.message = message


class PlayingError(Error):
    '''Lỗi thao tác khi game đang chơi'''

    message = 'Game đang chơi, nhưng chờ tí đi ra ngoài cái nhé\n'

    def __init__(self, message=message):
        self.message = message


class DealtError(Error):
    '''Lỗi chia bài nhiều lần'''

    message = 'Đã chia bài rồi !)\n'

    def __init__(self, message=message):
        self.message = message


class NotDealtError(Error):
    '''Lỗi lật bài khi chưa chia'''

    message = 'Bài chưa được chia\n'

    def __init__(self, message=message):
        self.message = message


class FlippedError(Error):
    '''Lỗi lật bài nhiều lần'''

    message = 'Bài lật rồi\n'

    def __init__(self, message=message):
        self.message = message


class FunctionDoesNotExists(Error):
    '''Lỗi chọn chức năng không tồn tại'''

    message = 'Chức năng không tồn tại\n'

    def __init__(self, message=message):
        self.message = message


class CancelError(Error):
    '''Lỗi khi hủy chức năng, ví dụ hủy thêm người chơi, hay xóa người chơi'''

    def __init__(self, message=''):
        self.message = message
