"""
Database Configuration Module
Handles MongoDB connection setup
"""
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection string
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "child_management_db"

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collection references
users_collection = db["users"]
children_collection = db["children"]
attendance_collection = db["attendance"]
health_collection = db["health"]

def init_db():
    """Initialize database with collections and indexes"""
    try:
        # Create collections if they don't exist
        if "users" not in db.list_collection_names():
            db.create_collection("users")
            users_collection.create_index("email", unique=True)
            print("✓ Users collection created")
        
        if "children" not in db.list_collection_names():
            db.create_collection("children")
            print("✓ Children collection created")
        
        if "attendance" not in db.list_collection_names():
            db.create_collection("attendance")
            print("✓ Attendance collection created")
        
        if "health" not in db.list_collection_names():
            db.create_collection("health")
            print("✓ Health records collection created")
        
        print("✓ Database initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Database initialization error: {str(e)}")
        return False

def close_connection():
    """Close MongoDB connection"""
    try:
        client.close()
        print("✓ Database connection closed")
    except Exception as e:
        print(f"✗ Error closing connection: {str(e)}")
