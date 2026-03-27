from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Віддача статичних файлів з папки static/
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory('static', filename)