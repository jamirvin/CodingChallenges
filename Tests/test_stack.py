from unittest import TestCase

from Classes.Stack import Stack


class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
            self.assertEqual(stack.top.data, i)

    def test_pop(self):
        stack = Stack(1)
        for i in range(10):
            stack.push(i)

        for i in range(9, 0, -1):
            top = stack.pop()
            self.assertEqual(top, i)

    def test_peak(self):
        stack = Stack(1)
        self.assertEqual(stack.peak(), 1)

    def test_isEmpty(self):
        new_stack = Stack()
        self.assertTrue(new_stack.isEmpty())

        new_stack.push(3)
        self.assertFalse(new_stack.isEmpty())
