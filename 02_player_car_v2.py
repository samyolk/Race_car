"""This is version two  of the player car. This adds movement to the player
car."""
# imports key presses
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
)
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
x_pos = 146
y_pos = 350

while running:
    # checks if user clicked the close button
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False

    # gets user input every loop
    pressed_keys = pygame.key.get_pressed()
    # moves player sprite every time key is pressed
    player.update(pressed_keys)

    if pressed_keys[K_UP]:
        y_pos -= 5
    if pressed_keys[K_DOWN]:
        y_pos += 5
    if pressed_keys[K_LEFT]:
        x_pos -= 5
    if pressed_keys[K_RIGHT]:
        x_pos += 5

    if bg_frame > 3:
        bg_frame = 0
    BackGround = Background(background_images[bg_frame], [0, 0])
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)

    player = PlayerCar([y_pos, x_pos])
    screen.blit(player.image, player.rect)

    bg_frame += 1
    pygame.display.update()
    clock.tick(64)
