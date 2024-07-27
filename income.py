import pymysql
import os
from dotenv import load_dotenv
from datetime import datetime


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



def income_insertion(user_id,Sender_name,Amount,date=datetime(2024,7,20)):
    try:
        connection = db_connection()
        cursor=connection.cursor()

        sql_que="INSERT INTO Income (user_id,Sender_name,Amount,date) VALUES (%s,%s,%s,%s)"

        values=(user_id,Sender_name,Amount,date)
        cursor.execute(sql_que,values)

        connection.commit()

        print("Income Entry inserted Successfully")

    except pymysql.MySQLError as ERROR:
        print(f"failed to record Insertion Entry: {ERROR}")
    
    finally:
        if connection.open:
            cursor.close()
            connection.close()

date=datetime(2024,7,20)
income_insertion(1,"Abdullah,",2000.00,date)

