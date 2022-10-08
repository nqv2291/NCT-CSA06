-- bai 1
SELECT TOP 1 OrderDate AS EarliestDate 
FROM Orders ORDER BY OrderDate ASC
-- bai 2
SELECT COUNT(OrderID) AS TotalOrders 
FROM Orders
-- bai 3
SELECT OrderID, SUM(Quantity) AS TotalItems 
FROM OrderDetails 
GROUP BY OrderID
-- bai 4
SELECT (SUM(Quantity) * 1.0 / COUNT(DISTINCT OrderID)) AS AvgItems 
FROM OrderDetails
-- bai 5
SELECT OrderID, COUNT(ProductID) AS DistinctItems 
FROM OrderDetails 
GROUP BY OrderID
-- bai 6
SELECT Category, AVG(ALL Price) AS AvgPrice 
FROM Products 
GROUP BY Category 
HAVING AVG(ALL Price) >= 20 and AVG(ALL Price) <= 30 
-- bai 7
SELECT Country, COUNT(CustomerID) AS CustomerCount 
FROM Customers 
GROUP BY Country 
HAVING COUNT(CustomerID) > 10
-- bai 8
SELECT CustomerID, COUNT(OrderID) AS Ordered 
FROM Orders 
GROUP BY CustomerID ORDER BY COUNT(OrderID) DESC
-- bai 0
SELECT ProductID, COUNT(OrderID) AS Ordered 
FROM OrderDetails 
GROUP BY ProductID 
HAVING COUNT(OrderID) > 10
-- bai 10
SELECT ProductID, SUM(Quantity) AS TotalItems 
FROM OrderDetails 
WHERE ProductID = 1 
GROUP BY ProductID