import pygame
from Scenes.Scene import Scene
from Components.Constants import SKY_IMG, HILLS_IMG, FLOOR_IMG, BOBBING_IMGS, WHITE, WIN_WIDTH, WIN_HEIGHT

class Intro(Scene):
    def __init__(self):
        super().__init__()
        self.sky_img = SKY_IMG
        self.hills_img = HILLS_IMG
        self.floor_img = FLOOR_IMG
        self.IMGS = BOBBING_IMGS
        self.x = 150
        self.y = 388
        self.current_img = self.IMGS[0]
        self.bobLoop = 15
        self.bobCount = 0
        self.s1 = 0
        self.s2 = self.sky_img.get_width()
        self.s_vel = 1
        self.h1 = 0


    def startup(self, persist):
        self.done = False
        self.persist = persist

    def cleanup(self):
        self.persist = {"s1": self.s1,
                        "s2": self.s2}
        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.done = True
            self.next = "Game"

    def update(self):
        self.s1 -= self.s_vel
        self.s2 -= self.s_vel

        if self.s1 + self.sky_img.get_width() <0:
            self.s1 = self.s2 + self.sky_img.get_width()

        if self.s2 + self.sky_img.get_width() <0:
            self.s2 = self.s1 + self.sky_img.get_width()

        self.bobCount += 1
        if self.bobCount < self.bobLoop:
            self.current_img = self.IMGS[0]
        elif self.bobCount < self.bobLoop * 2:
            self.current_img = self.IMGS[1]
        else:
            self.current_img = self.IMGS[0]
            self.bobCount = 0

    def draw(self, screen):
        screen.blit(self.sky_img, (self.s1, -20))
        screen.blit(self.sky_img, (self.s2, -20))
        screen.blit(self.hills_img, (self.h1, -20))
        screen.blit(self.floor_img, (0,-20))
        screen.blit(self.current_img, (self.x, self.y))
        self.draw_message(screen)

    def draw_message(self, screen):
        text = self.font.render("Press SPACE to start.", True, WHITE)
        rect = text.get_rect(center = (WIN_WIDTH // 2, WIN_HEIGHT //2 ))
        screen.blit(text, rect)
