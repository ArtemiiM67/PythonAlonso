def setup():
    size(400, 400)

def draw():
    background(240)
    rect_mode(CENTER)
    grid()
    displayCoordinates()

    cx = 200 
    cy = 200  

    fill(200)
    rect(cx, cy - 120, 100, 80)

    fill(0)
    ellipse(cx - 20, cy - 130, 10, 10)
    ellipse(cx + 20, cy - 130, 10, 10)

    line(cx - 20, cy - 105, cx + 20, cy - 105)

    fill(180)
    rect(cx, cy, 120, 120)

    rect(cx - 80, cy, 40, 100)
    rect(cx + 80, cy, 40, 100)

    rect(cx - 30, cy + 120, 40, 80)
    rect(cx + 30, cy + 120, 40, 80)

         
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
    
    