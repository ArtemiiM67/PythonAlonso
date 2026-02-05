def setup():
    size(1000,1000)
    
y = 0
speed = 5

def draw():
    global y
    circle(500, y, 100)
    circle(500, 800, 100)
    y += speed
    
    

def collideCircleCircle(circ1x, circ1y, circ1d, circ2x, circ2y, circ2d):
  """Input x,y coordinates and diameter for both circles.
  Returns true if the two circles are touching.
  
  Does not work for ellipse/oval shapes."""
  
  distance = dist(circ1x, circ1y, circ2x, circ2y)
  circ1rad = circ1d/2
  circ2rad = circ2d/2
  
  if distance <= circ1rad + circ2rad:
    return True
  else:
    return False
