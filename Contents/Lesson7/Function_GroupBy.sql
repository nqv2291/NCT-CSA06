-- Count number of products of each category
SELECT Category, COUNT(ProductID) AS Quantity
FROM Products
GROUP BY Category

-- show number of customer in all countries that having more than 10 customers
SELECT Country, COUNT(CustomerID) AS NoCustomer
FROM Customers
WHERE Country != ''
GROUP BY Country
HAVING COUNT(CustomerID) >= 10

-- Replace empty cell in Country by 'Nothing'
SELECT	CASE 
			WHEN Country = '' THEN 'Nothing'
			ELSE Country
		END Country, 
		COUNT(CustomerName) AS Qty
FROM Customers
GROUP BY Country

-- Manipulation with Function
SELECT COUNT(CustomerID) - COUNT(Address) as 'Number of customer without country info'
FROM Customers
