from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json
import os

app = Flask(__name__)

# שימוש בסביבת סביבה עבור כתובת MongoDB
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://mongodb:27017/userdb")
mongo = PyMongo(app)

@app.route('/add_user', methods=['POST'])
def add_user():
    # בדיקה שהבקשה היא JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    
    if not first_name or not last_name:
        return jsonify({"error": "First name and last name are required"}), 400
    
    user_data = {
        "first_name": first_name,
        "last_name": last_name
    }
    
    mongo.db.users.insert_one(user_data)
    return jsonify({"message": "User added successfully", "user": user_data}), 201

@app.route('/get_users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find())
    return json.loads(json_util.dumps(users))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
