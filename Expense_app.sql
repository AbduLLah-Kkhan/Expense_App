create schema Expense_app;

use Expense_app;


create table Users ( 
	user_id int auto_increment	primary key,
    user_name varchar (255) not null
);

create table Expenses ( 
	expense_id int auto_increment primary key,
    user_id int,
    Item_name varchar (255),
    Amount decimal (10,2),
    date DATE not null,
    foreign key (user_id) references Users(user_id)
);

CREATE TABLE Income (
    Income_id INT AUTO_INCREMENT PRIMARY KEY,
    Sender_name VARCHAR(255),
    Amount DECIMAL(10,2),
    date DATE NOT NULL
);


create table Balance (
	balance_id int auto_increment primary key,
    Total_Income decimal (10,2),
    Current_amount decimal (10,2),
    Expense decimal (10,2),
    Remaining_amount decimal (10,2)
);

