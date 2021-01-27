import pygame
import random

from Scenes.Scene import Scene
from Components.Player import Player
from Components.Tree import Tree
from Components.Rhino import Rhino
from Components.Bird import Bird
from Components.Constants import SKY_IMG, HILLS_IMG, FLOOR_IMG

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.sky_img = SKY_IMG
        self.hills_img = HILLS_IMG
        self.floor_img = FLOOR_IMG
        self.s_vel = 1
        self.s1 = 0
        self.s2 = self.sky_img.get_width()
        self.h1 = 0
        self.h2 = self.hills_img.get_width()
        self.h_vel = 2
        self.f1 = 0
        self.f2 = self.floor_img.get_width()
        self.f_vel = 7
        self.player = Player()
        self.enemies = [Tree()]
        self.enemy_timer = 0
        self.min_gap = 60
        self.range_gap = 40
        self.speed_timer = 0
        self.speed_loop = 1000
        self.score = 0

    def startup(self, persist):
        self.reset()
        self.manager.FPS = 45
        self.persist = persist
        self.s1 = persist["s1"]
        self.s2 = persist["s2"]

    def cleanup(self):
        self.done = False
        self.manager.FPS = 30
        self.persist = {"Score": self.score,
                        "Player": self.player,
                        "Enemies": self.enemies,
                        "s1": self.s1,
                        "s2": self.s2,
                        "h1": self.h1,
                        "h2": self.h2,
                        "f1": self.f1,
                        "f2": self.f2}

        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if not self.player.sliding and not self.player.jumping and not self.player.crashing:
                self.player.sliding = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if not self.player.jumping and not self.player.sliding and not self.player.crashing:
                self.player.jumping = True

    def update(self):
        self.s1 -= self.s_vel
        self.s2 -= self.s_vel
        self.h1 -= self.h_vel
        self.h2 -= self.h_vel
        self.f1 -= self.f_vel
        self.f2 -= self.f_vel

        if self.s1 + self.sky_img.get_width() <0:
            self.s1 = self.s2 + self.sky_img.get_width()

        if self.s2 + self.sky_img.get_width() <0:
            self.s2 = self.s1 + self.sky_img.get_width()

        if self.h1 + self.hills_img.get_width() <0:
            self.h1 = self.h2 + self.hills_img.get_width()

        if self.h2 + self.hills_img.get_width() <0:
            self.h2 = self.h1 + self.hills_img.get_width()

        if self.f1 + self.floor_img.get_width() <0:
            self.f1 = self.f2 + self.floor_img.get_width()

        if self.f2 + self.floor_img.get_width() <0:
            self.f2 = self.f1 + self.floor_img.get_width()


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
        screen.blit(self.sky_img, (self.s1, -20))
        screen.blit(self.sky_img, (self.s2, -20))
        screen.blit(self.hills_img, (self.h1, -20))
        screen.blit(self.hills_img, (self.h2, -20))
        screen.blit(self.floor_img, (self.f1, -20))
        screen.blit(self.floor_img, (self.f2, -20))

        for en in self.enemies:
            en.draw(screen)

        self.player.draw(screen)


    def add_enemy(self):
        self.enemy_timer += 1
        if self.enemy_timer > self.min_gap + 75 * random.randint(0,self.range_gap):
            rand = random.random()
            if rand > 0.6:
                self.enemies.append(Tree())
            elif rand > 0.3:
                self.enemies.append(Bird())
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

