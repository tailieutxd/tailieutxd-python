from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

PROBLEM = "problems/sum"

def run_test(code, input_file):

    os.makedirs("temp", exist_ok=True)

    with open("temp/code.py", "w") as f:
        f.write(code)

    with open(input_file) as f:
        input_data = f.read()

    result = subprocess.run(
        ["python3", "temp/code.py"],
        input=input_data,
        text=True,
        capture_output=True,
        timeout=2
    )

    return result.stdout.strip()


@app.route("/")
def home():
    return "Judge server running"


@app.route("/submit", methods=["POST"])
def submit():

    code = request.json["code"]

    tests = [
        ("input1.txt", "output1.txt"),
        ("input2.txt", "output2.txt")
    ]

    results = []
    passed = 0

    for inp, out in tests:

        output = run_test(code, f"{PROBLEM}/{inp}")

        with open(f"{PROBLEM}/{out}") as f:
            expected = f.read().strip()

        if output == expected:
            results.append("OK")
            passed += 1
        else:
            results.append("Wrong")

    return jsonify({
        "results": results,
        "score": f"{passed}/{len(tests)}"
    })


app.run(host="0.0.0.0", port=5000)
