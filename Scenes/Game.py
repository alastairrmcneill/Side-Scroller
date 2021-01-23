from Scenes.Scene import Scene
from Components.Constants import BG_IMG

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.img = BG_IMG.convert()
        self.vel = 2
        self.x1 = 0
        self.x2 = self.img.get_width()

    def startup(self, persist):
        pass

    def cleanup(self):
        self.done = False
        return self.persist

    def handle_event(self, event):
        pass

    def update(self):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if self.x1 + self.img.get_width() <0:
            self.x1 = self.x2 + self.img.get_width()

        if self.x2 + self.img.get_width() <0:
            self.x2 = self.x1 + self.img.get_width()


    def draw(self, screen):
        screen.blit(self.img, (self.x1,0))
        screen.blit(self.img, (self.x2,0))