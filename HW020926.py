def setup():
    size(600, 600)
    frame_rate(30)
    background(30)
    
    global brush
    brush = {
        "x": width / 2,
        "y": height / 2,
        "size": 50,
        "color": color(255, 100, 150)
    }

def draw():
    background(30)
    
    brush["x"] += random(-5, 5)
    brush["y"] += random(-5, 5)
    brush["size"] = 50 + 10 * sin(frame_count * 0.1)
    
    r = int(150 + 100 * sin(frame_count * 0.05))
    g = int(100 + 100 * cos(frame_count * 0.1))
    b = int(200 + 55 * sin(frame_count * 0.03))
    brush["color"] = color(r, g, b)
    
    fill(brush["color"])
    no_stroke()
    ellipse(brush["x"], brush["y"], brush["size"], brush["size"])
