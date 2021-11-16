from game import Game
def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    game = Game() 
    game.setup()
    game.guide()
    choose_opt = int(input())

    while choose_opt != 8 :
        if(choose_opt==1):
            game.list_players()
        if(choose_opt==2):
            game.add_player()
        if(choose_opt==3):
            game.remove_player()
        if(choose_opt==4):
            game.deal_card()
        game.guide()
        choose_opt = int(input())
    print("END GAME")


if __name__ == '__main__':
    main()
