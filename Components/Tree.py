import pygame
from Components.Enemy import Enemy
from Components.Constants import TREES_IMGS

class Tree(Enemy):
    def __init__(self):
        super().__init__()
        self.y = 372
        self.IMGS = TREES_IMGS
        self.animateLoop = 15
