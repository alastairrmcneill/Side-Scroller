import pygame
from Components.Constants import PLAYER_IMGS, CRASHING_IMGS

class Player:
    def __init__(self):
        self.x = 150
        self.y = 388
        self.floor = 388
        self.vel = -3
        self.g = 0.3
        self.crashing = False
        self.crashed = False
        self.jumping = False
        self.sliding = False
        self.crashCount = 0
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.runLoop = 8
        self.IMGS = PLAYER_IMGS
        self.CRASHING_IMGS = CRASHING_IMGS
        self.current_img = self.IMGS[0]

    def move(self):
        if self.sliding:
            if self.slideCount < 30:
                self.current_img = self.IMGS[3]
            elif self.slideCount > 32:
                self.slideCount = 0
                self.sliding = False

            self.slideCount += 1


        elif self.jumping:
            self.current_img = self.IMGS[4]
            self.jumpCount += 1

            s = self.vel * self.jumpCount + 0.5 * self.g * self.jumpCount ** 2
            s = min(s, 8)

            self.y = self.y + s

            if self.y >= self.floor:
                self.y = self.floor
                self.jumping = False
                self.jumpCount = 0

        elif self.crashing:
            self.crashCount += 1
            if self.crashCount < 8:
                self.current_img = self.CRASHING_IMGS[0]
            elif self.crashCount == 8:
                self.y += 36
                self.current_img = self.CRASHING_IMGS[1]
            elif self.crashCount < 40:
                self.current_img = self.CRASHING_IMGS[1]
            else:
                self.crashed = True

        else:
            self.runCount += 1

            if self.runCount < self.runLoop:
                self.current_img = self.IMGS[0]
            elif self.runCount < self.runLoop * 2:
                self.current_img = self.IMGS[1]
            elif self.runCount < self.runLoop * 3:
                self.current_img = self.IMGS[2]
            elif self.runCount < self.runLoop * 4:
                self.current_img = self.IMGS[1]
            else:
                self.current_img = self.IMGS[0]
                self.runCount = 0

    def get_mask(self):
        return pygame.mask.from_surface(self.current_img)


    def draw(self, screen):
        screen.blit(self.current_img, (self.x, self.y))