def setup():
    size(800, 800)
    background(255,182,193)
    no_fill()
    stroke_weight(2)

def draw():
    translate(width / 2, height / 2)

    r = frame_count * 0.5
    angle = frame_count * 0.05

    x = cos(angle) * r
    y = sin(angle) * r

    stroke(
        100 + 100 * sin(angle),
        100 + 100 * sin(angle + 2),
        100 + 100 * sin(angle + 4),
        80
    )

    ellipse(x, y, 40 + 20 * sin(angle * 2), 40 + 20 * cos(angle * 2))

    if r > width:
        no_loop()
