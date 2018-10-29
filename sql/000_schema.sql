CREATE TABLE users
(
  user_id SERIAL NOT NULL
    CONSTRAINT users_pkey
    PRIMARY KEY,
  nick    TEXT   NOT NULL
    CONSTRAINT users_nick_key
    UNIQUE
    CONSTRAINT users_nick_check
    CHECK (length(nick) < 32),
  name    TEXT   NOT NULL
    CONSTRAINT users_name_check
    CHECK (length(name) < 32),
  avatar  TEXT
    CONSTRAINT users_avatar_check
    CHECK (length(avatar) < 2048)
);

CREATE TABLE chats
(
  chat_id       SERIAL NOT NULL
    PRIMARY KEY,
  is_group_chat BOOLEAN,
  topic         TEXT
    CONSTRAINT chats_topic_check
    CHECK (length(topic) < 32),
  last_message  TEXT   NOT NULL
    CONSTRAINT chats_last_message_check
    CHECK (length(last_message) < 65536)
);

CREATE TABLE messages
(
  message_id SERIAL                  NOT NULL
    CONSTRAINT messages_pkey
    PRIMARY KEY,
  user_id    INTEGER                 NOT NULL
    CONSTRAINT messages_user_id_fkey
    REFERENCES users,
  chat_id    INTEGER                 NOT NULL
    CONSTRAINT messages_chat_id_fkey
    REFERENCES chats,
  content    TEXT                    NOT NULL
    CONSTRAINT messages_content_check
    CHECK (length(content) < 65536),
  added_at   TIMESTAMP DEFAULT now() NOT NULL
);

CREATE TABLE attachments
(
  attach_id  SERIAL  NOT NULL
    CONSTRAINT attachments_pkey
    PRIMARY KEY,
  chat_id    INTEGER NOT NULL
    CONSTRAINT attachments_chat_id_fkey
    REFERENCES chats,
  user_id    INTEGER NOT NULL
    CONSTRAINT attachments_user_id_fkey
    REFERENCES users,
  message_id INTEGER NOT NULL
    CONSTRAINT attachments_message_id_fkey
    REFERENCES messages,
  type       TEXT    NOT NULL
    CONSTRAINT attachments_type_check
    CHECK (length(type) < 32)
    CONSTRAINT attachments_type_check1
    CHECK (length(type) < 2048),
  url        TEXT    NOT NULL
);

CREATE TABLE members
(
  user_id              INTEGER           NOT NULL
    CONSTRAINT members_user_id_fkey
    REFERENCES users,
  chat_id              INTEGER           NOT NULL
    CONSTRAINT members_chat_id_fkey
    REFERENCES chats,
  last_read_message_id INTEGER           NOT NULL
    CONSTRAINT members_last_read_message_id_fkey
    REFERENCES messages,
  new_messages         INTEGER DEFAULT 0 NOT NULL
);
