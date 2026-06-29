-- School Children Record Management System Database Schema

CREATE DATABASE IF NOT EXISTS school_management;
USE school_management;

-- Students Table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(10),
    admission_date DATE NOT NULL,
    status ENUM('Active', 'Inactive', 'Graduated') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Classes Table
CREATE TABLE IF NOT EXISTS classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50) NOT NULL,
    section VARCHAR(10) NOT NULL,
    class_teacher VARCHAR(100),
    capacity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Student-Class Enrollment
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    academic_year VARCHAR(10) NOT NULL,
    enrollment_date DATE NOT NULL,
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE KEY unique_enrollment (student_id, class_id, academic_year),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Parents/Guardians Table
CREATE TABLE IF NOT EXISTS parents (
    parent_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    parent_name VARCHAR(100) NOT NULL,
    relationship VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    occupation VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Attendance Table
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Leave', 'Late') DEFAULT 'Present',
    remarks VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE KEY unique_attendance (student_id, class_id, attendance_date),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Academics Table (Grades/Marks)
CREATE TABLE IF NOT EXISTS academics (
    academic_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    exam_type VARCHAR(50),
    marks_obtained DECIMAL(5, 2),
    total_marks DECIMAL(5, 2),
    percentage DECIMAL(5, 2),
    grade VARCHAR(2),
    academic_year VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fees Table
CREATE TABLE IF NOT EXISTS fees (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    fee_type VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    due_date DATE,
    payment_date DATE,
    status ENUM('Pending', 'Paid', 'Overdue') DEFAULT 'Pending',
    academic_year VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Indexes for better performance
CREATE INDEX idx_student_roll ON students(roll_number);
CREATE INDEX idx_student_status ON students(status);
CREATE INDEX idx_enrollment_student ON enrollments(student_id);
CREATE INDEX idx_attendance_date ON attendance(attendance_date);
CREATE INDEX idx_fees_status ON fees(status);

-- Insert Sample Data
INSERT INTO classes (class_name, section, class_teacher, capacity) VALUES
('10', 'A', 'Mr. John Smith', 40),
('10', 'B', 'Mrs. Sarah Johnson', 40),
('9', 'A', 'Mr. Robert Brown', 35),
('9', 'B', 'Ms. Emily Davis', 35);

INSERT INTO students (roll_number, first_name, last_name, date_of_birth, gender, email, phone, address, city, state, postal_code, admission_date, status) VALUES
('STU001', 'Arjun', 'Kumar', '2008-05-15', 'Male', 'arjun.kumar@mail.com', '9876543210', '123 Main Street', 'Delhi', 'Delhi', '110001', '2022-04-01', 'Active'),
('STU002', 'Priya', 'Singh', '2008-08-22', 'Female', 'priya.singh@mail.com', '9876543211', '456 Park Avenue', 'Mumbai', 'Maharashtra', '400001', '2022-04-01', 'Active'),
('STU003', 'Rohan', 'Patel', '2008-12-10', 'Male', 'rohan.patel@mail.com', '9876543212', '789 Oak Road', 'Bangalore', 'Karnataka', '560001', '2022-04-01', 'Active'),
('STU004', 'Ananya', 'Desai', '2008-03-08', 'Female', 'ananya.desai@mail.com', '9876543213', '321 Elm Street', 'Pune', 'Maharashtra', '411001', '2022-04-01', 'Active'),
('STU005', 'Vikram', 'Gupta', '2009-07-14', 'Male', 'vikram.gupta@mail.com', '9876543214', '654 Maple Drive', 'Chennai', 'Tamil Nadu', '600001', '2023-04-01', 'Active');

INSERT INTO enrollments (student_id, class_id, academic_year, enrollment_date, status) VALUES
(1, 1, '2023-24', '2023-04-01', 'Active'),
(2, 1, '2023-24', '2023-04-01', 'Active'),
(3, 2, '2023-24', '2023-04-01', 'Active'),
(4, 3, '2023-24', '2023-04-01', 'Active'),
(5, 4, '2023-24', '2023-04-01', 'Active');

INSERT INTO parents (student_id, parent_name, relationship, email, phone, occupation, address, city, state, postal_code) VALUES
(1, 'Rajesh Kumar', 'Father', 'rajesh.kumar@mail.com', '9876543220', 'Engineer', '123 Main Street', 'Delhi', 'Delhi', '110001'),
(2, 'Neha Singh', 'Mother', 'neha.singh@mail.com', '9876543221', 'Doctor', '456 Park Avenue', 'Mumbai', 'Maharashtra', '400001'),
(3, 'Arun Patel', 'Father', 'arun.patel@mail.com', '9876543222', 'Businessman', '789 Oak Road', 'Bangalore', 'Karnataka', '560001'),
(4, 'Kavya Desai', 'Mother', 'kavya.desai@mail.com', '9876543223', 'Teacher', '321 Elm Street', 'Pune', 'Maharashtra', '411001'),
(5, 'Suresh Gupta', 'Father', 'suresh.gupta@mail.com', '9876543224', 'Manager', '654 Maple Drive', 'Chennai', 'Tamil Nadu', '600001');
