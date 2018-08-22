from flask import Flask, request, redirect, render_template
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=["GET"])
def home():
    return render_template("body.html")

app.run()