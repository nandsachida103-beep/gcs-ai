from flask import Flask, render_template, request, jsonify
from data import SCHOOL_DATA, CONTACT

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").lower()

    for key, answer in SCHOOL_DATA.items():
        if key in user_msg:
            return jsonify({
                "reply": f"Sinoy:-- {answer}"
            })

    return jsonify({
        "reply": f"Sinoy:-- Is question ka jawab available nahi hai. Kripya in numbers par contact karein {CONTACT['numbers']} ya school visit karein."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
