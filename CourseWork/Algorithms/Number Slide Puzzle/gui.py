"""GUI to draw k-puzzle on the screen.
Being able to run this file is purely optional.
"""

from board import Board
import pygame

pygame.font.init()


class GUI(object):
    def __init__(self, board, fps=60, cell_size=100):
        self.board = board

        self.running = True
        self.fps = fps
        self.cell_size = cell_size
        self.current_index = 0

        pygame.display.set_caption("6.006 k-Slider Puzzle")
        self.screen = pygame.display.set_mode(
            (self.board.cols * cell_size, self.board.rows * cell_size)
        )
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Arial", cell_size // 2)

    def print_instructions(self):
        print(
            """
            GUI Intructions:
                Arrow Keys: Move puzzle piece.
                Q:          Quit.
            """
        )

    def draw_board(self):
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            pygame.Rect(
                0,
                0,
                self.board.cols * self.cell_size,
                self.board.rows * self.cell_size,
            ),
            width=1,
        )

    def draw_matrix(self, matrix, offset):
        off_x, off_y = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                val = "_" if val == self.board.hole else str(val)
                pygame.draw.rect(
                    self.screen,
                    (255, 255, 255),
                    pygame.Rect(
                        (off_x + x) * self.cell_size,
                        (off_y + y) * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                    1,
                )

                w, h = self.font.size(val)
                text_surface = self.font.render(val, True, (255, 255, 255), (0, 0, 0))
                self.screen.blit(
                    text_surface,
                    (
                        (off_x + x) * self.cell_size + self.cell_size // 2 - w // 2,
                        (off_y + y) * self.cell_size + self.cell_size // 2 - h // 2,
                    ),
                )

    def update(self, human_input=True):
        self.screen.fill((0, 0, 0))

        self.draw_matrix(self.board._board, (0, 0))
        self.draw_board()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.running = False

            if event.type == pygame.KEYDOWN and human_input:
                offsets = {
                    pygame.K_LEFT: (0, 1),
                    pygame.K_RIGHT: (0, -1),
                    pygame.K_UP: (1, 0),
                    pygame.K_DOWN: (-1, 0),
                }
                if event.key in offsets:
                    offset = offsets[event.key]
                    move = self.board.get_move_from_offset(offset)
                    if move:
                        self.board = self.board.make_move(move)

        self.clock.tick(self.fps)
