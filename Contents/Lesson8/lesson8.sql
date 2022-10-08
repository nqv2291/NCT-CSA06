-- JOIN
SELECT *
FROM Orders o INNER JOIN Customers c
	ON o.CustomerID = c.CustomerID
SELECT *
FROM Orders o LEFT JOIN Customers c
	ON o.CustomerID = c.CustomerID
SELECT *
FROM Orders o RIGHT JOIN Customers c
	ON o.CustomerID = c.CustomerID



-- Tim Ten tat ca cac khach hang da mua hang truoc ngay 8/8/1996
-- c1
SELECT CustomerName FROM Customers
WHERE CustomerID IN
	(SELECT CustomerID
	FROM Orders
	WHERE OrderDate < '1996-08-08')
-- c2
SELECT DISTINCT CustomerName
FROM Customers JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderDate < '1996-08-08'

-- Tim tat ca cac khach hang chua co don hang nao
SELECT *
FROM Customers c
WHERE NOT EXISTS (
	SELECT *
	FROM Orders
	WHERE CustomerID = c.CustomerID)
