# School Management System

A comprehensive Java-based web application for managing student information, built with Servlets and JSP for educational institutions and schools.

## Project Overview

This application provides a complete solution for schools and educational institutions to manage:
- **Student Management**: Create, read, update, and delete student records
- **Student Information**: Maintain comprehensive student details and contact information
- **Search & Filter**: Quick search functionality to find students by name or roll number
- **Responsive UI**: Modern and user-friendly interface with gradient styling
- **Error Handling**: Custom error pages with graceful error management

---

## Technology Stack

### Backend
- **Framework**: Apache Tomcat (Servlet Container)
- **Language**: Java with Servlets
- **Template Engine**: JSP (JavaServer Pages)
- **Version**: Java 8+, Servlet 4.0, JSP 2.3

### Frontend
- **Markup**: HTML5
- **Styling**: CSS3
- **Architecture**: Server-side rendered JSP templates
- **Features**: Responsive design with modern UI

### Database
- **Type**: Configurable (MySQL, PostgreSQL, Oracle, etc.)
- **Access**: JDBC with DAO pattern

---

## Project Structure

```
child-management-system/
│
├── src/main/java/
│   └── com/schoolmgmt/
│       ├── servlet/                # Servlet classes
│       │   ├── StudentServlet.java
│       │   ├── AddStudentServlet.java
│       │   ├── EditStudentServlet.java
│       │   ├── DeleteStudentServlet.java
│       │   └── SearchStudentServlet.java
│       │
│       ├── model/                  # Domain models
│       │   └── Student.java
│       │
│       ├── dao/                    # Data Access Objects
│       │   └── StudentDAO.java
│       │
│       └── config/                 # Configuration classes
│           └── DBConfig.java
│
├── src/main/webapp/
│   ├── index.jsp                   # Home page
│   └── WEB-INF/
│       ├── web.xml                 # Deployment descriptor
│       └── jsp/
│           ├── student-list.jsp    # List all students
│           ├── add-student.jsp     # Add new student form
│           ├── edit-student.jsp    # Edit student form
│           ├── error-404.jsp       # 404 error page
│           └── error-500.jsp       # 500 error page
│
├── pom.xml                         # Maven configuration
└── README.md                       # This file
```

---

## Prerequisites

Before setting up the application, ensure you have:

