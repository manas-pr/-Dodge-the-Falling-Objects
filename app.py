import pygame
import random
import streamlit as st
import threading
import os

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dodge the Falling Objects")
    clock = pygame.time.Clock()
    
    player_x = WIDTH // 2 - PLAYER_WIDTH // 2
    player_y = HEIGHT - PLAYER_HEIGHT - 10
    player_speed = 7
    
    obstacles = []
    obstacle_speed = 5
    score = 0
    
    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
            player_x += player_speed
        
        # Generate obstacles
        if random.randint(1, 50) == 1:
            obstacles.append(pygame.Rect(random.randint(0, WIDTH - OBSTACLE_WIDTH), 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        
        # Move and draw obstacles
        for obstacle in obstacles[:]:
            obstacle.y += obstacle_speed
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
                score += 1
            pygame.draw.rect(screen, RED, obstacle)
        
        # Check for collisions
        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                running = False
                break
        
        # Draw player
        pygame.draw.rect(screen, BLACK, player_rect)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    os._exit(0)

def start_game():
    threading.Thread(target=game).start()

def main():
    st.title("🎮 Dodge the Falling Objects")
    st.write("Use left and right arrow keys to avoid falling obstacles!")
    if st.button("Start Game"):
        start_game()
        st.write("Game started! Switch to the pygame window.")

if __name__ == "__main__":
    main()
