cols = 20
rows = 10
base_size = 30
spacing = 40
design_mode = 0 

def setup():
    size(800, 450)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)

def draw():
    background(15, 20, 40)
    draw_pattern()
    draw_buttons()


def draw_pattern():
    
    for r in range(rows):
        for c in range(cols):
            
            x = c * spacing + spacing / 2
            y = r * spacing + spacing / 2
            
            red_val = (c * 20) % 255
            blue_val = (r * 25) % 255
            green_val = (c * r * 5) % 255
            
            fill(red_val, green_val, blue_val)
            no_stroke()
            
            size_offset = (r + c) * 2
            
            if design_mode == 0:
                ellipse(x, y, base_size + size_offset, base_size + size_offset)
            
            elif design_mode == 1:
                rect(x, y, base_size + size_offset, base_size + size_offset)
            
            elif design_mode == 2:
                push_matrix()
                translate(x, y)
                rotate(PI/4)
                rect(0, 0, base_size + size_offset, base_size + size_offset)
                pop_matrix()

def draw_buttons():
    draw_button(100, 420, 160, 30, "More Shapes")
    draw_button(300, 420, 160, 30, "Change Spacing")
    draw_button(500, 420, 160, 30, "Change Style")


def draw_button(x, y, w, h, label):
    fill(50)
    rect(x, y, w, h)
    fill(255)
    text(label, x, y)

def mouse_pressed():
    global cols, rows, spacing, design_mode
    
    if 20 < mouse_y < 450 and 405 < mouse_y < 435:
        pass
    
    if 20 < mouse_y < 435:
        if 20 < mouse_x < 180:
            cols += 2
            rows += 1

        elif 220 < mouse_x < 380:
            spacing -= 5
            if spacing < 15:
                spacing = 40
    
        elif 420 < mouse_x < 580:
            design_mode = (design_mode + 1) % 3