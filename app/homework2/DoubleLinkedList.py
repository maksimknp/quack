from app.homework2.Item import Item


class DoubleLinkedList(object):

    def __init__(self, root=None):
        self.root = root
        if self.root is not None:
            self.size = 1
        else:
            self.size = 0

    def unshift(self, data):
        new_item = Item(data, None, self.root)
        if self.root is not None:
            self.root.set_previous_item(new_item)
        self.root = new_item
        self.size += 1

    def last(self):
        last_item = self.root
        if last_item is not None:
            while last_item.get_next_item() is not None:
                last_item = last_item.get_next_item()
            return last_item
        else:
            return None

    def first(self):
        return self.root

    def push(self, data):
        last_item = self.last()
        new_item = Item(data, last_item, None)
        if last_item is not None:
            last_item.set_next_item(new_item)
        else:
            self.root = new_item
        self.size += 1

    def len(self):
        return self.size

    def pop(self):
        current_last_item = self.last()
        if self.size == 1:
            self.root = None
            self.size = 0
        elif self.size > 1:
            last_item = self.last()
            last_item.get_previous_item().set_next_item(None)
            self.size -= 1
        return current_last_item

    def shift(self):
        current_root = self.root
        if self.size == 1:
            current_root = self.root
            self.root = None
            self.size = 0
        elif self.size > 1:
            current_root = self.root
            self.root = self.root.get_next_item()
            self.root.set_previous_item(None)
            self.size -= 1
        return current_root

    def contains(self, data):
        if self.size == 0:
            return "List is empty"
        current_item = self.root
        while current_item is not None:
            if current_item.get_data() == data:
                return True
            else:
                current_item = current_item.get_next_item()
        return False

    def delete(self, data):
        if self.size == 0:
            raise IOError("List is empty")
        current_item = self.root
        while current_item is not None:
            if current_item.get_data() == data:
                previous_item = current_item.get_previous_item()
                next_item = current_item.get_next_item()
                self.size -= 1

                if previous_item is not None:
                    previous_item.set_next_item(next_item)
                else:
                    self.root = current_item.get_next_item()

                if next_item is not None:
                    next_item.set_previous_item(previous_item)
                    current_item = next_item
                else:
                    return True

            else:
                current_item = current_item.get_next_item()
        raise IOError("Item not found")
