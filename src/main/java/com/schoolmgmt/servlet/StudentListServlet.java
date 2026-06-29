package com.schoolmgmt.servlet;

import com.schoolmgmt.dao.StudentDAO;
import com.schoolmgmt.model.Student;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/students")
public class StudentListServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        List<Student> students = StudentDAO.getAllStudents();
        request.setAttribute("students", students);
        request.getRequestDispatcher("/WEB-INF/jsp/student-list.jsp").forward(request, response);
    }
}
