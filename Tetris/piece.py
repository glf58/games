import random
import pygame

import colorsys


def generate_random_color():

    h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
    r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
    return (r, g, b)


# colors = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan', 'purple', 'navy', 'lime']
shapes = {
    "I": [
        [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
    ],
    "S": [
        [[0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]],
    ],
    "Z": [
        [[0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
    ],
    "O": [[[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]],
    "L": [
        [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 1, 1], [0, 0, 0, 0]],
    ],
    "T": [
        [[1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]],
        [[0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
    ],
}
n_picture = 4


class Piece:
    def __init__(self, i, j, c) -> None:
        self.i = i
        self.j = j
        self.c = c
        self.shape = random.choice(list(shapes.keys()))
        # self.color = random.choice(colors)
        self.color = generate_random_color()
        self.rotation = 0

    def draw_piece(self, surface, corner):
        for i in range(n_picture):
            for j in range(n_picture):
                if shapes[self.shape][self.rotation][i][j] == 1:
                    pygame.draw.rect(
                        surface=surface,
                        color="grey",
                        rect=(
                            (self.j + j) * self.c + corner[0],
                            (self.i + i) * self.c + corner[1],
                            self.c,
                            self.c,
                        ),
                        width=1,
                    )
                    pygame.draw.rect(
                        surface=surface,
                        color=self.color,
                        rect=(
                            (self.j + j) * self.c + corner[0] + 1,
                            (self.i + i) * self.c + corner[1] + 1,
                            self.c - 1,
                            self.c - 1,
                        ),
                    )

    # def hit_boundary(self, nCols, nRows):
    #     for i in range(n_picture):
    #         for j in range(n_picture):
    #             if shapes[self.shape][self.rotation][i][j] == 1:
    #                 # if ((self.j+j)*self.c<left) or ((self.j + (j+1))*self.c>right) or ((self.i+(i+1))*self.c>bottom):
    #                 if ((self.j+j)<0) or ((self.j + (j+1))>nCols) or ((self.i+(i+1))>nRows):
    #                     # print(self.x, self.y, i, j, left, right, bottom)
    #                     return True
    #     return False

    def is_valid_move(self, grid):
        for i in range(n_picture):
            for j in range(n_picture):
                if shapes[self.shape][self.rotation][i][j] == 1:
                    if (
                        (i + self.i >= len(grid))
                        or (j + self.j < 0)
                        or (j + self.j >= len(grid[0]))
                        or (grid[i + self.i][j + self.j] != "black")
                    ):
                        return False
        return True

    def add_to_grid(self, grid):
        for i in range(n_picture):
            for j in range(n_picture):
                if shapes[self.shape][self.rotation][i][j] == 1:
                    grid[i + self.i][j + self.j] = self.color
