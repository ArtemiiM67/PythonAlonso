def setup():
  size(510,350)

def draw():
  background(220)
  translate(250,175)
  rotate(-mouse_x / 200)
  rect(150,150,100,20)

#COMPLETE THE FOLLOWING AND LEAVE YOUR ANSWERS AS COMMENTS:

#1. Play with the values for rotation (keep them below 6.28 for now - that's 2 pi!)
  # Changes rotation of the rectangle, at 2pi is back to normal.

#2. What happens if you move the rectangle to (0, 0)?
  # Goes outside the screen
  
#3. What happens if you add a translation before the rotation? (Try changing where it translates to!)

#4. What if you make the rortation the center of the page with a translation?

#5. What if the rotation is controlled by mouseX or mouseY?

#6. What if you plug in radians(50) to rotate()?