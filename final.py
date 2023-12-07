import pygame
import random
import math

## why chosing this Game ?!

## In this project, I made a simple Pac-Man game. As a kid, I loved playing Pac-Man.
## Creating my version of this game brings back fond memories of my childhood gaming days.


## Description:

## Experience a classic Pac-Man-inspired game where you control a character navigating a maze to collect food items. Use arrow keys for movement,
## strategically gather all food items to win. Enjoy the challenge of maneuvering through the maze while avoiding obstacles.

## Instructions:

## Use arrow keys (←↑→↓) to move the character.
## Collect all food items to achieve victory, and avoind beint eaten.
## Press 'R' to restart the game after winning or to reset during play.



## building the game ##

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module for sound

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 36)
SCREEN_TITLE = "Simple Pac-Man"

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Load background music
pygame.mixer.music.load('Intro.mp3')  # Replace 'Intro.mp3' with the path to your music file
pygame.mixer.music.set_volume(0.5)  # Set the volume level (0.0 to 1.0)
pygame.mixer.music.play(loops=-1)  # Play the music (-1 loops the music infinitely)

# Player
player_radius = 15
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Score
score = 0
score_font = pygame.font.Font(None, 24)

# Food
food_radius = 10
foods = []
for _ in range(10):
    food_x = random.randint(50, WIDTH - 50)
    food_y = random.randint(50, HEIGHT - 50)
    foods.append((food_x, food_y))

# Enemies
enemy_radius = 20
enemy_speed = 3
enemy_1_x = random.randint(50, WIDTH - 50)
enemy_1_y = random.randint(50, HEIGHT - 50)
enemy_2_x = random.randint(50, WIDTH - 50)
enemy_2_y = random.randint(50, HEIGHT - 50)
enemy_1_direction = random.choice(['up', 'down', 'left', 'right'])
enemy_2_direction = random.choice(['up', 'down', 'left', 'right'])

clock = pygame.time.Clock()

running = True
game_over = False
won = False
show_instructions = True

while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                show_instructions = False
            if event.key == pygame.K_r:
                # Restart the game
                score = 0
                player_radius = 15
                player_x = WIDTH // 2
                player_y = HEIGHT // 2
                foods = []
                for _ in range(10):
                    food_x = random.randint(50, WIDTH - 50)
                    food_y = random.randint(50, HEIGHT - 50)
                    foods.append((food_x, food_y))
                game_over = False
                won = False

    if show_instructions:
        instructions_text = FONT.render("Welcome to Simple Pac-Man!", True, WHITE)
        instructions_text2 = FONT.render("Use arrow keys to move.", True, WHITE)
        instructions_text3 = FONT.render("Collect all food items to win.", True, WHITE)
        instructions_text4 = FONT.render("Press Enter to start.", True, YELLOW)

        text_rect = instructions_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        text_rect2 = instructions_text2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        text_rect3 = instructions_text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        text_rect4 = instructions_text4.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        screen.blit(instructions_text, text_rect)
        screen.blit(instructions_text2, text_rect2)
        screen.blit(instructions_text3, text_rect3)
        screen.blit(instructions_text4, text_rect4)
    else:
        if not game_over and not won:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < WIDTH - player_radius:
                player_x += player_speed
            if keys[pygame.K_UP] and player_y > 0:
                player_y -= player_speed
            if keys[pygame.K_DOWN] and player_y < HEIGHT - player_radius:
                player_y += player_speed

            # Check for collision with food
            for food in foods[:]:
                food_x, food_y = food
                if (player_x - food_x) ** 2 + (player_y - food_y) ** 2 <= (player_radius + food_radius) ** 2:
                    foods.remove(food)
                    player_radius += 1  # Increase player radius slightly
                    score += 10  # Increment score by 10 for each food collected

            # Draw food
            for food in foods:
                pygame.draw.circle(screen, YELLOW, food, food_radius)

            # Draw player
            pygame.draw.circle(screen, WHITE, (player_x, player_y), player_radius)

            # Draw score
            score_text = score_font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            # Move enemies
            if enemy_1_direction == 'up':
                enemy_1_y -= enemy_speed
                if enemy_1_y < 0:
                    enemy_1_direction = 'down'
            elif enemy_1_direction == 'down':
                enemy_1_y += enemy_speed
                if enemy_1_y > HEIGHT:
                    enemy_1_direction = 'up'
            elif enemy_1_direction == 'left':
                enemy_1_x -= enemy_speed
                if enemy_1_x < 0:
                    enemy_1_direction = 'right'
            elif enemy_1_direction == 'right':
                enemy_1_x += enemy_speed
                if enemy_1_x > WIDTH:
                    enemy_1_direction = 'left'

            if enemy_2_direction == 'up':
                enemy_2_y -= enemy_speed
                if enemy_2_y < 0:
                    enemy_2_direction = 'down'
            elif enemy_2_direction == 'down':
                enemy_2_y += enemy_speed
                if enemy_2_y > HEIGHT:
                    enemy_2_direction = 'up'
            elif enemy_2_direction == 'left':
                enemy_2_x -= enemy_speed
                if enemy_2_x < 0:
                    enemy_2_direction = 'right'
            elif enemy_2_direction == 'right':
                enemy_2_x += enemy_speed
                if enemy_2_x > WIDTH:
                    enemy_2_direction = 'left'

            # Draw enemies
            pygame.draw.circle(screen, RED, (enemy_1_x, enemy_1_y), enemy_radius)
            pygame.draw.circle(screen, RED, (enemy_2_x, enemy_2_y), enemy_radius)

            # Check collision with enemies
            for enemy in [(enemy_1_x, enemy_1_y), (enemy_2_x, enemy_2_y)]:
                if math.sqrt((player_x - enemy[0])**2 + (player_y - enemy[1])**2) < (player_radius + enemy_radius):
                    game_over = True

            # Check for win condition
            if len(foods) == 0:
                game_over = True
                won = True

        if game_over and won:
            text = FONT.render("You won! Press 'R' to restart.", True, WHITE)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)

            # Stop the music when winning
            pygame.mixer.music.stop()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
