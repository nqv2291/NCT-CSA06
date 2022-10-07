SELECT MIN(OrderDate) AS EarliestDate
FROM Orders

SELECT COUNT(OrderID) AS TotalOrders 
FROM Orders

SELECT OrderID, SUM(Quantity) AS TotalItems 
FROM OrderDetails 
GROUP BY OrderID

SELECT SUM(Quantity) *1/COUNT(DISTINCT OrderID) AS AvgItems 
FROM OrderDetails

SELECT OrderID, COUNT(Quantity) AS DistinctItems
From OrderDetails
GROUP BY OrderID

SELECT Category, AVG(Price) AS Avgprice
FROM Products
GROUP BY CATEGORY
HAVING AVG(Price)=>20 AND AVG(Price)<=30

SELECT Country, COUNT(CustomerID) AS CustomerCount 
FROM Customers 
GROUP BY Country 
HAVING COUNT(CustomerID)>10

SELECT CustomerID, COUNT(OrderID) AS Ordered
FROM Orders
GROUP BY CustomerID
ORDER BY COUNT(OrderID) DESC

SELECT ProductID, COUNT(OrderID) AS Ordered 
FROM OrderDetails 
GROUP BY ProductID 
HAVING COUNT(OrderID)>10

SELECT ProductID,  SUM(Quantity) AS TotalItems
FROM OrderDetails

upcheck123456
