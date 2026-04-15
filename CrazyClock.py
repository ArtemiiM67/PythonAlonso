def setup():
    size(800, 800)
    color_mode(HSB, 360, 100, 100, 100)
    background(0)

def draw():
    fill(0, 15)
    no_stroke()
    rect(0, 0, width, height)
    
    hr = hour() % 12
    mn = minute()
    sc = second()
    
    base_hue = remap(hour(), 0, 24, 0, 360)
    
    for i in range(12):
        angle = remap(i, 0, 12, 0, TWO_PI)
        rad = 150
        px = width/2 + cos(angle) * rad
        py = 200 + sin(angle) * (rad * 0.3)
        
        if i < hr:
            fill(base_hue, 80, 100, 80)
            sz = 15 + sin(frame_count * 0.1 + i) * 5
        elif i == hr:
            fill(base_hue, 30, 100, 100)
            sz = 25 + sin(frame_count * 0.2) * 10
        else:
            stroke(base_hue, 20, 40, 30)
            no_fill()
            sz = 5
        
        ellipse(px, py, sz, sz)

    y_min = remap(mn, 0, 60, 250, height - 150)
    no_fill()
    stroke_weight(3)
    stroke(base_hue, 70, 100, 60)
    
    begin_shape()
    for x in range(0, width + 20, 20):
        vibration = (60 - sc) * 0.5
        noise_val = sin(x * 0.02 + frame_count * 0.1) * vibration
        curve_vertex(x, y_min + noise_val)
    end_shape()
    
    fill(base_hue, 90, 100)
    no_stroke()
    ellipse(width/2, y_min, 10, 10)

    spacing = (width - 100) / 60
    for i in range(60):
        x = 50 + i * spacing
        h_sec = 50
        
        if i < sc:
            fill((base_hue + 40) % 360, 80, 90, 70)
            rect(x, height - 80, spacing - 2, -h_sec)
        elif i == sc:
            fill(0, 0, 100, 100)
            rect(x, height - 80, spacing - 2, -(h_sec + sin(frame_count * 0.3) * 20))
        else:
            fill(base_hue, 10, 20, 40)
            rect(x, height - 80, spacing - 2, -5)
            
    stroke((base_hue + 180) % 360, 50, 100, 20)
    stroke_weight(1)
    line(50, y_min, 50, height - 80)
    line(width - 50, y_min, width - 50, height - 80)