from collections import deque

def homomorphic_hash(board, prev_hash, move):
    """Update the hash of a board after applying a move in O(1) time.

    Args:
        board: An instance of the `Board` class. Please see the helper `board.py` file.
        prev_hash (int): Hash of the previous board.
        move (Tuple[int, int, int, int]): Contains (r1, c1, r2, c2) where the move will
                swap location (r1, c1) with (r2, c2). Note that (r2, c2) must be the
                hole location.
    
    Returns (int):
        Returns the hash of the board after move has been applied.
    """
    return hash(board.make_move(move))

def one_level_bfs(my_hash,other_hash,my_q):
    next_q = []
    for board, current_hash in my_q:
        for move in board.get_legal_moves():
            next_hash = homomorphic_hash(board, current_hash, move)
            if next_hash in other_hash:
                my_hash[next_hash] = (current_hash, move)
                return my_hash, next_q,next_hash
            elif next_hash not in my_hash:
                my_hash[next_hash] = (current_hash, move)
                next_q += [(board.make_move(move), next_hash)]
    return my_hash,next_q,None


def double_BFS(B):
    """
    B is the initial board state
    """
    goal = B.get_solved_board()
    forward_hash,backward_hash = {hash(B):(None,None)}, {hash(goal):(None,None)}
    forward_q,backward_q = [(B,hash(B))], [(goal,hash(goal))]
    mid_hash = None

    while mid_hash is None:
        forward_hash,forward_q,mid_hash = one_level_bfs(forward_hash,backward_hash,forward_q)
        backward_hash,backward_q,mid_hash = one_level_bfs(backward_hash,forward_hash,backward_q)
    return forward_hash, backward_hash, mid_hash


def solve(B):
    """Find the moves that would solve the board given by `B`.

    Args:
        B: An instance of the `Board` class. Please see the `board.py` file. This is the
            starting state of the board that you need to solve.

    Returns:
        A list of moves, in the form of (r1, c1, r2, c2) that would solve `B`.
    """

    forward_hash, backward_hash, mid_hash = double_BFS(B)
    if mid_hash is None:
        return

    first_half = []
    # reversed_move = backward_hash[mid_hash][1]
    # forward_move = reversed_move[2:] + reversed_move[:2]
    second_half = []
    current_hash = mid_hash
    while True:
        current_hash,move = forward_hash[current_hash]
        if move is None:
            break
        first_half = [move] + first_half

    current_hash = mid_hash
    while True:
        current_hash,reversed_move = backward_hash[current_hash]
        if reversed_move is None:
            break
        forward_move = reversed_move[2:] + reversed_move[:2]
        second_half += [forward_move]
    return first_half + second_half

# board = board.Board(3).scramble(0,100)
# print(board)
# moves = solve(board)
# for m in moves:
#     board = board.make_move(m)
#     print(board)

