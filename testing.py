def setup():
    size(400,400)
    
def draw():
    background(220)
    # HSB RED COLOR FILL
    color_mode(HSB, 360, 100, 100)
    redColor = color(0, 100, 100)
    fill(redColor)

    # RGB BLUE COLOR OUTLINE
    color_mode(RGB, 255, 255, 255)
    blueColor = color(0, 0, 255)
    stroke(blueColor)
    stroke_weight(1)

    # BODY
    square(150, 150, 100)

    # HEAD
    square(175, 100, 50)
    circle(193, 115, 15)
    circle(211, 130, 15)
    arc(200, 125, 25, 15, 0, PI)

    # LEGS
    rect(175, 250, 30, 50)
    rect(225, 250, 30, 50)

    # FEET
    rect(150, 300, 55, 20)
    rect(225, 300, 55, 20)

    # ARMS
    rect(100, 175, 50, 15)
    rect(250, 175, 50, 15)
