def setup():
    size(500, 500)
    rect_mode(CENTER)
    no_stroke()

def draw():
    bgcolor1 = remap(sin(frame_count * 0.01) * width + mouse_x, 0, width, 50, 255)
    bgcolor2 = remap(cos(frame_count * 0.015) * width + mouse_y, 0, width, 50, 255)
    bgcolor3 = remap(sin(frame_count * 0.02 + mouse_x * 0.01) * width, 0, width, 50, 255)
    background(bgcolor1, bgcolor2, bgcolor3)
    
    translate(width / 2, height / 2)
    for i in range(10):
        push_matrix()
        angle = frame_count * 0.05 + i * PI / 5
        rotate(angle)
        scale_factor = 0.5 + 0.5 * sin(frame_count * 0.03 + i)
        scale(scale_factor)
        fill(
            remap(sin(frame_count*0.02 + i), -1, 1, 50, 255),
            remap(cos(frame_count*0.25 + i), -1, 1, 50, 255),
            remap(sin(frame_count*0.03 + i), -1, 1, 50, 255),
            200
        )
        square(0, 0, 100 + i * 30)
        pop_matrix()
    
    for j in range(3):
        push_matrix()
        rotate(-frame_count * 0.03 + j)
        fill(255, 255, 255, 50)
        ellipse(0, 0, 250 + j * 50, 250 + j * 50)
        pop_matrix()