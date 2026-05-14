from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "")
    lang = data.get("lang", "en")

    reply, cards = get_response(user_message, lang)

    return jsonify({
        "reply": reply,
        "cards": cards
    })

if __name__ == "__main__":
    app.run(debug=True)