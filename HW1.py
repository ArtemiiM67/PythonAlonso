def setup(): 
    size(500, 400)
    print("width =", width, "\nheight =", height)
 
def draw(): 
    background(230) 
    fill(0) 
    text(str(mouse_x) + ", " + str(mouse_y), 227, 200)
    
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