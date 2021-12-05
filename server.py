# server flask
from flask import Flask

app = Flask(__name__)

UPLOAD_FOLDER ="C:/Users/MANUEL_SE/Documents/dev/python/projects/env1/flask/uploads/"

app.config['UPLOAD_FLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return "MI PRIMERA WEB CON FLASK"
