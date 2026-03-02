from PIL import Image
import random

image_files = [f"meme{i}.jpg" for i in range(1, 21)]

phrases = [
    "When the WiFi stops working...",
    "Me pretending to understand math",
    "That moment before the teacher calls on you",
    "When you realize it's Monday tomorrow",
    "I said 5 more minutes... 3 hours ago",
    "The feeling when knee surgery is tomorrow",
    "Average school day:",
    "How bro looks at me before installing \n a virus on my computer",
    "When you finally realize it's Monday.",
    "That feeling when you finish a series and don't know what to do with your life.",
    "Me: I'll be productive today. Also me: *scrolls for 3 hours*",
    "When you’re too tired to function but still have 5 more tasks to do.",
    "When the Wi-Fi goes down for 5 minutes and you start panicking.",
    "When you’re trying to act normal but your brain is screaming for help.",
    "How I think I look vs. How I actually look.",
    "When the teacher calls on you and you haven't been paying attention.",
    "That moment when you realize you’ve been singing the wrong lyrics for years.",
    "Me pretending to listen while thinking about food.",
    "When you try to be healthy but pizza calls your name.",
    "Me: I’m going to bed early tonight. Also me: *stays up until 3 AM*",
    "When you see someone you know, but you don’t know if they saw you first.",
    "That moment when you find a snack you forgot about.",
    "When you find a new show and watch it in one sitting.",
    "Me on my way to make the worst decision of my life.",
    "When your pet looks at you like you're crazy for no reason.",
    "When you finally get the joke after 10 minutes of silence.",
    "Me trying to act like I’m not embarrassed after a small mistake.",
    "When you successfully avoid adulting for just one more day.",
]

font_sizes = [25, 30, 35, 40]
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
    reroll_meme()

def draw():
    background(0) 
    image(meme["py5_image"], 0, 0, width, height)
    text_size(meme["font_size"])
    fill(*meme["font_color"])
    text(meme["phrase"], 375, 100)

    fill(0, 255, 0) 
    rect(button_x, button_y, button_w, button_h)
    fill(0, 0, 0) 
    text_align(CENTER, CENTER)
    text_size(30)
    text("Reroll Meme", button_x + button_w / 2, button_y + button_h / 2)

def reroll_meme():
    meme["image_file"] = random.choice(image_files)
    meme["phrase"] = random.choice(phrases)
    meme["font_size"] = random.choice(font_sizes)
    meme["font_color"] = random.choice(font_colors)
    meme["py5_image"] = load_image(meme["image_file"])

def mouse_pressed():
    if (button_x < mouse_x < button_x + button_w and
        button_y < mouse_y < button_y + button_h):
        reroll_meme()
