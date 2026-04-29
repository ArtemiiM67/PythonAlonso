from PIL import Image
import numpy as np

pixel_list = []
img_width, img_height = 0, 0
img = Image.open("alonso1.jpg")
img_width, img_height = img.size
img = img.convert("RGB")
threshold = 1

def setup():
    size(img_width, img_height)
    image_mode(CENTER)
    
    pixels1 = img.load()
    for y in range(img_height):
        pixel_row = []
        for x in range(img_width):
            r, g, b = pixels1[x, y]
            pixel_row.append((r, g, b))
        pixel_list.append(pixel_row)
        
    background(220)

def draw():   
    if is_mouse_pressed:
        background(220)
        
        img_w = len(pixel_list[0])
        img_h = len(pixel_list)

        load_pixels()

        for y in range(img_h - 1):  
            for x in range(img_w - 1):
                r, g, b = pixel_list[y][x]
                brightness1 = (r + g + b) / 3
            
                r_r, g_r, b_r = pixel_list[y][x + 1]
                brightness_right = (r_r + g_r + b_r) / 3
                
                r_b, g_b, b_b = pixel_list[y + 1][x]
                brightness_below = (r_b + g_b + b_b) / 3
                
                diff_right = abs(brightness1 - brightness_right)
                diff_below = abs(brightness1 - brightness_below)
                
                if diff_right > threshold and diff_below > threshold:
                    c = color(159, 21, 21)
                else:
                    c = color(0)

                index = x + y * width
                pixels[index] = c

        update_pixels()  
