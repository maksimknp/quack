import unittest
from app.homework2.Item import Item
from app.homework2.DoubleLinkedList import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):

    def test_push(self):
        list = DoubleLinkedList(Item("Moscow"))
        list.push("Minsk")
        self.assertEqual(list.last().get_data(), "Minsk")

    def test_pop(self):
        list = DoubleLinkedList(Item("Moscow"))
        list.push("Minsk")
        list.pop()
        self.assertEqual(list.last().get_data(), "Moscow")
        list.pop()
        self.assertIsNone(list.last())
        self.assertEqual(list.pop(), "List is empty")

    def test_unshift(self):
        list = DoubleLinkedList(Item("Moscow"))
        list.unshift("Minsk")
        self.assertEqual(list.first().get_data(), "Minsk")

    def test_shift(self):
        list = DoubleLinkedList(Item("Moscow"))
        list.push("Minsk")
        list.shift()
        self.assertEqual(list.last().get_data(), "Minsk")
        list.shift()
        self.assertIsNone(list.last())
        self.assertEqual(list.shift(), "List is empty")

    def test_len(self):
        list = DoubleLinkedList(Item("London"))
        self.assertEqual(list.len(), 1)
        list.pop()
        self.assertEqual(list.len(), 0)
        list.push("Minsk")
        self.assertEqual(list.len(), 1)
        list.push("Moscow")
        self.assertEqual(list.len(), 2)

    def test_delete(self):
        list = DoubleLinkedList(Item("Moscow"))
        self.assertTrue(list.delete("Moscow"))
        self.assertEqual(list.delete("Moscow"), "List is empty")
        list.push("Minsk")
        self.assertFalse(list.delete("Moscow"))

    def test_contains(self):
        list = DoubleLinkedList()
        self.assertEqual(list.contains("Moscow"), "List is empty")
        list.push("Moscow")
        self.assertTrue(list.contains("Moscow"))

    def test_first_and_last(self):
        list = DoubleLinkedList()
        list.push("Minsk")
        list.push("Moscow")
        list.push("London")
        self.assertEqual(list.first().get_data(), "Minsk")
        self.assertEqual(list.last().get_data(), "London")