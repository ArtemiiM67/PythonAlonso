def setup():
    size(400, 600)

hover_counts = [0, 0, 0, 0, 0, 0]

prev_hovering = [False] * 6

def draw():
    global prev_hovering
    background(220)

    hovering = [False] * 6

    # check hovers
    hovering[0] = collidePointCircle(mouse_x, mouse_y, 100, 200, 75)
    hovering[1] = collidePointCircle(mouse_x, mouse_y, 200, 200, 75)
    hovering[2] = collidePointCircle(mouse_x, mouse_y, 300, 200, 75)
    hovering[3] = collidePointCircle(mouse_x, mouse_y, 100, 300, 75)
    hovering[4] = collidePointCircle(mouse_x, mouse_y, 200, 300, 75)
    hovering[5] = collidePointCircle(mouse_x, mouse_y, 300, 300, 75)

    for i in range(6):
        if hovering[i] and not prev_hovering[i]:
            hover_counts[i] += 1

    fill(255)
    circle(100, 200, 75)
    circle(200, 200, 75)
    circle(300, 200, 75)
    circle(100, 300, 75)
    circle(200, 300, 75)
    circle(300, 300, 75)

    if hovering[0]:
        fill(20, 174, 234) if hover_counts[0] <= 5 else fill(random(255), random(255), random(255))
        circle(100, 200, 75)

    if hovering[1]:
        fill(163, 31, 163) if hover_counts[1] <= 5 else fill(random(255), random(255), random(255))
        circle(100, 300, 75)
        circle(300, 300, 75)

    if hovering[2]:
        fill(0) if hover_counts[2] <= 5 else fill(random(255), random(255), random(255))
        circle(300, 200, 75)
        circle(200, 300, 75)

    if hovering[3]:
        fill(255, 0, 0) if hover_counts[3] <= 5 else fill(random(255), random(255), random(255))
        circle(100, 200, 75)
        circle(200, 200, 75)
        circle(300, 200, 75)

    if hovering[4]:
        fill(0, 255, 0) if hover_counts[4] <= 5 else fill(random(255), random(255), random(255))
        circle(100, 200, 75)

    if hovering[5]:
        fill(255, 166, 0) if hover_counts[5] <= 5 else fill(random(255), random(255), random(255))
        circle(100, 300, 75)
        
    prev_hovering = hovering.copy()


def collidePointCircle(pointX, pointY, circX, circY, diameter):
    distance = dist(pointX, pointY, circX, circY)
    return distance <= diameter / 2
