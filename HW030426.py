import random
import math

sign = {"x": 450, "y": 350, "xSpeed": 10, "ySpeed": 5}
img = None

def setup():
    size(1000, 800)
    global img
    img = load_image("logo.jpg")

def draw():
    background(0)
    
    if sign['x'] > width - img.width or sign['x'] < 0:
        sign['xSpeed'] = -sign['xSpeed']
    if sign['y'] > height - img.height or sign['y'] < 0:
        sign['ySpeed'] = -sign['ySpeed']
    
    sign['x'] += sign['xSpeed']
    sign['y'] += sign['ySpeed']
    
    image(img, sign['x'], sign['y'])