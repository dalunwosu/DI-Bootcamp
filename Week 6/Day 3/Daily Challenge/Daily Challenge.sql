-- Part 1
create table customer (
id serial primary key,
first_name varchar (100) not null, 
last_name varchar (100) not null
);

create table customer_profile(
id serial,
isLoggedIn boolean default false, 
customer_id int references customer(id),
primary key(customer_id)
);


insert into customer (first_name, last_name) values
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');


insert into customer_profile (isLoggedIn, customer_id) 
values
(true, (select id from customer where first_name = 'John')),
(false, (select id from customer where first_name = 'Jerome'));


select customer.first_name from customer 
join customer_profile 
on customer.id = customer_profile.customer_id
where customer_profile.isLoggedIn = true;

select customer.first_name, customer_profile.isLoggedIn
from customer 
left join customer_profile 
on customer.id = customer_profile.customer_id;


select count(*) from customer 
join customer_profile 
on customer.id = customer_profile.customer_id
where customer_profile.isLoggedIn = false;

-- Part 2

-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
create table book (
book_id SERIAL PRIMARY KEY, 
title varchar (30) NOT NULL,
author varchar (30) NOT NULL
);

insert into book (title, author) values 
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');


create table student (
student_id SERIAL PRIMARY KEY,
name varchar(30) NOT NULL UNIQUE,
age int check (age <= 15)
); 

insert into student (name, age) values
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

create table library (
book_id int references book(book_id) on delete cascade, 
student_id int references student(student_id) on delete cascade, 
borrowed_date date
); 

insert into library (book_id, student_id, borrowed_date)
values
((select book_id from book where title = 'Alice In Wonderland'), 
(select student_id from student where name = 'John'),
'2022-02-15'), 
((select book_id from book where title = 'To kill a mockingbird'), 
(select student_id from student where name = 'Bob'),
'2021-03-03'), 
((select book_id from book where title = 'Alice In Wonderland'), 
(select student_id from student where name = 'Lera'),
'2021-05-23'), 
((select book_id from book where title = 'Harry Potter'), 
(select student_id from student where name = 'Bob'),
'2021-08-12');

select student.name, book.title, library.borrowed_date from library
join student
on library.student_id = student.student_id
join book 
on library.book_id = book.book_id
;

select avg(student.age) from library
join student
on library.student_id = student.student_id
join book 
on library.book_id = book.book_id
where book.title = 'Alice In Wonderland'
;

-- Delete a student from the Student table, what happened in the junction table ?

delete from student where name = 'Bob';
-- Bob got deleted from it
