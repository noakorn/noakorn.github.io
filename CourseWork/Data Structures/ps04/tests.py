import unittest
from kresge_grass import KresgeGrass


class Tests(unittest.TestCase):

    def test_01(self):
        A = [10, 9, 8, 7, 6, 5]
        test = KresgeGrass(A)
        for i in range(len(A)):
            self.assertEqual(test.get(i), 10 - i)
        test.increment(0, 5, 10)
        for i in range(len(A)):
            self.assertEqual(test.get(i), 10 + 10 - i)

    def test_02(self):
        A = [5, 6, 7, 8, 9, 10]
        test = KresgeGrass(A)
        for i in range(len(A)):
            self.assertEqual(test.get(i), 5 + i)
        test.increment(1, 4, 10)
        for i in range(1, 4):
            self.assertEqual(test.get(i), 5 + 10 + i)
        self.assertEqual(test.get(0), 5)
        self.assertEqual(test.get(5), 10)

    def test_03(self):
        A = [6, 9, 10, 7, 5, 8]
        test = KresgeGrass(A)
        self.assertEqual(test.get(1), 9)
        self.assertEqual(test.get(2), 10)
        self.assertEqual(test.get(3), 7)
        test.increment(1, 1, 5)
        self.assertEqual(test.get(1), 14)
        self.assertEqual(test.get(2), 10)
        self.assertEqual(test.get(3), 7)
        test.increment(3, 3, 73)
        self.assertEqual(test.get(1), 14)
        self.assertEqual(test.get(2), 10)
        self.assertEqual(test.get(3), 80)
        test.increment(2, 2, -10)
        self.assertEqual(test.get(1), 14)
        self.assertEqual(test.get(2), 0)
        self.assertEqual(test.get(3), 80)

    def test_04(self):
        A = [7, 14, 11]
        test = KresgeGrass(A)
        self.assertEqual(test.get(0), 7)
        self.assertEqual(test.get(1), 14)
        self.assertEqual(test.get(2), 11)
        test.increment(0, 2, 0)
        self.assertEqual(test.get(0), 7)
        self.assertEqual(test.get(1), 14)
        self.assertEqual(test.get(2), 11)
        test.increment(0, 2, 10)
        test.increment(1, 1, -5)
        self.assertEqual(test.get(0), 17)
        self.assertEqual(test.get(1), 19)
        self.assertEqual(test.get(2), 21)

    def test_05(self):
        A = [i + 2 for i in range(26)]
        test = KresgeGrass(A)
        for j in range(13):
            test.increment(j, 25 - j, 1)
        for i in range(13):
            self.assertEqual(test.get(i), 2 * i + 3)
            self.assertEqual(test.get(25 - i), 28)


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)