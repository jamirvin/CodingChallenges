class Node:
    def __init__(self, value):
        self.next = None
        self.data = value

    def __repr__(self):
        nextData = self.next.data if self.next is not None else "None"
        return "next node: %r, data: %r" % (nextData, self.data)
