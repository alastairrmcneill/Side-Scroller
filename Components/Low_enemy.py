import pygame
from Components.Enemy import Enemy
from Components.Constants import PLAYER_IMGS

class Low_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.y = 400
        self.IMGS = PLAYER_IMGS
