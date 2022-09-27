USE NorthwindFullData
GO

--Mỗi hàng là một câu

SELECT * FROM Customers WHERE Country='Mexico'
SELECT DISTINCT Country FROM Customers
SELECT * FROM Customers WHERE Country='Mexico' OR Country='USA' OR Country='Canada'
SELECT CustomerName FROM Customers WHERE Country='USA' AND Country!='San Francisco'
SELECT ProductName AS 'Name', Unit FROM Products WHERE Unit LIKE '% bottles'
SELECT ProductID, Price FROM Products ORDER BY Price ASC
SELECT TOP 5 ProductID, Category, Price FROM Products WHERE Category LIKE 'Beverages' ORDER BY Price DESC
SELECT ProductID, Unit, Price FROM Products WHERE Price>=10 AND Price<=25 AND Unit LIKE '%boxes%'
SELECT OrderID, OrderDate FROM Orders WHERE OrderDate LIKE '1996-08%'
SELECT ProductID, Quantity FROM OrderDetails WHERE Quantity>10