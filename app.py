from flask import Flask, render_template, request, redirect, url_for, flash
import gemini_summarize
from werkzeug.utils import secure_filename
import whisper
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/audio'

@app.route('/')
def index():
    return render_template("index.html", summary="", transcription="")

@app.route("/", methods=["POST"])
def summary():    
    transcript = request.form['transcript'] 
    summary = gemini_summarize.get_summary(transcript) 
    return render_template("index.html", summary=summary)

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio_file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['audio_file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        model = whisper.load_model("base")
        transcription = model.transcribe(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template("index.html", summary="", transcription=transcription["text"])


if __name__ == '__main__':
    app.run()