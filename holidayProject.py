import threading
from random import uniform, randint, choice
from playsound import playsound
from math import sin
import os
import time

pig_img = None
decorations = []
pig_obj = None
images_folder = "Peppa/"

class Pig:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.y_offset = 0
        self.direction = 1
        self.size = 400
        self.exploding = False
        self.particles = []

    def update(self):
        if not self.exploding:
            self.y_offset += 2 * self.direction
            if self.y_offset > 20 or self.y_offset < -20:
                self.direction *= -1
            self.angle += 0.02
        else:
            for p in self.particles:
                p.update()
            self.particles = [p for p in self.particles if not p.isDead()]

    def display(self):
        if not self.exploding:
            push_matrix()
            translate(width / 2, height / 2 + self.y_offset)
            rotate(self.angle)
            image_mode(CENTER)
            image(pig_img, 0, 0, self.size, self.size)
            pop_matrix()
        else:
            for p in self.particles:
                p.display()

    def clicked(self, mx, my):
        d = dist(mx, my, width / 2, height / 2 + self.y_offset)
        if d < self.size / 2:
            self.explode()
            threading.Thread(target=self.revert_pig_image, daemon=True).start()
            
    def horrorclicked(self, mx, my):
        d = dist(mx, my, width / 2, height / 2 + self.y_offset)
        if d < self.size / 2:
            self.horror()

    def explode(self):
        self.exploding = True
        for _ in range(50):
            self.particles.append(Particle(width / 2, height / 2 + self.y_offset))
            
    def horror(self):
        global pig_img
        pig_img = load_random_image()
        threading.Thread(target=play_horror_music, daemon=True).start()
        threading.Thread(target=self.horror_glitch, daemon=True).start()
        threading.Thread(target=self.revert_pig_image, daemon=True).start()

    def revert_pig_image(self):
        global pig_img
        time.sleep(2)
        pig_img = load_image("pig.jpg")
        self.exploding = False
        self.particles = []

    def horror_glitch(self):
        for _ in range(10):
            self.size += randint(-10, 10)
            self.angle += uniform(-0.5, 0.5)
            time.sleep(0.05)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = uniform(-5, 5)
        self.vy = uniform(-5, -1)
        self.life = randint(40, 70)
        self.size = randint(5, 15)
        self.color = color(uniform(200, 255), uniform(50, 150), uniform(100, 255))
        self.gravity = 0.2
        self.fade_speed = uniform(2, 5)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.life -= self.fade_speed
        self.size *= 0.96

    def display(self):
        if self.life > 0:
            fill(self.color, max(self.life * 4, 0))
            no_stroke()
            ellipse(self.x, self.y, self.size, self.size)

    def isDead(self):
        return self.life <= 0 or self.size <= 0

class Decoration:
    def __init__(self):
        self.x = randint(0, 800)
        self.y = randint(-200, 0)
        self.size = randint(10, 30)
        self.color = color(randint(100, 255), randint(100, 255), randint(100, 255))
        self.type = randint(0, 2)
        self.speed = uniform(1, 4)
        self.angle = uniform(0, 360)
        self.rotation_speed = uniform(-0.05, 0.05)

    def update(self):
        self.y += self.speed
        self.angle += self.rotation_speed
        if self.y > 800:
            self.y = randint(-200, 0)
            self.x = randint(0, 800)

    def display(self):
        push_matrix()
        translate(self.x, self.y)
        rotate(self.angle)
        fill(self.color)
        no_stroke()
        if self.type == 0:
            ellipse(0, 0, self.size, self.size)
        elif self.type == 1:
            rect(-self.size / 4, -self.size / 2, self.size / 2, self.size)
        else:
            ellipse(0, 0, self.size / 3, self.size / 3)
        pop_matrix()

def play_music():
    while True:
        playsound('PeppaPig.mp3')

def play_horror_music():
    playsound('PeppaPigHorror.mp3')

def load_random_image():
    images = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if images:
        return load_image(os.path.join(images_folder, choice(images)))
    return load_image("pig.jpg") 

def setup():
    global pig_img, pig_obj, decorations
    size(800, 800)
    pig_img = load_image("pig.jpg")
    text_align(CENTER, CENTER)
    text_size(60)
    pig_obj = Pig(width / 2, height / 2)

    for _ in range(30):
        decorations.append(Decoration())

    threading.Thread(target=play_music, daemon=True).start()

def draw():
    background(255, 220, 220)
    
    pig_obj.update()
    pig_obj.display()

    for deco in decorations:
        deco.update()
        deco.display()

    wave = 10 * sin(frame_count * 0.1)
    fill(255, 105, 180)
    text_size(25)
    text("March 1st - Happy National Pig Day!", width / 2, height - 100 + wave)

def mouse_pressed():
    if mouse_button == LEFT:
        pig_obj.clicked(mouse_x, mouse_y)
    elif mouse_button == RIGHT:
        pig_obj.horrorclicked(mouse_x, mouse_y)