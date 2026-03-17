# --- Shooter Game with Difficulty and Discrete Movement ---

# Game states
game_state = "menu"  # menu, playing, game_over

# Player setup
player_x = 400
player_y = 550
player_width = 50
player_height = 20
player_speed = 25

# Bullets
bullets = []

# Enemies
enemies = []
enemy_width = 40
enemy_height = 20
enemy_speed = 3
spawn_interval = 60
frame_count_since_spawn = 0

# Score
score = 0

# Difficulty
difficulty = "Medium"  # Default
difficulty_settings = {
    "Easy": {"enemy_speed": 2, "spawn_interval": 90},
    "Medium": {"enemy_speed": 3, "spawn_interval": 60},
    "Hard": {"enemy_speed": 4, "spawn_interval": 40}
}

def setup():
    size(800, 600)
    text_align(CENTER, CENTER)
    text_size(32)
    
def draw():
    global frame_count_since_spawn, game_state, enemies, score
    
    background(30, 30, 40)
    
    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        draw_playing()
    elif game_state == "game_over":
        draw_game_over()

# --- Menu ---
def draw_menu():
    fill(200)
    text("Select Difficulty", width/2, height/3)
    text("Press E for Easy, M for Medium, H for Hard", width/2, height/2)

def key_pressed():
    global game_state, difficulty, player_x, bullets
    
    if game_state == "menu":
        if key in ["E", "e"]:
            difficulty = "Easy"
            start_game()
        elif key in ["M", "m"]:
            difficulty = "Medium"
            start_game()
        elif key in ["H", "h"]:
            difficulty = "Hard"
            start_game()
    elif game_state == "playing":
        if key_code == LEFT:
            player_move(-player_speed)
        elif key_code == RIGHT:
            player_move(player_speed)
        elif key == ' ':
            shoot_bullet()
    elif game_state == "game_over":
        if key == 'R' or key == 'r':
            game_state = "menu"

def start_game():
    global game_state, enemies, bullets, player_x, score, enemy_speed, spawn_interval, frame_count_since_spawn
    game_state = "playing"
    enemies = []
    bullets = []
    player_x = width / 2
    score = 0
    settings = difficulty_settings[difficulty]
    global enemy_speed, spawn_interval
    enemy_speed = settings["enemy_speed"]
    spawn_interval = settings["spawn_interval"]
    frame_count_since_spawn = 0

def player_move(amount):
    global player_x
    player_x += amount
    player_x = constrain(player_x, 0, width - player_width)

def shoot_bullet():
    bullets.append({
        'x': player_x + player_width / 2 - 5,
        'y': player_y,
        'width': 10,
        'height': 20,
        'speed': 7
    })

# --- Playing ---
def draw_playing():
    global frame_count_since_spawn, enemies, score, game_state
    
    # Draw player
    fill(0, 255, 0)
    rect(player_x, player_y, player_width, player_height, 10)
    
    # Handle bullets
    for bullet in bullets[:]:
        bullet['y'] -= bullet['speed']
        fill(255, 255, 0)
        rect(bullet['x'], bullet['y'], bullet['width'], bullet['height'], 5)
        if bullet['y'] < 0:
            bullets.remove(bullet)
    
    # Spawn enemies
    frame_count_since_spawn += 1
    if frame_count_since_spawn >= spawn_interval:
        frame_count_since_spawn = 0
        enemies.append({
            'x': random(width - enemy_width),
            'y': -enemy_height,
            'width': enemy_width,
            'height': enemy_height,
            'speed': enemy_speed
        })
    
    # Handle enemies
    for enemy in enemies[:]:
        enemy['y'] += enemy['speed']
        fill(255, 80, 80)
        rect(enemy['x'], enemy['y'], enemy['width'], enemy['height'], 5)
        
        # Check collision with bullets
        for bullet in bullets[:]:
            if collide_rect_rect(
                bullet['x'], bullet['y'], bullet['width'], bullet['height'],
                enemy['x'], enemy['y'], enemy['width'], enemy['height']
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break
        
        # Game over if enemy reaches bottom
        if enemy['y'] > height:
            game_state = "game_over"
    
    # Draw score
    fill(255)
    text_size(20)
    text(f"Score: {score}", 70, 30)

# --- Game Over ---
def draw_game_over():
    fill(255, 50, 50)
    text_size(50)
    text("GAME OVER", width/2, height/3)
    text_size(30)
    text(f"Score: {score}", width/2, height/2)
    text("Press R to Restart", width/2, height*2/3)

# --- Collision function ---
def collide_rect_rect(x1, y1, w1, h1, x2, y2, w2, h2):
    return not (x1 + w1 < x2 or x1 > x2 + w2 or y1 + h1 < y2 or y1 > y2 + h2)