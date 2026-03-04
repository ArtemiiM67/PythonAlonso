def setup():
    size(800, 800)
    global cars, traffic_lights, green_light
    cars = [
        {'x': 315, 'y': 0, 'color': color(255, 0, 0), 'direction': 'down', 'speed': 3, 'lane': 1},
        {'x': 420, 'y': 0, 'color': color(0, 255, 0), 'direction': 'down', 'speed': 4, 'lane': 1},
        {'x': 0, 'y': 320, 'color': color(0, 0, 255), 'direction': 'right', 'speed': 3, 'lane': 2},
        {'x': 0, 'y': 430, 'color': color(255, 255, 0), 'direction': 'right', 'speed': 2, 'lane': 2}
    ]

    traffic_lights = [
        {'x': 400, 'y': 100, 'color': 'green', 'timer': 0},
        {'x': 400, 'y': 700, 'color': 'green', 'timer': 0},
        {'x': 100, 'y': 400, 'color': 'green', 'timer': 0},
        {'x': 700, 'y': 400, 'color': 'green', 'timer': 0}
    ]

def update_traffic_lights():
    for light in traffic_lights:
        light['timer'] += 1
        if light['timer'] > 300:
            light['timer'] = 0
            if light['color'] == 'green':
                light['color'] = 'yellow'
            elif light['color'] == 'yellow':
                light['color'] = 'red'
            elif light['color'] == 'red':
                light['color'] = 'green'

def draw_traffic_lights():
    for light in traffic_lights:
        if light['color'] == 'green':
            fill(0, 255, 0)
        elif light['color'] == 'yellow':
            fill(255, 255, 0)
        elif light['color'] == 'red':
            fill(255, 0, 0)
        ellipse(light['x'], light['y'], 30, 60)

def update_cars():
    global green_light
    green_light = traffic_lights[0]['color'] == 'green'
    yellow_light = traffic_lights[0]['color'] == 'yellow'

    for car in cars:
        if green_light:
            if car['direction'] == 'up':
                car['y'] -= car['speed']
            elif car['direction'] == 'down':
                car['y'] += car['speed']
            elif car['direction'] == 'left':
                car['x'] -= car['speed']
            elif car['direction'] == 'right':
                car['x'] += car['speed']
        if yellow_light:
            if car['direction'] == 'up':
                car['y'] -= (car['speed'] / 2)
            elif car['direction'] == 'down':
                car['y'] += (car['speed'] / 2)
            elif car['direction'] == 'left':
                car['x'] -= (car['speed'] / 2)
            elif car['direction'] == 'right':
                car['x'] += (car['speed'] / 2)

        if car['x'] > width:
            car['x'] = 0
        elif car['x'] < 0:
            car['x'] = width

        if car['y'] > height:
            car['y'] = 0
        elif car['y'] < 0:
            car['y'] = height

def draw_cars():
    for car in cars:
        fill(car['color'])
        no_stroke()
        rect(car['x'], car['y'], 60, 30)
        fill(200)
        rect(car['x'] + 15, car['y'] + 5, 30, 15)
        fill(0)
        ellipse(car['x'] + 15, car['y'] + 28, 10, 10)
        ellipse(car['x'] + 45, car['y'] + 28, 10, 10)

def draw():
    background(220)
    fill(150)
    rect(0, 300, width, 200)
    rect(300, 0, 200, height)

    stroke(0)
    stroke_weight(5)
    line(width / 2, 0, width / 2, height)
    line(0, height / 2, width, height / 2)

    update_traffic_lights()
    draw_traffic_lights()

    update_cars()
    draw_cars()