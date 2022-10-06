--bai1
SELECT TOP 1 OrderDate AS EarliestDate FROM Orders
ORDER BY OrderDate ASC

--bai2
SELECT COUNT(OrderID) AS TotalOrders FROM Orders

-- bai3
SELECT OrderID, SUM(Quantity) AS TotalItems 
FROM OrderDetails GROUP BY OrderID

--bai4
SELECT (SUM(Quantity)*1.0/COUNT(DISTINCT(OrderID))) AS AvgItems  
FROM OrderDetails 

--bai5
SELECT OrderID, COUNT(DISTINCT(ProductID)) 
FROM OrderDetails GROUP BY OrderID

-- bai6
SELECT Category, AVG(ALL Price) AS AvgPrice 
FROM Products 
GROUP BY Category
HAVING 20 <= AVG(ALL Price) AND 30 >= AVG(ALL Price)

-- bai7 
SELECT Country, Count(CustomerID) AS CustomerCount
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID)>10

--bai8
SELECT CustomerID, COUNT(OrderID) AS Ordered
FROM Orders
GROUP BY CustomerID
ORDER BY COUNT(OrderID) DESC

--bai9
SELECT ProductID, COUNT(DISTINCT OrderID) AS Ordered
FROM OrderDetails
GROUP BY ProductID
HAVING COUNT(DISTINCT OrderID)>10

--bai10
SELECT ProductID, SUM(Quantity) AS TotalItems
FROM OrderDetails
GROUP BY ProductID
HAVING ProductID = 1


