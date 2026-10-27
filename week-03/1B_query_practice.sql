USE northwind; 


-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells. 
select * from products; 
SELECT ProductID, ProductName, UnitPrice FROM products; 

-- 2. Write a query to identify the products where the unit price is $7.50 or less.
select ProductName, UnitPrice from products where UnitPrice <= 7.50; 

-- 3. What are the products that we carry where we have no units on hand, but 1 or more units are on backorder?
select ProductName, UnitsInStock, UnitsOnOrder from products 
where UnitsInStock = 0 and UnitsOnOrder >= 1; 
-- Product: Gorgonzola Telino


-- 4. Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories? Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry.
-- The products table has a CategoryID column that references the corresponding CategoryName in the categories table. We can find a list of all categories in the categories table. 
select * from categories; 
select ProductName from products where CategoryID = 8; 

-- 5. Examine the products table again. How do you know what supplier each product comes from? Where can you find info on suppliers? Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.
-- The products table has a SupplierID column that references the corresponding supplier (CompanyName) in the suppliers table. The suppliers table contains information about each suppliers, such as the CompanyName and ContactName. 
select * from suppliers; 
select ProductName from products where SupplierID = 4;

-- or 
select ProductName from products where SupplierID = (select SupplierID from suppliers where CompanyName = 'Tokyo Traders');

-- or 
select products.ProductName FROM products 
join suppliers
on products.SupplierID = suppliers.SupplierID
where CompanyName = 'Tokyo Traders'; 
 
 
-- 6.  How many employees work at northwind? What employees have "manager" somewhere in their job title? Write queries to answer each question
select * from employees; 
select COUNT( * ) as totalemployees from employees; 
-- Nine employees work at northwind. 
select EmployeeID, FirstName, LastName, Title from employees where Title like '%manager%';
-- Steven Buchanan, Sales Manager. 