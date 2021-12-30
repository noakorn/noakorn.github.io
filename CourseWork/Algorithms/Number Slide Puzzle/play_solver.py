"""Optional file to watch your solver play the slider puzzle.
Run it as,
    python play_solver.py --test 0
"""

try:
    from gui import GUI
    from absl import flags
    from absl import app
except:
    print("You don't have some libraries installed.")
    print("Try running `pip install absl-py pygame`")
    print("or `pip3 install absl-py pygame` depending on your python.")
    print("")
    print("Remember, running this file is just for fun.")
    exit()

from board import Board

try:
    from tests import cases
except:
    from staff_tests import cases

try:
    from solver import solve
except:
    from staff_solution import solve


flags.DEFINE_integer("test", 0, "Test index to play.")
flags.DEFINE_integer("seed", 1337, "Seed for scramble.")
FLAGS = flags.FLAGS


def main(argv):
    k, seed, length = cases[FLAGS.test]
    board = Board(k).scramble(seed, length)

    print("Running your solver ...")
    moves = solve(board)

    if moves is None:
        print("Your solver generated no moves.")
        exit()

    print(
        """
        Solver found a solution.
        Your solver is playing!
        """
    )

    gui = GUI(board)

    for m in moves:
        print("Playing move, {}".format(m))
        gui.update(human_input=False)
        gui.board = gui.board.make_move(m)
        gui.clock.tick(3)

    print("Done! Press Q to quit.")

    while gui.running:
        gui.update(human_input=False)


if __name__ == "__main__":
    app.run(main)
