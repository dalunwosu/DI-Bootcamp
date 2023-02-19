-- Create a table house_expenses(id,water,electricity,paid_by)
-- create table house_expenses(
-- id int,
-- date_pay date,
-- water float,
-- electricity float,
-- paid_by varchar(20)
-- );

-- insert into house_expenses(id,date_pay,water,electricity,paid_by)
-- values (1,'14/11/2005',100.75,234.72,'Dalu');
-- insert into house_expenses(id,date_pay,water,electricity,paid_by)
-- values (2,'25/05/2005',100.75,234.72,'Charles')

-- insert into house_expenses values (4,'19/02/2005',150.00,350.86,'Dalu'),
-- (5,'19/03/2005',150.00,350.86,'Fari'),
-- (6,'19/04/2005',150.00,350.86,'Zic'),
-- (7,'19/06/2005',150.00,350.86,'Zara'),
-- (8,'19/07/2005',150.00,350.86,'Ceci')
-- select * from house_expenses;

-- select max(electricity) from house_expenses;
-- select min(electricity) from house_expenses;
-- select avg(electricity) from house_expenses where paid_by != 'Dalu';

-- select paid_by, sum(electricity)+ sum(water) as total_paid from house_expenses
-- group by paid_by;
-- select paid_by, max(electricity + water)
-- from house_expenses
-- group by paid_by
-- update house_expenses
-- set paid_by = 'Josh' where id = 1;

-- update house_expenses
-- set electricity = 0 where paid_by = 'Tom';

delete from house_expenses where electricity<300;
delete from house_expenses where date_pay > '2005-06-06';
select * from house_expenses order by id;
