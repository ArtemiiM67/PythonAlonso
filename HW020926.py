def setup():
    size(600, 600)
    frame_rate(30)
    background(30)
    
    global brush
    brush = {
        "x": width/2,
        "y": height/2,
        "size": 50,
        "angle": 0,
        "color": color(255, 100, 150, 150)
    }

def draw():
    fill(0, 20)
    rect(0, 0, width, height)
    
    brush["angle"] += 0.05
    brush["x"] = width/2 + cos(brush["angle"])*200
    brush["y"] = height/2 + sin(brush["angle"])*200
    brush["size"] = 30 + 20*sin(brush["angle"]*2)
    
    r = int(150 + 100*sin(brush["angle"]))
    g = int(100 + 100*cos(brush["angle"]/2))
    b_val = int(200 + 55*sin(brush["angle"]/3))
    brush["color"] = color(r, g, b_val, 120)

    push_matrix()
    translate(brush["x"], brush["y"])
    rotate(brush["angle"]*2)
    fill(brush["color"])
    no_stroke()
    begin_shape()
    for i in range(5):
        a = i*TWO_PI/5
        vertex(cos(a)*brush["size"], sin(a)*brush["size"])
        a += PI/5
        vertex(cos(a)*brush["size"]/2, sin(a)*brush["size"]/2)
    end_shape(CLOSE)
    pop_matrix()
    
    stroke(brush["color"])
    stroke_weight(2)
    if brush["x"] < width/2:
        line(brush["x"], brush["y"], brush["x"]+random(-50,50), brush["y"]+random(-50,50))
    else:
        line(brush["x"], brush["y"], width/2 + cos(frame_count*0.1)*100, height/2 + sin(frame_count*0.1)*100)
