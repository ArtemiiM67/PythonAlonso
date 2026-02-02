def setup(): 
    size(500, 400)
    print("width =", width, "\nheight =", height)
 
def draw():
    #HOMEWORK SHAPES
    background(230) 
    fill(0) 
    #text(str(mouse_x) + ", " + str(mouse_y), 227, 10)
    
    fill(200)
    square(0,0,40)
    circle (20,20,40)
    
    fill(200)
    square(0,359,40)
    circle (20,379,40)
    
    fill(200)
    square(459,0,40)
    circle (479,20,40)
    
    fill(200)
    square(459,359,40)
    circle (479,379,40)
    
    fill(200)
    square(209,159,40)
    
    fill(200)
    square(249,159,40)
    
    fill(200)
    square(209,199,40)
    
    fill(200)
    square(249,199,40)
    
    #EXTRA STUFF
    for x in range(35):
        fill(10*x, 20*x, 30*x)
        ellipse(5*x+45, 10*x+60, 30, 20)

    for x in range(35):
        fill(10*x, 20*x, 30*x)
        ellipse(5*x+290, 410-10*x, 30, 20)
    
    for x in range(47):
        fill(10*x, 20*x, 30*x)
        ellipse(9*x+45, 0.3*x+55, 30, 20)