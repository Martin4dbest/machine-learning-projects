from flask import Flask, render_template, request, jsonify
from chatbot import create_chat, send_message, PERSONALITIES

app = Flask(__name__)

# Store active chats (simple in-memory storage)
chats = {}


@app.route("/")
def home():
    return render_template(
        "index.html",
        personalities=PERSONALITIES
    )


@app.route("/start_chat", methods=["POST"])
def start_chat():

    data = request.get_json()

    name = data.get("name", "").strip()
    personality = data.get("personality", "").strip()
    custom_prompt = data.get("custom_prompt", "").strip()

    chat, personality_name = create_chat(
        name=name,
        personality_choice=personality,
        custom_prompt=custom_prompt
    )

    chats[name] = chat

    return jsonify({
        "success": True,
        "personality": personality_name
    })


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    name = data.get("name")
    message = data.get("message")

    if name not in chats:
        return jsonify({
            "success": False,
            "reply": "Chat session not found."
        })

    result = send_message(
        chats[name],
        message
    )

    return jsonify(result)


@app.route("/reset", methods=["POST"])
def reset():

    data = request.get_json()

    name = data.get("name")

    if name in chats:
        del chats[name]

    return jsonify({
        "success": True
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )