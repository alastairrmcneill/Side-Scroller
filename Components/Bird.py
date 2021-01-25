import pygame
from Components.Enemy import Enemy
from Components.Constants import BIRD_IMGS

class Bird(Enemy):
    def __init__(self):
        super().__init__()
        self.y = 364
        self.IMGS = BIRD_IMGS
