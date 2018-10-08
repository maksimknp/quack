import unittest
from app.homework2.Item import Item
from app.homework2.DoubleLinkedList import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):

    def test_push(self):
        cities = DoubleLinkedList()
        for city in ['Moscow', 'Minsk']:
            cities.push(city)
        self.assertEqual(cities.last().get_data(), 'Minsk')

    def test_pop(self):
        cities = DoubleLinkedList()
        for city in ['Moscow', 'Minsk']:
            cities.push(city)
        self.assertEqual(cities.pop().get_data(), 'Minsk')
        self.assertEqual(cities.pop().get_data(), 'Moscow')
        self.assertIsNone(cities.pop())

    def test_unshift(self):
        cities = DoubleLinkedList(Item('Moscow'))
        cities.unshift('Minsk')
        self.assertEqual(cities.first().get_data(), 'Minsk')

    def test_shift(self):
        cities = DoubleLinkedList()
        for city in ['Moscow', 'Minsk']:
            cities.push(city)
        self.assertEqual(cities.shift().get_data(), 'Moscow')
        self.assertEqual(cities.shift().get_data(), 'Minsk')
        self.assertIsNone(cities.shift())

    def test_len(self):
        cities = DoubleLinkedList(Item('London'))
        self.assertEqual(cities.len(), 1)
        cities.pop()
        self.assertEqual(cities.len(), 0)
        cities.push('Minsk')
        self.assertEqual(cities.len(), 1)
        cities.push('Moscow')
        self.assertEqual(cities.len(), 2)

    def test_delete(self):
        cities = DoubleLinkedList()
        for city in range(3):
            cities.push('Moscow')
        cities.delete('Moscow')
        self.assertEqual(cities.len(), 0)
        with self.assertRaises(IOError):
            cities.delete('Moscow')
        cities.push('Minsk')
        with self.assertRaises(IOError):
            cities.delete('Moscow')


    def test_contains(self):
        cities = DoubleLinkedList()
        self.assertEqual(cities.contains('Moscow'), 'List is empty')
        cities.push('Moscow')
        self.assertTrue(cities.contains('Moscow'))

    def test_first_and_last(self):
        cities = DoubleLinkedList()
        for city in ['Minsk', 'Moscow', 'London']:
            cities.push(city)
        self.assertEqual(cities.first().get_data(), 'Minsk')
        self.assertEqual(cities.last().get_data(), 'London')