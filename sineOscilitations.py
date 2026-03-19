angle = 15
num_circles = 12  
rotation = 0
bounce_direction = 1  
bounce_amount = 0

diag_x = 0
diag_y = 0

horiz_x = 0
vert_y = 0

def setup():
    size(510, 350)

def draw():
    global angle, rotation, bounce_amount, bounce_direction
    global diag_x, diag_y, horiz_x, vert_y
    
    background(20, 20, 30, 50)  
    
    push_matrix()
    translate(width / 2, height / 2) 
    rotate(radians(rotation))  
    
    for i in range(num_circles):
        theta = remap(i, 0, num_circles, 0, TWO_PI)
        x = cos(theta) * (100 + bounce_amount)  
        y = sin(theta) * (100 + bounce_amount)
        
        sin_value = sin(radians(angle + (i * 30)))
        circle_size = remap(sin_value, -1, 1, 30, 90)
        r = remap(sin_value, -1, 1, 50, 255)
        g = remap(cos(radians(angle + i*20)), -1, 1, 50, 255)
        b = remap(sin(radians(angle + i*40)), -1, 1, 50, 255)
        
        fill(r, g, b, 180)
        no_stroke()
        ellipse(x, y, circle_size, circle_size)
    
    pop_matrix()
    
    diag_x += 2
    diag_y += 1.5
    
    if diag_x > width:
        diag_x = 0
    if diag_y > height:
        diag_y = 0
    
    fill(255, 150, 200, 180)
    rect(diag_x, diag_y, 20, 20)
    rect(width - diag_x, height - diag_y, 15, 15)
    
    horiz_x += 3
    if horiz_x > width:
        horiz_x = 0
    
    fill(100, 200, 255, 150)
    rect(horiz_x, 50, 60, 10)
    rect(width - horiz_x, 100, 40, 8)
    
    vert_y += 2
    if vert_y > height or vert_y < 0:
        vert_y = 0
    
    fill(200, 255, 120, 180)
    ellipse(80, vert_y, 20, 20)
    ellipse(width - 80, height - vert_y, 25, 25)
    
    angle += 2 
    rotation += 0.5
    
    if angle >= 360:
        angle = 0
        
    if rotation >= 360:
        rotation = 0
        
    if frame_count % 240 == 0:
        bounce()
        bounce()
        bounce()

def bounce():
    global bounce_direction, bounce_amount
    bounce_amount += 20 * bounce_direction
    if bounce_amount > 50 or bounce_amount < 0:
        bounce_direction *= -1