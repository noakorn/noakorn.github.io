import unittest
from tree_rescue import tree_rescue

cases = [
    ([1, 0, 3, 2, 4], [0, 1, 1, 2, 2], [0, 1, 2, 3, 4]),
    ([0, 1, 4, 3, 2], [0, 1, 2, 3, 4], [2, 3, 4, 1, 0]),
    ([5, 4, 0, 1, 3, 2, 6], [0, 1, 2, 3, 4, 5, 1], [2, 3, 1, 0, 4, 5, 6]),
    ([4, 1, 0, 2, 3, 5, 6], [0, 1, 2, 2, 3, 1, 2], [0, 1, 3, 2, 4, 6, 5]),
    (
        [14, 10, 8, 6, 4, 2, 1, 0, 3, 5, 7, 9, 13, 11, 12, 15, 16, 18, 17, 19],
        [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 3, 4, 1, 2, 3, 4, 4],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13, 14, 17, 18, 19, 16, 15],
    ),
]


class Tests(unittest.TestCase):
    def test_01(self):
        A, L, expected = cases[0]
        ans = tree_rescue(A, L)
        self.assertEqual(ans, expected)

    def test_02(self):
        A, L, expected = cases[1]
        ans = tree_rescue(A, L)
        self.assertEqual(ans, expected)

    def test_03(self):
        A, L, expected = cases[2]
        ans = tree_rescue(A, L)
        self.assertEqual(ans, expected)

    def test_04(self):
        A, L, expected = cases[3]
        ans = tree_rescue(A, L)
        self.assertEqual(ans, expected)

    def test_05(self):
        A, L, expected = cases[4]
        ans = tree_rescue(A, L)
        self.assertEqual(ans, expected)


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)