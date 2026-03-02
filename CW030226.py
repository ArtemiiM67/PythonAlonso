circ1 = {
    "x":30,
    "xSpeed":5,
}

circ2 = {
    "y": 30,
    "ySpeed":5,
}

circ3 = {
    "x": 30,
    "y": 30,
    "xSpeed":5,
    "ySpeed":5,
}

circ4 = {
    "x": 100,
    "y": 100,
    "xSpeed":5,
    "ySpeed":5,
}

def setup():
    size(800,600)
    
x = 1
def draw():
    background(220)
    global x
    fill(200)
    stroke_weight(2)
    stroke(0)
    
    circle(circ1['x'], 250, 30)
    if circ1['x'] >= width:
        circ1['x'] = 0
        
    circ1['x'] += circ1['xSpeed']
    
    circle(30, circ2['y'], 30)
    if circ2['y'] >= height:
        circ2['y'] = 0
        
    circ2['y'] += circ2['ySpeed']
    
    circle(circ3['x'], circ3['y'], 30)
    if circ3['x'] >= width:
        circ3['x'] = 100 
    if circ3['y'] >= height:
        circ3['y'] = 100
        
    circ3['x'] += circ3['xSpeed']
    circ3['y'] += circ3['ySpeed']
    
    
    circle(circ4['x'], circ4['y'], 30)
    if circ4['x'] >= width:
        circ4['x'] = 0 
    if circ4['y'] >= height:
        circ4['y'] = 0
        
    circ4['x'] += circ4['xSpeed'] * -1 ** random(3) + 12 * cos(random(90))
    circ4['y'] += circ4['ySpeed'] * -1 ** random(3) + 12 * cos(random(90))
    
    