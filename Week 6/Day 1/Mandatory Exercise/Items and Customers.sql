create table items(
 	id int,
 	item varchar(20),
 	price int
);

create table customers(
	id int,
	first_name varchar(20),
	last_name varchar(20)
);

insert into items
values(1,'Small desk',100);

insert into items
values(2,'Large desk',300);

insert into items
values(3,'Fan',80);

insert into customers
values(1,'Greg','Jones');

insert into customers
values(2,'Sandra','Jones');

insert into customers
values(3,'Scott','Scott');

insert into customers
values(4,'Trevor','Green');

insert into customers
values(5,'Melanie','Johnson');

select * from items;
select * from items where price>80;
select * from items where price<=300;

select * from customers where last_name = 'Smith'
my outcome was an empty table because there was nothing for the table to return

select * from customers where last_name = 'Jones'
select * from customers where first_name != 'Scott'


