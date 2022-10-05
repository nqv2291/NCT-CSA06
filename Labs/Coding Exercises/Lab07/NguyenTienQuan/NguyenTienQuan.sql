--1
SELECT DISTINCT TOP 1 OrderDate AS EarliestDate FROM Orders

--2
SELECT COUNT(OrderID)
FROM Orders

--3
SELECT SUM(Quantity) AS TotalItems, OrderID
FROM OrderDetails
GROUP BY OrderID

--4
SELECT (SUM(Quantity)*1.0/COUNT(DISTINCT(OrderID))) AS AvgItems
FROM OrderDetails

--5
SELECT OrderID, COUNT(DISTINCT ProductID) AS DistinctItems
FROM OrderDetails
GROUP BY OrderID


--6 
SELECT Category, (SUM(Price)/Count(ProductID)) AS AvgPrice
FROM Products
GROUP BY Category
HAVING SUM(Price)/Count(ProductID)>=20 AND SUM(Price)/Count(ProductID)<=30

--7
SELECT Country, Count(CustomerID) AS CustomerCount
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID)>10

--8
SELECT CustomerID, COUNT(OrderID) AS Ordered
FROM Orders
GROUP BY CustomerID
ORDER BY COUNT(OrderID) DESC

--9
SELECT ProductID, COUNT(DISTINCT OrderID) AS Ordered
FROM OrderDetails
GROUP BY ProductID
HAVING COUNT(DISTINCT OrderID)>10

--10
SELECT ProductID, SUM(Quantity) AS TotalItems
FROM OrderDetails
WHERE ProductID = 1
GROUP BY ProductID
