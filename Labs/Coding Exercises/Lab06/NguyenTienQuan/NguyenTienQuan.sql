--1
SELECT * FROM Customers
WHERE Country = 'Mexico'

--2
SELECT DISTINCT Country FROM Customers

--3 
SELECT * FROM Customers
WHERE Country IN ('Canada', 'USA', 'Mexico')

--4
SELECT CustomerName FROM Customers 
WHERE Country = 'USA' and NOT City = 'San Francisco'	

--5
SELECT ProductName AS 'Name', Unit FROM Products

--6
SELECT * FROM Products
ORDER BY Price ASC

--7
SELECT * FROM Products
WHERE Category = 'Beverages'
ORDER BY Price DESC

--8
SELECT * FROM Products
WHERE Price>=10
	and Price<=25
	and Unit LIKE '%boxes%'

--9
SELECT * FROM Orders
WHERE OrderDate LIKE '1996-08%'

--10
SELECT ProductID, Quantity FROM OrderDetails
WHERE Quantity>10