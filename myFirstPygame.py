# My First Pygame, David Gay, 11/30/21, 2:39,v0.3

import pygame, sys
from pygame. locals import*

    # Start Pygame
pygame.init()

# setup the game window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup color values.
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
TANGOBLUE = (0,255,255)