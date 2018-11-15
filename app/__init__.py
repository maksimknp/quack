from flask import Flask
from flask_jsonrpc import JSONRPC

from instance.config import ProductionConfig
from instance.config import JSONRPC_URL

app = Flask(__name__)
jsonrpc = JSONRPC(app, JSONRPC_URL)
app.config.from_object(ProductionConfig)

from app.controller import *
from app.lesson6.views import *
