from flask import Flask, redirect, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from markupsafe import Markup
import json
import urllib

app = Flask(__name__)
version = "1.37"

@app.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)

def set_current_json(name):
    with open("json_data/current_data.txt", "w") as file:
        file.write(name)
        return True


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/load_json", methods=["POST"])
def load_json():
    res = False
    if request.form["url"] != "":
        res = load_json_by_url(request.form["url"])
    elif request.files["json_file"]:
        res = load_json_by_file(request.files["json_file"])
    if res:
        return redirect("/view", 302)

def load_json_by_url(url):
    if url:
        url = Markup.escape(request.form["url"])
        data = urllib.urlopen(url).read()
        if set_current_json(data):
            return True

def load_json_by_file(file):
    if file:
        file.save(f"json_data/{secure_filename(file.filename)}")
        if set_current_json(secure_filename(file.filename)):
            return True


@app.route("/view", methods=["GET"])
def view_json():
    keys = ["a", "b"]
    values = ["a value", "b value"]
    text = "cherto pert"
    json = "boz"
    return render_template("json_view.html", keys=keys, values=values, text=text, json=json)

print(
    f"""
    JemCMS V{version}
    JEM Started!
    Developed By Seyed Mahdi Hosseini
    Github & Linkedin : seyedmehdi23
    """)