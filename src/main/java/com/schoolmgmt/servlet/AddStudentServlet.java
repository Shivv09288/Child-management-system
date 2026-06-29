package com.schoolmgmt.servlet;

import com.schoolmgmt.dao.StudentDAO;
import com.schoolmgmt.model.Student;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.time.LocalDate;

@WebServlet("/addStudent")
public class AddStudentServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.getRequestDispatcher("/WEB-INF/jsp/add-student.jsp").forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        try {
            String rollNumber = request.getParameter("rollNumber");
            String firstName = request.getParameter("firstName");
            String lastName = request.getParameter("lastName");
            LocalDate dateOfBirth = LocalDate.parse(request.getParameter("dateOfBirth"));
            String gender = request.getParameter("gender");
            String email = request.getParameter("email");
            String phone = request.getParameter("phone");
            String address = request.getParameter("address");
            String city = request.getParameter("city");
            String state = request.getParameter("state");
            String postalCode = request.getParameter("postalCode");
            LocalDate admissionDate = LocalDate.parse(request.getParameter("admissionDate"));
            
            Student student = new Student(rollNumber, firstName, lastName, dateOfBirth, gender,
                    email, phone, address, city, state, postalCode, admissionDate, "Active");
            
            if (StudentDAO.addStudent(student)) {
                request.setAttribute("message", "Student added successfully!");
                request.setAttribute("messageType", "success");
            } else {
                request.setAttribute("message", "Failed to add student.");
                request.setAttribute("messageType", "error");
            }
        } catch (Exception e) {
            request.setAttribute("message", "Error: " + e.getMessage());
            request.setAttribute("messageType", "error");
        }
        
        request.getRequestDispatcher("/WEB-INF/jsp/add-student.jsp").forward(request, response);
    }
}
