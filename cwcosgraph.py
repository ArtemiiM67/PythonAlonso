from gridNdot import *

def setup():
    size(600,600)
    
def draw():
    draw_grid()
    translate(width/2,height/2)
    fill(255)
    circle(0,0,300)
    fill(0)
    circle(0,0,2)