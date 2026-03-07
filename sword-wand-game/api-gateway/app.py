from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Legends of Sword and Wand Game"

if __name__ == "__main__":
    app.run(port=8080)