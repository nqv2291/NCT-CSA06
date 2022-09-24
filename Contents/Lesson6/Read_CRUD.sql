
-- Select all rows & columns of the table
SELECT * FROM Customers
SELECT * FROM Orders
SELECT * FROM Products

-- Rename column(s)
SELECT CustomerName AS 'Ten Khach Hang', City AS TP
FROM Customers


-- Select without duplicate values
-- Retrieve all categories
SELECT DISTINCT Category
FROM Products

-- Select some specific columns with conditions and sort the result
SELECT ProductName, Price			-- choose columns to show
FROM Products
WHERE Price <= 10 AND Price >= 8	-- condition for filtering rows
ORDER BY Price DESC					-- sort the final result in Descending order of Price

-- Retrieve all products that have unit in bottles
SELECT ProductName, Unit
FROM Products
WHERE unit LIKE '%bottles'

/* Retrieve all products that have name begin with a character in range from 'a' to 'c', 
 * and length = 5. Order by name of product
 */
SELECT * FROM Products
WHERE ProductName LIKE '[^a-c]%' 
ORDER BY  ProductName

-- Retrieve all products in category Beverages or Seafood
SELECT ProductName, Category
FROM Products
WHERE Category IN ('Beverages', 'Seafood')

-- Show all orders between 2/2/1997 and 5/2/1997
SELECT * FROM Orders
WHERE OrderDate >= '1997-02-02' AND OrderDate <= '1997-02-05'

-- Find 1 product that is the most costly
SELECT TOP 1 ProductName, Price
FROM Products
Order By Price DESC
