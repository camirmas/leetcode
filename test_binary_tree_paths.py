import unittest

from binary_tree_paths import binary_tree_paths

class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class BinaryTreePathsTests(unittest.TestCase):

    def test_binary_tree_paths(self):
        node = TreeNode(1)
        node.left = TreeNode(2)
        node.right = TreeNode(3)
        node.left.left = TreeNode(5)

        res = binary_tree_paths(node)

        self.assertIn([1, 2, 5], res)
        self.assertIn([1, 3], res)
        self.assertEqual(len(res), 2)

if __name__ == '__main__':
    unittest.main()
