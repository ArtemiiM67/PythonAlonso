from PIL import Image, ImageFilter
import numpy as np

Img = Image.open('test.jpg').convert("RGBA") 

def setup():
    size(800, 800)
    image(Img, 0, 0, width, height)
    load_np_pixels()
    global original
    original = np_pixels.copy()
    
current_effect = 0

def key_pressed():
    global current_effect
    if key == '1':
        current_effect = 1
    if key == '2':
        current_effect = 2
    if key == '3':
        current_effect = 3
    if key == '4':
        current_effect = 4
    if key == '5':
        current_effect = 5
    if key == '6':
        current_effect = 6
    if key == '7':
        current_effect = 7
    if key == '8':
        current_effect = 8
    if key == '9':
        current_effect = 9

def draw():
    np_pixels[:, :, :] = original.copy()

    temp = remap(mouse_x, 0, width, -50, 50)
    np_pixels[:, :, 0:3] = np.clip(np_pixels[:, :, 0:3] + temp, 0, 255)

    if current_effect == 1:
        # Inversion
        np_pixels[:, :, 0:3] = 255 - np_pixels[:, :, 0:3]
    elif current_effect == 2:
        # Zoom in
        zoom_factor = 1.2
        zoomed = np.array(Image.fromarray(np_pixels).resize(
            (int(width*zoom_factor), int(height*zoom_factor)), Image.BICUBIC))
        h_start = (zoomed.shape[0] - height) // 2
        w_start = (zoomed.shape[1] - width) // 2
        np_pixels[:, :, :] = zoomed[h_start:h_start+height, w_start:w_start+width, :]
    elif current_effect == 3:
        # Zoom out
        zoom_factor = 0.8
        zoomed = np.array(Image.fromarray(np_pixels).resize(
            (int(width*zoom_factor), int(height*zoom_factor)), Image.BICUBIC))
        np_pixels[:zoomed.shape[0], :zoomed.shape[1], :] = zoomed
    elif current_effect == 4:
        # Blur
        blurred = np.array(Image.fromarray(np_pixels).filter(ImageFilter.GaussianBlur(radius=10)))
        np_pixels[:, :, :] = blurred
    elif current_effect == 5:
        # Color flip (swap R <-> B)
        np_pixels[:, :, [0, 2]] = np_pixels[:, :, [2, 0]]
    elif current_effect == 6:
        # Grayscale
        gray = np.mean(np_pixels[:, :, 0:3], axis=2, keepdims=True)
        np_pixels[:, :, 0:3] = gray
    elif current_effect == 7:
        # Edge detection (basic)
        from scipy.ndimage import sobel
        gray = np.mean(np_pixels[:, :, 0:3], axis=2)
        sx = sobel(gray, axis=0)
        sy = sobel(gray, axis=1)
        edge = np.clip(np.sqrt(sx**2 + sy**2), 0, 255)
        np_pixels[:, :, 0:3] = edge[:, :, None]

    update_np_pixels()