from flask import Flask
from instance.config import ProductionConfig
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/appi/')
app.config.from_object(ProductionConfig)

from app.homework4.views import *
from app.lesson6.views import *
