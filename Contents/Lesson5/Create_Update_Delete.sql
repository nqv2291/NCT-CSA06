-- Tạo và chọn database (SQLite ko cần bước này)
CREATE DATABASE introDB
GO
USE introDB
GO

-- Tạo bảng -------------------------------------------------------------------
CREATE TABLE school (
	level_id INT PRIMARY KEY,
	name VARCHAR(20)
)

CREATE TABLE student (
	student_id INT,
	name VARCHAR(100),
	age INT,
	school_level INT,

	CONSTRAINT student_pk PRIMARY KEY (student_id),
	CONSTRAINT student_fk_school
		FOREIGN KEY (school_level)
		REFERENCES school (level_id)
)

-- Nhập giá trị vào bảng -------------------------------------------------------
-- Vào những cột cụ thể
INSERT INTO school (level_id)
VALUES (99)

INSERT INTO student (student_id, name)
VALUES (0, 'Ngo Quang Viet')

-- Vào tất cả các cột (ko cần gõ tên cột sau school)
-- 1 giá trị
INSERT INTO school
VALUES (1, 'Primary School')

-- Nhiều giá trị
INSERT INTO school
VALUES (2, 'Secondary School'),
		(3, 'High school'),
		(4, 'University/College')

INSERT INTO student
VALUES (99, 'Yassuo', 12, 1)

-- Có thể xem dữ liệu trong bảng bằng cách:
SELECT * FROM school
SELECT * FROM student


-- Cập nhật/chỉnh sửa bảng -----------------------------------------------------
-- Cập nhật dữ liệu trong bảng
UPDATE student
SET age = 21, school_level = 4
WHERE student_id = 99

-- Cập nhật cấu tạo bảng
-- Thêm cột
ALTER TABLE school
ADD difficulty INT

-- Xóa dữ liệu/cột/bảng --------------------------------------------------------
-- Xóa bảng
DROP TABLE student

-- Xóa cột trong bảng
ALTER TABLE school
DROP COLUMN difficulty

-- Xóa dữ liệu (dòng trong bảng)
DELETE FROM school
WHERE level_id = 99 -- nếu ko có dòng điều kiện này thì cả bảng sẽ bị xóa
