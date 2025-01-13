import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Load mole image
mole_image = pygame.image.load("mole.png")
mole_rect = mole_image.get_rect()
mole_width, mole_height = mole_rect.size

# Game variables
mole_position = (random.randint(0, WIDTH - mole_width), random.randint(0, HEIGHT - mole_height))
score = 0
font = pygame.font.Font(None, 36)

# Timer variables
game_time = 60  # Game duration in seconds
start_ticks = pygame.time.get_ticks()
mole_timer = 1000  # Time in milliseconds
last_mole_time = pygame.time.get_ticks()

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mole_rect.collidepoint(event.pos):
                score += 1
                mole_position = (random.randint(0, WIDTH - mole_width), random.randint(0, HEIGHT - mole_height))

    # Update mole position based on timer
    current_time = pygame.time.get_ticks()
    if current_time - last_mole_time > mole_timer:
        mole_position = (random.randint(0, WIDTH - mole_width), random.randint(0, HEIGHT - mole_height))
        score -= 1  # Deduct score for missing the mole
        last_mole_time = current_time

    # Draw mole
    mole_rect.topleft = mole_position
    screen.blit(mole_image, mole_position)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Draw timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    remaining_time = max(0, game_time - int(elapsed_time))
    timer_text = font.render(f"Time: {remaining_time}s", True, BLACK)
    screen.blit(timer_text, (WIDTH - 150, 10))

    # Check for game over
    if remaining_time <= 0:
        running = False

    # Refresh screen
    pygame.display.flip()
    clock.tick(30)

# Game over screen
screen.fill(WHITE)
game_over_text = font.render("Game Over!", True, RED)
final_score_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
