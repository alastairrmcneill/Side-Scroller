import pygame
from Scenes.Scene import Scene
from Components.Constants import SKY_IMG, HILLS_IMG, FLOOR_IMG, GAME_OVER_IMG, WIN_WIDTH, WIN_HEIGHT, WHITE

class Crash(Scene):
    def __init__(self):
        super().__init__()
        self.sky_img = SKY_IMG
        self.hills_img = HILLS_IMG
        self.floor_img = FLOOR_IMG
        self.game_over_img = GAME_OVER_IMG.convert_alpha()
        self.rect = self.game_over_img.get_rect()
        self.rect.midright = (-1 * self.game_over_img.get_width() - 5, WIN_HEIGHT // 2 - 100)
        self.s1 = 0
        self.s2 = 0
        self.h1 = 0
        self.h2 = 0
        self.f1 = 0
        self.f2 = 0
        self.g_vel = 50
        self.s_vel = 1
        self.h_vel = 2
        self.player = None
        self.score = 0
        self.enemies = []

    def startup(self, persist):
        self.persist = persist
        self.player = persist["Player"]
        self.score = persist["Score"]
        self.enemies = persist["Enemies"]
        self.s1 = persist["s1"]
        self.s2 = persist["s2"]
        self.h1 = persist["h1"]
        self.h2 = persist["h2"]
        self.f1 = persist["f1"]
        self.f2 = persist["f2"]
        self.player.current_img = self.player.CRASHING_IMGS[2]

        for en in self.enemies:
            en.vel = 0

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.done = True
            self.next = "Intro"

    def update(self):
        self.s1 -= self.s_vel
        self.s2 -= self.s_vel

        if self.s1 + self.sky_img.get_width() <0:
            self.s1 = self.s2 + self.sky_img.get_width()

        if self.s2 + self.sky_img.get_width() <0:
            self.s2 = self.s1 + self.sky_img.get_width()

        self.rect.x += self.g_vel
        if self.rect.centerx > WIN_WIDTH // 2:
            self.rect.centerx = WIN_WIDTH // 2




        for en in self.enemies:
            en.move()

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

        screen.blit(self.game_over_img, self.rect)
        self.draw_score(screen)
        self.draw_message(screen)


    def draw_score(self, screen):
        text = self.font.render("Score: " + str(self.score), True, WHITE)
        rect = text.get_rect(center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50))
        screen.blit(text, rect)

    def draw_message(self, screen):
        text = self.font.render("Press ENTER to try again.", True, WHITE)
        rect = text.get_rect(center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 110))
        screen.blit(text, rect)
