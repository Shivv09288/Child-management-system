# Child Management System

A comprehensive full-stack web application for managing child information, attendance tracking, health records, and parent authentication.

## Project Overview

This application provides a complete solution for educational institutions and childcare centers to manage:
- **User Management**: Parent registration, login, and authentication
- **Child Management**: Create and manage child information
- **Attendance Tracking**: Mark and track child attendance
- **Health Records**: Maintain health and medical information
- **Parent Details**: Manage parent profile information

---

## Technology Stack

### Backend
- **Framework**: Flask 2.3.2 (Python)
- **Database**: MongoDB
- **Authentication**: Session-based with password hashing (Werkzeug)
- **HTTP Server**: Flask development server

### Frontend
- **Markup**: HTML5
- **Styling**: CSS3
- **Templates**: Flask Jinja2 template engine
- **Architecture**: Server-side rendered templates

---

## Project Structure

```
child-management-system/
│
├── backend/                    # Python Flask backend
│   ├── app.py                 # Main Flask application with all routes
│   ├── config.py              # MongoDB configuration and connection
│   ├── utils.py               # Utility functions
│   └── requirements.txt        # Python dependencies
│
├── frontend/                   # HTML/CSS frontend assets
│   ├── templates/             # Flask HTML templates
│   │   ├── base.html          # Base template with navigation
│   │   ├── login.html         # User login page
│   │   ├── register.html      # User registration page
│   │   ├── dashboard.html     # Main dashboard
│   │   ├── add_child.html     # Add child form
│   │   ├── view_children.html # View/Edit children list
│   │   ├── attendance.html    # Mark child attendance
│   │   ├── health_records.html # Manage health records
│   │   ├── parent_details.html # View/Edit parent profile
│   │   ├── 404.html           # 404 error page
│   │   └── 500.html           # 500 error page
│   └── static/                # Static assets
│       └── css/
│           └── style.css      # Application styling
│
└── README.md                   # This file
```

---

## Prerequisites

Before setting up the application, ensure you have:

1. **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
2. **MongoDB** - [Download MongoDB Community](https://www.mongodb.com/try/download/community)
3. **pip** - Python package manager (included with Python)

### MongoDB Setup

**Windows Installation:**
1. Download MongoDB Community edition
2. Run the installer and follow the setup wizard
3. MongoDB will typically be installed at `C:\Program Files\MongoDB\Server\{version}`
4. Add MongoDB to PATH or start it manually

**Verify MongoDB is running:**
```bash
mongod --version
```

---

## Installation & Setup

### Step 1: Clone/Navigate to Project
```bash
cd child-management-system
```

### Step 2: Backend Setup

Navigate to the backend directory:
```bash
cd backend
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

**Dependencies included:**
- Flask 2.3.2 - Web framework
- pymongo 4.4.1 - MongoDB driver
- Werkzeug 2.3.6 - Security utilities

### Step 3: Configure Database

1. Ensure MongoDB is running on your machine
2. The default configuration connects to `mongodb://localhost:27017`
3. Database name: `child_management_db`

To modify the connection, edit `backend/config.py`:
```python
MONGO_URI = "mongodb://your-connection-string"
DB_NAME = "your_database_name"
```

---

## Running the Application

### Start Backend Server

1. Navigate to backend directory:
```bash
cd backend
```

2. Run the Flask application:
```bash
python app.py
```

**Expected output:**
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

3. Open your browser and navigate to: `http://localhost:5000`

### First Time Setup

When you first run the application:
- The database collections will be automatically created
- Indexes will be set up for optimal performance
- You'll see initialization messages in the console

---

## Features

### Authentication
- User registration with email validation
- Secure password hashing using Werkzeug
- Session-based authentication
- Login/logout functionality

### Child Management
- Add and manage multiple children per parent
- Store child information (name, age, DOB, etc.)
- Edit and update child details
- View all children associated with parent account

### Attendance Tracking
- Mark attendance for each child
- Track attendance history
- View attendance records

### Health Records
- Store health and medical information
- Track vaccinations and medical history
- Manage health-related notes

### Parent Management
- Create and update parent profiles
- Manage contact information
- View account details

### Error Handling
- Custom 404 error page
- Custom 500 error page
- User-friendly error messages

---

## Database Schema

### Collections

**users**
- User authentication and profile information
- Indexes: email (unique)

**children**
- Child information linked to parent accounts
- Stores child profile data

**attendance**
- Attendance records for each child
- Tracks date and status

**health**
- Health and medical records
- Stores health-related information

---

## Configuration & Customization

### Secret Key Security
In `backend/app.py`, change the secret key for production:
```python
app.secret_key = "your-secure-secret-key-here"
```

### Port Configuration
To run on a different port:
```bash
# In backend/app.py, modify:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

---

## Troubleshooting

### MongoDB Connection Error
- **Error**: `ConnectionFailure`
- **Solution**: Ensure MongoDB is running. Start with: `mongod`

### Port Already in Use
- **Error**: `Address already in use`
- **Solution**: Change port in app.py or kill the process using port 5000

### Module Not Found
- **Error**: `ModuleNotFoundError`
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

### Template Not Found
- **Error**: `TemplateNotFound`
- **Solution**: Ensure you're running app.py from the correct directory

---

## Development Notes

### File Locations
- Backend code: `/backend/app.py`
- Frontend templates: `/frontend/templates/`
- Styling: `/frontend/static/css/style.css`
- Database config: `/backend/config.py`

### Adding New Routes
1. Add route function to `backend/app.py`
2. Create corresponding template in `frontend/templates/`
3. Add styling to `frontend/static/css/style.css` if needed
4. Update navigation in `frontend/templates/base.html`

### Database Operations
All database operations use PyMongo in `backend/config.py`:
- Collections are globally accessible
- Indexes are created on initialization
- Connection is configured in `MONGO_URI`

---

## Future Enhancements

Potential features for future versions:
- [ ] API endpoints for mobile app integration
- [ ] Real-time notifications
- [ ] Advanced reporting and analytics
- [ ] Photo galleries
- [ ] Parent-teacher messaging
- [ ] Fee management system
- [ ] Document upload and storage
- [ ] Multi-language support

---

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify MongoDB is running
3. Ensure all dependencies are installed
4. Check browser console for JavaScript errors

---

## License

This project is provided as-is for educational and institutional use.

---

**Last Updated**: February 25, 2026
**Version**: 1.0
