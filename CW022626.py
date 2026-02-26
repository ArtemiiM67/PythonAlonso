import random
from PIL import Image

image_files = [
    "meme1.jpg",
    "meme2.jpg",
    "meme3.jpg",
    "meme4.jpg",
    "meme5.jpg"
]

phrases = [
    "When the WiFi stops working...",
    "Me pretending to understand math",
    "That moment before the teacher calls on you",
    "When you realize it's Monday tomorrow",
    "I said 5 more minutes... 3 hours ago"
]

font_sizes = [20, 30, 40, 50, 60]

font_colors = [
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0)
]

meme = {
    "image_file": "",
    "phrase": "",
    "font_size": 30,
    "font_color": (255, 255, 255),
    "py5_image": None
}

button_x = 250
button_y = 520
button_w = 200
button_h = 50


def setup():
    size(700, 600)
    #reroll_meme()


#def draw():
#BODY


#def reroll_meme():
#BODY


def mouse_pressed():
    if (button_x < mouse_x < button_x + button_w and
        button_y < mouse_y < button_y + button_h):
        reroll_meme()