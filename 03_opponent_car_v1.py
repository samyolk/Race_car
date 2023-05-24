"""This is version one opponent car. This adds opponent cars as obstacles for
the player. This is built on top of 02_player_car_v3"""
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
import random
pygame.init()
clock = pygame.time.Clock()

# list for background image frames
background_images = ['assets/background_1.png', 'assets/background_2.png',
                     'assets/background_3.png', 'assets/background_4.png']
bg_frame = 0

# list for opponent car images
opponent_images = ['assets/opp_car_sprite_1.png',
                   'assets/opp_car_sprite_2.png',
                   'assets/opp_car_sprite_3.png',
                   'assets/opp_car_sprite_4.png',
                   'assets/opp_car_sprite_5.png',
                   'assets/opp_car_sprite_6.png',
                   'assets/opp_car_sprite_7.png']

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


class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        image_num = random.randint(0, 6)
        self.image = pygame.image.load(opponent_images[image_num]).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(
            center=(
                random.randint(51, 262),
                -70,
            )
        )
        self.speed = random.uniform(1, 300)
        self.speed /= 100

    # Move the sprite based on speed
    # Remove the sprite when it passes the bottom of the screen
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > 600:
            self.kill()
            opp.remove(self)


# sets current state to running
running = True
player = PlayerCar([100, 100])
x_pos = 146
y_pos = 350

# sprite lists to store sprites
opp = []
all_sprites = [player]


while running:
    # checks if user clicked the close button
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
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

    # checks if player sprite has crossed border and moves player inside if yes
    if x_pos >= 262:
        x_pos = 261
    if x_pos <= 31:
        x_pos = 32
    if y_pos <= 0:
        y_pos = 1
    if y_pos >= 435:
        y_pos = 434

    if bg_frame > 3:
        bg_frame = 0
    BackGround = Background(background_images[bg_frame], [0, 0])
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)

    player = PlayerCar([y_pos, x_pos])
    screen.blit(player.image, player.rect)

    # randomly creates a new opponent
    new_opp = random.randint(0, 64)
    if new_opp == 0:
        opponent = Opponent()
        opp.append(opponent)
        all_sprites.append(opponent)

    # displays all opponents on screen
    for entity in opp:
        screen.blit(entity.image, entity.rect)
        entity.update()

    bg_frame += 1
    pygame.display.update()
    clock.tick(64)
