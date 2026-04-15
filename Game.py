from random import randint
from time import time
import random

# Car and Game Variables
car_width = 50
car_height = 100
car_x = 275
car_y = 550
speed = 5
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 3
obstacles = []
score = 0
game_over = False
level = 1
max_level = 5
background_color = (135, 206, 250)  # Sky blue
score_color = (0, 0, 0)
font = "Arial"
high_score = 0
bg_scroll_speed = 1
background_offset = 0

# Set up initial game settings
def setup():
    global car_x, car_y, obstacles, score, level, game_over, obstacle_speed, background_offset
    size(600, 600)
    frame_rate(60)
    car_x = 275
    car_y = 550
    obstacles = []
    score = 0
    level = 1
    obstacle_speed = 3
    game_over = False
    background_offset = 0

# Draw everything on the screen
def draw():
    global car_x, car_y, obstacles, score, game_over, level, obstacle_speed, background_offset

    # Background with scrolling effect
    draw_background()

    if game_over:
        display_game_over()
        return

    # If game is not over, handle player input
    if not game_over:
        if is_key_pressed:
            if key_code == LEFT and car_x > 0:
                car_x -= speed
            elif key_code == RIGHT and car_x < width - car_width:
                car_x += speed

        # Draw the car
        draw_car()

        # Create and move obstacles
        if frame_count % 30 == 0:
            create_obstacle()

        move_obstacles()

        check_collisions()

        # Display score and level
        display_score_and_level()

# Draw the background with scrolling effect
def draw_background():
    global background_offset
    fill(135, 206, 250)  # Sky blue
    rect(0, 0, width, height)

    # Scroll ground
    background_offset += bg_scroll_speed
    fill(255, 250, 205)  # Ground color
    rect(0, height - 100 + (background_offset % 100), width, 100)

# Create an obstacle at random positions
def create_obstacle():
    obstacle_x = randint(0, width - obstacle_width)
    obstacles.append([obstacle_x, 0])

# Move the obstacles downwards, with increased speed at higher levels
def move_obstacles():
    global score, obstacle_speed

    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        draw_obstacle(obstacle[0], obstacle[1])

        # Remove obstacles that are off-screen and increase score
        if obstacle[1] > height:
            obstacles.remove(obstacle)
            score += 1

    if score % 10 == 0 and score != 0 and level < max_level:
        level_up()

# Draw the car sprite (with animation for movement)
def draw_car():
    fill(255, 0, 0)  # Red car
    rect(car_x, car_y, car_width, car_height)

# Draw the obstacles
def draw_obstacle(x, y):
    fill(0, 255, 0)  # Green obstacles
    rect(x, y, obstacle_width, obstacle_height)

# Check for collisions between car and obstacles
def check_collisions():
    global game_over

    for obstacle in obstacles:
        if (car_x + car_width > obstacle[0] and car_x < obstacle[0] + obstacle_width) and \
           (car_y < obstacle[1] + obstacle_height):
            game_over = True

# Display the score and level on the screen
def display_score_and_level():
    fill(*score_color)
    text_size(24)
    text(f"Score: {score}", 20, 30)
    text(f"Level: {level}", 20, 60)

# Level up the game (increase speed and difficulty)
def level_up():
    global level, obstacle_speed, speed
    level += 1
    obstacle_speed += 0.5
    speed += 0.5

# Show the Game Over screen
def display_game_over():
    global high_score
    fill(0)
    text_size(36)
    text("GAME OVER", width / 3, height / 2)
    text_size(24)
    text(f"Score: {score}", width / 3, height / 2 + 40)
    text(f"High Score: {high_score}", width / 3, height / 2 + 70)
    text("Press 'R' to Restart", width / 3, height / 2 + 100)

    # Update high score if needed
    if score > high_score:
        high_score = score

# Restart the game when the player presses 'R'
def key_pressed():
    global game_over, score, level, obstacles, car_x, car_y, obstacle_speed
    if game_over:
        if key == 'r':  # Restart game after Game Over
            setup()

    # Handle movement during gameplay
    if not game_over:
        if key_code == LEFT and car_x > 0:
            car_x -= speed
        elif key_code == RIGHT and car_x < width - car_width:
            car_x += speed

# Display the start screen for difficulty selection
def display_start_screen():
    fill(0)
    text_size(48)
    text("Car Dodge Game", width / 3, height / 3)
    text_size(24)
    text("Press '1' for Easy, '2' for Medium, '3' for Hard", width / 4, height / 2)

# Set the game difficulty based on user input
def key_pressed_level():
    global level, obstacle_speed, speed
    if key == '1':
        level = 1
        obstacle_speed = 3
        speed = 5
    elif key == '2':
        level = 2
        obstacle_speed = 4
        speed = 6
    elif key == '3':
        level = 3
        obstacle_speed = 5
        speed = 7

# Main game loop that controls the state
def main():
    global score, game_over
    if score == 0:  # If score is 0, show start screen and allow difficulty selection
        display_start_screen()
        key_pressed_level()
    else:
        draw()  # Continue the game loop and handle drawing, collisions, etc.
