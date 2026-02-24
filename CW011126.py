brush = {
    "stroke": 5,
    "color1": 0,
    "color2": 0,
    "color3": 0,
    "eraser": False,
    "tool": "pencil"
}

start_x = 0
start_y = 0


def setup():
    size(1280, 720)
    background(255)


def draw():
    draw_ui()
    draw_brush()


# KEYBOARD CONTROL
def key_pressed():
    global brush

    if key == '=':
        brush["stroke"] += 1

    if key == '-' and brush["stroke"] > 1:
        brush["stroke"] -= 1

    if key == 'c' or key == 'C':
        background(255)

    if key == 'e' or key == 'E':
        brush["eraser"] = True
        brush["tool"] = "pencil"

    if key == 'r' or key == 'R':
        brush["color1"] = random(255)
        brush["color2"] = random(255)
        brush["color3"] = random(255)
        brush["eraser"] = False

    if key == 's' or key == 'S':
        save_frame("my_drawing.png")

    if key == '1':
        brush["tool"] = "pencil"
        brush["eraser"] = False

    if key == '2':
        brush["tool"] = "line"
        brush["eraser"] = False

    if key == '3':
        brush["tool"] = "rect"
        brush["eraser"] = False

    if key == '4':
        brush["tool"] = "circle"
        brush["eraser"] = False

    if key == '5':
        brush["tool"] = "triangle"
        brush["eraser"] = False


def draw_ui():
    stroke(0)
    stroke_weight(2)
    fill(191, 172, 172)
    rect(0, 0, width, 158)
    rect(0, 158, 158, height)

    fill(0)
    text_size(20)
    text("Artemii's Paint App", 500, 698)

    fill(200)
    rect(32, 18, 64, 27)     
    rect(112, 18, 64, 27)    
    rect(192, 18, 128, 27)   
    rect(336, 18, 128, 27)   
    rect(480, 18, 128, 27)   
    rect(624, 18, 128, 27)   

    fill(0)
    text("+", 58, 37)
    text("-", 138, 37)
    text("CLEAR", 225, 37)  
    text("ERASER", 360, 37)
    text("RANDOM", 490, 37)
    text("SAVE", 658, 37)
    
    text_size(15)
    text("(↑)", 75, 40)
    text("(↓)", 155, 40)
    text("(c)", 295, 40)  
    text("(e)", 440, 40)   
    text("(r)", 585, 40)   
    text("(s)", 725, 40)
    text_size(20)

    text_size(13)
    text("(=)", 82, 44)
    text("(-)", 164, 44)
    text("(C)", 300, 44)
    text("(E)", 445, 44)
    text("(R)", 585, 44)
    text("(S)", 735, 44)

    text_size(20)
    text("Size: " + str(brush["stroke"]), 800, 36)

    if is_mouse_pressed and mouse_button == LEFT:

        if 32 < mouse_x < 96 and 18 < mouse_y < 45:
            if brush["stroke"] < 100:
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
<<<<<<< HEAD
    draw_rgb_controls()
=======
    text_size(15)
    text("(1)", 120, 200)
    text("(2)", 120, 300)
    text("(3)", 120, 400)
    text("(4)", 120, 450)
    text("(5)", 120, 550)
    text_size(20)

>>>>>>> e5964c256ba7e7a8219d8f0c57c21321825958a1

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

def draw_rgb_controls():
    x_start = 20    
    y_start = 620      
    spacing = 30

    labels = ["R", "G", "B"]
    keys = ["color1", "color2", "color3"]

    fill(0)
    text_size(16)
    text("RGB Manual Colors", x_start, y_start - 20)

    for i in range(3):
        y = y_start + i * spacing

        fill(0)
        text(labels[i] + ":", x_start, y)

        fill(200)
        rect(x_start + 40, y - 15, 25, 20)
        fill(0)
        text("-", x_start + 48, y)

        fill(200)
        rect(x_start + 100, y - 15, 25, 20)
        fill(0)
        text("+", x_start + 108, y)

        fill(0)
        text(str(int(brush[keys[i]])), x_start + 75, y)

        if is_mouse_pressed and mouse_button == LEFT:
            if (x_start + 40 < mouse_x < x_start + 65 and
                y - 15 < mouse_y < y + 5):
                brush[keys[i]] = max(0, brush[keys[i]] - 1)

            if (x_start + 100 < mouse_x < x_start + 125 and
                y - 15 < mouse_y < y + 5):
                brush[keys[i]] = min(255, brush[keys[i]] + 1)

def draw_left_panel():
    fill(220)
    y = 180
    h = 60

    tools = ["pencil", "line", "rect", "circle", "triangle"]

    for i in range(len(tools)):
        tool = tools[i]

        if brush["tool"] == tool:
            fill(180)
        else:
            fill(220)

        rect(20, y, 118, h)

        fill(0)
        text_size(18)
        text(tool.upper(), 35, y + 30)

        text_size(12)
        text("(" + str(i + 1) + ")", 35, y + 50)

        text_size(20)

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
<<<<<<< HEAD

        begin_shape()
        points1 = int(random(5, 12))

=======
        begin_shape()
        points1 = int(random(5, 12))
>>>>>>> e5964c256ba7e7a8219d8f0c57c21321825958a1
        for i in range(points1):
            angle = TWO_PI / points1 * i
            radius = random(10, 60)
            x = cos(angle) * radius + random(-10, 10)
            y = sin(angle) * radius + random(-10, 10)
            vertex(x, y)

        end_shape(CLOSE)
<<<<<<< HEAD
        pop_matrix()
=======
        pop_matrix()


def key_pressed():
    if key == CODED:
        if key_code == UP:
            if brush["stroke"] < 100:
                brush["stroke"] += 1
        elif key_code == DOWN:
            if brush["stroke"] > 1:
                brush["stroke"] -= 1
    elif key == 'c': 
        background(255)
    elif key == 'e':  
        brush["eraser"] = True
        brush["tool"] = "pencil"
    elif key == 'r': 
        brush["color1"] = random(255)
        brush["color2"] = random(255)
        brush["color3"] = random(255)
        brush["eraser"] = False
    elif key == 's': 
        save_frame("my_drawing.png")
    elif key == '1': 
        brush["tool"] = "pencil"
        brush["eraser"] = False
    elif key == '2': 
        brush["tool"] = "line"
        brush["eraser"] = False
    elif key == '3': 
        brush["tool"] = "rect"
        brush["eraser"] = False
    elif key == '4':  
        brush["tool"] = "circle"
        brush["eraser"] = False
    elif key == '5': 
        brush["tool"] = "triangle"
        brush["eraser"] = False
>>>>>>> e5964c256ba7e7a8219d8f0c57c21321825958a1
