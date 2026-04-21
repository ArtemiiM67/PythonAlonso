import PIL

def setup():
    img = load_image("test.jpg")  
    img.load_pixels() 
    pixel_list = []

    for y in range(img.height):
        pixel_row = []
        for x in range(img.width):
            pixel_color = img.pixels[y * img.width + x]  
            # Convert pixel color from the internal format (assumed to be ARGB) to RGB
            alpha = (pixel_color >> 24) & 0xFF
            red = (pixel_color >> 16) & 0xFF
            green = (pixel_color >> 8) & 0xFF
            blue = pixel_color & 0xFF
            
            # Print in both formats (standard RGBA and x, y, z)
            print(f"Pixel at ({x},{y}): {pixel_color} (RGBA) -> ({red}, {green}, {blue}) (RGB)")
            
            # Append RGB values to the row list
            pixel_row.append((red, green, blue))
        
        pixel_list.append(pixel_row)