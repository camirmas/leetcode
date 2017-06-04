import unittest

from largest_values import largest_values

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LargestValuesTests(unittest.TestCase):

    def test_largest_values(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(9)

        self.assertEqual(largest_values(root), [1, 3, 9])


if __name__ == '__main__':
    unittest.main()

