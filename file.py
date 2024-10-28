import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0) # Black
BG_COLOR = (255, 255, 255) # White
LINE_WIDTH = 10

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Game loop
running = True
while running:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False

 screen.fill(BG_COLOR)

 
 # Drawing grid lines
 pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
 pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)
 pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
 pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)

 pygame.display.update()

pygame.quit()
sys.exit()

# Game board: 3x3 grid (initially empty)
board = [["" for _ in range(3)] for _ in range(3)]

# Variables to track turns and game state
player_turn = 'X'

def draw_marks():
 for row in range(3):
  for col in range(3):
   if board[row][col] == 'X':
    pygame.draw.line(screen, (0, 0, 255), (col * 100 + 20, row * 100 + 20), (col * 100
