import unittest

from intersection import intersection


class IntersectionTests(unittest.TestCase):

    def test_intersection(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]

        self.assertEqual(intersection(nums1, nums2), [2, 2])


if __name__ == '__main__':
    unittest.main()
