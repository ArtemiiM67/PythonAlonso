def setup():
  size(510,350)
  
a = 0
b = 0

def draw():
  background(220)
  global a, b
  
  #2. move the origin to the pivot point (what you want to rotate around)
  translate(255, 175)
  
  #3. then rotate the grid around the pivot point using the variable you created
  rotate(a)
  rect(0,0,100,20)
  rotate(b)
  rect(0,0,100,20)
  circle(0,0,50)
  
  #4. Increment your rotation variable to make the rotation animated
  a = a + random(-10,10)
  b = b + random(-10,10)
  fill(0)
