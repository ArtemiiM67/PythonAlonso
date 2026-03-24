from PIL import Image
from random import uniform
from playsound import playsound

pig = None

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
            image(pig, 0, 0, self.size, self.size)
            pop_matrix()
        else:
            for p in self.particles:
                p.display()

    def clicked(self, mx, my):
        d = dist(mx, my, width/2, height/2 + self.y_offset)
        if d < self.size / 2:
            self.explode()

    def explode(self):
        self.exploding = True
        for _ in range(50):
            self.particles.append(Particle(width/2, height/2 + self.y_offset))

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = uniform(-5, 5)
        self.vy = uniform(-5, 5)
        self.life = 60
        self.color = color(uniform(200,255), uniform(50,150), uniform(100,255))

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1 
        self.life -= 1

    def display(self):
        fill(self.color, self.life * 4) 
        no_stroke()
        ellipse(self.x, self.y, 10, 10)

    def isDead(self):
        return self.life <= 0

pig_obj = None

def setup():
    global pig, pig_obj
    size(800, 800)
    pig = load_image("pig.jpg")
    text_align(CENTER, CENTER)
    text_size(60)
    pig_obj = Pig(width/2, height/2)
    playsound('PeppaPig.mp3')

def draw():
    background(255, 220, 220)
    
    pig_obj.update()
    pig_obj.display()

    wave = 10 * sin(frame_count * 0.1)
    fill(255, 105, 180)
    text("Happy National Pig Day!", width / 2, height - 100 + wave)

def mouse_pressed():
    if mouse_button == LEFT:
        pig_obj.clicked(mouse_x, mouse_y)