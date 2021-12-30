import unittest
from back_front import BackFront


class TestCorrectness(unittest.TestCase):

    def test_00(self):
        example = BackFront()
        example.append(4)
        example.prepend(5)
        example.append(7)
        answer = example.as_list()
        expected = [5, 4, 7]
        self.assertEqual(answer, expected)

    def test_01(self):
        # test case from alg.mit.edu
        example = BackFront()
        example.append(4)
        example.prepend(5)
        answer = example.as_list()
        expected = [5, 4]
        self.assertEqual(answer, expected)

        example.delete_first()
        self.assertEqual(example.as_list(), [4])

        example.delete_first()
        self.assertEqual(example.as_list(), [])

    def test_02(self):
        example = BackFront()
        example.prepend(3)
        example.prepend(2)
        example.delete_last()
        self.assertEqual(example.as_list(), [2])

    def test_04(self):
        example = BackFront()
        for i in range(8):
            example.append(i)
        self.assertEqual(example.as_list(), list(range(8)))

        for i in range(8):
            self.assertEqual(example.as_list(), list(range(i, 8)))
            example.delete_first()

        self.assertEqual(example.as_list(), [])

    def test_05(self):
        example = BackFront()
        for i in range(8):
            example.append(i)

        example.delete_first()
        for i in range(7):
            self.assertEqual(example[i], i+1)
            example[i] = 6

        self.assertEqual(example.as_list(), [6]*7)

    def test_06(self):
        example = BackFront()
        for i in range(8):
            example.prepend(i)

        example.delete_last()
        for i in range(7):
            self.assertEqual(example[i], 7-i)
            example[i] = 6

        self.assertEqual(example.as_list(), [6]*7)


class TestEfficiency(unittest.TestCase):
    # these test cases are large in order to test for the amortized runtimes.
    # they shouldn't take more than a few seconds on a reasonable machine.
    def helper(self, example):
        n = 300000

    def test_07(self):
        n = 300000
        example = BackFront()
        for i in range(n):
            example.append(i)
        self.assertEqual(example.as_list(), list(range(n)))

        for _ in range(n//2):
            example.delete_first()
        self.assertEqual(example.as_list(), list(range(n//2, n)))

        for _ in range(n//2):
            example.delete_last()
        self.assertEqual(example.as_list(), [])

    def test_08(self):
        n = 300000
        example = BackFront()
        for i in range(n):
            example.prepend(i)
        self.assertEqual(example.as_list(), list(reversed(range(n))))

        for _ in range(n//2):
            example.delete_first()
        self.assertEqual(example.as_list(), list(reversed(range(n//2))))

        for _ in range(n//2):
            example.delete_last()
        self.assertEqual(example.as_list(), [])

    def test_09(self):
        # similar to 7, but also tests for indexing in O(1) time
        n = 300000
        example = BackFront()
        for i in range(n):
            example.append(i)
        self.assertEqual(example.as_list(), list(range(n)))

        for i in range(n//2):
            self.assertEqual(example[0], i)
            example.delete_first()
        self.assertEqual(example.as_list(), list(range(n//2, n)))

        first = example[0]
        for _ in range(n//2):
            self.assertEqual(example[0], first)
            example.delete_last()
        self.assertEqual(example.as_list(), [])

    def test_10(self):
        # similar to 8 but also tests for indexing in O(1) time
        n = 300000
        example = BackFront()
        for i in range(n):
            example.prepend(i)
        self.assertEqual(example.as_list(), list(reversed(range(n))))

        for i in range(n//2):
            self.assertEqual(example[2], n-3-i)
            example.delete_first()
        self.assertEqual(example.as_list(), list(reversed(range(n//2))))

        for _ in range(n//2):
            example.delete_last()
        self.assertEqual(example.as_list(), [])


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)