import unittest

from shuffle import shuffle

class ShuffleTests(unittest.TestCase):

    def test_shuffle(self):
        inp = [i for i in range(0, 1000)]

        self.assertNotEqual(inp.copy(), shuffle(inp))

if __name__ == '__main__':
    unittest.main()



