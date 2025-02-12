#1. Importing Libraries
import pygame
import random

# Initialize pygame
pygame.init()

# 3. Setting Up the Game Window

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake settings
snake = [(100, 100), (90, 100), (80, 100)]  # Initial position
direction = (CELL_SIZE, 0)  # Moving right initially
food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE, 
        random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)


clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 30)

running = True
print("Game Started!")  # Debugging Message

while running:
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit Event Triggered!")  # Debugging Message
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # Move Snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Collision Detection
    if (
        new_head in snake or  # Collision with itself
        new_head[0] < 0 or new_head[0] >= WIDTH or  # Collision with walls
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        print("Game Over!")  # Debugging Message
        running = False

    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food:
        score += 1
        food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE, 
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    else:
        snake.pop()  # Maintain snake length

    # Draw the Snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Draw the Food
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Display Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)  # Control game speed

pygame.quit()
print("Game Closed")  # Debugging Message
