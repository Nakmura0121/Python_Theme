import os
import psycopg2 

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

#ユーザー
def insert_user(name, mail, pw):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO book_user VALUES (default, %s, %s, %s)'
    cursor.execute(sql, (name, mail, pw))
    connection.commit()
    cursor.close()
    connection.close()