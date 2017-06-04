import unittest

from decode_string import decode_string

class DecodeTests(unittest.TestCase):

    def test_decode_string(self):
        inp = '3[a]2[bc]'
        out = 'aaabcbc'

        self.assertEqual(decode_string(inp), out)

    def test_decode_string_2(self):
        inp = '3[a2[c]]'
        out = 'accaccacc'

        self.assertEqual(decode_string(inp), out)

    def test_decode_string_3(self):
        inp = '2[abc]3[cd]ef'
        out = 'abcabccdcdcdef'

        self.assertEqual(decode_string(inp), out)

    def test_decode_string_4(self):
        inp = "sd2[f2[e]g]i"
        out = "sdfeegfeegi"

        self.assertEqual(decode_string(inp), out)

    def test_decode_string_5(self):
        inp = "2[ab3[cd]]4[xy]"
        out = "abcdcdcdabcdcdcdxyxyxyxy"

        self.assertEqual(decode_string(inp), out)


if __name__ == '__main__':
    unittest.main()


