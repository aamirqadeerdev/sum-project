from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b  # fixed addition

@app.route("/add")
def add_route():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        result = add(a, b)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Add API. Use /add?a=NUM&b=NUM"})