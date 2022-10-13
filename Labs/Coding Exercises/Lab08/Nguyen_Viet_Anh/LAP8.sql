--1
SELECT DISTINCT Orders.OrderID, Customers.CustomerID, Customers.CustomerName, Customers.Country
FROM Orders JOIN Customers 
		ON Orders.CustomerID = Customers.CustomerID
ORDER BY Orders.OrderID ASC

--2
SELECT DISTINCT Customers.Country, COUNT(Orders.OrderID)
FROM Customers JOIN Orders 
		ON Orders.CustomerID = Customers.CustomerID
GROUP BY Customers.Country
ORDER BY COUNT(Orders.OrderID) DESC

--3
SELECT DISTINCT Products.ProductID, Products.ProductName, OrderDetails.Quantity, Products.Price 
FROM Products JOIN OrderDetails 
		ON Products.ProductID = OrderDetails.ProductID
WHERE OrderDetails.OrderID = 10248

--4
SELECT DISTINCT OrderDetails.OrderID, SUM(OrderDetails.Quantity * Products.Price) AS TotalAmount
FROM Products JOIN OrderDetails 
		ON Products.ProductID = OrderDetails.ProductID
GROUP BY OrderDetails.OrderID HAVING OrderDetails.OrderID = 10248

--5
SELECT DISTINCT OrderDetails.OrderID, SUM(OrderDetails.Quantity * Products.Price) AS TotalAmount
FROM Products JOIN OrderDetails 
		ON Products.ProductID = OrderDetails.ProductID
WHERE OrderDetails.OrderID IN 
		(SELECT OrderID 
		FROM Orders 
		WHERE OrderDate = '1996-08-01')
GROUP BY OrderDetails.OrderID

--6 
SELECT DISTINCT OrderDetails.OrderID, Customers.CustomerID, Orders.OrderDate
FROM Products JOIN OrderDetails 
		ON Products.ProductID = OrderDetails.ProductID
JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE Orders.OrderDate < '1996-07-08' OR Customers.Country = 'Argentina'

--7
SELECT DISTINCT ProductID, ProductName, Price 
FROM Products
WHERE Price > (SELECT AVG(Price) 
				FROM Products)
ORDER BY Price ASC

-- 8
SELECT DISTINCT OrderDetails.OrderID, Customers.CustomerID, Orders.OrderDate
FROM Products JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE Products.Category = 'Dairy Products'
ORDER BY OrderDetails.OrderID

-- 9
SELECT DISTINCT Customers.CustomerID, Customers.CustomerName
FROM Products JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE Products.Category = 'Dairy Products'
ORDER BY Customers.CustomerID

