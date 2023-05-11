"""This is the third version for the main display for the video game
I have animated the background display to make it look like the cars are
going forwards.
I have also added the game title and icon."""
# imports and initialises pygame
import pygame
import time
pygame.init()
clock = pygame.time.Clock


# window resolution setup
display = pygame.display.set_mode([330, 500])
# loads image as icon
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
# sets window caption
pygame.display.set_caption("Pixel Car 2D")
# class for loading background image file


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# sets current state to running
running = True


while running:
    # checks if user clicked the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # calls function to load background images in sequence to make animation
    BackGround = Background('assets/background_1.png', [0, 0])
    display.fill([255, 255, 255])
    display.blit(BackGround.image, BackGround.rect)
    time.sleep(0.01)
    BackGround = Background('assets/background_2.png', [0, 0])
    display.fill([255, 255, 255])
    display.blit(BackGround.image, BackGround.rect)
    pygame.display.update()
    time.sleep(0.01)
    BackGround = Background('assets/background_3.png', [0, 0])
    display.fill([255, 255, 255])
    display.blit(BackGround.image, BackGround.rect)
    pygame.display.update()
    time.sleep(0.01)
    BackGround = Background('assets/background_4.png', [0, 0])
    display.fill([255, 255, 255])
    display.blit(BackGround.image, BackGround.rect)
    pygame.display.update()
