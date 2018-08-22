from flask import Flask, request, redirect, render_template
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

item_list = []

@app.route("/")
def add_item():
    item = request.args.get("theinput")
    item_list.append(item)
    return render_template("body.html", list=item_list)





app.run()