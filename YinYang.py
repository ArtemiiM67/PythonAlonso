def setup():
    size(800, 800)
    background(225)

def yin_yang(x, y, s, angle):
    push_matrix()
    translate(x, y)
    rotate(angle)

    stroke_weight(3)

    fill(255)
    circle(0, 0, s)

    fill(0)
    arc(0, 0, s, s, PI/2, 3*PI/2, PIE)

    no_stroke()
    fill(255)
    circle(0, s/4, s/2)

    fill(0)
    circle(0, s/4, s/10)

    fill(0)
    circle(0, -s/4, s/2)

    fill(255)
    circle(0, -s/4, s/10)

    pop_matrix()

def tongue(x, y):
    tongue_offset = sin(frame_count) * 40
    tongue_offset_horizontal = cos(frame_count) * 40

    no_stroke()
    fill(200, 60, 90)

    rect(x - 40 - tongue_offset_horizontal, y, 80, 140 + tongue_offset, 40)

    circle(x - tongue_offset_horizontal, y + 140 + tongue_offset, 90)

def draw():
    if is_mouse_pressed and mouse_button == LEFT:
        background(random(255), random(255), random(255))
        angle = frame_count * 0.02
    if is_mouse_pressed and mouse_button == RIGHT:
        background(220)
        angle = frame_count * 0.005
    
    angle = frame_count * 0.02

    fill(224, 157, 30)
    stroke_weight(3)
    circle(400, 400, 500)

    fill(172, 65, 65)
    arc(400, 500, 200, 100, radians(315), radians(585), CHORD)

    fill(255)
    rect(350, 465, 30, 50)
    rect(415, 465, 30, 50)
    
    tongue(400, 500)

    yin_yang(300, 320, 120, angle)
    yin_yang(500, 320, 120, -angle)

    no_fill()
    stroke(5)
    arc(300, 250, 100, 60, PI, TWO_PI)
    arc(500, 250, 100, 60, PI, TWO_PI)
