from flask import Flask
from instance.config import ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)

from app.sem4.views import *
