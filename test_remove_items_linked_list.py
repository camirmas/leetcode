import unittest

from remove_items_linked_list import remove_elements


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class RemoveElementsTests(unittest.TestCase):

    def test_remove_elements(self):
        head = ListNode(1)
        curr = head

        for i in range(2, 7):
            node = ListNode(i)
            curr.next = node
            curr = node

        res = remove_elements(head, 3)
        curr = res

        length = 1

        while curr.next:
            length += 1
            curr = curr.next

        self.assertEqual(length, 5)


if __name__ == '__main__':
    unittest.main()



