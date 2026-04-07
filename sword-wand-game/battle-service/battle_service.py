from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/battle", methods=["POST"])
def battle():

    player_attack = random.randint(5, 20)
    enemy_attack = random.randint(5, 20)

    if player_attack > enemy_attack:
        result = "player wins"
    else:
        result = "enemy wins"

    return jsonify({
        "player_attack": player_attack,
        "enemy_attack": enemy_attack,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)