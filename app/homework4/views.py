from app.homework4 import app
from flask import request, abort, jsonify


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return """
        <html>
            <head></head>
            <body>
                <form method="POST", action ="/form/">
                    <input name="username" >
                    <input name="password" >
                    <input type="submit" >
                </form>
            </body>
        </html>"""
    else:
        response = jsonify(request.form)
        response.status_code = 200
        return response


@app.route('/search_users/')
def search_users():
    query = str(request.args.get('param'))
    limit = int(request.args.get('limit'))

    user1 = {
        "user_id": 1,
        "nick": "the.good",
        "name": "Clint Eastwood",
        "avatar": "avatars/d9099cd0d3e6cb47fe3a9b0e631901fa.png"
    }

    user2 = {
        "user_id": 2,
        "nick": "the.bad",
        "name": "Pack Man",
        "avatar": "avatars.png"
    }

    response = jsonify({"users": [user1, user2]})
    response.status_code = 200
    return response


@app.route('/search_chats/')
def search_chats():
    query = str(request.args.get('param'))
    limit = int(request.args.get('limit'))

    chat1 = {
        "chat_id": 1,
        "is_group_chat": False,
        "topic": "Chuck Norris",
        "last_message": "argh!",
        "new_messages": 30,
        "last_read_message_id": 214
    }

    chat2 = {
        "chat_id": 2,
        "is_group_chat": True,
        "topic": "Mark Twen",
        "last_message": "YOU!",
        "new_messages": 13,
        "last_read_message_id": 41
    }

    response = jsonify({"chats": [chat1, chat2]})
    response.status_code = 200
    return response


@app.route('/create_pers_chat/', methods=['POST'])
def create_pers_chat():
    user_id = int(request.args.get('user_id'))

    chat = {
        "chat_id": 1,
        "is_group_chat": False,
        "topic": "Chuck Norris",
        "last_message": "argh!",
        "new_messages": 30,
        "last_read_message_id": 214
    }

    response = jsonify({"chat": chat})
    response.status_code = 200
    return response


@app.route('/create_group_chat/', methods=['POST'])
def create_group_chat():
    topic = str(request.args.get('topic'))

    chat = {
        "chat_id": 1,
        "is_group_chat": False,
        "topic": topic,
        "last_message": "argh!",
        "new_messages": 30,
        "last_read_message_id": 214
    }

    response = jsonify({"chat": chat})
    response.status_code = 200
    return response


@app.route('/add_members_to_group_chat/', methods=['POST'])
def add_members_to_group_chat():
    chat_id = int(request.args.get('chat_id'))
    user_ids = list(request.args.get('user_ids'))
    # No-op.
    response = jsonify({})
    response.status_code = 200
    return response


@app.route('/leave_group_chat/', methods=['POST'])
def leave_group_chat():
    chat_id = int(request.args.get('chat_id'))
    # No-op.
    response = jsonify({})
    response.status_code = 200
    return response


@app.route('/send_message/', methods=['POST'])
def send_message():
    chat_id = int(request.args.get('chat_id'))
    content = str(request.args.get('content'))
    attach_id = int(request.args.get('attach_id'))

    message = {
        "message_id": 200,
        "chat_id": chat_id,
        "user_id": 22,
        "content": content,
        "added_at": 1540198594
    }

    response = jsonify({"message": message})
    response.status_code = 200
    return response


@app.route('/read_message/')
def read_message():
    message_id = int(request.args.get('message_id'))

    chat = {
        "chat_id": 1,
        "is_group_chat": False,
        "topic": "abracadabra",
        "last_message": "argh!",
        "new_messages": 30,
        "last_read_message_id": 214
    }

    response = jsonify({"chat": chat})
    response.status_code = 200
    return response


@app.route('/upload_file/', methods=['POST'])
def upload_file():
    chat_id = int(request.args.get('chat_id'))
    content = str(request.args.get('content'))

    attach = {
        "attach_id": 1,
        "message_id": 200,
        "chat_id": 33,
        "user_id": 22,
        "type": "image",
        "url": "attach/e7ed63c5f815d5b308c9a3720dd1949d.png"
    }

    response = jsonify({"attach": attach})
    response.status_code = 200
    return response
