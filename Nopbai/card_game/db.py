from pymysql import connect, cursors, Error
import sys

# Tạo CSDL vs file game_log.sql, khởi chạy CSDL trước
# config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '123456',
#     'database': 'game_log',
#     'cursorclass': cursors.DictCursor
# }

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'game_log',
    'cursorclass': cursors.DictCursor
}

try:
    cnx = connect(**config)
    cur = cnx.cursor()
except Error as e:
    print('Can not connect to MySQL Server')
    print(e.args[1])
    sys.exit()


def log(winner, players):
    sql = '''INSERT INTO games (winner) VALUES (%s)'''
    cur.execute(sql, winner)

    game_id = cur.lastrowid

    sql = f'''
    INSERT INTO logs (game_id, player, cards, point, biggest_card)
    VALUES ({game_id}, %(player)s, %(cards)s, %(point)s, %(biggest_card)s)
    '''
    cur.executemany(sql, players)

    cnx.commit()


def get_last_game():
    sql = '''
    SELECT *
    FROM games AS g
    ORDER BY g.play_at DESC
    '''

    cur.execute(sql)
    game = cur.fetchone()

    if not game:
        raise Exception('No history !\n')

    sql = f'''
    SELECT *
    FROM logs
    WHERE game_id = {game['game_id']}
    '''
    cur.execute(sql)
    players = cur.fetchall()

    return game, players


def history():
    sql = '''
    SELECT
        winner as player,
        COUNT(*) AS game_won
    FROM games AS g
    WHERE DATE(g.play_at) = CURDATE()
    GROUP BY player
    ORDER BY game_won DESC
    '''

    cur.execute(sql)
    records = cur.fetchall()

    if not records:
        raise Exception('No history !\n')

    total_game = sum([r['game_won'] for r in records])
    return total_game, records
