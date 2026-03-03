
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to add two numbers
def add(a, b):
    return a + b

# Root route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Add API. Use /add?a=NUM&b=NUM"})

# /add route
@app.route("/add")
def add_route():
    try:
        # Get 'a' and 'b' from query parameters
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        result = add(a, b)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400

# Required for Vercel serverless functions
if __name__ == "__main__":
    app.run()
