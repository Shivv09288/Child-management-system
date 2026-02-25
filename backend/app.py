"""
Child Management System - Flask Backend
Main application file with all routes
"""
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
from bson.objectid import ObjectId
import re
from config import db, users_collection, children_collection, attendance_collection, health_collection, init_db

app = Flask(__name__)
app.secret_key = "your-secret-key-change-this-in-production"

# Initialize database on startup
init_db()

# ==================== Authentication Routes ====================

def login_required(f):
    """Decorator to check if user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET"])
def index():
    """Redirect to login if not authenticated, else to dashboard"""
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page and authentication"""
    if request.method == "POST":
        data = request.get_json()
        email = data.get("email", "").strip()
        password = data.get("password", "")

        # Validate input
        if not email or not password:
            return jsonify({"success": False, "message": "Email and password required"}), 400

        # Check if user exists
        user = users_collection.find_one({"email": email})
        if not user:
            return jsonify({"success": False, "message": "Invalid email or password"}), 401

        # Verify password
        if not check_password_hash(user["password"], password):
            return jsonify({"success": False, "message": "Invalid email or password"}), 401

        # Create session
        session["user_id"] = str(user["_id"])
        session["email"] = user["email"]
        session["name"] = user["name"]

        return jsonify({"success": True, "message": "Login successful"}), 200

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Registration page for new parents"""
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "")
        confirm_password = data.get("confirm_password", "")
        phone = data.get("phone", "").strip()

        # Validation
        errors = []

        if not name:
            errors.append("Name is required")
        if len(name) < 2:
            errors.append("Name must be at least 2 characters")

        if not email:
            errors.append("Email is required")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            errors.append("Invalid email format")

        if not password:
            errors.append("Password is required")
        if len(password) < 6:
            errors.append("Password must be at least 6 characters")

        if password != confirm_password:
            errors.append("Passwords do not match")

        if not phone or len(phone) < 10:
            errors.append("Valid phone number required")

        if errors:
            return jsonify({"success": False, "message": ", ".join(errors)}), 400

        # Check if email already exists
        if users_collection.find_one({"email": email}):
            return jsonify({"success": False, "message": "Email already registered"}), 409

        # Create new user
        user_data = {
            "name": name,
            "email": email,
            "password": generate_password_hash(password),
            "phone": phone,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }

        result = users_collection.insert_one(user_data)
        if result.inserted_id:
            return jsonify({"success": True, "message": "Registration successful. Please login."}), 201
        else:
            return jsonify({"success": False, "message": "Registration failed"}), 500

    return render_template("register.html")

@app.route("/logout", methods=["GET"])
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for("login"))

# ==================== Dashboard Route ====================

@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    """Main dashboard"""
    user_id = session.get("user_id")
    children = list(children_collection.find({"parent_id": ObjectId(user_id)}))
    
    # Convert ObjectId to string for template rendering
    for child in children:
        child["_id"] = str(child["_id"])
        child["parent_id"] = str(child["parent_id"])
    
    total_children = len(children)
    return render_template("dashboard.html", total_children=total_children, children=children)

# ==================== Child Management Routes ====================

@app.route("/api/children", methods=["GET"])
@login_required
def get_children():
    """Get all children for the logged-in parent"""
    user_id = session.get("user_id")
    children = list(children_collection.find({"parent_id": ObjectId(user_id)}))
    
    for child in children:
        child["_id"] = str(child["_id"])
        child["parent_id"] = str(child["parent_id"])
    
    return jsonify({"success": True, "children": children}), 200

@app.route("/add-child", methods=["GET", "POST"])
@login_required
def add_child():
    """Add a new child"""
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "").strip()
        age = data.get("age")
        date_of_birth = data.get("date_of_birth", "").strip()
        gender = data.get("gender", "").strip()
        school = data.get("school", "").strip()
        grade = data.get("grade", "").strip()

        # Validation
        errors = []

        if not name or len(name) < 2:
            errors.append("Valid child name required (min 2 characters)")

        try:
            age = int(age)
            if age < 0 or age > 18:
                errors.append("Age must be between 0 and 18")
        except (ValueError, TypeError):
            errors.append("Valid age required")

        if not date_of_birth:
            errors.append("Date of birth required")

        if not gender or gender not in ["Male", "Female", "Other"]:
            errors.append("Valid gender required")

        if not school or len(school) < 2:
            errors.append("School name required")

        if errors:
            return jsonify({"success": False, "message": ", ".join(errors)}), 400

        # Create child record
        child_data = {
            "parent_id": ObjectId(session.get("user_id")),
            "name": name,
            "age": age,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "school": school,
            "grade": grade,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }

        result = children_collection.insert_one(child_data)
        if result.inserted_id:
            return jsonify({"success": True, "message": "Child added successfully", "child_id": str(result.inserted_id)}), 201
        else:
            return jsonify({"success": False, "message": "Failed to add child"}), 500

    return render_template("add_child.html")

@app.route("/view-children", methods=["GET"])
@login_required
def view_children():
    """View all children"""
    user_id = session.get("user_id")
    children = list(children_collection.find({"parent_id": ObjectId(user_id)}))
    
    for child in children:
        child["_id"] = str(child["_id"])
        child["parent_id"] = str(child["parent_id"])
    
    return render_template("view_children.html", children=children)

@app.route("/api/children/<child_id>", methods=["GET", "PUT", "DELETE"])
@login_required
def manage_child(child_id):
    """Get, update, or delete a specific child"""
    user_id = session.get("user_id")
    
    try:
        child_obj_id = ObjectId(child_id)
    except:
        return jsonify({"success": False, "message": "Invalid child ID"}), 400

    child = children_collection.find_one({"_id": child_obj_id, "parent_id": ObjectId(user_id)})
    if not child:
        return jsonify({"success": False, "message": "Child not found"}), 404

    if request.method == "GET":
        child["_id"] = str(child["_id"])
        child["parent_id"] = str(child["parent_id"])
        return jsonify({"success": True, "child": child}), 200

    elif request.method == "PUT":
        data = request.get_json()
        update_fields = {}

        if "name" in data:
            update_fields["name"] = data["name"].strip()
        if "age" in data:
            update_fields["age"] = int(data["age"])
        if "date_of_birth" in data:
            update_fields["date_of_birth"] = data["date_of_birth"]
        if "gender" in data:
            update_fields["gender"] = data["gender"]
        if "school" in data:
            update_fields["school"] = data["school"].strip()
        if "grade" in data:
            update_fields["grade"] = data["grade"].strip()

        update_fields["updated_at"] = datetime.now()

        children_collection.update_one({"_id": child_obj_id}, {"$set": update_fields})
        return jsonify({"success": True, "message": "Child updated successfully"}), 200

    elif request.method == "DELETE":
        children_collection.delete_one({"_id": child_obj_id})
        attendance_collection.delete_many({"child_id": child_obj_id})
        health_collection.delete_many({"child_id": child_obj_id})
        return jsonify({"success": True, "message": "Child deleted successfully"}), 200

# ==================== Attendance Routes ====================

@app.route("/attendance", methods=["GET", "POST"])
@login_required
def attendance():
    """Mark attendance"""
    user_id = session.get("user_id")
    children = list(children_collection.find({"parent_id": ObjectId(user_id)}))
    
    for child in children:
        child["_id"] = str(child["_id"])

    if request.method == "POST":
        data = request.get_json()
        child_id = data.get("child_id")
        date = data.get("date")
        status = data.get("status")  # "Present" or "Absent"
        remarks = data.get("remarks", "").strip()

        if not child_id or not date or not status:
            return jsonify({"success": False, "message": "Child ID, date, and status required"}), 400

        if status not in ["Present", "Absent"]:
            return jsonify({"success": False, "message": "Status must be Present or Absent"}), 400

        try:
            child_obj_id = ObjectId(child_id)
            attendance_record = {
                "child_id": child_obj_id,
                "parent_id": ObjectId(user_id),
                "date": date,
                "status": status,
                "remarks": remarks,
                "recorded_at": datetime.now()
            }

            attendance_collection.insert_one(attendance_record)
            return jsonify({"success": True, "message": "Attendance recorded"}), 201
        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 500

    return render_template("attendance.html", children=children)

@app.route("/api/attendance/<child_id>", methods=["GET"])
@login_required
def get_attendance(child_id):
    """Get attendance records for a child"""
    user_id = session.get("user_id")
    
    try:
        child_obj_id = ObjectId(child_id)
    except:
        return jsonify({"success": False, "message": "Invalid child ID"}), 400

    records = list(attendance_collection.find({"child_id": child_obj_id, "parent_id": ObjectId(user_id)}))
    
    for record in records:
        record["_id"] = str(record["_id"])
        record["child_id"] = str(record["child_id"])
        record["parent_id"] = str(record["parent_id"])

    return jsonify({"success": True, "records": records}), 200

# ==================== Health Records Routes ====================

@app.route("/health-records", methods=["GET", "POST"])
@login_required
def health_records():
    """Manage health records"""
    user_id = session.get("user_id")
    children = list(children_collection.find({"parent_id": ObjectId(user_id)}))
    
    for child in children:
        child["_id"] = str(child["_id"])

    if request.method == "POST":
        data = request.get_json()
        child_id = data.get("child_id")
        record_type = data.get("record_type")  # "Vaccination", "Medical Checkup", etc.
        date = data.get("date")
        description = data.get("description", "").strip()
        notes = data.get("notes", "").strip()

        if not child_id or not record_type or not date:
            return jsonify({"success": False, "message": "Child ID, record type, and date required"}), 400

        try:
            child_obj_id = ObjectId(child_id)
            health_record = {
                "child_id": child_obj_id,
                "parent_id": ObjectId(user_id),
                "record_type": record_type,
                "date": date,
                "description": description,
                "notes": notes,
                "recorded_at": datetime.now()
            }

            health_collection.insert_one(health_record)
            return jsonify({"success": True, "message": "Health record added"}), 201
        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 500

    return render_template("health_records.html", children=children)

@app.route("/api/health/<child_id>", methods=["GET"])
@login_required
def get_health_records(child_id):
    """Get health records for a child"""
    user_id = session.get("user_id")
    
    try:
        child_obj_id = ObjectId(child_id)
    except:
        return jsonify({"success": False, "message": "Invalid child ID"}), 400

    records = list(health_collection.find({"child_id": child_obj_id, "parent_id": ObjectId(user_id)}))
    
    for record in records:
        record["_id"] = str(record["_id"])
        record["child_id"] = str(record["child_id"])
        record["parent_id"] = str(record["parent_id"])

    return jsonify({"success": True, "records": records}), 200

# ==================== Parent Details Routes ====================

@app.route("/parent-details", methods=["GET", "POST"])
@login_required
def parent_details():
    """View and edit parent details"""
    user_id = session.get("user_id")
    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()

        if not name or len(name) < 2:
            return jsonify({"success": False, "message": "Valid name required"}), 400

        if not phone or len(phone) < 10:
            return jsonify({"success": False, "message": "Valid phone required"}), 400

        users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"name": name, "phone": phone, "updated_at": datetime.now()}}
        )

        session["name"] = name
        return jsonify({"success": True, "message": "Details updated successfully"}), 200

    user["_id"] = str(user["_id"])
    return render_template("parent_details.html", user=user)

# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
