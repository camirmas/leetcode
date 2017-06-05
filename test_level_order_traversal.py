import unittest

from level_order_traversal import level_order_traversal


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TraversalTests(unittest.TestCase):

    def test_level_order_traversal(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        out = [[3], [9, 20], [15, 7]]

        self.assertEqual(level_order_traversal(root), out)


if __name__ == '__main__':
    unittest.main()
