/*
a) 
*/
/*
a) actor_id, first_name, last_name, and last_update.
b) film_id, title, description, release_year, language_id, original_language_id, 
rental-duration, rental_rate, length, replacement_cost, rating, special_features, last_update.
c) film_actor, film_category, and film_text.
d) The table include information about the rental such as rental date, return date and 
customers id. The information is fairly easy to read because the table is clear, the data 
are well-organized and properly ordered, they are not cluttered. 
The exceptions are the date columns, which can be a little more difficult to read because
 of the date format used.
 e) This table includes inventory_id, film_id, store_id and last_update columns. 
 The information in the tabale is easy to read as the data are not cluttered. Again, except for
 the last_update columm. 
 f) To find the names of all films that were rented on a specific date, we need to use
 the 'rental' and 'inventory' tables. The 'rental' table contains the rental_date
 and the inventory_id, while the 'inventory' table links each inventory_id
 to a film_id. By joining these two tables using the inventory_id,
 we can identify which films were rented on a specific date. We can then use 
 the film_id to identify the name of the corresponding film.
 */
 
 SELECT rental_date, inventory_id FROM sakila.rental; 
 SELECT inventory_id, film_id FROM sakila.inventory; 