import pygame
from Scenes.Scene import Scene
from Components.Constants import BG_IMG, CLOUDS_IMG, BOBBING_IMGS, WHITE, WIN_WIDTH, WIN_HEIGHT

class Intro(Scene):
    def __init__(self):
        super().__init__()
        self.bg_img = BG_IMG
        self.clouds_img = CLOUDS_IMG
        self.IMGS = BOBBING_IMGS
        self.x = 150
        self.y = 388
        self.current_img = self.IMGS[0]
        self.bobLoop = 15
        self.bobCount = 0
        self.c1 = 0
        self.c2 = self.clouds_img.get_width()
        self.c_vel = 1

    def startup(self, persist):
        self.done = False
        self.persist = persist

    def cleanup(self):
        self.persist = {"c1": self.c1,
                        "c2": self.c2}
        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.done = True
            self.next = "Game"

    def update(self):
        self.c1 -= self.c_vel
        self.c2 -= self.c_vel

        if self.c1 + self.clouds_img.get_width() <0:
            self.c1 = self.c2 + self.clouds_img.get_width()

        if self.c2 + self.clouds_img.get_width() <0:
            self.c2 = self.c1 + self.clouds_img.get_width()

        self.bobCount += 1
        if self.bobCount < self.bobLoop:
            self.current_img = self.IMGS[0]
        elif self.bobCount < self.bobLoop * 2:
            self.current_img = self.IMGS[1]
        else:
            self.current_img = self.IMGS[0]
            self.bobCount = 0

    def draw(self, screen):
        screen.blit(self.bg_img, (0,-20))
        screen.blit(self.clouds_img, (self.c1, -20))
        screen.blit(self.clouds_img, (self.c2, -20))
        screen.blit(self.current_img, (self.x, self.y))
        self.draw_message(screen)

    def draw_message(self, screen):
        text = self.font.render("Press SPACE to start.", True, WHITE)
        rect = text.get_rect(center = (WIN_WIDTH // 2, WIN_HEIGHT //2 ))
        screen.blit(text, rect)
