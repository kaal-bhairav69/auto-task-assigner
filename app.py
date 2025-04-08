from flask import Flask, redirect, request, url_for, render_template
import os
from whisper_model import transcribe_audio
from task_extractor import extract_tasks_clean

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=['POST', 'GET'])
def index():
    tasks = []

    if request.method == 'POST':
        print("Received POST request")

        if 'audio' not in request.files:
            print("No audio part in request")
            return "No audio file uploaded", 400

        audio = request.files['audio']

        if audio.filename != "":
            print(f"Received file: {audio.filename}")
            path = os.path.join(UPLOAD_FOLDER, audio.filename)
            audio.save(path)
            print(f"Saved audio to: {path}")

            transcript = transcribe_audio(path)
            print(f"Transcript: {transcript}")

            tasks = extract_tasks_clean(transcript)
            print(f"Extracted tasks: {tasks}")

    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=False)
