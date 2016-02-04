
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList(object):

    def __init__(self):
        # empty linked list
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        # notify if node at head and or tail position
        head_str = 'head: ' + str(self.head) if self.head else ''
        tail_str = 'tail: ' + str(self.tail) if self.head else ''
        return 'LinkedList({}{})'.format(head_str, tail_str)

    def is_empty(self):
        return self.size == 0

    def is_valid(self):
        # check if node is in LinkedList
        head_true = self.head is not None
        tail_true = self.tail is not None
        size_true = self.size > 0
        if head_true and tail_true and size_true:
            return True
        elif not head_true and not tail_true and not size_true:
            return True
        else:
            return False

    def insert_head(self, data):
        # create a node
        new_node = Node(data)
        # new node points to previous head node
        new_node.next = self.head
        if self.head is True:
            self.head.prev = new_node
        # change head to new node
        self.head = new_node
        # update LinkedList size
        self.size += 1
        # if no tail pointer, means only one node which is both head and tail
        if self.tail is None:
            self.tail = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        # if LinkedList is empty set new node as head
        if self.is_empty():
            self.head = new_node
        else:
            # append new node to existing tail
            self.tail.next = new_node
            # new tail node points to node that comes before it
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError('linked list is empty!')
        self.head = self.head.next
        self.size -= 1

    def remove_tail(self):
        if self.is_empty():
            raise ValueError('linked list is empty!')
        else:
            self.tail = self.tail.prev
            self.size -= 1

    def calculate_size(self):
        return str(self.size)

ll = LinkedList()
node1 = ll.insert_head({'apple': 1})
node2 = ll.insert_tail(('boy', 4))
print(ll.head.data)
print('next node data: ', ll.head.next.data)
print('prev node data: ', ll.head.prev)
print(ll.tail.data)
print('previous node data: ', ll.tail.prev.data)
print('next node data: ', ll.tail.next)
