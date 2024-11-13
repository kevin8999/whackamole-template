import pygame
import random

class Board:
    def __init__(self, rows=16, cols=20, WIDTH=640, HEIGHT=512):
        self.rows = rows
        self.cols = cols
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        # Size of each square on the board
        self.SQUARE_SIZE = 32
        
        # Position of rendered mole
        self.mole_x = 0
        self.mole_y = 0

    def create_board(self):
        # Create a rows by cols board
        self.board = [[False] * self.cols] * self.rows

    def pick_rand_pos(self):
        # Pick a random position to put the mole at
        rand_row = random.randint(0, self.rows-1)
        rand_col = random.randint(0, self.cols-1)

        print(rand_col, rand_row)

        # Ensure each position is False
        self.create_board()
        # Pick another position if it's the same one
        if self.board[rand_row][rand_col] == True:
            self.pick_rand_pos()

        # Set position on board to True to indicate the mole is there
        self.board[rand_row][rand_col] = True

        # Set position to render mole in self.render_mole()
        self.mole_x = rand_col * self.SQUARE_SIZE
        self.mole_y = rand_row * self.SQUARE_SIZE
        print(self.mole_x, self.mole_y)

def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        # Set screen size
        WIDTH, HEIGHT = 640, 512
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Set internal clock
        clock = pygame.time.Clock()

        # Create board
        BOARD_ROWS, BOARD_COLS = 16, 20
        board = Board(BOARD_ROWS, BOARD_COLS)
 
        # Define random variables
        board.pick_rand_pos()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mole was clicked with left mouse button
                    if event.button == 1:
                        # Find position of mouse click
                        x, y = event.pos
                        print(f"Mouse: {(x, y)}")
                        # Check mouse click is inside the square that the mole is in
                        col_range = range( board.mole_x, board.mole_x + board.SQUARE_SIZE )
                        row_range = range( board.mole_y, board.mole_y + board.SQUARE_SIZE )
                        if x in col_range and y in row_range:
                            board.pick_rand_pos()

            screen.fill("light green")
            
            # Render mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(board.mole_x, board.mole_y)))

            # Draw lines
            for i in range(board.cols):
                pygame.draw.line(screen, "black", start_pos=(i * board.SQUARE_SIZE,0), end_pos=(i * board.SQUARE_SIZE, WIDTH), width=1)
            for i in range(board.rows):
                pygame.draw.line(screen, "blue", start_pos=(0, i * board.SQUARE_SIZE), end_pos=(WIDTH, i * board.SQUARE_SIZE))

            # Update display
            pygame.display.flip()

            # frames per second            
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
