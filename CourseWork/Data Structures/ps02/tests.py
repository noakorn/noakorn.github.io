import unittest
from happy_accidents import count_happy_accidents


class TestCorrectness(unittest.TestCase):

    def test_00(self):
        inp = [200, 400, 250, 150]
        ans = count_happy_accidents(inp)
        expected = 4
        self.assertEqual(ans, expected)

    def test_01(self):
        inp = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
        ans = count_happy_accidents(inp)
        expected = 0
        self.assertEqual(ans, expected)

    def test_02(self):
        inp = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50]
        ans = count_happy_accidents(inp)
        expected = 45
        self.assertEqual(ans, expected)

class TestEfficiency(unittest.TestCase):
    # these test cases are large in order to test for the amortized runtimes.
    # they shouldn't take more than a few seconds on a reasonable machine.

    def test_03(self):
        inp = [i for i in range(10000)]
        ans = count_happy_accidents(inp)
        expected = 0
        self.assertEqual(ans, expected)

    def test_04(self):
        inp = [i for i in range(10000, 0, -1)]
        ans = count_happy_accidents(inp)
        expected = 49995000
        self.assertEqual(ans, expected)

    def test_05(self):
        inp = [i for i in range(50001)] + [i for i in range(100000, 50000, -1)]
        ans = count_happy_accidents(inp)
        expected = 1249975000
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)