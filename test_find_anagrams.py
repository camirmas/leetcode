import unittest

from find_anagrams import find_anagrams

class AnagramTests(unittest.TestCase):

    def test_find_anagrams(self):
        s = 'cbaebabacd'
        p = 'abc'

        self.assertEqual(find_anagrams(s, p), [0, 6])

    def test_find_anagrams_2(self):
        s = 'abab'
        p = 'ab'

        self.assertEqual(find_anagrams(s, p), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
