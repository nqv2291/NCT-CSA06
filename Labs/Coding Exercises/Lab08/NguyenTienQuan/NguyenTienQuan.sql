SELECT * FROM Customers
SELECT * FROM Orders
SELECT * FROM Products
SELECT * FROM OrderDetails
--1
SELECT o.OrderID, c.* FROM Orders o JOIN Customers c
	ON o.CustomerID = c.CustomerID
ORDER BY o.OrderID

--2
SELECT c.Country, COUNT(o.OrderID) AS Ordered FROM Customers c JOIN Orders o
	ON c.CustomerID = o.CustomerID
GROUP BY c.Country
ORDER BY COUNT(o.OrderID) DESC

--3
SELECT p.ProductID, p.ProductName, od.Quantity, p.Price FROM Products p JOIN OrderDetails od
	ON p.ProductID = od.ProductID
WHERE od.OrderID = '10248'

--4
SELECT od.OrderID, SUM(od.Quantity*p.Price) AS TotalAmount FROM Products p JOIN OrderDetails od
	ON p.ProductID = od.ProductID
WHERE od.OrderID = '10248'
GROUP BY OrderID

--5
SELECT od.OrderID, SUM(od.Quantity*p.Price) AS TotalAmount FROM Products p JOIN OrderDetails od 
	ON p.ProductID = od.ProductID
WHERE od.OrderID IN (
	SELECT OrderID
	FROM Orders
	WHERE OrderDate = '1996-08-01'
)
GROUP BY od.OrderID

--6
SELECT o.* FROM Orders o JOIN Customers c
	ON o.CustomerID = c.CustomerID
WHERE c.Country = 'Argentina' or o.OrderDate < '1996-07-08'

--7
SELECT ProductID, ProductName, Price FROM Products
WHERE Price > (
	SELECT AVG(Price)
	FROM Products)
ORDER BY Price ASC

--8
SELECT DISTINCT o.* FROM OrderDetails od
	JOIN Orders o ON o.OrderID = od.OrderID
	JOIN Products p ON p.ProductID = od.ProductID
WHERE p.Category = 'Dairy Products'
ORDER BY OrderID

--10
SELECT DISTINCT c.CustomerID, c.CustomerName FROM Customers c
	JOIN Orders o ON c.CustomerID = o.CustomerID
	JOIN OrderDetails od ON o.OrderID = od.OrderID
	JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Category = 'Dairy Products'
ORDER BY c.CustomerID