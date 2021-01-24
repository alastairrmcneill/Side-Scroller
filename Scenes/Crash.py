import pygame
from Scenes.Scene import Scene
from Components.Constants import BG_IMG, WIN_WIDTH, WIN_HEIGHT, WHITE

class Crash(Scene):
    def __init__(self):
        super().__init__()
        self.x1 = 0
        self.x2 = 0
        self.bg_img = BG_IMG
        self.player = None
        self.score = 0
        self.enemies = []

    def startup(self, persist):
        self.persist = persist
        self.player = persist["Player"]
        self.score = persist["Score"]
        self.enemies = persist["Enemies"]
        self.x1 = persist["x1"]
        self.x2 = persist["x2"]

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
        for en in self.enemies:
            en.move()

    def draw(self, screen):
        screen.blit(self.bg_img, (self.x1, 0))
        screen.blit(self.bg_img, (self.x2, 0))
        for en in self.enemies:
            en.draw(screen)

        self.player.draw(screen)

        self.draw_score(screen)
        self.draw_message(screen)


    def draw_score(self, screen):
        text = self.font.render("Score: " + str(self.score), True, WHITE)
        rect = text.get_rect(center = (WIN_WIDTH // 2, WIN_HEIGHT // 2))
        screen.blit(text, rect)

    def draw_message(self, screen):
        text = self.font.render("Press ENTER to start again.", True, WHITE)
        rect = text.get_rect(center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
        screen.blit(text, rect)
