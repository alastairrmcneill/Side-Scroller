import pygame
from Components.Enemy import Enemy
from Components.Constants import RHINO_IMGS

class Rhino(Enemy):
    def __init__(self):
        super().__init__()
        self.y = 420
        self.IMGS = RHINO_IMGS
