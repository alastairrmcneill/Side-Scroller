import pygame
from Components.Constants import PLAYER_IMGS

class Enemy:
    def __init__(self):
        self.x = 900
        self.y = 0
        self.IMGS = PLAYER_IMGS
        self.current_img = self.IMGS[0]
        self.animateLoop = 5
        self.animateCount = 0
        self.vel = -6

    def move(self):
        self.x += self.vel

        self.animateCount += 1

        if self.animateCount < self.animateLoop:
            self.current_img = self.IMGS[0]
        elif self.animateCount < self.animateLoop * 2:
            self.current_img = self.IMGS[1]
        else:
            self.current_img = self.IMGS[0]
            self.animateCount = 0


    def check_collision(self, Player):
        player_mask = Player.get_mask()

        enemy_mask = self.get_mask()
        offset = (self.x - Player.x, self.y - round(Player.y))
        intersect = player_mask.overlap(enemy_mask, offset)

        if intersect:
            return True

        return False

    def get_mask(self):
        return pygame.mask.from_surface(self.current_img)

    def draw(self, screen):
        screen.blit(self.current_img, (self.x, self.y))
