 create table users (
 user_id serial primary key,
 first_name varchar(30),
 last_name varchar(30)
);
create table product_orders (
 order_id serial primary key,
 user_id int references users(user_id) on delete cascade 
);
create table items (
 item_id serial primary key,
 name varchar(100) not null,
 price int not null,
 order_id int references product_orders(order_id) on delete set null
);
insert into users (first_name, last_name) values 
('Dalu', 'Nwosu'), 
('Noa', 'Nakache'),
('Diego', 'Ripari'); 
insert into product_orders(user_id) values
((select user_id from users where first_name = 'Dalu')),
((select user_id from users where first_name = 'Diego')),
((select user_id from users where first_name = 'Dalu'));
insert into items (name, price, order_id) values 
 ('TV', 500, 1),
 ('Radio', 100, 1),
 ('AC', 350, 2),
 ('Phone', 200, 3), 
 ('Laptop', 350, 3);

CREATE or REPLACE FUNCTION total_order_price(orderid int) 
RETURNS int AS $$
BEGIN
   RETURN(select sum(price) as total_price from items where order_id = orderid);
END;
$$ LANGUAGE plpgsql;


CREATE or REPLACE FUNCTION user_order_price(userid int , orderid int) 
RETURNS int AS $$
declare
	user_orders int := (select order_id from product_orders where user_id = userid and order_id = orderid);
BEGIN
	RETURN (total_order_price(user_orders));
END
$$ LANGUAGE plpgsql;

select * from user_order_price(1,1);
