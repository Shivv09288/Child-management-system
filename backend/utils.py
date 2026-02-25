"""
Utility functions for Child Management System
Helper functions for validation, formatting, and common operations
"""

import re
from datetime import datetime, timedelta

def validate_email(email):
    """
    Validate email format
    Returns: True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """
    Validate phone number (at least 10 digits)
    Returns: True if valid, False otherwise
    """
    phone_digits = re.sub(r'\D', '', phone)
    return len(phone_digits) >= 10

def validate_password(password):
    """
    Validate password strength
    Requirements: At least 6 characters
    Returns: (is_valid, message)
    """
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    return True, "Password is strong"

def calculate_age(date_of_birth_str):
    """
    Calculate age from date of birth string (format: YYYY-MM-DD)
    Returns: Age in years
    """
    try:
        dob = datetime.strptime(date_of_birth_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
    except:
        return None

def format_date(date_obj):
    """
    Format date object to readable string
    Returns: Formatted date string (e.g., "January 15, 2024")
    """
    try:
        if isinstance(date_obj, str):
            return date_obj
        return date_obj.strftime("%B %d, %Y")
    except:
        return str(date_obj)

def get_attendance_summary(attendance_records):
    """
    Generate attendance summary
    Returns: dict with present, absent, and percentage
    """
    if not attendance_records:
        return {"present": 0, "absent": 0, "percentage": 0}
    
    total = len(attendance_records)
    present = len([r for r in attendance_records if r.get("status") == "Present"])
    absent = total - present
    percentage = (present / total * 100) if total > 0 else 0
    
    return {
        "present": present,
        "absent": absent,
        "total": total,
        "percentage": round(percentage, 2)
    }

def get_age_group(age):
    """
    Categorize child by age group
    Returns: Age group string
    """
    if age < 3:
        return "Toddler"
    elif age < 6:
        return "Preschool"
    elif age < 13:
        return "Elementary"
    elif age < 16:
        return "Middle School"
    else:
        return "High School"

def sanitize_input(input_string):
    """
    Basic input sanitization to prevent injection
    Returns: Sanitized string
    """
    if not input_string:
        return ""
    # Remove potentially dangerous characters
    dangerous_chars = ['<', '>', '"', "'", '&', ';']
    sanitized = input_string
    for char in dangerous_chars:
        sanitized = sanitized.replace(char, '')
    return sanitized.strip()

def generate_username(email):
    """
    Generate username from email
    Returns: Username string
    """
    return email.split('@')[0].lower()

def is_date_valid(date_str):
    """
    Validate if string is valid date (YYYY-MM-DD format)
    Returns: True if valid, False otherwise
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def get_next_vaccination_due(last_vaccination_date):
    """
    Calculate next vaccination due date (assuming annual)
    Returns: Next due date string
    """
    try:
        last_date = datetime.strptime(last_vaccination_date, "%Y-%m-%d")
        next_due = last_date + timedelta(days=365)
        return next_due.strftime("%Y-%m-%d")
    except:
        return None

# Sample usage functions
def demo_validation():
    """Demo function to show validation usage"""
    print("Email validation:", validate_email("user@example.com"))
    print("Phone validation:", validate_phone("1234567890"))
    print("Age:", calculate_age("2020-05-15"))
    print("Age group:", get_age_group(4))
    print("Attendance summary:", get_attendance_summary([
        {"status": "Present"},
        {"status": "Present"},
        {"status": "Absent"}
    ]))

if __name__ == "__main__":
    demo_validation()
