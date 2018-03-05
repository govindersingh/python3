import mysql.connector
from mysql.connector import Error
import time

def connect():
    try:
        conn = mysql.connector.connect(host='localhost', database='python_mysql', user='root', password='lion')

        if conn.is_connected():
            print('connnected to mysql database')

        c = conn.cursor()

        username = input("enter username :")
        msg = input("enter your tweet to %s :" %username)
        
        c.execute("insert into tweet (time, username, msg) values (%s, %s, %s)",(time.time(), username, msg))
        
        conn.commit()

        c.execute("select * from tweet")
        rows = c.fetchall()
        for i in rows:
            print(i)

    except Error as e:
        print(e)

    finally:
        conn.close()

if __name__=='__main__':
    connect()
