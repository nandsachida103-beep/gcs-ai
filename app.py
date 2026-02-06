from flask import Flask, render_template, request
from data import SCHOOL_INFO, CONTACT

app = Flask(__name__)

def clean(text):
    return text.lower()

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""

    if request.method == "POST":
        q = clean(request.form["question"])

        if "motto" in q or "मोटो" in q:
            reply = SCHOOL_INFO["motto"]

        elif "principal" in q or "प्रधानाचार्य" in q:
            reply = "Name of principal is Mrs. Neha Pandey"

        elif "vice" in q:
            reply = "Vice Principal is Mr. Ram Jit Yadav"

        elif "director" in q:
            reply = "Director is Mr. Shailesh Pandey"

        elif "monitor" in q:
            reply = str(SCHOOL_INFO["monitors"])

        elif "teacher" in q:
            reply = "Senior Teachers: " + ", ".join(SCHOOL_INFO["senior_teachers"].keys())

        elif "science exhibition" in q:
            reply = "Science Exhibition is on 7 February 2026"

        elif "best player" in q or "cricket" in q:
            reply = "Best cricket & volleyball player of school is Raj Kapoor"

        elif "founder" in q:
            reply = "Founders of GCS AI are Shashi Kapoor and Prince Bharti"

        else:
            reply = f"I don’t have this information. Please contact {CONTACT} or visit the school."

    return render_template("index.html", answer=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
