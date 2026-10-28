Use northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price.
select MIN(products.UnitPrice)
from products;

select 
products.ProductName, products.UnitPrice
from products
Where products.UnitPrice = (select min(products.unitprice) from products); 

-- 2. Write a query to find the average price of all items that Northwind sells. Bonus: Once you have written a working query, try asking Claude or ChatGPT for help using the ROUND function to round the average price to the nearest cent.)
select AVG(unitprice)
from products;

select ROUND(AVG(UnitPrice), 2)
from products; 

select ROUND(AVG (unitprice), 2), AVG(unitprice)
from products; -- personnal notes 

-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.
select MAX(products.UnitPrice) 
from products; -- First query

select products.ProductName, 
products.UnitPrice, 
suppliers.CompanyName AS Supplier 
from products
join suppliers
  on products.SupplierID = suppliers.SupplierID
where products.UnitPrice = (select MAX(products.UnitPrice) from products); -- Second query

select products.ProductName, 
products.UnitPrice, 
suppliers.CompanyName AS Supplier 
from products
join suppliers
  on products.SupplierID = suppliers.SupplierID
order by UnitPrice desc; -- Another way I use to check that I got the expected output (Second query).
  
  -- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).
  select sum(employees.Salary) 
  from employees;
  
  -- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!).
  select max(employees.Salary), min(employees.salary) from employees;
  
  -- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply. Hint: Join is your friend here.
  select suppliers.SupplierID, suppliers.CompanyName, COUNT(products.ProductID) AS Supplied_Items
  from suppliers
  join products
    on suppliers.SupplierID = products.SupplierID
  group by suppliers.SupplierID, suppliers.CompanyName;
  
  -- 7. Write a query to find the list of all category names and the average price for items in each category.
  select categories.CategoryName, avg(products.unitprice) 
  from categories
  join products
     on categories.CategoryID = products.CategoryID 
  group by categories.CategoryName; 
  
  -- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of each supplier and the number of items they supply.
  select suppliers.CompanyName AS supplier, count(products.productid) AS supplied_items
  from suppliers
  join products
    on suppliers.SupplierID = products.SupplierID
group by suppliers.CompanyName
having supplied_items >= 5; 

-- 9. Write a query to list products currently in inventory by the product id, product name, and inventory value (calculated by multiplying unit price by the number of units on hand). Sort the results in descending order by value. If two or more have the same value, order by product name. If a product is not in stock, leave it off the list.
select 
products.productid, 
products.ProductName, 
products.UnitPrice * products.unitsinstock as inventory_value
from products

where products.unitsinstock >= 1 -- or > 0
order by inventory_value desc, products.ProductName asc;


-- End
 
 
 















