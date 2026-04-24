from PIL import Image

pixel_list = []

def setup():
    size(800, 800)

    img = Image.open("test.jpg")
    img = img.convert("RGBA")
    
    img_width, img_height = img.size

    print(f"IMAGE HEIGHT: {img_height}")
    print(f"IMAGE WIDTH: {img_width}")

    center_x = (width - img_width) // 2
    center_y = (height - img_height) // 2
    
    image(img, center_x, center_y)

    pixels1 = img.load()
    for y in range(img_height):
        pixel_row = []
        for x in range(img_width):
            pixel_color = pixels1[x, y]
            red1, green1, blue1, alpha1 = pixel_color
            pixel_row.append((red1, green1, blue1))
        pixel_list.append(pixel_row)

    background(220)
    
def draw():
    if 0 <= mouse_x < len(pixel_list) and 0 <= mouse_y < len(pixel_list[0]):
        pixel_color = pixel_list[mouse_x][mouse_y]
        fill(pixel_color[0], pixel_color[1], pixel_color[2])
        no_stroke()
        circle(mouse_x, mouse_y, 20)