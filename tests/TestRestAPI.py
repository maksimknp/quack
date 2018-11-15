from unittest import TestCase
import json
from flask import jsonify
from app import app
from tests.testUtils.TestRestAPIUtils import *
from instance.config import JSONRPC_URL


class TestRestAPI(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_login(self):
        with app.app_context():
            request = get_request_json('login', username='ab', password='ba')
            response = self.app.post(JSONRPC_URL, data=request)
            expect = jsonify({"username": "ab", "password": "ba"})

            print(response.data)
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_search_users(self):
        with app.app_context():
            request = get_request_json('search_users', param='t', limit=1)
            response = self.app.post(JSONRPC_URL, data=request)

            user1 = {
                "user_id": 2,
                "nick": "tomy_cash",
                "name": "Tomy Cash",
                "avatar": "www.tomy.cash.ru"
            }

            expect = jsonify({"users": [user1]})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_list_chats(self):
        with app.app_context():
            request = get_request_json('list_chats', user_id=1)
            response = self.app.post(JSONRPC_URL, data=request)

            print(response)
            print(response.data)

            chat1 = {
                "chat_id": 1,
                "is_group_chat": True,
                "topic": "general",
                "last_message": "Hello, everyone!"
            }

            chat2 = {
                "chat_id": 2,
                "is_group_chat": False,
                "topic": "Chat with teacher",
                "last_message": "OK, do it"
            }

            expect = jsonify({"chats": [chat1, chat2]})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_create_pers_chat(self):
        with app.app_context():
            request = get_request_json('create_pers_chat', first_user_id=1, second_user_id=3)
            response = self.app.post(JSONRPC_URL, data=request)

            chat = {
                "chat_id": 2,
                "is_group_chat": False,
                "topic": "Chat with teacher",
                "last_message": "OK, do it",
            }

            expect = jsonify({"chat": chat})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_create_group_chat(self):
        with app.app_context():
            topic = 'lalal'
            request = get_request_json('create_group_chat', topic=topic)
            response = self.app.post(JSONRPC_URL, data=request)

            chat = {
                "chat_id": 1,
                "is_group_chat": False,
                "topic": topic,
                "last_message": "argh!",
                "new_messages": 30,
                "last_read_message_id": 214
            }

            expect = jsonify({"chat": chat})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_add_members_to_group_chat(self):
        with app.app_context():
            request = get_request_json('add_members_to_group_chat', chat_id=1, user_ids=[1, 2, 3])
            response = self.app.post(JSONRPC_URL, data=request)
            expect = jsonify({})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_leave_group_chat(self):
        with app.app_context():
            request = get_request_json('leave_group_chat', chat_id=1)
            response = self.app.post(JSONRPC_URL, data=request)
            expect = jsonify({})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_send_message(self):
        with app.app_context():
            chat_id = 3
            user_id = 3
            content = 'Hello, world!'
            request = get_request_json('send_message', user_id=user_id, chat_id=chat_id, content=content)
            response = self.app.post(JSONRPC_URL, data=request)

            print(response)
            print(response.data)

            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            # self.assertEqual(response.data.get('content'), content)
            # self.assertEqual(response.data.get('user_id'), user_id)
            # self.assertEqual(response.data.get('chat_id'), chat_id)

    def test_read_message(self):
        with app.app_context():
            request = get_request_json('read_message', user_id=3, message_id=1)
            response = self.app.post(JSONRPC_URL, data=request)

            print(response.data)

            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            # self.assertTrue(compare_two_json(expect.data, response.data))

    def test_upload_file(self):
        with app.app_context():
            request = get_request_json('upload_file', chat_id=1, content='Hello')
            response = self.app.post(JSONRPC_URL, data=request)

            attach = {
                "attach_id": 1,
                "message_id": 200,
                "chat_id": 33,
                "user_id": 22,
                "type": "image",
                "url": "attach/e7ed63c5f815d5b308c9a3720dd1949d.png"
            }

            expect = jsonify({"attach": attach})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def tearDown(self):
        pass
