drop table Income;
drop table Users;
drop table Expenses;
drop table Sender;
create schema Expense_app;


use Expense_app;

create table Users (
	user_id int auto_increment primary key,
    user_name varchar(255),
    user_email varchar(255) unique
);


create table Expenses ( 
	expense_id int auto_increment primary key,
    user_id int,
    item_name varchar (255),
	item_quantity int,
    item_price decimal (10,2),
    total_amount decimal (10,2),
    date DATE not null,
    foreign key (user_id) references Users(user_id)
);

-- total sum etc, total amount, remaining amount can be retrieved from income and expense table
CREATE TABLE Income (
    Income_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id int,
	sender_id int,
    Amount DECIMAL(10,2),
    date DATE NOT NULL,
    foreign key (user_id) references Users(user_id),
	foreign key (sender_id) references Sender(sender_id)
);

-- Sender seperate table. (Multiple senders possible)
-- sender's foriegn key in income, as multiple amount possible

create table Sender (
	sender_id int auto_increment primary key,
    sender_name varchar(255)
)




