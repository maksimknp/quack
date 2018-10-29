from app.homework4 import app, jsonrpc
from flask import request, abort, jsonify


@jsonrpc.method("print_name")
def foo():
    return {"name": "Ivan"}
