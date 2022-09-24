USE adventureworks
SELECT *
FROM SalesLT.Product
WHERE ProductCategoryID IN (7,19,40) AND LEFT(ProductNumber,2) IN ('PU','BK')
ORDER BY ListPrice DESC;