from flask import Flask
from flask_jsonrpc import JSONRPC

from instance.config import ProductionConfig

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/appi/')
app.config.from_object(ProductionConfig)

from app.views import *
from app.lesson6.views import *
