import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(host='localhost', database='creator', user='root', password='lion')
        c = conn.cursor()

        def create_table():
            
            #table_name = input("Enter new table name :")
            #fields_name = input("enter fields")
            tb = input("enter command for new table :")
            c.e xecute(tb)
            conn.commit()
            
            if c.execute:
                print("Table create successfully")

            c.execute("show tables")
            row = []
            rows = c.fetchall()
            for i in rows:
                row +=i
            print(row)

            choice()
            
        def insert_table_data():
            c.execute("show tables")
            row = []
            rows = c.fetchall()
            for i in rows:
                row +=i
            print(row)

            tb =  input("Which table you want to you for data entry :")
            
            c.execute("describe %s" %tb)
            show = c.fetchall()
            for i in enumerate(show,1):
                print(i)
            
            command = input("Enter insert command :")
            c.execute(command)
            conn.commit()

            if conn.commit:
                print("Data inserted successfully")

            c.execute("select * from %s" %tb)
            data = c.fetchall()
            for j in data:
                print(j)

        def update_table_data():
            c.execute('show tables')
            show = c.fetchall()
            for i in show:
                print(i)
            
            tb = input('which table you want to update :')
            c.execute('select * from %s' %tb)
            show = c.fetchall()
            for i in show:
                print(i)
                
            print('command eg. update table_name set col=val, col=val, ... where condition \n')
            command = input('Enter update command :')
            c.execute(command)
            conn.commit()
            
            if conn.commit:
                print("Data updated successfully")

            c.execute("select * from %s" %tb)
            data = c.fetchall()
            for j in data:
                print(j)
            
            
        update_table_data()
        #def delete()

        def choice():
            x = input('choice :\n create table press 1\n insert table data press 2\n update table data press 3\n delete press 4\n =')
            if x == '1':
                create_table()
            elif x == '2':
                insert_table_data()
            elif x == '3':
                update_table_data()

                
        def welcome():
            print('welcome to mysql databse')
            x = input('would you like to continue y/n :')
            if x == 'y':
                choice()
            else:
                print('thanku you')
                exit
        #welcome()


    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__=='__main__':
    connect()
