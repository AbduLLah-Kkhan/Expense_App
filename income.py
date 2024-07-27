import pymysql
import os
from dotenv import load_dotenv
from datetime import date


load_dotenv()

def db_connection():
    conn=pymysql.connect(
        host=os.getenv('host_'),
        user=os.getenv('user_'),
        password=os.getenv('password_'),
        db=os.getenv('DB_name'),
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn



def income_insertion(Sender_name,Amount,date=date(2024,7,20)):
    try:
        connection = db_connection()
        cursor=connection.cursor()

        sql_que="INSERT INTO Income (Sender_name,Amount,date) VALUES (%s,%s,%s)"

        values=(Sender_name,Amount,date)
        cursor.execute(sql_que,values)

        connection.commit()

        print("Income Entry inserted Successfully")

    except pymysql.MySQLError as ERROR:
        print(f"failed to record Insertion Entry: {ERROR}")
    
    finally:
        if connection.open:
            cursor.close()
            connection.close()

date=date(2024,7,20)
income_insertion("Abdullah",2000.00,date)


def fetch_income():

    try:
        connection= db_connection()
        cursor=connection.cursor()

        sql_que="select * from Income"
        cursor.execute(sql_que)
        result=cursor.fetchall()

        return result 
    
    except pymysql.MySQLError as ERROR:
        print(f"failed to fetch: {ERROR}")

        return None
    
    finally:
        if connection.open:
            cursor.close()
            connection.close()

entry = fetch_income()
print("Records fetched are:",entry)


