select * from customer;
select first_name ||' '|| last_name as full_name from customer;
select distinct create_date from customer
select customer_id,first_name,last_name,email,address_id from customer order by first_name desc;
select film_id,title,description,release_year,rental_rate from film order by rental_rate;
select address,phone from address where district = 'Texas';
select * from film where film_id = 15 or film_id = 150;
select film_id,title,description,length,rental_rate from film where title = 'The Godfather';
select film_id,title,description,length,rental_rate from film where title ilike 'Th%';
select * from film order by rental_rate  limit 10;
 select  * from film order by rental_rate limit 20;

select customer.first_name,customer.last_name,payment.amount,payment.payment_date 
from customer inner join payment 
on customer.customer_id = payment.customer_id
order by customer.customer_id;

select * from film where film_id not in(select film_id from inventory); 

select city.city,country.country
from city join country
on city.country_id = country.country_id
order by country.country_id;

