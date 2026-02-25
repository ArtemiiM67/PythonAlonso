randomColors = []
randomChoice = None

def setup():
    size(400, 600)
    global randomColors, randomChoice
    randomColors = [ color(255,0,0), color(0,255,0), color(0,0,255) ]
    randomChoice = int(random(3))
    MyList = [
        {
            'foo':12,
            'ba':14,
        },
        {
            'moo':52,
            'ch':641,
        },
        {
            'doo':52,
            'tan':84,
        },
    ]
    
def draw():
    background(220)
    fill(randomColors[randomChoice])
    circle(200,200,100)