from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(_name_)
CORS(app)  # Enable Cross-Origin Resource Sharing for development

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
collection = db['your_collection']

@app.route('/api/data', methods=['POST'])
def save_data():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Data saved successfully!"})

if _name_ == '_main_':
    app.run(debug=True)