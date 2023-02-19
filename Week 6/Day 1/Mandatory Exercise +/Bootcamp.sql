create TABLE students(
	id serial PRIMARY KEY,
	last_name varchar(20),
	first_name varchar(20),
	birth_date date
);

insert into students
values
(default,'Benichou','Marc','02/11/1998'),
(default,'Cohen','Yoan','03/12/2010'),
(default,'Benichou','Lea','27/07/1987'),
(default,'Dux','Amelia','07/04/1996'),
(default,'Grez','David','14/06/2003'),
(default,'Simpson','Omer','03/10/1980'),
(default,'Nwosu','Dalu','14/11/2005');

select * from students;
select first_name, last_name from students;
select first_name, last_name from students where id = 2;
select first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc';
select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Marc' ;
select first_name, last_name from students where first_name like '%a%';
select first_name, last_name from students where first_name like 'A%';
select first_name, last_name from students where first_name like '%a';
select first_name, last_name from students where first_name like '%a_';
 select first_name, last_name from students where id = 1 or id = 3;
select * from students where birth_date >= '1/01/2000';

