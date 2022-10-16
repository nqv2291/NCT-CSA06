

SELECT *
FROM Orders

SELECT *
From Customers

SELECT *
FROM OrderDetails

SELECT *
FROM Products

-- 1
SELECT O.OrderID, O.CustomerID, C.CustomerName, C.Country
FROM Orders O Inner Join  Customers C ON O.CustomerID = C.CustomerID 
Order By O.OrderID ASC

-- 2
SELECT c.country, COUNT(o.OrderID) AS ordered
FROM Orders O
INNER JOIN Customers C ON O.CustomerID = C.CustomerID
GROUP BY c.country
ORDER BY Ordered DESC

-- 3
SELECT P.ProductID, P.ProductName, OD.Quantity, P.Price
From OrderDetails OD 
INNER JOIN Products P ON OD.ORDERID = '10248' AND OD.ProductID = P.ProductID

--4
SELECT OD.OrderID, SUM(OD.Quantity*P.Price)
From OrderDetails OD 
INNER JOIN Products P ON OD.ORDERID = '10248' AND OD.ProductID = P.ProductID
GROUP BY OD.OrderID

-- 5
SELECT OD.OrderID, SUM(P.Price*OD.Quantity) AS TotalAmount
From OrderDetails OD 
INNER JOIN Orders O ON O.OrderDate = '1996-08-01' AND O.OrderID = OD.OrderID
INNER JOIN Products P ON P.ProductID = OD.ProductID
GROUP BY OD.OrderID

-- 6
SELECT *
FROM Orders
WHERE OrderDate < '1996-07-08'
UNION ALL
SELECT O.*
FROM ORDERS O
INNER JOIN Customers ON CUSTOMERS.CustomerID = o.CustomerID
WHERE Customers.Country = 'Argentina'

-- 7
SELECT *
FROM Products
WHERE Price > (
    SELECT AVG(PRICE)
    FROM PRODUCTS
)
ORDER BY PRICE ASC

-- 8

SELECT DISTINCT O.*
FROM OrderDetails OD
INNER JOIN Orders O ON O.OrderID = OD.OrderID
INNER JOIN Products P ON OD.ProductID = P.ProductID
WHERE P.Category = 'Dairy Products'
ORDER BY O.OrderID ASC

-- 9
SELECT *
FROM CUstomers
WHERE CustomerID in (
SELECT DISTINCT O.CustomerID
FROM OrderDetails OD
INNER JOIN Orders O ON O.OrderID = OD.OrderID
INNER JOIN Products P ON OD.ProductID = P.ProductID
WHERE P.Category = 'Dairy Products'
)

