from Classes.Node import Node
from Classes.NoneException import NoneError


class Stack:
    def __init__(self, data=None):
        if data is None:
            self.top = None
        else:
            self.top = Node(data)
            self.top.next = None

    def __repr__(self, *args, **kwargs):
        node = self.top
        data_list = []
        while node is not None:
            data_list.append(node.data)
            node = node.next
        return '%r' % data_list

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
        else:
            next = self.top
            self.top = Node(value)
            self.top.next = next

    def pop(self):
        if self.top is None:
            raise NoneError("The stack has no value")
        data = self.top.data
        self.top = self.top.next
        return data

    def peak(self):
        return self.top.data

    def isEmpty(self):
        return True if self.top is None else False
