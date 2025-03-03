import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PLAYER_SIZE = 50

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# Player setup
player = pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 5

# Enemy setup
enemy = pygame.Rect(random.randint(0, WIDTH - PLAYER_SIZE), 0, PLAYER_SIZE, PLAYER_SIZE)
enemy_speed = 3

# Game Loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
        player.x += player_speed
    
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.y = 0
        enemy.x = random.randint(0, WIDTH - PLAYER_SIZE)
    
    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, RED, enemy)
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
