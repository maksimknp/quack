from unittest import TestCase
from app.sem4 import app


class AppTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(200, rv.status_code)
        self.assertEqual(b'Hello, world!', rv.data)
        self.assertEqual("text/html", rv.mimetype)

    def test_form(self):
        rv = self.app.post('/form/', data={"first_name": "ab", "last_name": "ba"})
        self.assertEqual(b'{"first_name":"ab","last_name":"ba"}\n', rv.data)

    def tearDown(self):
        pass
