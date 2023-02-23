-- part 1
select first_name as first,last_name as last from employees;
select distinct department_id from employees;
select * from employees order by first_name desc;
select first_name, last_name,salary,(salary * 0.15) as PF from employees;
select employee_id,first_name,last_name,salary from employees order by salary;
select sum(salary) from employees;
select max(salary), min(salary) from employees;
select avg(salary) from employees;
select count(employee_id) from employees;
select upper (first_name) from employees;
select substring (first_name for 3) from employees;
select first_name ||' '|| last_name as full_name from employees;
select first_name,last_name, length( first_name ||''|| last_name) from employees;
select * from employees REGEXP_LIKE(first_name,'(0-9)')
select * from employees where first_name ~ ‘\d’;
select * from employees limit 10;

-- part 2
select first_name,last_name,salary from employees where 10000<salary and salary<15000;
select first_name,last_name,hire_date from employees where date_part('year',hire_date) = 1987;
select  first_name ||' '|| last_name as full_name from employees where first_name ilike ('%c%') and first_name ilike('%e%');

select employees.last_name,jobs.job_title, employees.salary
from employees inner join jobs 
ON jobs.job_id = employees.job_id
where jobs.job_title not in ('Programmer', 'Shipping Clerk') 
and salary not in (4500 , 10000 , 15000);

select last_name from employees where length(last_name) = 6
select last_name from employees where last_name ilike('__e%');

select jobs.job_title
from employees inner join jobs 
ON jobs.job_id = employees.job_id;

select * from employees where last_name in ('Jones','Blake','Scott','King','Ford');