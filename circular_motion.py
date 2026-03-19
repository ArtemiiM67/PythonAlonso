circ1 = {
  "angle": 0.0,
  "offsetX": 300,
  "offsetY": 210,
  "radius": 50,
  "speed": 0.1,
  "size": 20
}

def setup():
  size(600, 420)

def draw():
  global circ1
  
  no_stroke()
  if frame_count%60 == 0:
      background(255)
  
  r = 150 + 105 * sin(circ1["angle"])
  g = 150 + 105 * sin(circ1["angle"] + 2)
  b = 150 + 105 * sin(circ1["angle"] + 4)

  x = circ1["offsetX"] + cos(circ1["angle"]) * circ1["radius"]
  y = circ1["offsetY"] + sin(circ1["angle"]) * circ1["radius"]
  
  for i in range(4, 0, -1):
    fill(r, g, b, 40)
    circle(x, y, circ1["size"] + i * 10)
  
  fill(r, g, b)
  circle(x, y, circ1["size"])
  
  circ1["angle"] += circ1["speed"]
  circ1["radius"] += 0.05   
  circ1["size"] = 20 + 10 * sin(circ1["angle"] * 2)
  
  circ1["speed"] += 0.0002