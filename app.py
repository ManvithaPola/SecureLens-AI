from flask import Flask, render_template, request, jsonify
import os

from modules.parser import extract_text
from modules.detector import detect_sensitive_data
from modules.classifier import classify_risk
from modules.summarizer import generate_summary
from modules.chat import ask_document
from modules.rag import build_vector_store
from modules.masker import mask_text
app = Flask(__name__)

# -------------------------------------------------
# Global Variables
# -------------------------------------------------

current_document_text = ""
current_detections = {}
current_risk = {}
current_masked_text = ""
# -------------------------------------------------
# Upload Folder
# -------------------------------------------------

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -------------------------------------------------
# Home
# -------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------------------------
# Upload Document
# -------------------------------------------------

@app.route("/upload", methods=["POST"])
def upload():

    global current_document_text
    global current_detections
    global current_risk

    file = request.files["document"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Extract text
    text = extract_text(filepath)

    current_document_text = text

    # Build FAISS vector store
    build_vector_store(text)

    # Detect sensitive data
    detections = detect_sensitive_data(text)

    current_detections = detections

    # Risk Classification
    risk = classify_risk(detections)

    current_risk = risk

    # AI Summary
    summary = generate_summary(
        text,
        detections,
        risk
    )

    return jsonify({
        "detections": detections,
        "risk": risk,
        "summary": summary
    })


# -------------------------------------------------
# AI Chat
# -------------------------------------------------

@app.route("/chat", methods=["POST"])
def chat():

    global current_document_text
    global current_detections
    global current_risk

    data = request.get_json()

    question = data.get("question", "")

    if current_document_text == "":
        return jsonify({
            "answer": "Please upload a document first."
        })

    answer = ask_document(
        question,
        current_detections,
        current_risk
    )

    return jsonify({
        "answer": answer
    })


# -------------------------------------------------
# Run App
# -------------------------------------------------

@app.route("/mask", methods=["POST"])
def mask_document():

    global current_document_text
    global current_detections
    global current_masked_text

    if current_document_text == "":
        return jsonify({
            "masked_text": "Please upload a document first."
        })

    current_masked_text = mask_text(
        current_document_text,
        current_detections
    )

    return jsonify({
        "masked_text": current_masked_text
    })

if __name__ == "__main__":
    app.run(debug=True)