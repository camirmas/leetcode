import unittest

from reverse import my_reverse

class ReverseTests(unittest.TestCase):

    def test_reverse(self):
        inp = 'hello'

        self.assertEqual(my_reverse(inp), 'olleh')

if __name__ == '__main__':
    unittest.main()




