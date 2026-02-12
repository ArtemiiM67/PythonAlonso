brush = {
    "stroke": 5,
    "color1": 0,
    "color2": 0,
    "color3": 0,
    "eraser": False
}

def setup():
    size(800, 800)
    background(255)



def draw():
    draw_ui()
    draw_brush()


def draw_ui():
    no_stroke()
    fill(218,177,218)
    rect(0, 0, width, 175)

    fill(0)
    text_size(22)
    text("Artemii's Paint App", 315, 775)

    fill(200)
    rect(20, 20, 40, 30)   # +
    rect(70, 20, 40, 30)   # -
    rect(120, 20, 80, 30)  # CLEAR
    rect(210, 20, 80, 30)  # ERASER
    rect(300, 20, 80, 30)  # RANDOM
    rect(390, 20, 80, 30)  # SAVE

    fill(0)
    text("+", 35, 40)
    text("-", 85, 40)
    text("CLEAR", 130, 40)
    text("ERASER", 215, 40)
    text("RANDOM", 300, 40)
    text("SAVE", 410, 40)

    text("Size: " + str(brush["stroke"]), 500, 40)

    if is_mouse_pressed:
        # +
        if 20 < mouse_x < 60 and 20 < mouse_y < 50:
            brush["stroke"] += 1

        if 70 < mouse_x < 110 and 20 < mouse_y < 50:
            if brush["stroke"] > 1:
                brush["stroke"] -= 1

        if 120 < mouse_x < 200 and 20 < mouse_y < 50:
            background(255)

        if 210 < mouse_x < 290 and 20 < mouse_y < 50:
            brush["eraser"] = not brush["eraser"]

        if 300 < mouse_x < 380 and 20 < mouse_y < 50:
            brush["color1"] = random(255)
            brush["color2"] = random(255)
            brush["color3"] = random(255)
            brush["eraser"] = False

        if 390 < mouse_x < 470 and 20 < mouse_y < 50:
            save_frame("my_drawing.png")

    cols = 16
    rows = 2
    for row in range(rows):
        for col in range(cols):
            x = 20 + col * 45
            y = 70 + row * 45

            r = int(255 * (col / (cols - 1)))
            g = int(255 * (row / (rows - 1)))
            b = int(255 * (1 - col / (cols - 1)))

            fill(r, g, b)
            rect(x, y, 40, 40)

            if (x < mouse_x < x + 40 and
                y < mouse_y < y + 40 and
                is_mouse_pressed):
                brush["color1"] = r
                brush["color2"] = g
                brush["color3"] = b
                brush["eraser"] = False

    fill(brush["color1"], brush["color2"], brush["color3"])
    rect(750, 20, 30, 30)

    fill(0)
    text("Preview:", 600, 40)
    fill(brush["color1"], brush["color2"], brush["color3"])
    circle(700, 35, brush["stroke"] * 2)


def draw_brush():
    if mouse_y < 150:
        return

    if is_mouse_pressed:
        if brush["eraser"]:
            stroke(255)
            stroke_weight(brush["stroke"] * 2)
        else:
            stroke(brush["color1"], brush["color2"], brush["color3"])
            stroke_weight(brush["stroke"])

        line(pmouse_x, pmouse_y, mouse_x, mouse_y)
