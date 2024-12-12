import pygame
import constant as K

from piece import Piece, shapes


class Tetris:
    def __init__(self, surface, c, top_left, nRows, nCols):
        self.nRows = nRows
        self.nCols = nCols
        self.surface = surface
        self.c = c
        self.top_left = K.TOP_LEFT
        self.grid = [["black" for j in range(nCols)] for i in range(nRows)]
        self.score = 0
        self.current_piece = Piece(0, self.nCols // 2, self.c)
        self.next_piece = Piece(0, self.nCols // 2, self.c)
        self.last_fall = 0

    def draw_border(self, corner):
        pygame.draw.rect(
            self.surface, "red", (corner, (self.c * self.nCols, self.c * self.nRows)), 4
        )

    def draw_grid(self, corner):
        for i in range(self.nRows):
            for j in range(self.nCols):
                pygame.draw.rect(
                    surface=self.surface,
                    rect=(
                        j * self.c + corner[0],
                        i * self.c + corner[1],
                        self.c,
                        self.c,
                    ),
                    width=1,
                    color="grey",
                )
                if self.grid[i][j] != "black":
                    pygame.draw.rect(
                        surface=self.surface,
                        rect=(
                            j * self.c + corner[0] + 1,
                            i * self.c + corner[1] + 1,
                            self.c - 2,
                            self.c - 2,
                        ),
                        color=self.grid[i][j],
                    )

    def go_to_next_piece(self):
        self.current_piece.add_to_grid(self.grid)
        self.current_piece = self.next_piece
        self.next_piece = Piece(0, self.nCols // 2, self.c)
        self.last_fall = pygame.time.get_ticks()

    def handle_continuous_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.current_piece.j -= 1
                if not self.current_piece.is_valid_move(self.grid):
                    self.current_piece.j += 1
            if event.key == pygame.K_RIGHT:
                self.current_piece.j += 1
                if not self.current_piece.is_valid_move(self.grid):
                    self.current_piece.j -= 1
            if event.key == pygame.K_DOWN:
                while self.current_piece.is_valid_move(self.grid):
                    self.score += 5
                    self.current_piece.i += 1
                self.current_piece.i -= 1
            if event.key == pygame.K_q:
                self.current_piece.rotation += 1
                self.current_piece.rotation = self.current_piece.rotation % len(
                    shapes[self.current_piece.shape]
                )
                if not self.current_piece.is_valid_move(self.grid):
                    self.current_piece.rotation -= 1
                    self.current_piece.rotation = self.current_piece.rotation % len(
                        shapes[self.current_piece.shape]
                    )
            if event.key == pygame.K_s:
                self.current_piece.rotation -= 1
                self.current_piece.rotation = self.current_piece.rotation % len(
                    shapes[self.current_piece.shape]
                )
                if not self.current_piece.is_valid_move(self.grid):
                    self.current_piece.rotation += 1
                    self.current_piece.rotation = self.current_piece.rotation % len(
                        shapes[self.current_piece.shape]
                    )

    def remove_stack_and_return_score(self):
        rowsToKeep = []
        for i in range(self.nRows):
            if any(["black" in self.grid[self.nRows - 1 - i]]):
                rowsToKeep.append(self.nRows - 1 - i)

        for i in range(self.nRows):
            if i >= len(rowsToKeep):
                for j in range(self.nCols):
                    self.grid[self.nRows - 1 - i][j] = "black"
            else:
                for j in range(self.nCols):
                    self.grid[self.nRows - 1 - i][j] = self.grid[rowsToKeep[i]][j]
        if self.nRows - len(rowsToKeep) == 4:
            self.score += 1000
        else:
            self.score += (self.nRows - len(rowsToKeep)) * 100

    def get_fall_speed(self, time):
        return 1000
        # if time <= 5000:
        #     return 1000
        # elif time <= 10000:
        #     return 500
        # else:
        #     return 250


def main():

    pygame.init()
    screen = pygame.display.set_mode((K.SCREEN_WIDTH, K.SCREEN_HEIGHT))
    tetris = Tetris(screen, c=K.C, top_left=K.TOP_LEFT, nCols=K.NCOLS, nRows=K.NROWS)
    font = pygame.font.SysFont("comicsans", 30)

    clock = pygame.time.Clock()
    running = True
    elapsed_time = 0

    while running:

        screen.fill("black")

        tetris.draw_grid(corner=K.TOP_LEFT)
        tetris.draw_border(corner=K.TOP_LEFT)
        tetris.next_piece.draw_piece(screen, corner=K.NEXT_PIECE_CORNER)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            tetris.handle_continuous_move(event=event)

        tetris.current_piece.draw_piece(screen, corner=K.TOP_LEFT)
        elapsed_time = pygame.time.get_ticks()

        if elapsed_time - tetris.last_fall >= tetris.get_fall_speed(elapsed_time):
            tetris.current_piece.i += 1
            tetris.last_fall = pygame.time.get_ticks()
            if not tetris.current_piece.is_valid_move(tetris.grid):
                tetris.current_piece.i -= 1
                tetris.go_to_next_piece()

        tetris.remove_stack_and_return_score()
        label = font.render("Score: " + str(tetris.score), 1, (255, 255, 255))
        screen.blit(label, (K.SCORE_CORNER[0] + 20, K.SCORE_CORNER[1] + 160))

        if not tetris.current_piece.is_valid_move(tetris.grid):
            running = False
            print("GAME OVER")

        pygame.display.flip()

        dt = clock.tick(100) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
