import pygame
import random

from Scenes.Scene import Scene
from Components.Player import Player
from Components.High_enemy import High_enemy
from Components.Low_enemy import Low_enemy
from Components.Constants import BG_IMG

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.img = BG_IMG.convert()
        self.vel = 2
        self.x1 = 0
        self.x2 = self.img.get_width()
        self.player = Player()
        self.enemies = [High_enemy()]
        self.enemy_timer = 0
        self.min_gap = 50
        self.range_gap = 50

    def startup(self, persist):
        self.reset()

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

        self.add_enemy()

        self.player.move()

        for en in self.enemies:
            en.move()
            if en.check_collision(self.player):
                print("Crashed")
                self.done = True
                self.next = "Game"
            if en.x + en.current_img.get_width() < 0:
                self.enemies.pop(self.enemies.index(en))



    def draw(self, screen):
        screen.blit(self.img, (self.x1,0))
        screen.blit(self.img, (self.x2,0))
        self.player.draw(screen)
        for en in self.enemies:
            en.draw(screen)


    def add_enemy(self):
        self.enemy_timer += 1
        if self.enemy_timer > self.min_gap + 100 * random.randint(0,self.range_gap):
            if random.random() > 0.5:
                self.enemies.append(High_enemy())
            else:
                self.enemies.append(Low_enemy())
            self.enemy_timer = 0

