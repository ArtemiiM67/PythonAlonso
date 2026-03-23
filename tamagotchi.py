from tamagotchiClass import tamagotchi

pet = tamagotchi("Blob")


def setup():
    size(700, 500)
    text_align(CENTER, CENTER)
    rect_mode(CENTER)


def draw():
    background(135, 206, 235)

    pet.update()

    draw_room()
    draw_pet(pet)
    draw_ui(pet)


def draw_room():
    no_stroke()

    fill(245, 235, 220)
    rect(width / 2, 170, width, 340)

    fill(170, 120, 80)
    rect(width / 2, 420, width, 160)


def draw_pet(pet):
    x = pet.pos_x if pet.bouncing else width / 2
    y = pet.pos_y if pet.bouncing else 250

    if pet.destroying:
        elapsed = frame_count - pet.destroy_start_frame
        bounce = sin(frame_count * 0.25) * 10

        fill(0, 0, 0, 40)
        ellipse(x, y + 80, 150, 35)

        no_stroke()
        fill(255, 80, 80)
        ellipse(x, y + bounce, 180, 160)

        triangle(x - 60, y - 65 + bounce, x - 25, y - 130 + bounce, x - 5, y - 55 + bounce)
        triangle(x + 60, y - 65 + bounce, x + 25, y - 130 + bounce, x + 5, y - 55 + bounce)

        fill(0)
        ellipse(x - 35, y - 15 + bounce, 22, 28)
        ellipse(x + 35, y - 15 + bounce, 22, 28)

        fill(255, 255, 0)
        text_size(40)
        text("NOOO!", x, y + 20 + bounce)

        fill(255, 0, 0)
        text_size(42)
        if pet.destroy_stage > 0:
            text(str(pet.destroy_stage), x, 120)

        return

    if pet.alive:

        bounce = sin(frame_count * 0.08) * 5

        body_r = 130 + (pet.happiness * 125) / 100
        body_g = 100 + (pet.cleanliness * 120) / 100
        body_b = 180

        fill(0, 0, 0, 40)
        ellipse(x, y + 80, 150, 35)

        no_stroke()
        fill(body_r, body_g, body_b)
        ellipse(x, y + bounce, 180, 160)

        triangle(x - 60, y - 65 + bounce, x - 25, y - 130 + bounce, x - 5, y - 55 + bounce)
        triangle(x + 60, y - 65 + bounce, x + 25, y - 130 + bounce, x + 5, y - 55 + bounce)

        fill(0)
        ellipse(x - 35, y - 15 + bounce, 18, 24)
        ellipse(x + 35, y - 15 + bounce, 18, 24)

        fill(255)
        ellipse(x - 38, y - 20 + bounce, 5, 7)
        ellipse(x + 32, y - 20 + bounce, 5, 7)

        no_fill()
        stroke(0)
        stroke_weight(3)

        mood = pet.face_mood()

        if mood == "happy":
            arc(x, y + 20 + bounce, 45, 25, 0.1, PI - 0.1)
        elif mood == "neutral":
            line(x - 15, y + 20 + bounce, x + 15, y + 20 + bounce)
        else:
            arc(x, y + 32 + bounce, 45, 25, PI + 0.1, TWO_PI - 0.1)

    else:

        fill(0, 0, 0, 40)
        ellipse(x, y + 80, 150, 35)

        no_stroke()
        fill(160)
        ellipse(x, y, 180, 160)

        stroke(0)
        stroke_weight(3)
        line(x - 45, y - 20, x - 20, y)
        line(x - 20, y - 20, x - 45, y)
        line(x + 20, y - 20, x + 45, y)
        line(x + 45, y - 20, x + 20, y)

        no_fill()
        arc(x, y + 35, 40, 20, PI + 0.2, TWO_PI - 0.2)


def draw_ui(pet):
    draw_stat_bar(120, 55, pet.hunger, color(255, 120, 120), "Hunger")
    draw_stat_bar(120, 95, pet.happiness, color(255, 210, 90), "Happiness")
    draw_stat_bar(120, 135, pet.cleanliness, color(120, 220, 255), "Cleanliness")
    draw_stat_bar(120, 175, pet.energy, color(170, 140, 255), "Energy")

    fill(20)
    text_size(28)
    text(pet.name, width / 2, 40)

    text_size(16)
    text("Age: " + str(pet.age_seconds()) + "s", width - 90, 35)

    draw_button(150, 440, 120, 45, "F - Feed")
    draw_button(350, 440, 120, 45, "P - Play")
    draw_button(550, 440, 120, 45, "C - Clean")

    fill(20)
    text_size(18)
    text(pet.message, width / 2, 390)


def key_pressed():
    if key == "f" or key == "F":
        pet.feed()
    elif key == "p" or key == "P":
        pet.play()
    elif key == "c" or key == "C":
        pet.clean()
    elif (key == "r" or key == "R") and not pet.alive:
        pet.restart()
    elif key == "k" or key == "K":
        pet.secret_ending()


def mouse_pressed():
    if not pet.alive:
        return

    if inside_button(150, 440, 120, 45):
        pet.feed()
    elif inside_button(350, 440, 120, 45):
        pet.play()
    elif inside_button(550, 440, 120, 45):
        pet.clean()
        
def draw_stat_bar(x, y, value, bar_color, label):

    fill(20)
    text_size(16)
    text_align(LEFT, CENTER)
    text(label, x - 90, y)

    rect_mode(CORNER)

    no_stroke()
    fill(230)
    rect(x, y - 10, 180, 20)

    fill(bar_color)
    rect(x, y - 10, value * 1.8, 20)

    fill(20)
    text_align(CENTER, CENTER)
    text(str(value), x + 90, y)

    rect_mode(CENTER)


def draw_button(x, y, w, h, label):

    over = (
        mouse_x > x - w / 2 and mouse_x < x + w / 2
        and mouse_y > y - h / 2 and mouse_y < y + h / 2
    )

    if over:
        fill(255, 255, 255, 220)
    else:
        fill(255, 255, 255, 180)

    stroke(50)
    stroke_weight(2)
    rect(x, y, w, h, 12)

    fill(20)
    text_size(18)
    text_align(CENTER, CENTER)
    text(label, x, y)


def inside_button(x, y, w, h):

    return (
        mouse_x > x - w / 2 and mouse_x < x + w / 2
        and mouse_y > y - h / 2 and mouse_y < y + h / 2
    )