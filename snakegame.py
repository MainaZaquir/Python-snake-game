import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define your colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the Snake and Food
block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 50)


def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, BLACK)
    win.blit(value, [10, 10])


def draw_snake(block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(win, GREEN, [block[0], block[1], block_size, block_size])


def run_game():
    game_over = False
    game_close = False

    # Initialize the starting position of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    # Initialize the snake body and length
    snake_body = []
    length_of_snake = 1

    # Generate the first food location
    food_x = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            win.fill(BLACK)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            win.blit(message, [WIDTH / 6, HEIGHT / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for boundary collision
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, block_size,

