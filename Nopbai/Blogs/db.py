from pymysql import connect, cursors
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "data_post",
    "cursorclass": cursors.DictCursor
}
con = connect(**db_config)
cur=con.cursor()
def get_post():
    sql='''select* from data1'''
    cur.execute(sql)
    data=cur.fetchall()
    return data

def add_post(time, title, content):
    sql='''INSERT INTO data1(time, title, content) VALUES (%s, %s,%s)'''
    cur.execute(sql,(time, title, content))
    con.commit()
def edit_post1(b, time, title, content):
    sql='''UPDATE data1 SET time = %s, title = %s, content = %s WHERE id=%s'''
    cur.execute(sql,(time, title, content, b))
    con.commit()