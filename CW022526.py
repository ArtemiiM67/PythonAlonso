randomColors = []
randomChoice = None
randomX, randomY = 0, 0
randomIncr = 0
randomSize = 1
StarMap = []

def setup():
    size(400, 600)
    global randomColors, randomChoice, randomX, randomY, randomIncr, randomSize, StarMap
    randomColors = [ color(218, 205, 205), color(229, 221, 221), color(243, 230, 230), color(236, 225, 225), color(242, 242, 242), color(255, 255, 255) ]
    randomChoice = int(random(6))
    
    for _ in range(1000):
        star = {
            'xcor': random(width),
            'ycor': random(height),
            'color': randomColors[randomChoice],
            'opacity': random(100, 150),
            'stroke_weight': random(1, 3),
            'stroke': color(random(210, 255), random(210, 255), random(210, 255)),
        }
        StarMap.append(star)

def draw():
    background(34, 34, 86) 
    for star in StarMap:
        star['opacity'] = 100 + 50 * sin(radians(frame_count * 2)) 
        fill(star['color'], star['opacity'])
        stroke(star['stroke'])
        stroke_weight(star['stroke_weight'])
        circle(star['xcor'], star['ycor'], random(5))
