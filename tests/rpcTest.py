from unittest import TestCase
from app import app
import json


class JSONRPCTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_name(self):
        rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "print_name", "params": [], "id": "1" }')
        print(rv.data)
        self.assertEqual('', json.loads(rv.data))

