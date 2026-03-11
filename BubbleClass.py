# PY5 IMPORTED MODE CODE
class Bubble:
    def __init__(self):
        self.color = color(random(255), random(255), random(255))
        self.size = random(20, 50)
        
        self.x = random(self.size, width - self.size)
        self.y = random(self.size, height - self.size)
        
        self.xspeed = random(-5, 5)
        self.yspeed = random(-5, 5)
        
        self.hue = random(0, 360)
    
        self.exploded = False 
        
    def display(self):
        color_mode(HSB, 360, 100, 100, 100)
        fill(self.hue, 100, 100, 50)
        circle(self.x, self.y, self.size)
        
    def move(self):
        if not self.exploded: 
            self.x += self.xspeed
            self.y += self.yspeed
            self.jump()
        
    def jump(self):
        if self.x >= width - self.size or self.x <= self.size:
            self.xspeed = -self.xspeed
        if self.y >= height - self.size or self.y <= self.size:
            self.yspeed = -self.yspeed
            
    def explode(self):
        if not self.exploded: 
            self.size += random(20, 50)
            self.size = 0
            self.xspeed += random(-15, 15) 
            self.yspeed += random(-15, 15)  
            self.hue = (self.hue + random(50, 150)) % 360  
            self.exploded = True  