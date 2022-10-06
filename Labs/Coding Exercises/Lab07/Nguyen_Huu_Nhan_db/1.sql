
-- 1
SELECT MIN(OrderDate) AS EarliestDate
FROM Orders
-- 2
SELECT COUNT(OrderID) AS TotalOders
FROM Orders
-- 3
SELECT OrderID, SUM(Quantity) AS TotalItems
From OrderDetails
GROUP BY OrderID

-- 4
SELECT SUM(Quantity)*1.0/COUNT(DISTINCT OrderID) AS AvgItems
From OrderDetails

-- 5
SELECT OrderID, COUNT(Quantity)
From OrderDetails
GROUP BY OrderID

-- 6
SELECT Category, AVG(Price) AS Avgprice
FROM Products
GROUP BY CATEGORY
HAVING 20 <= AVG(Price) AND AVG(Price) <= 30
-- 7
SELECT Country, Count(Country) AS CustomerCount
FROM Customers
Group By Country
HAVING Count(Country) > 10
-- 8
SELECT CustomerID, COUNT(OrderID) AS Ordered
FROM Orders
GROUP BY CustomerID
ORDER BY COUNT(OrderID) DESC

-- 9
SELECT ProductiD, COUNT(ORDERID)
FROM OrderDetails
GROUP BY productID
HAVING COUNT(ORDERID) > 10

-- 10
SELECT ProductID,  SUM(Quantity) AS TotalItems
FROM OrderDetails
WHERE PRODUCTID = 1
GROUP BY ProductID
