import unittest

from min_depth import min_depth


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReverseWordsTests(unittest.TestCase):

    def test_min_depth(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)

        self.assertEqual(min_depth(root), 2)

    def test_min_depth_none(self):
        root = None

        self.assertEqual(min_depth(root), 0)


if __name__ == '__main__':
    unittest.main()
