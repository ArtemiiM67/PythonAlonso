from PIL import Image

pixel_list = []
img_width, img_height = 0, 0
img = Image.open("test.jpg")
img_width, img_height = img.size
img = img.convert("RGB") 

def setup():
    size(img_width, img_height)
    image_mode(CENTER)
    
    pixels1 = img.load()
    for y in range(img_height):
        pixel_row = []
        for x in range(img_width):
            pixel_color = pixels1[x, y]
            r, g, b = pixel_color
            pixel_row.append((r, g, b))
        pixel_list.append(pixel_row)
        
    background(220)

def draw():   
    if is_mouse_pressed:
        background(220)
        
        img_w = len(pixel_list[0])
        img_h = len(pixel_list)
        mid_x = img_w // 2
        mid_y = img_h // 2
        temp = remap(mouse_x, 0, width, 100, -100)

        for y in range(0, img_h, 2):
            for x in range(0, img_w, 2):  
                r, g, b = pixel_list[y][x]
                if x < mid_x and y < mid_y:
                    r, g, b = r * 1.5, g * 0.7, b * 0.7
                elif x >= mid_x and y < mid_y:
                    r, g, b = r * 0.7, g * 1.5, b * 0.7
                elif x < mid_x and y >= mid_y:
                    r, g, b = r * 0.7, g * 0.7, b * 1.5
                else:
                    r, g, b = r * 1.2, g * 1.2, b * 0.5

                r_final = constrain(int(r + temp), 0, 255)
                g_final = constrain(int(g), 0, 255)
                b_final = constrain(int(b - temp), 0, 255)
                
                fill(r_final, g_final, b_final)  
                no_stroke()
                ellipse(x, y, 2, 2)