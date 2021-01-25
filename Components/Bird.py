import pygame
import random
from Components.Enemy import Enemy
from Components.Constants import BIRD_IMGS

class Bird(Enemy):
    def __init__(self):
        super().__init__()
        self.y = 363
        self.animateLoop = 40
        rand = random.random()

        if rand < 0.45:
            self.IMGS = BIRD_IMGS[1]
            self.y -= 68
        elif rand < 0.9:
            self.IMGS = BIRD_IMGS[2]
            self.y -= 104
        else:
            self.IMGS = BIRD_IMGS[0]

