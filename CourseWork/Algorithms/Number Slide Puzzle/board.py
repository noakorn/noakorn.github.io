from functools import lru_cache

import math
import random

# Maps k -> hash of solved state.
solved_hashes = {}

# Cached square roots.
cached_sqrt = {}


@lru_cache(maxsize=64)
def is_perfect_square(k):
    root = math.sqrt(k)
    return int(root + 0.5) ** 2 == k


class Board(object):
    """Represents the board state for a k-puzzle."""

    def __init__(self, k, initial_board=None, initial_hole_coordinates=None):
        """Initialize a k-puzzle board. If an `initial_board` is not specificied, the
        board is initialized to the "solved" state for a k-puzzle.

        Args:
            k (int): The integer k value. k + 1 needs to be a perfect square.
            initial_board (2D array): For copy constructor.
            initial_hole (Tuple[int, int]): For copy constructor.
        """

        if k <= 1:
            raise ValueError("`k` has to be > 1.")

        if not is_perfect_square(k + 1):
            raise ValueError("`k + 1` should be a perfect square.")

        self._k = k
        self._rows = cached_sqrt.get(k + 1, int(math.sqrt(k + 1)))
        cached_sqrt[k + 1] = self._rows

        if initial_board:
            if not initial_hole_coordinates:
                raise ValueError("Initial board provided without initial hole.")

            self._board = initial_board
            self._hole_coordinates = initial_hole_coordinates
        else:
            self.reset()

    def get_solved_board(self):
        """Return a board that is in the solved state.

        The returned board will have the same `k`-size has the original board this
        method was called on.
        """

        return Board(self.k)

    def iterate(self):
        """Used to iterate through the board.

        ```
        for (r, c, v) in board.iterate():
            # r is the row, c the col and v the value at the board.
        ```
        """

        for r in range(self.rows):
            for c in range(self.cols):
                yield (r, c, self._board[r][c])

    def reset(self):
        """Reset the board to the solved state."""

        sequence = list(range(1, self.k + 2))
        self._board = []
        for i in range(0, self.k + 1, self.rows):
            self._board.append(sequence[i : i + self.rows])
        self._hole_coordinates = (self.rows - 1, self.cols - 1)

    def validate_bounds(self, r, c):
        """Check if provided row and column are within the bounds of the board."""

        return r >= 0 and c >= 0 and r < self.rows and c < self.cols

    def make_move(self, m):
        """Make a move `m` and return the new board state.

        Args:
            m (Tuple(int, int, int, int)): Contains (r1, c1, r2, c2) where the move will
                swap location (r1, c1) with (r2, c2). Note that (r2, c2) must be the
                hole location.

        Returns:
            A new `Board` that has the move applied.
        """

        r1, c1, r2, c2 = m
        if self._board[r2][c2] != self.hole:
            raise ValueError("Trying to make move into not a hole!")

        if not self.validate_bounds(r1, c1) or not self.validate_bounds(r2, c2):
            raise ValueError("One of the rows and columns was out of bounds.")

        dx = abs(r1 - r2)
        dy = abs(c1 - c2)

        if (dx > 1 or dy > 1) or not ((dx == 1) ^ (dy == 1)):
            raise ValueError(
                "Input row and column is not a direct neighbor of the hole."
            )

        # Swap.
        board = [x[:] for x in self._board]
        board[r1][c1], board[r2][c2] = (
            board[r2][c2],
            board[r1][c1],
        )

        return Board(self.k, initial_board=board, initial_hole_coordinates=(r1, c1))

    def get_legal_moves(self):
        """Returns a list of all legal moves from this board position."""

        hr, hc = self.hole_coordinates
        return [
            (hr + dx, hc + dy, hr, hc)
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]
            if self.validate_bounds(hr + dx, hc + dy)
        ]

    def get_move_from_offset(self, offset):
        """Ignore this method, only used for gui rendering."""
        hr, hc = self.hole_coordinates
        dx, dy = offset

        if not self.validate_bounds(hr + dx, hc + dy):
            return

        return (hr + dx, hc + dy, hr, hc)

    def is_solved(self):
        """Check if board is solved."""
        if self.k not in solved_hashes:
            solved_hashes[self.k] = hash(Board(self.k))
        return hash(self) == solved_hashes[self.k]

    def scramble(self, seed, length=100):
        """Return a board that is scrambled."""

        random.seed(seed)

        current = self
        for _ in range(length):
            m = random.choice(current.get_legal_moves())
            current = current.make_move(m)

        return current

    @property
    def k(self):
        return self._k

    @property
    def hole(self):
        return self.k + 1

    @property
    def hole_coordinates(self):
        return self._hole_coordinates

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._rows

    def __str__(self):
        lines = []
        for r in range(self.rows):
            line = []
            for c in range(self.cols):
                val = self._board[r][c]
                if val == self.hole:
                    val = "_"
                val = str(val)
                line.append(val.ljust(3))
            lines.append(" ".join(line))
        return "\n".join(lines)

    def __hash__(self) -> int:
        h = 0
        for v in self.iterate():
            h ^= hash(v)
        return h

    def __getitem__(self, i):
        return self._board[i]


if __name__ == "__main__":
    B = Board(15)
    B = B.scramble(1337)
