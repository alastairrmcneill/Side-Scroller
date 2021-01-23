import pygame
from Components.Constants import PLAYER_IMGS

class Player:
    def __init__(self):
        self.x = 150
        self.y = 388
        self.floor = 388
        self.vel = -3
        self.g = 0.3
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.runLoop = 8
        self.IMGS = PLAYER_IMGS
        self.current_img = self.IMGS[0]

    def move(self):
        if self.sliding:
            if self.slideCount < 50:
                self.y = 400
            elif self.slideCount > 50:
                self.y = 388
                self.slideCount = 0
                self.sliding = False

            self.slideCount += 1


        elif self.jumping:
            self.jumpCount += 1

            s = self.vel * self.jumpCount + 0.5 * self.g * self.jumpCount ** 2
            s = min(s, 8)

            self.y = self.y + s

            if self.y >= self.floor:
                self.y = self.floor
                self.jumping = False
                self.jumpCount = 0

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