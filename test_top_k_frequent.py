import unittest

from top_k_frequent import top_k_frequent

class TopKTests(unittest.TestCase):

    def test_top_k_frequent(self):
        inp = [1, 1, 1, 2, 2, 3]
        k = 2

        self.assertEqual(top_k_frequent(inp, k), [1, 2])

    def test_top_k_frequent_2(self):
        inp = [4,1,-1,2,-1,2,3]
        k = 2

        self.assertEqual(top_k_frequent(inp, k), [-1, 2])

    def test_top_k_frequent_3(self):
        inp = [2,3,4,1,4,0,4,-1,-2,-1]
        k = 2

        self.assertEqual(top_k_frequent(inp, k), [4, -1])

if __name__ == '__main__':
    unittest.main()


