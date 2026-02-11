brush = {
    "mode": RGB,
    "stroke": 5,
    "xcor": 0,
    "ycor": 0,
    "color1": 0,
    "color2": 0,
    "color3": 0,
    "hue": 0,
    "saturation": 100,
    "brightness": 100,
}

def setup():
    size(800, 800)
    brush["xcor"] = mouse_x
    brush["ycor"] = mouse_y

def draw():
    background(255)
    
    fill(0)
    text_size(25)
    text("Choose your color", 310, 30)
    
    for x in range(12): 
        r = int(255 * (x / 11)) 
        g = int(255 * (1 - abs(x / 6 - 1)))  
        b = int(255 * (1 - abs(x / 9 - 1)))  

        fill(r, g, b)
        rect(50 + x * 60, 60, 50, 50)
        
        if mouse_x > 50 + x * 60 and mouse_x < 50 + x * 60 + 50 and mouse_y > 60 and mouse_y < 110:
            brush["color1"], brush["color2"], brush["color3"] = r, g, b
            fill(brush["color1"], brush["color2"], brush["color3"])
            ellipse(brush["xcor"], brush["ycor"], 40, 40)
    
    brush["xcor"] = mouse_x
    brush["ycor"] = mouse_y
    stroke(brush["stroke"])
    stroke_weight(brush["stroke"])
    fill(brush["color1"], brush["color2"], brush["color3"])
    ellipse(brush["xcor"], brush["ycor"], 40, 40)
    
    if is_mouse_pressed and mouse_button == LEFT:
        line(mouse_
