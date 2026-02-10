def setup():
    size(400,600)
    
c = 0
moved1 = False
moved2 = False
moved3 = False
moved4 = False
moved5 = False
moved6 = False

def draw():
    frame_count = 1
    global c, moved1, moved2, moved3, moved4, moved5, moved6
    background(220)
    circle(100,200,75)
    circle(200,200,75)
    circle(300,200,75)
    circle(100,300,75)
    circle(200,300,75)
    circle(300,300,75)
    
    if moved1 == True:
        c = c + 1
        moved1 = False
    
    if moved2 == True:
        c = c + 1
        moved2 = False
        
    if moved3 == True:
        c = c + 1
        moved3 = False
        
    if moved4 == True:
        c = c + 1
        moved4 = False
    
    if moved5 == True:
        c = c + 1
        moved5 = False
        
    if moved6 == True:
        c = c + 1
        moved6 = False
        
    if collidePointCircle(mouse_x, mouse_y, 100, 200, 75):
        fill(20, 174, 234)
        if c>5:
            fill(60,60,60)
        circle(100,200,75)
        fill(255)
        moved1 = True
        
    if collidePointCircle(mouse_x, mouse_y, 200, 200, 75):
        fill(163, 31, 163)
        if c>5:
            fill(60,60,60)
        circle(100,300,75)
        circle(300,300,75)
        fill(255)
        moved2 = True
        
    if collidePointCircle(mouse_x, mouse_y, 300, 200, 75):
        fill(0)
        if c>5:
            fill(60,60,60)
        circle(300,200,75)
        circle(200,300,75)
        fill(255)
        moved3 = True
        
    if collidePointCircle(mouse_x, mouse_y, 100, 300, 75):
        fill(255, 0, 0)
        if c>5:
            fill(60,60,60)
        circle(100,200,75)
        circle(200,200,75)
        circle(300,200,75)
        fill(255)
        moved4 = True    
        
    if collidePointCircle(mouse_x, mouse_y, 200, 300, 75):
        fill(0, 255, 0)
        if c>5:
            fill(60,60,60)
        circle(100,200,75)
        fill(255)
        moved5 = True
        
        
    if collidePointCircle(mouse_x, mouse_y, 300, 300, 75):
        fill(255, 166, 0)
        if c>5:
            fill(60,60,60)
        circle(100,300,75)
        fill(255)
        moved6 = True
    

def collidePointCircle(pointX, pointY, circX, circY, diameter):
  """Input coordinates for the point and x, y, and diameter (the width/height) of the circle.
  Returns true if the point and circle are touching.
  
  Does not work for ellipse/oval shapes."""
  
  distance = dist(pointX, pointY, circX, circY)
  radius = diameter/2
  
  if(distance <= radius):
    return True
  else:
    return False