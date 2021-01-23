import pygame
from Components.Enemy import Enemy
from Components.Constants import PLAYER_IMGS

class High_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.y = 490
        self.IMGS = PLAYER_IMGS
