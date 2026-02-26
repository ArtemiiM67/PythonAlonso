from PIL import image

im = Image.open('image/CuteDog.jpg')

def setup():
    size(300,300)
    
def draw():
    #image(name, x, y, width, height)
    image(im, 10, 10, 250, 250)