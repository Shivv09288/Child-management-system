package com.schoolmgmt.dao;

import com.schoolmgmt.model.Student;
import com.schoolmgmt.util.DBConnection;

import java.sql.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class StudentDAO {

    /**
     * Add new student to database
     */
    public static boolean addStudent(Student student) {
        String query = "INSERT INTO students (roll_number, first_name, last_name, date_of_birth, gender, " +
                "email, phone, address, city, state, postal_code, admission_date, status) " +
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
        
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(query)) {
            
            pstmt.setString(1, student.getRollNumber());
            pstmt.setString(2, student.getFirstName());
            pstmt.setString(3, student.getLastName());
            pstmt.setDate(4, java.sql.Date.valueOf(student.getDateOfBirth()));
            pstmt.setString(5, student.getGender());
            pstmt.setString(6, student.getEmail());
            pstmt.setString(7, student.getPhone());
            pstmt.setString(8, student.getAddress());
            pstmt.setString(9, student.getCity());
            pstmt.setString(10, student.getState());
            pstmt.setString(11, student.getPostalCode());
            pstmt.setDate(12, java.sql.Date.valueOf(student.getAdmissionDate()));
            pstmt.setString(13, student.getStatus());
            
            int rows = pstmt.executeUpdate();
            return rows > 0;
        } catch (SQLException e) {
            System.out.println("Error adding student: " + e.getMessage());
            e.printStackTrace();
            return false;
        }
    }

    /**
     * Get all students
     */
    public static List<Student> getAllStudents() {
        List<Student> students = new ArrayList<>();
        String query = "SELECT * FROM students WHERE status = 'Active' ORDER BY first_name";
        
        try (Connection conn = DBConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {
            
            while (rs.next()) {
                Student student = new Student();
                student.setStudentId(rs.getInt("student_id"));
                student.setRollNumber(rs.getString("roll_number"));
                student.setFirstName(rs.getString("first_name"));
                student.setLastName(rs.getString("last_name"));
                student.setDateOfBirth(rs.getDate("date_of_birth").toLocalDate());
                student.setGender(rs.getString("gender"));
                student.setEmail(rs.getString("email"));
                student.setPhone(rs.getString("phone"));
                student.setAddress(rs.getString("address"));
                student.setCity(rs.getString("city"));
                student.setState(rs.getString("state"));
                student.setPostalCode(rs.getString("postal_code"));
                student.setAdmissionDate(rs.getDate("admission_date").toLocalDate());
                student.setStatus(rs.getString("status"));
                
                students.add(student);
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving students: " + e.getMessage());
            e.printStackTrace();
        }
        return students;
    }

    /**
     * Get student by ID
     */
    public static Student getStudentById(int studentId) {
        String query = "SELECT * FROM students WHERE student_id = ?";
        
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(query)) {
            
            pstmt.setInt(1, studentId);
            
            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    Student student = new Student();
                    student.setStudentId(rs.getInt("student_id"));
                    student.setRollNumber(rs.getString("roll_number"));
                    student.setFirstName(rs.getString("first_name"));
                    student.setLastName(rs.getString("last_name"));
                    student.setDateOfBirth(rs.getDate("date_of_birth").toLocalDate());
                    student.setGender(rs.getString("gender"));
                    student.setEmail(rs.getString("email"));
                    student.setPhone(rs.getString("phone"));
                    student.setAddress(rs.getString("address"));
                    student.setCity(rs.getString("city"));
                    student.setState(rs.getString("state"));
                    student.setPostalCode(rs.getString("postal_code"));
                    student.setAdmissionDate(rs.getDate("admission_date").toLocalDate());
                    student.setStatus(rs.getString("status"));
                    
                    return student;
                }
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving student: " + e.getMessage());
            e.printStackTrace();
        }
        return null;
    }

    /**
     * Search students by name or roll number
     */
    public static List<Student> searchStudents(String searchTerm) {
        List<Student> students = new ArrayList<>();
        String query = "SELECT * FROM students WHERE (first_name LIKE ? OR last_name LIKE ? OR roll_number LIKE ?) AND status = 'Active'";
        
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(query)) {
            
            String search = "%" + searchTerm + "%";
            pstmt.setString(1, search);
            pstmt.setString(2, search);
            pstmt.setString(3, search);
            
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    Student student = new Student();
                    student.setStudentId(rs.getInt("student_id"));
                    student.setRollNumber(rs.getString("roll_number"));
                    student.setFirstName(rs.getString("first_name"));
                    student.setLastName(rs.getString("last_name"));
                    student.setDateOfBirth(rs.getDate("date_of_birth").toLocalDate());
                    student.setGender(rs.getString("gender"));
                    student.setEmail(rs.getString("email"));
                    student.setPhone(rs.getString("phone"));
                    student.setAddress(rs.getString("address"));
                    student.setCity(rs.getString("city"));
                    student.setState(rs.getString("state"));
                    student.setPostalCode(rs.getString("postal_code"));
                    student.setAdmissionDate(rs.getDate("admission_date").toLocalDate());
                    student.setStatus(rs.getString("status"));
                    
                    students.add(student);
                }
            }
        } catch (SQLException e) {
            System.out.println("Error searching students: " + e.getMessage());
            e.printStackTrace();
        }
        return students;
    }

    /**
     * Update student information
     */
    public static boolean updateStudent(Student student) {
        String query = "UPDATE students SET first_name = ?, last_name = ?, email = ?, phone = ?, " +
                "address = ?, city = ?, state = ?, postal_code = ?, status = ? WHERE student_id = ?";
        
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(query)) {
            
            pstmt.setString(1, student.getFirstName());
            pstmt.setString(2, student.getLastName());
            pstmt.setString(3, student.getEmail());
            pstmt.setString(4, student.getPhone());
            pstmt.setString(5, student.getAddress());
            pstmt.setString(6, student.getCity());
            pstmt.setString(7, student.getState());
            pstmt.setString(8, student.getPostalCode());
            pstmt.setString(9, student.getStatus());
            pstmt.setInt(10, student.getStudentId());
            
            int rows = pstmt.executeUpdate();
            return rows > 0;
        } catch (SQLException e) {
            System.out.println("Error updating student: " + e.getMessage());
            e.printStackTrace();
            return false;
        }
    }

    /**
     * Delete student (mark as inactive)
     */
    public static boolean deleteStudent(int studentId) {
        String query = "UPDATE students SET status = 'Inactive' WHERE student_id = ?";
        
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(query)) {
            
            pstmt.setInt(1, studentId);
            
            int rows = pstmt.executeUpdate();
            return rows > 0;
        } catch (SQLException e) {
            System.out.println("Error deleting student: " + e.getMessage());
            e.printStackTrace();
            return false;
        }
    }
}
