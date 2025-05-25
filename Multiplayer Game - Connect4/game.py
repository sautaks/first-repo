import pygame

ROWS = 6
COLS = 7
SQUARESIZE = 100
RADIUS = SQUARESIZE // 2 - 5

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

class Connect4Game:
    def __init__(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.turn = 1  # Player 1 starts

    def drop_piece(self, col):
        row = self.get_next_open_row(col)
        if row is not None:
            self.board[row][col] = self.turn
            self.turn = 2 if self.turn == 1 else 1
            return True
        return False

    def get_next_open_row(self, col):
        for r in range(ROWS - 1, -1, -1):
            if self.board[r][col] == 0:
                return r
        return None

    def is_valid_location(self, col):
        return self.board[0][col] == 0

    def check_winner(self, piece):
        # Horizontal check
        for r in range(ROWS):
            for c in range(COLS - 3):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return True

        # Vertical check
        for c in range(COLS):
            for r in range(ROWS - 3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return True

        # Positive diagonal
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return True

        # Negative diagonal
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return True

        return False

    def draw_board(self, screen):
        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                color = BLACK
                if self.board[r][c] == 1:
                    color = RED
                elif self.board[r][c] == 2:
                    color = YELLOW
                pygame.draw.circle(screen, color, (c * SQUARESIZE + SQUARESIZE // 2, r * SQUARESIZE + SQUARESIZE + SQUARESIZE // 2), RADIUS)
        pygame.display.update()
