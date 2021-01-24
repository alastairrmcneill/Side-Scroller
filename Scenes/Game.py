import pygame
import random

from Scenes.Scene import Scene
from Components.Player import Player
from Components.Giraffe import Giraffe
from Components.Rhino import Rhino
from Components.Constants import BG_IMG

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.img = BG_IMG.convert()
        self.vel = 6
        self.x1 = 0
        self.x2 = self.img.get_width()
        self.player = Player()
        self.enemies = [Giraffe()]
        self.enemy_timer = 0
        self.min_gap = 50
        self.range_gap = 40
        self.speed_timer = 0
        self.speed_loop = 1000
        self.score = 0

    def startup(self, persist):
        self.reset()
        self.manager.FPS = 10


    def cleanup(self):
        self.done = False
        self.manager.FPS = 30
        self.persist = {"Score": self.score,
                        "Player": self.player,
                        "Enemies": self.enemies,
                        "x1": self.x1,
                        "x2": self.x2}

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
        self.set_speed()

        self.player.move()
        if self.player.crashed:
            self.done = True
            self.next = "Crash"

        for en in self.enemies:
            en.move()
            if en.check_collision(self.player):
                self.player.crashing = True
            if en.x + en.current_img.get_width() < 0:
                self.enemies.pop(self.enemies.index(en))
                self.score += 1



    def draw(self, screen):
        screen.blit(self.img, (self.x1,0))
        screen.blit(self.img, (self.x2,0))
        for en in self.enemies:
            en.draw(screen)

        self.player.draw(screen)


    def add_enemy(self):
        self.enemy_timer += 1
        if self.enemy_timer > self.min_gap + 75 * random.randint(0,self.range_gap):
            if random.random() > 0.6  :
                self.enemies.append(Giraffe())
            else:
                self.enemies.append(Rhino())
            self.enemy_timer = 0

    def set_speed(self):
        self.speed_timer += 1

        if self.speed_timer > self.speed_loop:
            self.manager.FPS += 5
            if self.manager.FPS > 100:
                self.manager.FPS = 100
            self.speed_timer = 0

