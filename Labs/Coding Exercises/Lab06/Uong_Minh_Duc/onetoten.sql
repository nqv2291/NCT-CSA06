USE NorthwindFullData
GO

SELECT * FROM Customers
WHERE Country = 'Mexico'

SELECT DISTINCT Country
FROM Customers

SELECT * FROM Customers
WHERE Country = ('Mexico', 'Canada', ' USA')

SELECT CustomerName FROM Customer
WHERE Country = 'USA' AND Country != 'San Francisco'

SELECT ProductName AS 'Name', Unit 
FROM Products

ORDER BY Price ASC


