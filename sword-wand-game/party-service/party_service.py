from flask import Flask, request, jsonify

app = Flask(__name__)

parties = {}

@app.route("/create_party", methods=["POST"])
def create_party():
    data = request.json
    username = data["username"]

    parties[username] = {
        "heroes": [],
        "gold": 1000
    }

    return jsonify({"message": "Party created"})


@app.route("/add_hero", methods=["POST"])
def add_hero():
    data = request.json
    username = data["username"]
    hero = data["hero"]

    parties[username]["heroes"].append(hero)

    return jsonify({"message": "Hero added"})


@app.route("/get_party/<username>")
def get_party(username):
    return jsonify(parties.get(username, {}))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)