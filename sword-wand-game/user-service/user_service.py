from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]

    if username in users:
        return jsonify({"error": "User exists"}), 400

    users[username] = password
    return jsonify({"message": "User created"})


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    if users.get(username) == password:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid login"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)