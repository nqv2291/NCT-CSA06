Use NorthwindFullData
Select *
FROM dbo.Customers
Where Country =' Mexico' 



Use NorthwindFullData
Select distinct Country
From dbo.Customers


Use NorthwindFullData
Select *
FROM dbo.Customers
Where Country In (' Mexico', 'Canada', 'America')

Use NorthwindFullData
Select *
FROM dbo.Customers
Where Country =' Mexico' 


Use NorthwindFullData
Select CustomerName
FROM dbo.Customers
Where Country =' America' and City !=' San Francisco'

Use NorthwindFullData
Select 
ProductName as Name
,Unit
FROM dbo.Products
Where Unit Like '%bottles'


Use NorthwindFullData
Select 
*
FROM dbo.Products
Order By Price 

Use NorthwindFullData
Select 
Top 5 * 
FROM dbo.Products
Where Category = 'Beverages'
Order By Price DESC

Use NorthwindFullData
Select 
*
FROM dbo.Products
Where Unit Like '%boxes%' and 10< Price And Price <25

Use NorthwindFullData
Select 
*
FROM dbo.Orders
Where FORMAT(OrderDate, 'yyyy-MM') = '1996-08'


Use NorthwindFullData
Select 
ProductID
,Quantity
FROM dbo.OrderDetails
Where Quantity >10 