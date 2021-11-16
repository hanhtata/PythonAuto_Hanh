from deck import Deck
from player import Player
import os
clear = lambda: os.system('cls')
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''
    
    

    def __init__(self):
        self.players = []
        self.deck = Deck()


    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        print("Wellcome.. Bao nhiêu người chơi")
        number_player = int(input())
        for i in range(number_player) :
            print("Nhập tên người chơi thứ " + str(i+1))
            player_name = input()
            self.players.append(Player(player_name))

    def guide(self):
        print("1.Danh sách người chơi"+ "(" + str(len(self.players)) +")")
        print("2.thêm người chơi")
        print("3.Loại người chơi")
        print("4.chia bài")
        print("5.Lật bài")
        print("6.Xem lại game vừa chơi")
        print("7.Xem lịch sử chơi hôm nay")
        print("8.Tốc biến")
    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        for player in self.players:
            print (player)

    def add_player(self):
        '''Thêm một người chơi mới'''
        print("Nhập tên người chơi thứ " + str(len(self.players)+1))
        player_name = input()
        self.players.append(Player(player_name))

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        print("Bạn muốn xóa người chơi thứ mấy")
        index_player = int(input())
        del self.players[index_player-1]

    def deal_card(self):
        '''Chia bài cho người chơi'''
        
        number_player = len(self.players)
        for player in self.players:
            player.add_card()
        

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        pass
    