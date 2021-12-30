from board import Board

from solver import homomorphic_hash, solve


import unittest

homomorphic_cases = [(8, 1337, 100), (15, 1212, 30)]
cases = [
    (3, 0, 100),
    (8, 6, 200),
    (15, 10, 30),
]


def check_homomorphic(case):
    k, seed, length = case

    board = Board(k).scramble(seed, length)

    move = board.get_legal_moves()[0]
    hash_before = hash(board)
    hash_after = hash(board.make_move(move))

    return hash_after, homomorphic_hash(board, hash_before, move)


def check_solver(case):
    k, seed, length = case
    board = Board(k).scramble(seed, length)
    moves = solve(board)
    for m in moves:
        board = board.make_move(m)
    return board


class Tests(unittest.TestCase):
    def test_01(self):
        after, rv = check_homomorphic(homomorphic_cases[0])
        self.assertEqual(after, rv)

    def test_02(self):
        after, rv = check_homomorphic(homomorphic_cases[1])
        self.assertEqual(after, rv)

    def test_03(self):
        self.assertTrue(check_solver(cases[0]).is_solved())

    def test_04(self):
        self.assertTrue(check_solver(cases[1]).is_solved())

    def test_05(self):
        self.assertTrue(check_solver(cases[2]).is_solved())


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)
