from unittest import TestCase

from Classes.LinkedList import LinkedList


class TestLinkedList(TestCase):
    def setUp(self):
        self.dupList = [3, 5, 2, 3, 3, 2, 10]
        self.removedDups = [1, 3, 5, 2, 10]
        self.linkedList = LinkedList(1)
        self.linkedList.listBuilder(self.dupList)
        array = [1]
        array.extend(self.dupList)
        self.dupList = array

    def test_getList(self):
        array = self.linkedList.getList()
        self.assertListEqual(array, self.dupList)
        self.assertListNotEqual(array, [])

    def assertListNotEqual(self, list1, list2):
        return not self.assertListEqual(list2, list2)

    def test_removeDups(self):
        self.linkedList.removeDups()
        self.assertListEqual(self.linkedList.getList(), self.removedDups)
        self.assertListNotEqual(self.linkedList.getList(), self.dupList)

    def test_removeDupsNoSpace(self):
        self.linkedList.removeDupsNoSpace()
        self.assertListEqual(self.linkedList.getList(), self.removedDups)
        self.assertListNotEqual(self.linkedList.getList(), self.dupList)

    def test_removeFromEnd(self):
        self.linkedList.removeFromEnd(3)
        del self.dupList[-3]
        self.assertListEqual(self.linkedList.getList(), self.dupList)

        self.linkedList.removeFromEnd(1)
        del self.dupList[-1]
        self.assertListEqual(self.linkedList.getList(), self.dupList)

    def test_length(self):
        length = self.linkedList.length()
        self.assertEqual(length, len(self.dupList))

    def test_getNode(self):
        list = self.linkedList.getList()
        node = self.linkedList.getNode(3)
        self.assertEqual(list[3], node.data)

    def test_removeNode(self):
        node = self.linkedList.getNode(3)
        LinkedList.removeNode(node)
        del self.dupList[3]
        self.assertListEqual(self.linkedList.getList(), self.dupList)

    def test_sum(self):
        one = LinkedList(1)
        four = LinkedList(4)
        five = one.sum(four)
        self.assertListEqual(five.getList(), [5])

        num318 = LinkedList(8)
        num318.listBuilder([1, 3])

        num1094 = LinkedList(4)
        num1094.listBuilder([9, 0, 1])

        sum = num1094.sum(num318)
        self.assertListEqual(sum.getList(), [2, 1, 4, 1])
