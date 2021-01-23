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

# Paths
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
IMGS_PATH = os.path.join(BASE_PATH, "Imgs")
FONTS_PATH = os.path.join(BASE_PATH, "Fonts")


# Images
BG_IMG = pygame.image.load(os.path.join(IMGS_PATH, "bg.png"))

# Fonts

