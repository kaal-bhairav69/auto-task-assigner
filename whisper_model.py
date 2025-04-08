import whisper 

print("loading whisper model....")

model = whisper.load_model("medium")

print("model loaded succesfully....")


def transcribe_audio(filepath):
    result = model.transcribe(filepath,task='translate')
    return result["text"]
