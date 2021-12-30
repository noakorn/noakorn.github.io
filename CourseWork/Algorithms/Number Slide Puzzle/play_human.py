"""Optional file to play the slider puzzle yourself.
Run it as,
    python play_human.py --k 15
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

flags.DEFINE_integer(
    "k", 15, "Number of tiles in this game. k + 1 must be a perfect square."
)
flags.DEFINE_integer("seed", 1337, "Seed for scramble.")
FLAGS = flags.FLAGS


def main(argv):
    board = Board(FLAGS.k).scramble(FLAGS.seed, length=1000)
    gui = GUI(board)
    gui.print_instructions()

    while gui.running:
        gui.update(human_input=True)


if __name__ == "__main__":
    app.run(main)
