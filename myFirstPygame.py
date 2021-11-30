# My First Pygame, David Gay, 11/30/21, 2:50,v0.5

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

# Setup fonts.
basicFont = pygame. font.SysFont(None, 48)

# Setup text
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx= windowSurface.get_rect().centerx
textRect.centerx= windowSurface.get_rect().centerx

# Draw the game background.
windowSurface.fill(TANGBLUE)
