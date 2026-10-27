USE northwind; 

-- 1. Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name.
SELECT products.ProductID,
products.ProductName, 
products.UnitPrice, 
categories.CategoryName
from products
JOIN categories
on products.CategoryID = categories.CategoryID
ORDER BY 
categories.CategoryName ASC,
products.ProductName ASC; 

-- 2. Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. Order by product name.
select products.ProductID, 
products.ProductName, 
products.UnitPrice,
suppliers.ContactName
from products
join suppliers
on products.SupplierID = suppliers.SupplierID
where UnitPrice> 75
ORDER BY ProductName;

-- 3. Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. Order by product name.
 select products.ProductID,
products.ProductName,
products.UnitPrice, 
categories.CategoryName,
suppliers.ContactName
from products
join categories
on products.CategoryID = categories.CategoryID
join suppliers
on products.SupplierID = suppliers.SupplierID
ORDER BY products.ProductName; 

-- 4. Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to.
-- select * from orders; (personnal comment) 
select orders.OrderID, orders.ShipName, orders.ShipAddress, 
shippers.CompanyName AS Shipper 
from orders
join shippers 
on orders.ShipVia = shippers.ShipperID
where orders.shipcountry = 'Germany'
ORDER BY shipper, orders.shipname; 

-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name.

select orders.ShipName, orders.ShipAddress, 
shippers.CompanyName AS Shipper,
Count(orders.OrderID) AS NumberOfOrders
from orders
join shippers 
on orders.ShipVia = shippers.ShipperID
where orders.shipcountry = 'Germany'
group by orders.ShipName, orders.ShipAddress, shippers.CompanyName
ORDER BY shipper, orders.shipname;

-- 6. Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale
select 
orders.OrderID, 
orders.OrderDate, 
orders.ShipName, 
orders.ShipAddress,
products.productname -- added to check the results properly 
from orders 
join `order details`
  on orders.orderid = `order details`.orderid 
join products
on `order details`.productid = products.productid
where products.ProductName = 'Sasquatch Ale';