def setup():
    size(400, 400)
    
def draw():
    background(220)
    displayCoordinates()
    grid()
    fill(235)
    rect(130, 120, 140, 80)
    fill(235)
    rect(190, 200, 20, 80)
    for x in range(10):
        fill(10*x, 20*x, 30*x)
        ellipse(5*x+130, 5*y+60, 20, 20)
         
def grid():
    stroke(255)
    for x in range(width):
        if x % 20 == 0:
            for y in range(height):
                if y % 20 == 0:
                    line(x,0,x,height)
                    line(0,y,width,y)
    stroke(0)

def displayCoordinates():
    fill(0)
    text(str(mouse_x) + ", " + str(mouse_y), 227, 10)
    
    