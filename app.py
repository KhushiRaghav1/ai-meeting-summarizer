from file_processor import extract_text_from_file
from flask import Flask, render_template, request, send_file
from summarizer import summarize_text
from database import init_db
from action_items import extract_action_items
from pdf_generator import generate_pdf
import sqlite3

app = Flask(__name__)

init_db()


@app.route("/", methods=["GET", "POST"])
def index():

    summary = ""
    actions = []

    if request.method == "POST":

        title = request.form["title"]

        transcript = request.form.get("transcript")

        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename != "":
            transcript = extract_text_from_file(uploaded_file)

        summary = summarize_text(transcript)

        actions = extract_action_items(transcript)

        conn = sqlite3.connect("meetings.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO meetings (title, transcript, summary) VALUES (?, ?, ?)",
            (title, transcript, summary)
        )

        conn.commit()
        conn.close()

    return render_template("index.html", summary=summary, actions=actions)


@app.route("/history")
def history():

    conn = sqlite3.connect("meetings.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title, summary, created_at FROM meetings ORDER BY created_at DESC")

    meetings = cursor.fetchall()

    conn.close()

    return render_template("history.html", meetings=meetings)


@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("meetings.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM meetings")
    total_meetings = cursor.fetchone()[0]

    cursor.execute("SELECT transcript, summary FROM meetings")
    data = cursor.fetchall()

    total_words = 0
    total_summary_words = 0

    for transcript, summary in data:
        total_words += len(transcript.split())
        total_summary_words += len(summary.split())

    reduction = 0

    if total_words > 0:
        reduction = round((1 - (total_summary_words / total_words)) * 100, 2)

    cursor.execute("SELECT title, created_at FROM meetings ORDER BY created_at DESC LIMIT 5")
    recent = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_meetings=total_meetings,
        total_words=total_words,
        reduction=reduction,
        recent=recent
    )


@app.route("/download_pdf", methods=["POST"])
def download_pdf():

    title = request.form["title"]
    summary = request.form["summary"]
    actions = request.form.getlist("actions")

    filename = generate_pdf(title, summary, actions)

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)