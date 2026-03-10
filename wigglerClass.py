# PY5 IMPORTED MODE CODE
from random import randint, uniform
from collide2d import collideCircleCircle

class Wiggler:
    def __init__(self, w, h, canvas_width, canvas_height):
        self.w = w
        self.h = h
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.x = uniform(0, self.canvas_width)
        self.y = uniform(0, self.canvas_height)
        self.xSpd = uniform(-10, 10)
        self.ySpd = uniform(-10, 10)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255), 150)
        self.click_count = 0

    def move(self):
        self.x += self.xSpd
        self.y += self.ySpd
        self.xSpd += uniform(-0.5, 0.5)
        self.ySpd += uniform(-0.5, 0.5)
        self.xSpd = max(min(self.xSpd, 5), -5)
        self.ySpd = max(min(self.ySpd, 5), -5)

    def bounce_on_edge(self):
        if self.x < 0:
            self.x = 0
            self.xSpd *= -1
        elif self.x > self.canvas_width:
            self.x = self.canvas_width
            self.xSpd *= -1

        if self.y < 0:
            self.y = 0
            self.ySpd *= -1
        elif self.y > self.canvas_height:
            self.y = self.canvas_height
            self.ySpd *= -1

    def animate(self):
        self.move()
        self.bounce_on_edge()
        self.display()

    def display(self):
        fill(*self.color)
        ellipse(self.x, self.y, self.w, self.h)

    def change_color_on_click(self):
        self.click_count += 1
        r = (self.color[0] + 50) % 256
        g = (self.color[1] + 80) % 256
        b = (self.color[2] + 100) % 256
        self.color = (r, g, b, 150)

    def check_collision(self, other):
        if collideCircleCircle(self.x, self.y, self.w, other.x, other.y, other.w):
            # Swap speeds for simple bounce effect
            self.xSpd, other.xSpd = other.xSpd, self.xSpd
            self.ySpd, other.ySpd = other.ySpd, self.ySpd
            return True
        return False