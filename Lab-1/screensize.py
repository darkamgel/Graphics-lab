# import package pygame
import pygame

# initialize pygame
pygame.init()

# Form screen
screen = pygame.display.set_mode()

# get the default size
x, y = screen.get_size()

# quit pygame
pygame.display.quit()

print(x, y)
