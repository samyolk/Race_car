"""This is an alternative way of doing main display version 3."""
# imports and initialises pygame
import pygame
pygame.init()
clock = pygame.time.Clock()


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

# puts the different background frames in a list
background_images = ['assets/background_1.png', 'assets/background_2.png',
                     'assets/background_3.png', 'assets/background_4.png']
bg_frame = 0

while running:
    # checks if user clicked the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if bg_frame > 3:
        bg_frame = 0
    BackGround = Background(background_images[bg_frame], [0, 0])
    display.fill([255, 255, 255])
    display.blit(BackGround.image, BackGround.rect)
    bg_frame += 1
    pygame.display.update()
    # sets frames per second
    clock.tick(64)
