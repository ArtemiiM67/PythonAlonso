brush = {
    "stroke": 5,
    "color1": 0,
    "color2": 0,
    "color3": 0,
    "eraser": False,
    "tool": "pencil"
}

def setup():
    size(1280, 720)
    background(255)


def draw():
    draw_ui()
    draw_brush()


def draw_ui():
    stroke(0)
    stroke_weight(2)
    fill(191, 172, 172)
    rect(0, 0, width, 158)           # top bar
    rect(0, 158, 158, height)        # left panel

    fill(0)
    text_size(20)
    text("Artemii's Paint App", 500, 698)

    fill(200)
    rect(32, 18, 64, 27)     # +
    rect(112, 18, 64, 27)    # -
    rect(192, 18, 128, 27)   # CLEAR
    rect(336, 18, 128, 27)   # ERASER
    rect(480, 18, 128, 27)   # RANDOM
    rect(624, 18, 128, 27)   # SAVE

    fill(0)
    text("+", 58, 37)
    text("-", 138, 37)
    text("CLEAR", 225, 37)
    text("ERASER", 360, 37)
    text("RANDOM", 490, 37)
    text("SAVE", 658, 37)

    text("Size: " + str(brush["stroke"]), 800, 36)

    if is_mouse_pressed and mouse_button == LEFT:

        if 32 < mouse_x < 96 and 18 < mouse_y < 45:
            brush["stroke"] += 1

        if 112 < mouse_x < 176 and 18 < mouse_y < 45:
            if brush["stroke"] > 1:
                brush["stroke"] -= 1

        if 192 < mouse_x < 320 and 18 < mouse_y < 45:
            background(255)

        if 336 < mouse_x < 464 and 18 < mouse_y < 45:
            brush["eraser"] = True
            brush["tool"] = "pencil"

        if 480 < mouse_x < 608 and 18 < mouse_y < 45:
            brush["color1"] = random(255)
            brush["color2"] = random(255)
            brush["color3"] = random(255)
            brush["eraser"] = False

        if 624 < mouse_x < 752 and 18 < mouse_y < 45:
            save_frame("my_drawing.png")

    draw_color_palette()
    draw_left_panel()


def draw_color_palette():
    cols = 16
    rows = 2
    for row in range(rows):
        for col in range(cols):
            x = 32 + col * 72
            y = 63 + row * 40

            r = int(255 * (col / (cols - 1)))
            g = int(255 * (row / (rows - 1)))
            b = int(255 * (1 - col / (cols - 1)))

            fill(r, g, b)
            rect(x, y, 64, 36)

            if (x < mouse_x < x + 64 and
                y < mouse_y < y + 36 and
                is_mouse_pressed):

                brush["color1"] = r
                brush["color2"] = g
                brush["color3"] = b
                brush["eraser"] = False

    fill(brush["color1"], brush["color2"], brush["color3"])
    rect(1200, 18, 48, 27)

    fill(0)
    text("Preview:", 960, 36)
    fill(brush["color1"], brush["color2"], brush["color3"])
    circle(1120, 31, brush["stroke"] * 2)


def draw_left_panel():
    fill(220)
    y = 180
    h = 60

    tools = ["pencil", "line", "rect", "circle", "triangle"]

    for tool in tools:
        if brush["tool"] == tool:
            fill(180)
        else:
            fill(220)

        rect(20, y, 118, h)

        fill(0)
        text(tool.upper(), 35, y + 35)

        if (20 < mouse_x < 138 and
            y < mouse_y < y + h and
            is_mouse_pressed):
            brush["tool"] = tool
            brush["eraser"] = False

        y += 80

    update_cursor()


def update_cursor():
    if brush["tool"] == "pencil":
        cursor(CROSS)
    elif brush["tool"] == "line":
        cursor(HAND)
    elif brush["tool"] == "rect":
        cursor(MOVE)
    elif brush["tool"] == "circle":
        cursor(TEXT)
    elif brush["tool"] == "triangle":
        cursor(WAIT)



start_x = 0
start_y = 0


def draw_brush():
    global start_x, start_y

    if mouse_y < 158 or mouse_x < 158:
        return

    if is_mouse_pressed and mouse_button == LEFT:

        if frame_count % 2 == 0:
            start_x = mouse_x
            start_y = mouse_y

        if brush["tool"] == "pencil":
            if brush["eraser"]:
                stroke(255)
                stroke_weight(brush["stroke"] * 2)
            else:
                stroke(brush["color1"], brush["color2"], brush["color3"])
                stroke_weight(brush["stroke"])

            line(pmouse_x, pmouse_y, mouse_x, mouse_y)

        elif brush["tool"] == "line":
            stroke(brush["color1"], brush["color2"], brush["color3"])
            stroke_weight(brush["stroke"])
            line(start_x, start_y, mouse_x, mouse_y)

        elif brush["tool"] == "rect":
            no_fill()
            stroke(brush["color1"], brush["color2"], brush["color3"])
            stroke_weight(brush["stroke"])
            rect(start_x, start_y,
                 mouse_x - start_x,
                 mouse_y - start_y)

        elif brush["tool"] == "circle":
            no_fill()
            stroke(brush["color1"], brush["color2"], brush["color3"])
            stroke_weight(brush["stroke"])
            ellipse(start_x, start_y,
                    mouse_x - start_x,
                    mouse_y - start_y)

        elif brush["tool"] == "triangle":
            no_fill()
            stroke(brush["color1"], brush["color2"], brush["color3"])
            stroke_weight(brush["stroke"])
            triangle(start_x, start_y,
                     mouse_x, mouse_y,
                     start_x, mouse_y)
            
    if is_mouse_pressed and mouse_button == RIGHT:
        r = random(255)
        g = random(255)
        b = random(255)
        stroke(r, g, b)
        fill(random(255), random(255), random(255))
        stroke_weight(random(1, 6))
        push_matrix()
        translate(mouse_x, mouse_y)
        rotate(random(TWO_PI))
        begin_shape() points1 = int(random(5, 12))
        for i in range(points1):
            angle = TWO_PI / points1 * i
            radius = random(10, 60)
            x = cos(angle) * radius + random(-10, 10)
            y = sin(angle) * radius + random(-10, 10)
            vertex(x, y)
        end_shape(CLOSE)
        pop_matrix()
