import pygame

from Scenes.Scene import Scene
from Components.Player import Player
from Components.High_enemy import High_enemy
from Components.Constants import BG_IMG

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.img = BG_IMG.convert()
        self.vel = 2
        self.x1 = 0
        self.x2 = self.img.get_width()
        self.player = Player()
        self.enemies = [High_enemy()]

    def startup(self, persist):
        pass

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if not self.player.sliding and not self.player.jumping:
                self.player.sliding = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if not self.player.jumping and not self.player.sliding:
                self.player.jumping = True

    def update(self):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if self.x1 + self.img.get_width() <0:
            self.x1 = self.x2 + self.img.get_width()

        if self.x2 + self.img.get_width() <0:
            self.x2 = self.x1 + self.img.get_width()

        self.player.move()

        for en in self.enemies:
            en.move()
            if en.check_collision(self.player):
                print("Crashed")



    def draw(self, screen):
        screen.blit(self.img, (self.x1,0))
        screen.blit(self.img, (self.x2,0))
        self.player.draw(screen)
        for en in self.enemies:
            en.draw(screen)
