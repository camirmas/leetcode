import unittest

from max_prod_word_lengths import max_product_word_lengths


class MaxProdTests(unittest.TestCase):

    def test_max_prod_word_lengths(self):
        words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]

        self.assertEqual(max_product_word_lengths(words), 16)

    def test_max_prod_word_lengths_2(self):
        words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]

        self.assertEqual(max_product_word_lengths(words), 4)

    def test_max_prod_word_lengths_3(self):
        words = ["a", "aa", "aaa", "aaaa"]

        self.assertEqual(max_product_word_lengths(words), 0)


if __name__ == '__main__':
    unittest.main()
