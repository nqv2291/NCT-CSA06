USE NorthwindFullData
GO

-- 1.
SELECT * FROM Customers 
WHERE Country='Mexico'
-- 2.
SELECT DISTINCT Country FROM Customers
-- 3.
SELECT * FROM Customers 
WHERE Country IN ('Canada', 'USA', 'Mexico')
-- 4.
SELECT CustomerName FROM Customers 
WHERE Country='USA' AND Country!='San Francisco'
-- 5. 
SELECT ProductName AS 'Name',
Unit FROM Products WHERE Unit LIKE '% bottles'
-- 6.
SELECT ProductID, Price FROM Products 
ORDER BY Price ASC
-- 7.
SELECT TOP 5 ProductID, Category, Price FROM Products 
WHERE Category LIKE 'Beverages' 
ORDER BY Price DESC
-- 8.
SELECT ProductID, Unit, 
Price FROM Products WHERE Price>=10 AND Price<=25 AND Unit LIKE '%boxes%'
-- 9.
SELECT OrderID, 
OrderDate FROM Orders WHERE OrderDate LIKE '1996-08%'
-- 10.
SELECT ProductID, Quantity FROM OrderDetails 
WHERE Quantity>10