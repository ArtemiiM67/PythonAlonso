def setup():
    size(800,800)
    color_mode(HSB, 360, 100, 100)
    
def draw():
    background(0)
    translate(width / 2, height / 2)
    
    for i in range(12):
        fill((frame_count+i*30)%360,100,100)
        rotate(PI/6)
        push_matrix()
        translate(20,0)
        ellipse(50,50,50*sin(frame_count / 60),50)
        pop_matrix()