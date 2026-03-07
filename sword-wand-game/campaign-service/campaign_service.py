from flask import Flask, jsonify
import random

app = Flask(__name__)

rooms = ["battle", "inn"]

@app.route("/next_room")
def next_room():

    room = random.choices(
        rooms,
        weights=[0.6,0.4]
    )[0]

    return jsonify({"room": room})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)