1. **Java Development Kit (JDK)** 8 or higher - [Download JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
2. **Apache Tomcat** 9.0 or higher - [Download Tomcat](https://tomcat.apache.org/download-90.cgi)
3. **Maven** 3.6+ - [Download Maven](https://maven.apache.org/download.cgi)
4. **Database** (MySQL/PostgreSQL) - [Download MySQL](https://dev.mysql.com/downloads/mysql/) or [PostgreSQL](https://www.postgresql.org/download/)

### Java Version Check
```bash
java -version
javac -version
```

### Maven Installation Check
```bash
mvn -version
```

---

## Installation & Setup

### Step 1: Clone/Navigate to Project
```bash
cd child-management-system
```

### Step 2: Database Setup

**Create Database (MySQL):**
```sql
CREATE DATABASE school_management;
USE school_management;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(20),
    date_of_birth DATE,
    admission_date DATE,
    email VARCHAR(100),
    phone VARCHAR(15),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(10),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Step 3: Configure Database Connection

Edit `src/main/java/com/schoolmgmt/config/DBConfig.java`:
```java
public class DBConfig {
    private static final String URL = "jdbc:mysql://localhost:3306/school_management";
    private static final String USER = "root";
    private static final String PASSWORD = "your-password";
    private static final String DRIVER = "com.mysql.cj.jdbc.Driver";
}
```

### Step 4: Build the Application

Using Maven:
```bash
mvn clean install
```

This will:
- Download all dependencies
- Compile the Java source code
- Create a WAR file in the `target/` directory

---

## Running the Application

### Option 1: Using Apache Tomcat

1. Copy the WAR file to Tomcat:
```bash
cp target/school-management-system.war $CATALINA_HOME/webapps/
```

2. Start Tomcat:
```bash
$CATALINA_HOME/bin/startup.sh  # Linux/Mac
$CATALINA_HOME/bin/startup.bat # Windows
```

3. Open browser and navigate to: `http://localhost:8080/school-management-system`

### Option 2: Using Maven Tomcat Plugin

```bash
mvn tomcat7:run
```

Then navigate to: `http://localhost:8080/school-management-system`

---

## Features

### Student Management
- ✅ Add new students with comprehensive details
- ✅ View all students in a paginated table
- ✅ Edit existing student information
- ✅ Delete student records
- ✅ Search students by name or roll number

### User Interface
- Modern gradient-based design
- Responsive layout that works on all devices
- Interactive forms with validation
- Clean navigation and action buttons
- Status indicators for student records

### Error Handling
- Custom 404 error page
- Custom 500 server error page
- User-friendly error messages
- Graceful navigation recovery

### Data Validation
- Required field validation
- Email format validation
- Phone number validation
- Date validation for enrollment

---

## Database Schema

### students Table

| Column | Type | Description |
|--------|------|-------------|
| student_id | INT | Primary key, auto-increment |
| roll_number | VARCHAR(20) | Unique student roll number |
| first_name | VARCHAR(50) | Student's first name |
| last_name | VARCHAR(50) | Student's last name |
| gender | VARCHAR(20) | Student's gender |
| date_of_birth | DATE | Student's date of birth |
| admission_date | DATE | Date of admission |
| email | VARCHAR(100) | Student's email |
| phone | VARCHAR(15) | Contact phone number |
| address | TEXT | Student's address |
| city | VARCHAR(50) | City of residence |
| state | VARCHAR(50) | State of residence |
| postal_code | VARCHAR(10) | Postal code |
| status | VARCHAR(20) | Active/Inactive status |
| created_at | TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | Record update time |

---

## API Routes/Servlets

| Route | Servlet | Method | Description |
|-------|---------|--------|-------------|
| `/students` | StudentServlet | GET | List all students |
| `/addStudent` | AddStudentServlet | GET/POST | Add new student form and processing |
| `/editStudent` | EditStudentServlet | GET/POST | Edit student form and processing |
| `/deleteStudent` | DeleteStudentServlet | GET | Delete student |
| `/searchStudent` | SearchStudentServlet | GET | Search students |

---

## Configuration & Customization

### Update Database Connection

Edit `src/main/java/com/schoolmgmt/config/DBConfig.java`:
```java
private static final String URL = "jdbc:mysql://localhost:3306/your_db";
private static final String USER = "your_username";
private static final String PASSWORD = "your_password";
```

### Change Servlet Mappings

Edit `src/main/webapp/WEB-INF/web.xml` to modify servlet paths and error pages.

### Customize UI

All CSS styling is embedded in JSP files. Modify the `<style>` sections to customize colors, fonts, and layouts.

---

## Troubleshooting

### Tomcat Connection Error
- **Error**: Connection refused on port 8080
- **Solution**: Check if Tomcat is running. Start with `$CATALINA_HOME/bin/startup.sh`

### Database Connection Error
- **Error**: `SQLException: Access denied for user`
- **Solution**: Verify database credentials in DBConfig.java

### ClassNotFound Error
- **Error**: `ClassNotFoundException: com.mysql.cj.jdbc.Driver`
- **Solution**: Ensure MySQL JDBC driver is in classpath (pom.xml dependency)

### JSP Not Compiling
- **Error**: `JasperException`
- **Solution**: Check JSP syntax and ensure all taglibs are properly declared

### Port Already in Use
- **Error**: `Address already in use: 8080`
- **Solution**: Change port in Tomcat configuration or kill existing process

---

## Development Notes

### Adding New Features

1. **Create a new Servlet**:
```java
@WebServlet("/newFeature")
public class NewFeatureServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // Implementation
    }
}
```

2. **Create corresponding JSP** in `src/main/webapp/WEB-INF/jsp/`

3. **Update DAO** if database operations are needed

### JDBC Best Practices
- Always close database connections in finally blocks
- Use prepared statements to prevent SQL injection
- Handle exceptions gracefully
- Implement connection pooling for production

---

## Performance Optimization

### Recommended Enhancements
- [ ] Implement connection pooling (HikariCP)
- [ ] Add caching layer for frequent queries
- [ ] Implement pagination for large result sets
- [ ] Add database indexing on search columns
- [ ] Use AJAX for real-time search
- [ ] Implement session management

---

## Security Considerations

### Implemented
- ✅ HTTPS cookie configuration
- ✅ XSS protection through JSP escaping
- ✅ CSRF token consideration

### Recommended for Production
- [ ] Implement authentication and authorization
- [ ] Add CSRF tokens to forms
- [ ] Use HTTPS/SSL encryption
- [ ] Implement input validation and sanitization
- [ ] Add rate limiting
- [ ] Implement audit logging

---

## Deployment to Production

1. **Build WAR file**:
```bash
mvn clean package
```

2. **Configure for Production**:
   - Update database connection strings
   - Set appropriate Tomcat memory settings
   - Enable HTTPS
   - Configure security headers

3. **Deploy to Server**:
```bash
scp target/school-management-system.war user@server:/path/to/tomcat/webapps/
```

---

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify database connection
3. Check Tomcat logs: `$CATALINA_HOME/logs/catalina.out`
4. Ensure all dependencies are installed: `mvn dependency:tree`

---

## License

This project is provided as-is for educational and institutional use.

---

## Version History

- **v2.0** - Java Servlet/JSP version (June 29, 2026)
- **v1.0** - Python Flask version (February 25, 2026)

---

**Last Updated**: June 29, 2026
**Version**: 2.0
**Framework**: Java Servlets & JSP
