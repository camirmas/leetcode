import unittest

from valid_anagram import valid_anagram

class AnagramTests(unittest.TestCase):

    def test_valid_anagram(self):
        s1 = "cat"
        s2 = "act"

        self.assertTrue(valid_anagram(s1, s2))

    def test_not_valid_anagram(self):
        s1 = "cat"
        s2 = "acto"

        self.assertFalse(valid_anagram(s1, s2))

    def test_not_valid_anagram_2(self):
        s1 = "ab"
        s2 = "a"

        self.assertFalse(valid_anagram(s1, s2))


if __name__ == '__main__':
    unittest.main()

