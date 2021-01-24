import pygame
from Components.Enemy import Enemy
from Components.Constants import GIRAFFE_IMGS

class Giraffe(Enemy):
    def __init__(self):
        super().__init__()
        self.y = 372
        self.IMGS = GIRAFFE_IMGS
