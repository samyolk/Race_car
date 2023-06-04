"""This is the completed final outcome of race car game."""
# imports key presses
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_r,
    K_SPACE
)
# imports and initialises pygame
import pygame
import random
import shelve
pygame.init()
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0, 0, 0]

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
OPPONENT_X_POS = [51, 96, 135, 191, 241, 280]

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
    def __init__(self, x_val):
        super(Opponent, self).__init__()
        image_num = random.randint(0, 6)
        self.image = pygame.image.load(opponent_images[image_num])
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(
            center=(
                x_val,
                -70,
            )
        )

        self.speed = random.uniform(1, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the bottom of the screen
    def update(self, lanes):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > 600:
            if self.rect.centerx == OPPONENT_X_POS[0]:
                opp_lanes[0] = 0
            if self.rect.centerx == OPPONENT_X_POS[1]:
                opp_lanes[1] = 0
            if self.rect.centerx == OPPONENT_X_POS[2]:
                opp_lanes[2] = 0
            if self.rect.centerx == OPPONENT_X_POS[3]:
                opp_lanes[3] = 0
            if self.rect.centerx == OPPONENT_X_POS[4]:
                opp_lanes[4] = 0
            if self.rect.centerx == OPPONENT_X_POS[5]:
                opp_lanes[5] = 0
            entity.kill()


# sets current state to running
running = True
player = PlayerCar([100, 100])
x_pos = 146
y_pos = 350
opp_x_pos = 0
new_opp = 0
opp_lanes = [0, 0, 0, 0, 0, 0]

# sprite groups to store sprites
opp = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# player score variable
player_score = 0
high_score = shelve.open('assets/high_score.txt')
highscore = high_score['high_score']
# sets the font
font = pygame.font.Font('assets/Grand9kPixel.ttf', 16)
title_font = pygame.font.Font('assets/Grand9kPixel.ttf', 32)
# sets the game state to menu screen
menu_screen = True
game_over = False

# while loop for menu screen
while menu_screen:
    # checks if user clicked the close button
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                menu_screen = False
        elif event.type == pygame.QUIT:
            running = False
            menu_screen = False
    if bg_frame > 3:
        bg_frame = 0 
    BackGround = Background(background_images[bg_frame], [0, 0])
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)

    player = PlayerCar([y_pos, x_pos])
    screen.blit(player.image, player.rect)

    # displays title and instructions
    title = title_font.render("Pixel Car 2D", True, white)
    titleRect = title.get_rect()
    titleRect.center = (165, 100)
    screen.blit(title, titleRect)

    instructions = font.render("PRESS SPACE BAR TO START", True, white)
    instructionRect = instructions.get_rect()
    instructionRect.center = (165, 200)
    screen.blit(instructions, instructionRect)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
        menu_screen = False

    bg_frame += 1
    pygame.display.update()
    clock.tick(32)


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
        y_pos -= 6
    if pressed_keys[K_DOWN]:
        y_pos += 6
    if pressed_keys[K_LEFT]:
        x_pos -= 6
    if pressed_keys[K_RIGHT]:
        x_pos += 6

    # checks if player has pressed R to reset high score
    if pressed_keys[K_r]:
        high_score['high_score'] = 0
        highscore = 0

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

    new_opp = random.randint(0, 96)
    # checks if there are no cars in lane and randomly creates a new opponent
    if new_opp == 0 and opp_lanes[0] == 0:
        opponent = Opponent(OPPONENT_X_POS[0])
        all_sprites.add(opponent)
        opp.add(opponent)
        opp_lanes[0] = 1
    if new_opp == 1 and opp_lanes[1] == 0:
        opponent = Opponent(OPPONENT_X_POS[1])
        all_sprites.add(opponent)
        opp.add(opponent)
        opp_lanes[1] = 1
    if new_opp == 2 and opp_lanes[2] == 0:
        opponent = Opponent(OPPONENT_X_POS[2])
        all_sprites.add(opponent)
        opp.add(opponent)
        opp_lanes[2] = 1
    if new_opp == 3 and opp_lanes[3] == 0:
        opponent = Opponent(OPPONENT_X_POS[3])
        all_sprites.add(opponent)
        opp.add(opponent)
        opp_lanes[3] = 1
    if new_opp == 4 and opp_lanes[4] == 0:
        opponent = Opponent(OPPONENT_X_POS[4])
        all_sprites.add(opponent)
        opp.add(opponent)
        opp_lanes[4] = 1
    if new_opp == 5 and opp_lanes[5] == 0:
        opponent = Opponent(OPPONENT_X_POS[5])
        all_sprites.add(opponent)
        opp.add(opponent)
        opp_lanes[5] = 1

    # displays all opponents on screen
    for entity in opp:
        screen.blit(entity.image, entity.rect)
        entity.update(opp_lanes)

    # checks for any collisions between the player and opponent
    if pygame.sprite.spritecollideany(player, opp):
        # If so, then stop score increasing and display game over screen
        game_over = True

    while game_over:
        # checks if user clicked the close button
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    game_over = False
            elif event.type == pygame.QUIT:
                running = False
                game_over = False
        final_score = str(player_score)
        final_score_text = title_font.render(final_score, True, white)
        finalscrRect = final_score_text.get_rect()
        finalscrRect.center = (165, 200)
        screen.blit(final_score_text, finalscrRect)
        game_over_text = title_font.render("GAME OVER", True, white)
        gameoverRect = game_over_text.get_rect()
        gameoverRect.center = (165, 100)
        screen.blit(game_over_text, gameoverRect)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            player_score = 0
            x_pos = 146
            y_pos = 350
            for entity in opp:
                entity.kill()
            opp_lanes = [0, 0, 0, 0, 0, 0]
            game_over = False

        pygame.display.update()

    display_score = "SCORE: " + str(player_score)
    display_hiscore = "HISCORE: " + str(highscore)
    text = font.render(display_score, True, white)
    text_hi = font.render(display_hiscore, True, white)
    textRect = text.get_rect()
    text_hiRect = text_hi.get_rect()
    textRect.bottomright = (295, 45)
    text_hiRect.bottomright = (295, 25)
    screen.blit(text, textRect)
    screen.blit(text_hi, text_hiRect)
    player_score += 1

    if highscore <= player_score:
        high_score['high_score'] = player_score
        highscore = player_score

    bg_frame += 1
    pygame.display.update()
    clock.tick(32)
