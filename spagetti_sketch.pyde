import random

spaghetti_strands = []

bowl_x = 300
bowl_y = 400
bowl_radius = 120

class Spaghetti:
    def __init__(self):
        self.x = random.randint(bowl_x - 20, bowl_x + 20)
        self.y = 0
        self.length = random.randint(20, 80)
        self.speed = random.uniform(1, 3)

    def display(self):
        stroke(255, 223, 132)  
        strokeWeight(3)
        line(self.x, self.y, self.x, self.y + self.length)

    def fall(self):
        if self.y < bowl_y - bowl_radius:
            self.y += self.speed

def setup():
    size(600, 500)
    noStroke()

def draw():
    background(200, 225, 255)  # Light blue background

    fill(255, 180, 120)  # Light brown for the bowl
    ellipse(bowl_x, bowl_y, bowl_radius * 2, bowl_radius / 1.5)

    if frameCount % 10 == 0:
        spaghetti_strands.append(Spaghetti())

    for strand in spaghetti_strands:
        strand.fall()
        strand.display()
