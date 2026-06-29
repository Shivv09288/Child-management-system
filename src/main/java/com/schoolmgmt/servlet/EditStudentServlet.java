package com.schoolmgmt.servlet;

import com.schoolmgmt.dao.StudentDAO;
import com.schoolmgmt.model.Student;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/editStudent")
public class EditStudentServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        int studentId = Integer.parseInt(request.getParameter("id"));
        Student student = StudentDAO.getStudentById(studentId);
        request.setAttribute("student", student);
        request.getRequestDispatcher("/WEB-INF/jsp/edit-student.jsp").forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        try {
            int studentId = Integer.parseInt(request.getParameter("studentId"));
            Student student = new Student();
            student.setStudentId(studentId);
            student.setFirstName(request.getParameter("firstName"));
            student.setLastName(request.getParameter("lastName"));
            student.setEmail(request.getParameter("email"));
            student.setPhone(request.getParameter("phone"));
            student.setAddress(request.getParameter("address"));
            student.setCity(request.getParameter("city"));
            student.setState(request.getParameter("state"));
            student.setPostalCode(request.getParameter("postalCode"));
            student.setStatus(request.getParameter("status"));
            
            if (StudentDAO.updateStudent(student)) {
                request.setAttribute("message", "Student updated successfully!");
                request.setAttribute("messageType", "success");
                student = StudentDAO.getStudentById(studentId);
            } else {
                request.setAttribute("message", "Failed to update student.");
                request.setAttribute("messageType", "error");
                student = StudentDAO.getStudentById(studentId);
            }
            request.setAttribute("student", student);
        } catch (Exception e) {
            request.setAttribute("message", "Error: " + e.getMessage());
            request.setAttribute("messageType", "error");
        }
        
        request.getRequestDispatcher("/WEB-INF/jsp/edit-student.jsp").forward(request, response);
    }
}
