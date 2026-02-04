def setup():
    size(800, 800)
    
def draw():
    circW = random(50,200)
    ellipse(200,200, circW, 100)
    circle(random(800), random(800), circW)
    background(220)
    color_mode(HSB, 360, 100, 100)
    d = 60
    dp5 = d + 5
    for x in range(d+1,width-dp5, dp5):
        for y in range(d+1,height-dp5, dp5):
            fill(random(360), 100, 100)
            circle(x,y,d)
    color_mode(RGB, 255, 255, 255)
    

    sat = 10
    for x in range(d+1,width-dp5*4,dp5):
        for y in range(d+1,height-dp5,dp5):
            fill(360,sat,100)
            circle(x,y,d)
            sat += 10
    bri = 10

    for x in range(d+1+dp5*3,width-dp5,dp5):
        for y in range(d+1,height-dp5,dp5):
            fill(360,100,bri)
            circle(x,y,d)
            bri += 10

    color_mode(RGB,255,255,255)