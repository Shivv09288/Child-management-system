<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>School Management System</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 60px;
            text-align: center;
            max-width: 600px;
        }
        .logo {
            font-size: 60px;
            margin-bottom: 20px;
        }
        h1 {
            color: #333;
            font-size: 32px;
            margin-bottom: 15px;
        }
        .subtitle {
            color: #666;
            font-size: 16px;
            margin-bottom: 40px;
            line-height: 1.6;
        }
        .features {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 40px 0;
            text-align: left;
        }
        .feature {
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        .feature h3 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .feature p {
            color: #666;
            font-size: 14px;
        }
        .cta-buttons {
            display: flex;
            gap: 15px;
            margin-top: 40px;
            justify-content: center;
        }
        .btn {
            padding: 14px 35px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }
        .btn-primary {
            background: #667eea;
            color: white;
        }
        .btn-primary:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        .btn-secondary {
            background: #6c757d;
            color: white;
        }
        .btn-secondary:hover {
            background: #5a6268;
            transform: translateY(-2px);
        }
        .stats {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            margin: 40px 0;
        }
        .stat {
            padding: 20px;
        }
        .stat-number {
            font-size: 28px;
            font-weight: bold;
            color: #667eea;
        }
        .stat-label {
            color: #666;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🏫</div>
        <h1>School Management System</h1>
        <p class="subtitle">Efficiently manage student information, attendance, and academic records</p>

        <div class="features">
            <div class="feature">
                <h3>👥 Student Management</h3>
                <p>Add, update, and manage student records easily</p>
            </div>
            <div class="feature">
                <h3>📊 Data Analytics</h3>
                <p>View comprehensive reports and statistics</p>
            </div>
            <div class="feature">
                <h3>🔍 Search & Filter</h3>
                <p>Find students quickly with advanced search</p>
            </div>
            <div class="feature">
                <h3>🔒 Secure Access</h3>
                <p>Protect sensitive student information</p>
            </div>
        </div>

        <div class="stats">
            <div class="stat">
                <div class="stat-number">100+</div>
                <div class="stat-label">Students Managed</div>
            </div>
            <div class="stat">
                <div class="stat-number">50+</div>
                <div class="stat-label">Staff Members</div>
            </div>
            <div class="stat">
                <div class="stat-number">24/7</div>
                <div class="stat-label">System Support</div>
            </div>
        </div>

        <div class="cta-buttons">
            <a href="students" class="btn btn-primary">📚 View Students</a>
            <a href="addStudent" class="btn btn-secondary">➕ Add Student</a>
        </div>
    </div>
</body>
</html>
