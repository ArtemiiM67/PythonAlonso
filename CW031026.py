from wigglerClass import Wiggler
from collide2d import collidePointCircle

wigglers = []

def setup():
    size(510,350)
    global wigglers, width1, height
    width1, height1 = 510, 350
    wigglers = [Wiggler(35, 35, width1, height1) for _ in range(3)]

def draw():
    background(220)
    for w in wigglers:
        w.animate()

    for i in range(len(wigglers)):
        for j in range(i + 1, len(wigglers)):
            wigglers[i].check_collision(wigglers[j])

    text(f"{mouse_x}, {mouse_y}", 20, 20)

def mousePressed():
    for w in wigglers:
        if collidePointCircle(mouseX, mouseY, w.x, w.y, w.w):
            w.change_color_on_click()