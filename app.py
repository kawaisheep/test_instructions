from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='.')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<path:filename>")
def files(filename):
    return send_from_directory('.', filename)
