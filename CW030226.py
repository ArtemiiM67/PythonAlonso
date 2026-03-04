import random
import math

circ1 = {"x": 30, "xSpeed": 10, "y": 150, "ySpeed": 0} 
circ2 = {"x": 400, "xSpeed": 0, "y": random.randint(50, 550), "ySpeed": 10} 
circ3 = {"x": random.randint(50, 800), "xSpeed": 10, "y": random.randint(50, 550), "ySpeed": 10}
circ4 = {"x": 300, "xSpeed": random.randint(-10, 10), "y": 400, "ySpeed": random.randint(-10, 10)}

balls = [circ1, circ2, circ3, circ4]

def setup():
    size(800, 600)

def draw():
    background(220)

    for ball in balls:
        fill(255, 0, 0)
        stroke_weight(2)
        stroke(0)
        
        circle(ball['x'], ball['y'], 30)
        
        if ball == circ1:
            if ball['x'] > width - 15 or ball['x'] < 15:
                ball['xSpeed'] = -ball['xSpeed']
            ball['x'] += ball['xSpeed']
        
        if ball == circ2:
            if ball['y'] > height - 15 or ball['y'] < 15:
                ball['ySpeed'] = -ball['ySpeed']
            ball['y'] += ball['ySpeed']
        
        if ball == circ3:
            if ball['x'] > width - 15 or ball['x'] < 15:
                ball['xSpeed'] = -ball['xSpeed']
            if ball['y'] > height - 15 or ball['y'] < 15:
                ball['ySpeed'] = -ball['ySpeed']
            
            ball['x'] += ball['xSpeed']
            ball['y'] += ball['ySpeed']
            
        if ball == circ4:
            ball['xSpeed'] = random.randint(-10, 10)
            ball['ySpeed'] = random.randint(-10, 10)
            
            if ball['x'] > width - 15 or ball['x'] < 15:
                ball['xSpeed'] = -ball['xSpeed']
                ball['x'] = 100
            if ball['y'] > height - 15 or ball['y'] < 15:
                ball['ySpeed'] = -ball['ySpeed']
                ball['y'] = 100
            
            ball['x'] += ball['xSpeed']
            ball['y'] += ball['ySpeed']