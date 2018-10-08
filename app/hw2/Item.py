class Item(object):

    def __init__(self, data, previous_item=None, next_item=None):
        self.data = data
        self.previous_item = previous_item
        self.next_item = next_item

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_previous_item(self):
        return self.previous_item

    def set_previous_item(self, previous_item):
        self.previous_item = previous_item

    def get_next_item(self):
        return self.next_item

    def set_next_item(self, next_item):
        self.next_item = next_item
