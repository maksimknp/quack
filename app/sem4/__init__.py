from flask import Flask

app = Flask(__name__)

from app.sem4.views import *
