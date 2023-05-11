"""This is the second version for the main display for the video game
I have added the background sprite to the display."""
# imports and initialises pygame
import pygame
pygame.init()

# window resolution setup
display = pygame.display.set_mode([330, 500])


# class for loading background image files
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

    # calls function to load background image
    BackGround = Background('assets/background_1.png', [0, 0])
    display.fill([255, 255, 255])
    display.blit(BackGround.image, BackGround.rect)
    pygame.display.update()



