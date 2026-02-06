from flask import Flask, render_template, request, jsonify
from data import data

app = Flask(__name__)

def clean(text):
    return text.lower().strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = clean(request.json.get("message", ""))
    reply = None

    # ---- SCHOOL BASIC ----
    if "school name" in msg or "नाम" in msg:
        reply = data["school_details"]["name"]

    elif "timing" in msg or "time" in msg or "समय" in msg:
        reply = data["school_details"]["general_timing"]

    # ---- MANAGEMENT ----
    elif "principal" in msg or "प्रधानाचार्य" in msg:
        reply = data["management"]["principal"]

    elif "vice principal" in msg or "vice-principal" in msg:
        reply = data["management"]["vice_principal"]

    elif "director" in msg or "निर्देशक" in msg:
        reply = data["management"]["director"]

    elif "system manager" in msg:
        reply = data["management"]["system_manager"]

    # ---- MOTTO / VISION / MISSION ----
    elif "motto" in msg or "aim" in msg or "उद्देश्य" in msg:
        reply = data["vision_mission"]["motto"]

    elif "mission" in msg:
        reply = ", ".join(data["vision_mission"]["mission"])

    elif "vision" in msg:
        reply = data["vision_mission"]["vision"]

    # ---- TEACHERS ----
    elif "chemistry teacher" in msg:
        reply = "Mr. Kuldeep Kumar"

    elif "biology teacher" in msg:
        reply = "Mrs. Vibha Ma’am"

    elif "physics teacher" in msg:
        reply = "Mr. Manish Mishra"

    elif "math teacher" in msg or "maths teacher" in msg:
        reply = "Mr. Manoj Dwivedi"

    elif "english teacher" in msg:
        reply = "Mr. Mohsin Khan"

    elif "hindi teacher" in msg:
        reply = "Mrs. Kanchan Shukla"

    elif "senior teacher" in msg:
        reply = "Kuldeep Sir, Vibha Ma’am, Manoj Sir, Manish Sir, Mohsin Sir, Kanchan Ma’am"

    # ---- EXAMS & EVENTS ----
    elif "final exam" in msg:
        reply = "Final exams start from the 1st week of March"

    elif "science exhibition" in msg:
        reply = "Science Exhibition is on 7 February 2026"

    # ---- SPORTS ----
    elif "best cricket" in msg or "best volleyball" in msg or "best player" in msg:
        reply = "Raj Kapoor"

    # ---- FOUNDERS ----
    elif "founder" in msg:
        reply = "Shashi Kapoor and Prince Bharti"

    # ---- FALLBACK ----
    if reply:
        return jsonify({"reply": f"Sinoy: {reply}"})

    return jsonify({
        "reply": (
            "Sinoy: Is question ka answer mere paas available nahi hai. "
            "Please contact school on 9838421968, 8317001959, 7518249280 "
            "ya directly school visit karein."
        )
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
