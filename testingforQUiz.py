def setup():
    size(800,800)
    color_mode(HSB, 360, 100, 100)
    
    
def draw():
    background(220)
    defaultColor = color(200, 100, 100, 50)
    newColor = color(150, 50, 75, 100)
    fill(defaultColor)
    stroke(0)
    stroke_weight(2)
    circle(400,400,400)
    no_stroke()
    fill(newColor)
    circle(300, 300, 50)
    circle(500, 300, 50)
    fill(0)
    circle(300,300, 10)
    circle(500,300,10)
    arc(400, 500, 200, 200, 0, PI)
    fill(defaultColor)
    triangle(400, 350, 450, 450, 350, 450)
    
    