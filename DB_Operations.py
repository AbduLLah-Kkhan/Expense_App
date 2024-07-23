import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


conn = pymysql.connect(
    host=os.getenv('host_'),
    user=os.getenv('user_'),
    password=os.getenv('password_'),
    db=os.getenv('DB_name'),
    cursorclass=pymysql.cursors.DictCursor
)


try:


    with conn.cursor() as cursor:
        sql= "select * from expenses where user_id=%s"
        cursor.execute(sql,(1,))

        results = cursor.fetchall()

        if results:
            for record in results:
                print(record)
        else:
            print("no record found")
            
    print("Fetch the requested data")

finally:
    conn.close()
