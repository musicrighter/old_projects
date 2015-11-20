SELECT title, description FROM film WHERE description LIKE "%Scientists%" limit 3;
(LIKE is a string search, not case sensitive)


use 'GROUP BY' to collapse rows intp groups that have he same value for specific column(s);
	SELECT rental_duration, count(*) FROM file GROUP BY rental_duration;


SELECT language.name AS language, category.name AS category FROM language, category;
language     category
---------    ---------
english      football
english      soccer
english      basketball


SELECT last_name, first_name, address FROM customer, address WHERE customer.address._id = address.address._id
sqlite> SELECT count(*) FROM customer;
599
sqlite> SELECT count(*) FROM address;



select 2 * 5;
2 * 5
-------------
10


select 'a' = 'A';
'a' = 'A'
-----------------
0