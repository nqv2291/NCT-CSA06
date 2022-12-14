CREATE DATABASE northwind1
GO
USE northwind1
GO

create table Customers (
		CustomerID Int PRIMARY KEY,
		CustomerName NVARCHAR(127),
		Address NVARCHAR(127),
		City NVARCHAR(127),
		Country NVARCHAR(127)
)

create table products (
		productID INT PRIMARY KEY,
		ProductName NVARCHAR(127),
		Category NVARCHAR(127),
		Unit NVARCHAR(1023),
		Price DECIMAL
)

create table orders (
		OrderID INT PRIMARY KEY,
		CustomerID INT,
		OrderDate DATE,
		CONSTRAINT OrdersFKCustomers FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
)
CREATE TABLE OrderDetails (
	OrderDetailID INT PRIMARY KEY,
	OrderID INT,
	ProductID INT,
	Quantity DECIMAL,
	CONSTRAINT OrderDetailsFKOrders FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
	CONSTRAINT OrderDetailsFKProducts FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
)

INSERT into Customers
VALUES (1, 'Alfreds Futterkiste', 'Obere Str.57', 'Berlin', 'Germany'), 
	   (2, 'Ana Trujillo Emparedados', 'Avda. de la Constituci?n 2222', 'M?xico D.F', 'Mexico'),
	   (3, 'Antonio Moreno Taquer?a', 'Mataderos 2312', 'M?xico D.F', 'Mexico'),
	   (4, 'Around the Horn', '120 Hanover Sq.', 'London', 'UK'),
	   (5, 'Berglunds snabbk?p', 'Berguvsv?gen 8', 'Lule?', 'Sweden')

INSERT into Products
VALUES (1, 'Chais', 'Beverages', '10 boxes x 20 bags', 18),
	   (2, 'Chang', 'Beverages', '24 - 12 oz bottles', 19),
	   (3, 'Aniseed Syrup', 'Condiments', '12 - 550 ml bottles', 10),
	   (4, 'Chef Anton''s Cajon Seasoning', 'Condiments', '48 - 6 oz jars', 22),
	   (5, 'Chef Anton''s Gumbo Mix', 'Condiments', '36 boxes', 21.35)

INSERT into Orders
VALUES (10248, 2, '1996-07-04'),
	   (10249, 3, '1996-07-05'),
	   (10250, 3, '1996-07-08'),
	   (10251, 5, '1996-07-08'),
	   (10252, 1, '1996-07-09')

INSERT into OrderDetails
VALUES (1, 10248, 1, 12),
	   (2, 10248, 3, 10),
	   (3, 10248, 2, 5),
	   (4, 10249, 4, 9),
	   (5, 10249, 1, 40)

