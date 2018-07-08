from flask import Flask
import os

app = Flask(__name__, instance_path=keys['path'])
app.config['SECRET_KEY'] = keys['secret']

from flaskexample import routes
