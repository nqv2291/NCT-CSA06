CREATE DATABASE Northwind
GO
USE Northwind
GO

CREATE TABLE Customers(
	CustomerID INT PRIMARY KEY,
	CustomerName NVARCHAR(130),
	Address NVARCHAR(1000),
	City NVARCHAR(20),
	Country NVARCHAR(127)
)

CREATE TABLE Products (
	ProductID INT PRIMARY KEY,
	ProductName NVARCHAR(127),
	Category NVARCHAR(127),
	Unit NVARCHAR(1023),
	Price DECIMAL
)

CREATE TABLE Orders(
	OrderID INT PRIMARY KEY,
	CustomerID INT,
	OderDate DATE
)

CREATE TABLE OrderDetails (
	OrderDetailID INT PRIMARY KEY,
	OrderID INT,
	ProductID INT,
	Quantity DECIMAL,
)


