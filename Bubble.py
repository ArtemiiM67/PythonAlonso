from BubbleClass import Bubble

bubblePopped = 0
bubbles = []
flashing = False
flashTime = 0
imageFlashing = None

def setup():
    size(1000, 1000)
    global bubbles, imageFlashing
    imageFlashing = load_image("image.png") 
    
    for a in range(50):
        bubbles.append(Bubble())

def draw():
    global bubblePopped, flashing, flashTime

    background(255)
    text_size(20)
    fill(0)
    text("Bubbles popped: ", 415, 50)
    text(str(bubblePopped), 600, 50)
    
    if bubblePopped >= 10 and not flashing:
        flashing = True
        flashTime = frame_count 
    
    if flashing:
        if (frame_count - flashTime) % 60 < 30:  
            image(imageFlashing, width/2 - imageFlashing.width/2, height/2 - imageFlashing.height/2)
        
    for b in bubbles:
        b.move()
        b.display()
        
        if is_mouse_pressed:
            distance = dist(mouse_x, mouse_y, b.x, b.y)
            if distance < b.size / 2 and not b.exploded:
                b.explode()
                bubblePopped += 1

