"""This is the first version of the player car which is built on the main
display component."""
# imports and initialises pygame
import pygame
pygame.init()
clock = pygame.time.Clock()


# window resolution setup
screen = pygame.display.set_mode([330, 500])
# loads image as icon
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
# sets window caption
pygame.display.set_caption("Pixel Car 2D")
# class for loading background image file


# background sprite class
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# player car sprite class
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        self.image = pygame.image.load("assets/player_car_sprite.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = location


# sets current state to running
running = True

background_images = ['assets/background_1.png', 'assets/background_2.png',
                     'assets/background_3.png', 'assets/background_4.png']
bg_frame = 0
player = PlayerCar([100, 100])


while running:
    # checks if user clicked the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if bg_frame > 3:
        bg_frame = 0
    BackGround = Background(background_images[bg_frame], [0, 0])
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)

    player = PlayerCar([100, 100])
    screen.blit(player.image, player.rect)

    bg_frame += 1
    pygame.display.update()
    clock.tick(64)
