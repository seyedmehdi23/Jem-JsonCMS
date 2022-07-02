from flask import Flask
from modules import *

app = Flask(__name__)

@app.route("/")
def index():
    return "JemCMS Init"