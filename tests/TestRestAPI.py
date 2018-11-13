from unittest import TestCase
import json
from flask import jsonify

from app import app
from tests.testUtils.TestRestAPIUtils import compare_two_json


class TestRestAPI(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_login(self):
        with app.app_context():
            params = json.loads({"username": "ab", "password": "ba"})
            response = self.app.post('/api/',
                                     data={"jsonrpc": "2.0", "method": "login", "params": [params], "id": "1"})
            expect = jsonify({"username": "ab", "password": "ba"})
            print(response)
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_search_users(self):
        with app.app_context():
            params = json.loads('{"param": "t", "limit": 1}')
            print("""{"jsonrpc": "2.0", "method": "search_users", "params": {"param": "t", "limit": 1}, "id": "1"}""")
            response = self.app.post('/api/',
                                     data="""{"jsonrpc": "2.0", "method": "search_users", "params": """
                                          + """{"param": "t", "limit": 1}"""
                                            +""", "id": "1"}""")
            print(response.data)

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
            response = self.app.get('/list_chats/?userid=1')

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
            response = self.app.post('/create_pers_chat/?fuserid=1&suserid=3')

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
            response = self.app.post('/create_group_chat/?topic=' + topic)

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
            response = self.app.post('/add_members_to_group_chat/?chat_id=1&user_ids=[1, 2, 3]')
            expect = jsonify({})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_leave_group_chat(self):
        with app.app_context():
            response = self.app.post('/leave_group_chat/?chat_id=1')
            expect = jsonify({})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_send_message(self):
        with app.app_context():
            chat_id = 1
            content = 'Hello, world!'
            response = self.app.post('/send_message/?attach_id=1&chat_id=' + str(chat_id) + '&content=' + content)

            message = {
                "message_id": 200,
                "chat_id": chat_id,
                "user_id": 22,
                "content": content,
                "added_at": 1540198594
            }

            expect = jsonify({"message": message})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_read_message(self):
        with app.app_context():
            response = self.app.get('/read_message/?message_id=1')

            chat = {
                "chat_id": 1,
                "is_group_chat": False,
                "topic": "abracadabra",
                "last_message": "argh!",
                "new_messages": 30,
                "last_read_message_id": 214
            }

            expect = jsonify({"chat": chat})
            self.assertEqual(200, response.status_code)
            self.assertEqual("application/json", response.mimetype)
            self.assertTrue(compare_two_json(expect.data, response.data))

    def test_upload_file(self):
        with app.app_context():
            response = self.app.post('/upload_file/?chat_id=1&content=Hello')

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
