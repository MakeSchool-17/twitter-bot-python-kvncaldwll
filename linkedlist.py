
class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        # empty LinkedList
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, data):
        # create a new node with the data
        new_node = Node(data)
        new_node.next = self.head
        # reassign head reference
        self.head = new_node
        self.size += 1
        # assign tail reference if list is empty
        if self.tail is None:
            self.tail = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            # assign head reference
            self.head = new_node
        else:
            # append new node after tail
            self.tail.next = new_node
        # reassign tail reference
        self.tail = new_node
        self.size += 1

    def remove_head(self):
        if self.head is None:
            raise ValueError('List is empty')
        self.head = self.head.next
        self.size -= 1

    # running time: O(n)
    def calculate_size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

