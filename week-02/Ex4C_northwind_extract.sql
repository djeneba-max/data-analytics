USE northwind;
select * from categories; 


/*
4. 
a) products
b) categories
*/

select * from employees; 

/* 
5.
a) Margaret Peacock.
*/

select * from products; 

/* 
6. 
a) The query returns 77 records. Using the toolbar at the top of the query pane, I can click 
the “Limit to 1000 rows” dropdown and select “Limit to 10 rows” to retrieve only 10 rows.
b) I can add a LIMIT clause at the end of the query, for example: 
SELECT * FROM northwind.products LIMIT 10;
*/
select * from categories; 
/*
7. 
c) The categoryID of seafood is 8. 
*/

select * from orders;
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM northwind.orders
LIMIT 50;
