from flask import request, jsonify

from app import app, model


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return """
        <html>
            <head></head>
            <body>
                <form method="POST", action ="/login/">
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
    users = model.find_users_by_name_or_nick(query, limit)
    response = jsonify({"users": users})
    response.status_code = 200
    return response


@app.route('/list_chats/')
def list_chats():
    user_id = str(request.args.get('userid'))
    chats = model.list_chats_by_user(user_id)
    response = jsonify({"chats": chats})
    response.status_code = 200
    return response


@app.route('/create_pers_chat/', methods=['POST'])
def create_pers_chat():
    first_user_id = int(request.args.get('fuserid'))
    second_user_id = int(request.args.get('suserid'))

    if first_user_id == second_user_id:
        return

    personal_chats = model.list_personal_chats_by_user(first_user_id)
    new_chat_id = 0
    for i in personal_chats:
        chat_id = i.get('chat_id')

        other_user_id = model.get_members_by_chat_without_user(chat_id, first_user_id).get('user_id')
        if other_user_id == second_user_id:
            new_chat_id = chat_id
            break

    if new_chat_id == 0:
        model.create_new_personal_chat()
        new_chat_id = int(model.get_max_chat_id().get('chat_id'))
        model.create_new_member(first_user_id, new_chat_id)
        model.create_new_member(second_user_id, new_chat_id)

    chat = model.get_chat_by_id(new_chat_id)
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
