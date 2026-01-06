from flask import Flask, render_template, request, jsonify
from main import ask_fishy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)
        user_input = data["user_input"]

        print("Received:", user_input)   # DEBUG PROOF

        output = ask_fishy(user_input)

        print("Output:", output)         # DEBUG PROOF

        return jsonify({"output": output})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"output": "Fishy crashed internally 🐟"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
