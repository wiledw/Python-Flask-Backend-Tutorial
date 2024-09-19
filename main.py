import os
from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the MongoDB connection string from the environment variable
MONGO_URI = os.getenv('MONGO_URI')

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client['flaskApplication']  
users_collection  = db['users']  

# Create User (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    # Validate required fields
    if 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and Email are required!'}), 400
    
    user_id = users_collection.insert_one({
        'name': data['name'],
        'email': data['email'],
        'age': data.get('age', None)  # Optional age field
    }).inserted_id
    
    return jsonify({"message": "User created", "id": str(user_id)}), 201

# Read All Users (GET)
@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'_id': 1, 'name': 1, 'email': 1, 'age': 1}))
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string
    return jsonify(users), 200

# Read Single User by ID (GET)
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({'_id': ObjectId(user_id)}, {'_id': 1, 'name': 1, 'email': 1, 'age': 1})
    
    if user:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404
    
# Update User by ID (PUT)
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    update_data = {}
    
    if 'name' in data:
        update_data['name'] = data['name']
    if 'email' in data:
        update_data['email'] = data['email']
    if 'age' in data:
        update_data['age'] = data['age']
    
    if not update_data:
        return jsonify({'error': 'Nothing to update'}), 400
    
    result = users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': update_data})
    
    if result.matched_count > 0:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
    
# Delete User by ID (DELETE)
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users_collection.delete_one({'_id': ObjectId(user_id)})
    
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
