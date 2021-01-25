"""
Constants for the game
"""

import pygame
import os
pygame.font.init()

# Window variables
WIN_WIDTH = 800
WIN_HEIGHT = 550

# Colours
WHITE = (255, 255, 255)

# Paths
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
IMGS_PATH = os.path.join(BASE_PATH, "Imgs")
FONTS_PATH = os.path.join(BASE_PATH, "Fonts")


# Images
BG_IMG = pygame.image.load(os.path.join(IMGS_PATH, "bg.png"))
PLAYER_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player1.png")), (100,96)),
               pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player2.png")), (100,96)),
               pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player3.png")), (100,96)),
               pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player_slide.png")), (164,96)),
               pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player_jump.png")), (100,96)),]

GIRAFFE_IMGS = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "G-Man 1.png")), (72,114)), True, False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "G-Man 2.png")), (72,114)), True, False)]

BIRD_IMGS = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "G-Man 1.png")), (72,114)), True, False),
             pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "G-Man 2.png")), (72,114)), True, False)]

RHINO_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Rhino 1.png")), (125,65)),
                pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Rhino 2.png")), (125,65))]

BOBBING_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player0.png")), (100, 96)),
                pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player0.png")), (100, 90))]

# Fonts

