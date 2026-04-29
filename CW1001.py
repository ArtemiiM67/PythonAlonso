from PIL import Image
import numpy as np

Img = Image.open('alonso.jpg').convert("RGBA") 

def setup():
    size(200, 800)
    image(Img, 0, 0, width, height)
    load_np_pixels()
    global original
    original = np_pixels.copy()
    
    np_pixels[:, :, 3] = 255
    update_np_pixels()

def draw():
    temp = remap(mouse_x, 0, width, -50, 50)
    hue_shift = remap(mouse_y, 0, height, -50, 50)

    np_pixels[:, :, 0] = constrain(original[:, :, 0] + temp + hue_shift, 0, 255)
    np_pixels[:, :, 1] = constrain(original[:, :, 1] + temp, 0, 255)
    np_pixels[:, :, 2] = constrain(original[:, :, 2] + temp - hue_shift, 0, 255)

    h_mid = height // 2
    w_mid = width // 2
    
    np_pixels[0:h_mid, 0:w_mid, 0] = constrain(original[0:h_mid, 0:w_mid, 0] + 50, 0, 255)
    np_pixels[0:h_mid, w_mid:, 1] = constrain(original[0:h_mid, w_mid:, 1] + 30, 0, 255)
    np_pixels[h_mid:, 0:w_mid, 2] = constrain(original[h_mid:, 0:w_mid, 2] + 40, 0, 255)
    np_pixels[h_mid:, w_mid:, 0] = constrain(original[h_mid:, w_mid:, 0] + 60, 0, 255)
    np_pixels[h_mid:, w_mid:, 1] = constrain(original[h_mid:, w_mid:, 1] + 45, 0, 255)
    
    if is_mouse_pressed:
        alpha_value = remap(mouse_x, 0, width, 0, 255) 
        np_pixels[:, :, 3] = alpha_value

    update_np_pixels()