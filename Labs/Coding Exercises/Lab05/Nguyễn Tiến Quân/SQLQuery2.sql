CREATE DATABASE Northwind
GO

USE Northwind
GO

CREATE TABLE customers(
	customer_id INT PRIMARY KEY,
	customer_name VARCHAR(100),
	address VARCHAR(100),
	city VARCHAR(30),
	country VARCHAR(30)
)

CREATE TABLE orders(
	order_id INT PRIMARY KEY,
	customer_id INT,
	order_date VARCHAR(30),

	CONSTRAINT order_fk_customer
		FOREIGN KEY (customer_id)
		REFERENCES customers(customer_id)
)

CREATE TABLE products(
	product_id INT PRIMARY KEY,
	product_name VARCHAR(100),
	category VARCHAR(30),
	unit VARCHAR(100),
	price INT
)

CREATE TABLE order_details(
	order_detail_id INT PRIMARY KEY,
	order_id INT,
	product_id INT,
	quantity INT,

	CONSTRAINT order_detail_fk_order
		FOREIGN KEY (order_id)
		REFERENCES orders (order_id),

	CONSTRAINT oder_detail_fk_product
		FOREIGN KEY (product_id)
		REFERENCES products (product_id)
)

INSERT INTO customers
VALUES (1, 'Alfreds Futterkiste', 'Obere Str.57', 'Berlin', 'German'),
		(2, 'Ana Trujillo Emparedados', 'Avda. de la Consitución 2222', 'México D.F.', 'Mexico'),
		(3, 'Antonio Moreno Taquería', 'Mataderos 2312', 'México D.F.', 'Mexico'),
		(4, 'Around the Horn', '120 Hanover Sq.', 'London', 'UK'),
		(5, 'Berglunds snabbkop', 'Berguvsvagen 8', 'Lulea', 'Sweden')

SELECT * FROM customers

ALTER TABLE products 
DROP COLUMN price

ALTER TABLE products 
ADD price FLOAT

INSERT INTO products
VALUES (1, 'Chais', 'Beverages', '10 boxes x 20 bags', 18),
		(2, 'Chang', 'Beverages', '24-12 oz bottles', 19),
		(3, 'Aniseed Syrup', 'Condiments', '12-550 ml bottles', 10),
		(4, 'Chef Anton''s Cajun Seasoning', 'Condiments', '48-6 oz jars', 22),
		(5, 'Chef Anton''s Gumbo Mix', 'Condiments', '36 boxes', 21.35)

SELECT * FROM products

INSERT INTO orders
VALUES (10248, 2, '07/04/1996'),
		(10249, 3, '07/05/1996'),
		(10250, 3, '07/08/1996'),
		(10251, 5, '07/08/1996'),
		(10252, 1, '07/09/1996')


SELECT * FROM orders 


INSERT INTO order_details
VALUES (1, 10248, 1, 12),
		(2, 10248, 3, 10),
		(3, 10248, 2, 5),
		(4, 10249, 4, 9),
		(5, 10249, 1, 40)

SELECT * FROM order_details