create schema Expense_app;

<<<<<<< HEAD
<<<<<<< HEAD
use Expense_app;
=======
use expense_app;

>>>>>>> 76d91cb (add database for expense_app)
=======
use Expense_app;
>>>>>>> 4aabe59 (modify Expense_App.sql)


create table Users ( 
	user_id int auto_increment	primary key,
<<<<<<< HEAD
<<<<<<< HEAD
    user_name varchar (255) not null
=======
    user_name varchar (255)
>>>>>>> 76d91cb (add database for expense_app)
=======
    user_name varchar (255) not null
>>>>>>> 4aabe59 (modify Expense_App.sql)
);

create table Expenses ( 
	expense_id int auto_increment primary key,
    user_id int,
    Item_name varchar (255),
    Amount decimal (10,2),
<<<<<<< HEAD
<<<<<<< HEAD
    date DATE,
    foreign key (user_id) references Users(user_id)
=======
    date DATE
>>>>>>> 76d91cb (add database for expense_app)
=======
    date DATE,
    foreign key (user_id) references Users(user_id)
>>>>>>> 4aabe59 (modify Expense_App.sql)
);

create table Income (
	Income_id int auto_increment primary key,
    Sender_name varchar (255),
    Amount decimal (10,2),
    date DATE
);

create table Balance (
	balance_id int auto_increment primary key,
    Total_Income decimal (10,2),
    Current_amount decimal (10,2),
    Expense decimal (10,2),
    Remaining_amount decimal (10,2)
);

