from unittest import TestCase
from app.homework4 import app


class JSONRPCTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_name(self):
        rv = self.app.post('/appi/', data='{"jsonrpc": "2.0", "method": "print_name", "params": [], "id": "1" }')
        print(rv.data)
        self.assertEqual('', rv.data)

