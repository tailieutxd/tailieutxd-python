from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Tailieutxd Python server running!"

@app.route("/submit", methods=["POST"])
def submit():
    code = request.json["code"]
    return jsonify({"received_code": code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
