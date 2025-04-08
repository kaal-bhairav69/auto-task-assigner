# 🧠 Meeting Task Extractor using Whisper & spaCy

# 🧠 Meeting Task Extractor using Whisper & spaCyThis project takes meeting audio, converts it to text using OpenAI Whisper, and then extracts clear, actionable tasks using spaCy and custom NLP logic. Each person in the meeting gets exactly one consolidated task.

## 🚀 Features
- 🎤 Converts meeting audio to text using Whisper
- 🧠 Extracts tasks using spaCy and custom NLP
- 👤 Assigns **one clear task per person** (no duplicates!)
- ⚙️ Backend powered by Flask
- 🔍 Optionally integrates LLM-based task validation
- 📊 Can be deployed with a Streamlit or React frontend

## 🚀 Tech Stack

- **Python** – Main programming language
- **Flask** – Backend web framework
- **Whisper (OpenAI)** – For speech-to-text transcription
- **spaCy** – For Named Entity Recognition (NER) and task extraction
- **HTML/CSS/JavaScript** – For basic frontend interface
- **Bootstrap** – Styling the frontend
- **Werkzeug** – Flask file handling

## 🛠️ Setup Instructions

Follow these steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaal-bhairav69/your-repo-name.git
   cd your-repo-name
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
3. **Run the application**

   ```bash
   python app.py

## 📁 Project Structure

- app.py                  # Main Flask app
- task_extractor.py      # Task extraction logic using spaCy
- whisper.model          # Whisper model (loaded once and reused)
- requirements.txt       # Python dependencies
- uploads/               # Folder for uploaded audio files
- README.md              # Project documentation
