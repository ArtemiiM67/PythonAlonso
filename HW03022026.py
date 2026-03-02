import random

racers = {}
track_end = 700
winner = None

def setup():
    global racers
    size(800, 400)
    
    racers = {
        "r1": {"name": "Speedy", "x": 50, "y": 80,  "color": (255, 0, 0), "speed": random.uniform(1, 4), "stop_at": random_stop()},
        "r2": {"name": "Flash",  "x": 50, "y": 150, "color": (0, 255, 0), "speed": random.uniform(1, 4), "stop_at": random_stop()},
        "r3": {"name": "Zoom",   "x": 50, "y": 220, "color": (0, 0, 255), "speed": random.uniform(1, 4), "stop_at": random_stop()},
        "r4": {"name": "Player", "x": 50, "y": 290, "color": (255, 165, 0), "speed": 0, "stop_at": track_end}
    }

def random_stop():
    if random.random() < 0.7:
        return track_end
    else:
        return random.randint(200, track_end - 100)

def draw():
    global winner
    
    background(230)

    stroke(0)
    line(track_end, 0, track_end, height)

    for racer in racers.values():
        if racer["name"] != "Player" and winner is None:
            if racer["x"] < racer["stop_at"]:
                racer["x"] += racer["speed"]

        if racer["x"] >= track_end and winner is None:
            winner = racer["name"]

        fill(*racer["color"])
        no_stroke()
        circle(racer["x"], racer["y"], 40)

        fill(0)
        text(racer["name"], racer["x"] - 20, racer["y"] - 30)

    if winner:
        text_size(32)
        fill(0)
        text(f"{winner} wins!", 280, 370)

def mouse_pressed():
    global winner
    if winner is None:
        racers["r4"]["x"] += 20