from app import db


def list_messages_by_chat(chat_id, limit):
    return db.query_all("""
    SELECT user_id, nick, name,
    message_id, content, added_at
    FROM messages
    JOIN users USING (user_id)
    WHERE chat_id =%(chat_id)s
    ORDER BY added_at DESC
    LIMIT %(limit)s
    """, chat_id=int(chat_id), limit=int(limit))


def find_users_by_name_or_nick(query, limit):
    return db.query_all("""
    SELECT * FROM users
    WHERE 
    lower(name) LIKE lower(%(query)s) 
    OR lower(nick) LIKE lower(%(query)s)
    LIMIT %(limit)s
    """, query='%' + str(query) + '%', limit=int(limit))


def list_chats_by_user(user_id):
    return db.query_all("""
    SELECT chats.* FROM members
    JOIN chats USING (chat_id)
    WHERE user_id = %(user_id)s
    """, user_id=int(user_id))


def list_personal_chats_by_user(user_id):
    return db.query_all("""
    SELECT chats.chat_id FROM members
    JOIN chats USING (chat_id)
    JOIN users USING (user_id)
    WHERE user_id = %(user_id)s AND is_group_chat = FALSE 
    """, user_id=int(user_id))


def get_members_by_chat_without_user(chat_id, user_id):
    return db.query_one("""
    SELECT user_id FROM members
    WHERE chat_id = %(chat_id)s
    AND user_id != %(user_id)s
    """, chat_id=int(chat_id), user_id=int(user_id))


def create_new_personal_chat():
    return db.insert("""
    INSERT INTO chats (is_group_chat, topic, last_message)
    VALUES (FALSE, 'topic', 'Sey HI')
    """)


def create_new_member(user_id, chat_id):
    return db.insert("""
    INSERT INTO members (user_id, chat_id)
    VALUES (%(user_id)s, %(chat_id)s)
    """, user_id=int(user_id), chat_id=chat_id)


def create_member_with_last_read_message(user_id, chat_id, last_read_message_id):
    return db.insert("""
    INSERT INTO members (user_id, chat_id, last_read_message_id)
    VALUES (%(user_id)s, %(chat_id)s, %(last_read_message_id)s)
    """, user_id=int(user_id), chat_id=int(chat_id), last_read_message_id=int(last_read_message_id))


def get_chat_by_id(chat_id):
    return db.query_one("""
    SELECT * FROM chats
    WHERE chat_id = %(chat_id)s
    """, chat_id=int(chat_id))


def get_max_chat_id():
    return db.query_one("""
    SELECT chat_id  
    FROM chats 
    ORDER BY chat_id DESC 
    LIMIT 1
    """)


def add_new_message(user_id, chat_id, content):
    return db.insert("""
    INSERT INTO messages (user_id, chat_id, content)
    VALUES (%(user_id)s, %(chat_id)s, %(content)s)
    """, user_id=int(user_id), chat_id=int(chat_id), content=str(content))


def get_max_message_id():
    return db.query_one("""
    SELECT message_id 
    FROM messages 
    ORDER BY message_id DESC 
    LIMIT 1
    """)


def add_new_attachment(chat_id, user_id, message_id, type, url):
    return db.insert("""
    INSERT INTO attachments (chat_id, user_id, message_id, type, url)
    VALUES (%(chat_id)s, %(user_id)s, %(message_id)s, %(type)s, %(url)s)
    """, chat_id=int(chat_id), user_id=int(user_id), message_id=int(message_id),
                     type=str(type), url=str(url))


def get_message_by_id(message_id):
    return db.query_one("""
        SELECT * FROM messages
        WHERE message_id = %(message_id)s
        """, message_id=int(message_id))
