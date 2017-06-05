import unittest

from reverse_words import reverse_words


class ReverseWordsTests(unittest.TestCase):

    def test_reverse_words(self):
        inp = "Let's take LeetCode contest"
        out = "s'teL ekat edoCteeL tsetnoc"

        self.assertEqual(reverse_words(inp), out)


if __name__ == '__main__':
    unittest.main()
