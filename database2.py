import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(host='localhost', database='creator', user='root', password='lion')
        c = conn.cursor()

        def create_table():
            table_name = input("Enter new table name :")
            c.execute("create table %s" %table_name)
            conn.commit()

            c.execute("show tables")
            row = c.fetchall()
            for i in row:
                print(i)

        #def insert_table_data()

        #def update_table_data()

        #def delete()

        def choice():
            x = input('choice :\n create table press 1\n insert table data press 2\n update table data press 3\n delete press 4')
            if x == '1':
                create_table()

        def welcome():
            print('welcome to mysql databse')
            x = input('would you like to continue y/n :')
            if x == 'y':
                choice()
            else:
                print('thanku you')
                exit
        welcome()


    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__=='__main__':
    connect()
