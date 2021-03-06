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
SKY_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Sky.png")), (4000,572))
HILLS_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Hills.png")), (12000,572))
FLOOR_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Floor.png")), (4000,572))

CLOUDS_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Clouds.png")), (4000,572))

PLAYER_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player 1.png")), (100,96)),
               pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player 2.png")), (100,96)),
               pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player 3.png")), (100,96)),
               pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player_slide.png")), (164,96)),
               pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Player_jump.png")), (100,96))]

CRASHING_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Crash 1.png")), (100,96)),
                 pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Crash 2.png")), (136,60)),
                 pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Crash 3.png")), (136,60))]

TREES_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Tree 1.png")), (72,112)),
              pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Tree 2.png")), (72,112))]

BIRD_IMGS = [[pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Bird 1.png")), (72,64)),
              pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Bird 2.png")), (72,64))],
             [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "2 Birds 1.png")), (104,132)),
              pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "2 Birds 2.png")), (104, 132))],
             [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "3 Birds 1.png")), (116,168)),
              pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "3 Birds 2.png")), (116,168))]]

RHINO_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Rhino 1.png")), (125,65)),
                pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Rhino 2.png")), (125,65))]

BOBBING_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Bobbing 1.png")), (100, 96)),
                pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Bobbing 2.png")), (100, 96))]

GAME_OVER_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMGS_PATH, "Game over w shadow.png")), (300,180))

# Fonts

