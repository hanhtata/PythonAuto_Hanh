import os
import sys
import db
import error
from deck import Deck
from player import Player


class Game:
    min_players = 2
    max_players = 12
    cards_per_player = 3

    def __init__(self):
        self.is_playing = False
        self.is_dealt = False
        self.is_flipped = False
        self._deck = Deck()
        self._players = []

        self.choices = {
            '1': self.list_players,
            '2': self.add_player,
            '3': self.remove_player,
            '4': self.dealing_card,
            '5': self.flip_cards,
            '6': self.last_game,
            '7': self.history,
            '8': self.quit
        }

    @property
    def deck(self):
        return self._deck

    @property
    def players(self):
        return self._players

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def setup(self):
        self.cls()
        print('Welcome!!!')
        print('Chào mừng đến với game đánh bài 3 cây')
        print('Có bao nhiêu người chơi ?')

        while True:
            try:
                num_of_players = int(input('> '))

                if num_of_players < Game.min_players:
                    raise error.MinimumPlayerError(
                        f'Tối thiểu {Game.min_players} người chơi')
                elif num_of_players > Game.max_players:
                    raise error.MaximumPlayerError(
                        f'Tối đa {Game.max_players} người chơi')
                else:
                    for i in range(num_of_players):
                        self.add_player()
                    break

            except error.Error as e:
                print(e.message)
            except ValueError as e:
                print('Có muốn chơi không ?')
                print('Nhập một số :')

    def menu(self):
        num_of_player = len(self.players)

        print(f'1. Danh sách người chơi ({num_of_player})')
        print('2. Thêm người chơi')
        print('3. Loại người chơi')
        print('4. Chia bài')
        print('5. Lật bài')
        print('6. Xem lại game vừa chơi')
        print('7. Xem lịch sử chơi')
        print('8. Exit')

    def list_players(self):
        print('{:2} {}'.format('ID', 'Tên'))

        for player in self.players:
            print(player.info)

    def add_player(self):
        if self.is_playing:
            raise error.PlayingError()
        elif len(self.players) >= Game.max_players:
            raise error.MaximumPlayerError()
        else:
            name = input(
                f'Tên người chơi {len(self.players) + 1}: ').strip()[0:6]
            self.players.append(Player(name))

    def remove_player(self):
        if self.is_playing:
            raise error.PlayingError()
        elif len(self.players) <= Game.min_players:
            raise error.MinimumPlayerError()
        else:
            self.list_players()
            print()

            id = int(input('Nhập ID người chơi: '))
            print(id)
            self.cls()

            try:
                player = self.players[id - 1]
                self.players.remove(player)
                print('Thôi xong, hết tiền !!')
            except IndexError as e:
                raise error.PlayerDoesNotExistsError()

    def dealing_card(self):
        if self.is_dealt:
            raise error.DealtError()
        else:
            for player in self.players:
                player.remove_cards()

            self.deck.build()
            self.deck.shuffle_cards()

            for i in range(Game.cards_per_player):
                for player in self.players:
                    card = self.deck.deal_card()
                    player.add_card(card)

            self.is_dealt = True
            self.is_flipped = False
            self.is_playing = True

            print('Đã chia xong bài...')

    def flip_cards(self):
        if not self.is_dealt:
            raise error.NotDealtError()
        if self.is_flipped:
            raise error.FlippedError()
        else:
            self.winner = max(self.players)

            for player in self._players:
                print(f'Người chơi: {player.name}')
                print(
                    f'Bộ bài: {player.flip_cards()} Điểm: {player.point:2} Lá lớn nhất: {player.biggest_card}')
                print()

            print(f'🏆 Chúc mừng {self.winner.name} có xiền !\n')

            self.is_dealt = False
            self.is_flipped = True
            self.is_playing = False

            players = [{'player': p.name, 'cards': p.flip_cards(
            ), 'point': p.point, 'biggest_card': p.biggest_card} for p in self.players]

            db.log(self.winner.name, players)

    def last_game(self):
        if self.is_playing:
            raise error.PlayingError()
        else:
            last_game, players = db.get_last_game()

            print(last_game['play_at'])
            print()

            for p in players:
                print(f'Người chơi: {p["player"]}')
                print(
                    f'Bộ bài: {p["cards"]} Điểm: {p["point"]} Lá bài lớn nhất: {p["biggest_card"]}')
                print()

            print(f'🏆 Người chơi chiến thắng: {last_game["winner"]} :)')

    def history(self):
        if self.is_playing:
            raise error.PlayingError()
        else:
            total_game, records = db.history()
            print(f'Hôm nay đã chơi: {total_game} ván bài\n')

            for r in records:
                print(f'{r["player"]:6} thắng {r["game_won"]} ván')

    def run(self):
        self.setup()
        self.cls()

        while True:
            self.menu()

            try:
                c = input("> ")
                choice = self.choices.get(c)
                self.cls()

                if choice:
                    choice()
                    print()
                else:
                    raise error.FunctionDoesNotExists()
            except ValueError as e:
                raise error.FunctionDoesNotExists()
            except error.Error as e:
                print(e.message)

    def quit(self):
        print("Cũng vui đấy !!")
        sys.exit()
