def setup():
    size(800, 800)
    color_mode(HSB, 360, 100, 100)
    no_stroke()

def draw():
    background(0)
    translate(width / 2, height / 2)
    
    n = 12
    t = frame_count * 0.05
    
    for i in range(n):
        base_angle = TWO_PI / n * i
        
        push_matrix()
        
        rotate(t)
        
        rotate(base_angle)
        translate(200, 0)
        
        rotate(PI)   
        
        rotate(-t)
        
        hue1 = (i * 360 / n + frame_count * 2) % 360
        fill(hue1, 100, 100)
    
        w = 40 + 20 * sin(t * 2 + i)
        h = 60 + 20 * cos(t * 2 + i)
        
        ellipse(0, 0, w, h)
        
        pop_matrix()