import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game window
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Font
font = pygame.font.SysFont(None, 35)

def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], block, block])

def show_score(score):
    value = font.render(f"Score: {score}", True, GREEN)
    window.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - SNAKE_BLOCK, 10)
    food_y = random.randrange(0, HEIGHT - SNAKE_BLOCK, 10)

    while not game_over:

        while game_close:
            window.fill(BLACK)
            msg = font.render("Game Over! Press C-Play Again or Q-Quit", True, RED)
            window.blit(msg, [WIDTH // 6, HEIGHT // 3])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(BLACK)
        pygame.draw.rect(window, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - SNAKE_BLOCK, 10)
            food_y = random.randrange(0, HEIGHT - SNAKE_BLOCK, 10)
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    sys.exit()

game_loop()
