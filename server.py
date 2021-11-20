# server flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "MI PRIMERA WEB CON FLASK"
