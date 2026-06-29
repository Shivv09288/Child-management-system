package com.schoolmgmt.servlet;

import com.schoolmgmt.dao.StudentDAO;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/deleteStudent")
public class DeleteStudentServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        try {
            int studentId = Integer.parseInt(request.getParameter("id"));
            if (StudentDAO.deleteStudent(studentId)) {
                response.sendRedirect("students?message=Student deleted successfully");
            } else {
                response.sendRedirect("students?message=Failed to delete student");
            }
        } catch (Exception e) {
            response.sendRedirect("students?message=Error: " + e.getMessage());
        }
    }
}
