import pymysql
import os
from dotenv import load_dotenv


load_dotenv()

def db_connection():
    conn=mysql.connect(
        host=os.getenv('host_'),
        user=os.getenv('user_'),
        password=os.getenv('password_'),
        db=os.getenv('DB_name'),
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn



def income_insertion(user_id,Sender_name,Amount,date):
    try:
        connection = db_connection()
        cursor=connection.cursor()

        sql_que="INSERT INTO Income (user_id,Sender_name,Amount,date) VALUES (%s,%s,%s,%a)"

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

