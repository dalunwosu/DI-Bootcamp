-- Exercise 1
-- select name from language

-- select film.title, film.description, language.name
-- from film inner join language
-- on film.language_id = language.language_id
-- order by film.title;

-- select film.title, film.description, language.name
-- from film full join language
-- on film.language_id = language.language_id
-- order by film.title;

-- select film.title, film.description, language.name
-- from film inner join language
-- on film.language_id = language.language_id
-- where film.language_id is NULL
-- order by film.title;

-- create table new_film(
-- id serial primary key,
-- name varchar (30)
-- );

-- insert into new_film
-- values (default,'Goodfellas'),(default,'The Godfather'),(default,'The Irishman'),(default,'Scarface'),(default,'The Godfather Part II');
-- select * from new_film

-- create table customer_review(
-- review_id serial Not Null,
-- film_id int Not Null,
-- language_id int Not null,
-- title varchar(30),
-- score int,
-- review_text varchar(1000),
-- last_update timestamp,
-- PRIMARY KEY (review_id),
-- CONSTRAINT fk_film_id FOREIGN key(film_id)REFERENCES new_film (id) on delete cascade,
-- foreign key (language_id) REFERENCES language(language_id)
-- );

-- insert into customer_review
-- values(default,2,1,'The Godfather',10,'One of the best movies I have watched. A total masterpiece', '1972-03-24'),
-- (default,3,1,'The Irishman',9,'Wonderful movie, Enjoyed every second of it, Wonderful performances by De niro, Pesci and Pacino', '2019-09-27');

-- delete from new_film where id = 3;
-- The row was removed from the customer_review table as well

-- Exercise 2
-- update film
-- set language_id = 2
-- where film_id>300 ;

-- update film
-- set language_id = 3
-- where film_id>500 ;

-- update film
-- set language_id = 4
-- where film_id>600 ;

-- update film
-- set language_id = 5
-- where film_id>650 ;

-- update film
-- set language_id = 6
-- where film_id>900 ;

-- The store_id and the address_id are referenced, hence if one wants to insert they have to link it with the other tables

-- drop table customer_review;
-- It needs a little extra checking because it's linked to some other tables

-- select count(rental_id) from rental where return_date is null;

-- select rental.rental_id, film.title, film.rental_rate
-- from (inventory join rental on inventory.inventory_id = rental.inventory_id)
-- join film on film.film_id = inventory.film_id
-- where return_date is null
-- order by rental_rate desc
-- limit 30;

-- select title, rental_rate from film where film_id in
-- (select film_id from inventory join rental
-- on rental.inventory_id = inventory.inventory_id
-- where rental.return_date is null)
-- order by rental_rate DESC
-- limit 30;

-- select film.title, first_name, last_name
-- from (actor join film_actor on actor.actor_id = film_actor.actor_id)
-- join film on film.film_id = film_actor.film_id
-- where film.description ilike '%Sumo%' and actor.first_name = 'Penelope' and actor.last_name = 'Monroe';

-- select title from film 
-- join film_category 
-- on film.film_id = film_category.film_id
-- where film_category.category_id = (select category_id from category where name = 'Documentary')
-- and length < 60 and rating = 'R';
