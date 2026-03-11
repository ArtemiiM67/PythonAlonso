from BubbleClass import Bubble

def setup():
    size(1000, 1000)
    global bubbles
    global bubblePopped
    bubblePopped = 0
    bubbles = []
    for a in range(50): 
        bubbles.append(Bubble())

def draw():
    global bubblePopped
    background(255)
    text_size(20)
    fill(0)
    text("Bubbles popped: ", 415, 50)
    text(str(bubblePopped), 600, 50)
    
    for b in bubbles:
        b.move()  
        b.display() 
        
        if is_mouse_pressed:
            distance = dist(mouse_x, mouse_y, b.x, b.y)
            if distance < b.size / 2 and not b.exploded:
                b.explode()
                bubblePopped += 1