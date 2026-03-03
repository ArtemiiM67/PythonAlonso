import random
import math

circ1 = {
    "x": 30,
    "xSpeed": 5,
}

circ2 = {
    "y": 30,
    "ySpeed": 5,
}

circ3 = {
    "x": 30,
    "y": 30,
    "xSpeed": 5,
    "ySpeed": 5,
}

circ4 = {
    "x": 100,
    "y": 100,
    "xSpeed": 5,
    "ySpeed": 5,
}

def setup():
    size(800, 600)

def draw():
    background(220)

    # Draw and move circ1 (horizontal movement)
    fill(200)
    stroke_weight(2)
    stroke(0)
    
    circle(circ1['x'], 250, 30)
    if circ1['x'] >= width:  # Reset if goes out of bounds
        circ1['x'] = 0
    circ1['x'] += circ1['xSpeed']
    
    # Draw and move circ2 (vertical movement)
    circle(30, circ2['y'], 30)
    if circ2['y'] >= height:  # Reset if goes out of bounds
        circ2['y'] = 0
    circ2['y'] += circ2['ySpeed']
    
    # Draw and move circ3 (horizontal + vertical movement)
    circle(circ3['x'], circ3['y'], 30)
    if circ3['x'] >= width:  # Reset horizontal position
        circ3['x'] = 100
    if circ3['y'] >= height:  # Reset vertical position
        circ3['y'] = 100
    circ3['x'] += circ3['xSpeed']
    circ3['y'] += circ3['ySpeed']
    
    # Draw and move circ4 (complex random movement)
    circle(circ4['x'], circ4['y'], 30)
    if circ4['x'] >= width:  # Reset horizontal position
        circ4['x'] = 0
    if circ4['y'] >= height:  # Reset vertical position
        circ4['y'] = 0
    
    # Adjust circ4's position using randomization + cos for smooth motion
    random_factor_x = random.choice([-1, 1]) * circ4['xSpeed'] + 12 * math.cos(random.uniform(0, math.pi))
    random_factor_y = random.choice([-1, 1]) * circ4['ySpeed'] + 12 * math.cos(random.uniform(0, math.pi))
    
    circ4['x'] += random_factor_x
    circ4['y'] += random_factor_y