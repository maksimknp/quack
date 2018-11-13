from flask import request, jsonify
from app import app, model, jsonrpc


@jsonrpc.method("login")
def login():
    response = jsonify(request.data)
    print(response)
    response.status_code = 200
    return response


@jsonrpc.method("search_users")
def search_users(param, limit):
    print('--------------------------')
    # query = str(request.args.get('param'))
    # limit = int(request.args.get('limit'))
    users = model.find_users_by_name_or_nick(param, limit)
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

        other_user_id = model.get_member_by_chat_without_user(first_user_id, chat_id).get('user_id')
        if other_user_id == second_user_id:
            new_chat_id = chat_id
            break

    if new_chat_id == 0:
        new_chat_id = model.create_new_personal_chat()
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
    user_id = int(request.args.get('user_id'))
    chat_id = int(request.args.get('chat_id'))
    content = str(request.args.get('content'))
    attach_id = int(request.args.get('attach_id', 0))

    message_id = int(model.add_new_message(user_id, chat_id, content))
    model.create_member_with_last_read_message(user_id, chat_id, message_id)

    if attach_id != 0:
        model.add_new_attachment(chat_id, user_id, message_id, 'some_type', 'some_url')

    message = model.get_message_by_id(message_id)
    response = jsonify({"message": message})
    response.status_code = 200
    return response


@app.route('/read_message/')
def read_message():
    message_id = int(request.args.get('messageid'))
    user_id = int(request.args.get('userid'))

    chat_id = model.get_message_by_id(message_id).get('chat_id')
    print(chat_id)
    model.decrease_message_count_by_user_and_chat(user_id, chat_id)
    chat = model.get_chat_with_new_messages(user_id, chat_id)

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


@app.route('/chat_messages/', methods=['GET'])
def chat_messages():
    chat_id = int(request.args.get('chatid'))
    limit = int(request.args.get('limit'))
    messages = model.list_messages_by_chat(chat_id, limit)
    response = jsonify({"messages": messages})
    response.status_code = 200
    return response

