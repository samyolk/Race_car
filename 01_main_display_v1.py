"""This is the first version for the main display for the video game"""
# imports and initialises pygame
import pygame
pygame.init()

# window resolution setup
display = pygame.display.set_mode([330, 500])

# sets current state to running
running = True

while running:
    # checks if user clicked the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
