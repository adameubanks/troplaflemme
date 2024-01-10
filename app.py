from flask import Flask, render_template, request
import gemini_summarize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", summary="")

@app.route("/", methods=["POST"])
def summary():    
    transcript = request.form['transcript'] 
    summary = gemini_summarize.get_summary(transcript) 
    return render_template("index.html", summary=summary)

if __name__ == '__main__':
    app.run()