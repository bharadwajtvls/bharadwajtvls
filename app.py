from flask import Flask, request, render_template, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb+srv://pingalipraneeth1:DgCwSk9Cn9mTx32a@augatepass.1dvhlzv.mongodb.net/gatepass_db?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route("/")
def hello():
    return render_template('index.html')

# Route to add guest details
@app.route("/add_guest", methods=["POST"])
def add_guest():
    data = request.json
    name = data.get("name")
    action = data.get("action")

    if not name or not action:
        return jsonify({"error": "Name and action are required"}), 400

    # Insert guest details into MongoDB
    guest = {"name": name, "action": action}
    mongo.db.guests.insert_one(guest)
    return jsonify({"message": "Guest added successfully"}), 201

# Route to fetch all guests
@app.route("/get_guests", methods=["GET"])
def get_guests():
    guests = list(mongo.db.guests.find({}, {"_id": 0}))
    return jsonify(guests), 200

if __name__ == "__main__":
    app.run(debug=True)
