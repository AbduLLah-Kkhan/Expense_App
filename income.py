import pymysql
import os
from dotenv import load_dotenv
from datetime import datetime
import re


load_dotenv()

def db_connection():
    conn=pymysql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        db=os.getenv('DB_NAME'),
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn


def validate_name(name):
    name_regex= r'^([A-Z][a-z]*\s)+[A-Z][a-z]*$'
    return re.match(name_regex,name)

def validate_email(email):
    regex_email=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(regex_email,email)


def insert_user(user_name,user_email):
    # Now checking for valid name and email. We call in the validate function for both name and email
    
    if not validate_name(user_name):
        print("invalid name, Write in correct formate.")
        return #using the return statement here, to ensure that the function doesnt proceed with the invalid data.

    if not validate_email(user_email):
        print("The email is incorrect format, Please write in correct formate.")
        return 
    try:
        connection=db_connection()
        cursor=connection.cursor()

        sql_query="insert into Users (user_name,user_email) values (%s,%s)"
        values=(user_name,user_email)
        cursor.execute(sql_query,values)
        connection.commit()

        print("Entries Inserted in the User table successfully")

    except pymysql.MySQLError as ERROR:
        print (f"failed to insert the Entry {ERROR}")

    finally:
        if connection.open:
            cursor.close()
            connection.close()
#insert_user("Hamza Khan","hamza.dbz1@gmail.com")


"""
validating date and Positive values for item_price,total_amount.
"""

def validate_positive_val(value):

    try:
        if isinstance(value,(int,float)):
            if value > 0:
                print(value)
            else:
                print("value is not positive")
        else:
            raise ValueError("non-numeric value is not acceptable as an input:")
    except ValueError as ERROR:
        print(f"Only positive values are accepted as an input:")


def validate_date():
    while True:
        try:
            DDate=input("Enter Date yyyymmdd:")
            DDate=datetime.strptime(DDate,'%Y%m%d').date()
            print("Valid Date has been Entered:",DDate)
            return DDate
        except ValueError:
            print("Invalid Date, Please Enter Valid date")





def expense_insertion(user_id,item_name,item_quantity,item_price,expense_date):



    #INCASE DATE VALIDATION VERIFICATION NEEDED.
    #    if not isinstance(expense_date, datetime.date):
    #    print("Invalid date format. Please provide a valid date object.")
    #    return

    connection= None

    try:
        validate_positive_val(item_price)
    
        if not isinstance(item_quantity,int) or item_quantity <=0:
            print("Item Quantity ought to be integer and Non-negative Value")
            return

        
        connection=db_connection()
        if connection is None:
            print("Failed to connect to the Database")
            return
        cursor=connection.cursor()

        total_amount=item_quantity*item_price

        sql_query= "insert into Expenses(user_id,item_name,item_quantity,item_price,total_amount,date) values (%s,%s,%s,%s,%s,%s)"
        values=(user_id,item_name,item_quantity,item_price,total_amount,expense_date)
        cursor.execute(sql_query,values)

        connection.commit()

        print("Entries insert in the Expense table successfully")

    except ValueError as error:
        print(f"value error:{error}")
    except pymysql.MySQLError as ERROR:
        print(f"couldn't insert the entries,{ERROR}")

    finally:
        if connection.open:
            cursor.close()
            connection.close()

Date=validate_date()

entry=expense_insertion("1","Roti",2,40,Date)




def income_insertion(Sender_name,Amount,date):
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

income_date=date(2024,7,20)
#income_insertion("Abdullah",2000.00,date)


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

#entry = fetch_income()
#print("Records fetched are:",entry)



# validate data for months
# date validation
# validaiton of each entry


