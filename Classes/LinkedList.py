from Classes.Node import Node


class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
        else:
            self.head = Node(value)

    def __repr__(self):
        node = self.head
        node_data = []
        while node is not None:
            node_data.append(node.data)
            node = node.next
        return "%r" % node_data

    def insertAtEnd(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next

            node.next = Node(value)

    def listBuilder(self, list):
        for i in list:
            self.insertAtEnd(i)

    def getList(self):
        node = self.head
        values = []
        while node is not None:
            values.append(node.data)
            node = node.next
        return values

    def getNode(self, index):
        count = 0
        node = self.head
        while count < index and node.next is not None:
            node = node.next
            count += 1
        return node

    def length(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def removeDups(self):
        node = self.head
        found = {}
        while node.next is not None:
            value = node.next.data
            if value in found:
                node.next = node.next.next
            else:
                node = node.next
                found[value] = True

    def removeDupsNoSpace(self):
        current = self.head

        while current is not None:
            runner = current
            while runner.next is not None:
                if current.data == runner.next.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def removeFromEnd(self, index=1):
        node = self.head
        runner = self.head
        count = 0
        while count < index and runner.next is not None:
            count += 1
            runner = runner.next

        while runner.next is not None:
            runner = runner.next
            node = node.next

        node.next = node.next.next

    @staticmethod
    def removeNode(node):
        if node is None or node.next is None:
            return 0
        node.data = node.next.data
        node.next = node.next.next

    def sum(self, number):
        if self.head is None or number.head is None:
            return

        node = self.head
        number = number.head
        head = LinkedList()
        carry = 0
        while node is not None or number is not None:
            value = carry
            if node is not None:
                value += node.data
                node = node.next

            if number is not None:
                value += number.data
                number = number.next

            carry = value // 10
            value %= 10

            head.insertAtEnd(value)

        return head
