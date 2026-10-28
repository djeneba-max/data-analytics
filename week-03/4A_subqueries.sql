Use northwind;

-- 1. What is the product name(s) of the most expensive products?
select products.ProductName, products.UnitPrice from products
where products.UnitPrice = (select max(products.UnitPrice) from products); 
-- Product name : Cte de Blaye.

-- 2. What is the product name(s) and categories of the least expensive products?
select products.ProductName, categories.CategoryName
from products
join categories
  on products.CategoryID = categories.CategoryID
where products.UnitPrice = (select min(products.UnitPrice) from products);
-- Product name : Geitost. Category name: Dairy Products. 

-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?

select orders.OrderID, orders.ShipName, orders.ShipAddress
from orders
where ShipVia = (
select shippers.ShipperID  
from shippers  
where shippers.CompanyName = 'Federal Shipping'); 

/* If I needed to display the shipper name:
select orders.OrderID, orders.ShipName, orders.ShipAddress, shippers.CompanyName
from orders
join shippers
on orders.ShipVia = shippers.ShipperID
where shippers.CompanyName = 'Federal Shipping';  */

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
select `order details`.OrderID from `order details` 
where `order details`.ProductID IN ( 
select products.ProductID from products 
where products.ProductName like '%Sasquatch Ale%'); 
                                  
							
-- 5. What is the name of the employee that sold order 10266?
select employees.FirstName, employees.LastName, orders.OrderID
from employees
join orders
on employees.EmployeeID = orders.EmployeeID
where orders.OrderID = 10266; 
-- Employee's name : Janet Leverling.


-- 6. What is the name of the customer that bought order 10266?
select customers.CompanyName, orders.OrderID
from customers
join orders
on customers.CustomerID = orders.CustomerID
where orders.OrderID = 10266; 
-- Customer's (Company) name : Wartian Herkku. 

-- End



