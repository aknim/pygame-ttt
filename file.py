import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 300, 400
LINE_COLOR = (0, 0, 0) # Black
BG_COLOR = (255, 255, 255) # White
LINE_WIDTH = 10

# Button dimensions
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
BUTTON_COLOR = (0, 255, 0)
BUTTON_TEXT_COLOR = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")


# Game board: 3x3 grid (initially empty)
board = [["" for _ in range(3)] for _ in range(3)]

# Variables to track turns and game state
player_turn = 'X'
running = True
game_active = True
ai_enabled = True

# Fonts
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 32)

def draw_marks():
 for row in range(3):
  for col in range(3):
   if board[row][col] == 'X':
    pygame.draw.line(screen, (0, 0, 255), (col * 100 + 20, row * 100 + 20), (col * 100 + 80, row * 100 + 80), 10)
    pygame.draw.line(screen, (0, 0, 255), (col * 100 + 80, row * 100 + 20), (col * 100 + 20, row * 100 + 80), 10)
   elif board[row][col] == '0':
    pygame.draw.circle(screen, (255, 0, 0), (col * 100 + 50, row * 100 + 50), 40, 10)

def check_winner():
 # Check rows, columns, and diagonals for a winner
 for row in range(3):
  if board[row][0] == board[row][1] == board[row][2] != "": 
   return board[row][0] 
 for col in range(3):
  if board[0][col] == board[1][col] == board[2][col] != "": 
   return board[0][col] 
  if board[0][0] == board[1][1] == board[2][2] != "": 
   return board[0][0]
 if board[0][2] == board[1][1] == board[2][0] != "": 
  return board[0][2]
 return None

def handle_click(pos):
 global player_turn, game_active

 x, y = pos
 row = y // 100
 col = x // 100

 if board[row][col] == "":
  board[row][col] = player_turn
  if player_turn == 'X':
   player_turn = '0'
  else:
   player_turn = 'X'
  winner = check_winner()
  if winner:
   pygame.display.set_caption(f"{winner} wins!")
   game_active = False

def draw_button():
  pygame.draw.rect(screen, BUTTON_COLOR, (75, 320, BUTTON_WIDTH, BUTTON_HEIGHT))
  text_surface = button_font.render("Restart", True, BUTTON_TEXT_COLOR)
  screen.blit(text_surface, (95, 335))

def reset_game():
  global board, player_turn, game_active
  board = [["" for _ in range(3)] for _ in range(3)]
  player_turn = 'X'
  game_active = True
  pygame.display.set_caption("Tic-Tac-Toe")

def ai_move():
  global player_turn, game_active

  if not game_active or player_turn != '0':  # Let AI move, only when it's 0's turn
    return

  available_spots = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ""]

  if available_spots:
    row, col = random.choice(available_spots)
    board[row][col] = '0'
    player_turn = 'X'
    winner = check_winner()
    if winner:
      pygame.display.set_caption(f"{winner} wins!")
      game_active = False

# Game loop
running = True
while running:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False
  if event.type == pygame.MOUSEBUTTONDOWN: 
    if 75 <= event.pos[0] <= 75 + BUTTON_WIDTH and 320 <= event.pos[1] <= 320 + BUTTON_HEIGHT:
      reset_game()
    elif game_active:
      handle_click(event.pos)

 if ai_enabled and player_turn == '0':
  ai_move()

 screen.fill(BG_COLOR)
 draw_marks()

 # Drawing grid lines
 pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
 pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)
 pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
 pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)

 draw_button()
 pygame.display.update()

