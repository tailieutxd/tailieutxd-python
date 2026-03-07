from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Tailieutxd Python server running!"

@app.route("/grader")
def grader():
    return "Trang grader"

@app.route("/chambai")
def chambai():
    return "Trang cham bai"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
