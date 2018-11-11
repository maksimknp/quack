from app import jsonrpc


@jsonrpc.method("print_name")
def foo():
    return {"name": "Ivan"}
