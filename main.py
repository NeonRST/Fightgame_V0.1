import pygame
from Playable import Player
from pygame import mixer

# Pk is coming
mixer.init()
pygame.init()

# frame rate
FPS = 60
clock = pygame.time.Clock()

# Window Size
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Anime Battle")

# define colors
black = "Black"
green = "Green"
white = "White"
red = "Red"

# define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()

# player scores. [P1, P2]
score = [0, 0]
round_over = False
ROUND_OVER_COOLDOWN = 3000

# define fighter variables
Player1_size = 128
Player1_scale = 2
Player1_offset = [100, 200]
Player1_data = [Player1_size, Player1_scale, Player1_offset]
Player2_size = 128
Player2_scale = 2
Player2_offset = [100, 200]
Player2_data = [Player2_size, Player2_scale, Player2_offset]

# load music and sounds
pygame.mixer.music.load("graphics/audio/background_music1.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
Death_SFX = pygame.mixer.Sound("graphics/audio/death.mp3")
Player1_attack = pygame.mixer.Sound("graphics/audio/punch.mp3")
Player1_attack.set_volume(0.5)
Player2_attack = pygame.mixer.Sound("graphics/audio/woosh.mp3")
Player2_attack.set_volume(0.9)

# load background image
background_image = pygame.image.load("graphics/images/background/merlion.jpg").convert_alpha()
# menu image
menu_image = pygame.image.load("graphics/images/menu/menu.jpg").convert_alpha()
menu_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 50)
menu_surface = menu_font.render("start", True, "Red")
menu_surface_rect = menu_surface.get_rect(midbottom=(960, 300))
menu = True
# load sprite sheets
Player1_spritesheet = pygame.image.load("graphics/Fighter/Fighter_Spritelist.png").convert_alpha()
Player2_spritesheet = pygame.image.load("graphics/Shinobi/Shinobi_Spritelist.png").convert_alpha()
# define number of steps in each animation
Player1_step = [6, 8, 8, 10, 4, 3, 4, 2, 3, 3]
Player2_step = [6, 8, 8, 12, 5, 3, 4, 4, 2, 4]
# define font
Exit_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 50)
count_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 80)
score_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 30)
Victory_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 150)
Victory_surface = Victory_font.render("Fatality", True, "Red")
Victory_surface_rect = Victory_surface.get_rect(midbottom=(960, 550))
Exit_surface = Exit_font.render("Exit", True, "Black")
Exit_surface_rect = Exit_surface.get_rect(midbottom=(960, 80))
# function for drawing background


def draw_menu():
    scaled_menu = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_menu, (0, 0))

def draw_background():
    scaled_bg = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 200
    pygame.draw.rect(screen, white, (x - 2, y - 2, 608, 34))
    pygame.draw.rect(screen, red, (x, y, 600, 30))
    pygame.draw.rect(screen, green, (x, y, 600 * ratio, 30))


# create two instances of fighters
Player1_spawn = Player(1, 200, 1120, False, Player1_data, Player1_spritesheet,
                       Player1_step, Player1_attack)
Player2_spawn = Player(2, 1800, 1120, True, Player2_data, Player2_spritesheet,
                       Player2_step, Player2_attack)

# game loop
run = True
while run:
    clock.tick(FPS)
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Exit_surface_rect.collidepoint(pygame.mouse.get_pos()):
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_surface_rect.collidepoint(pygame.mouse.get_pos()):
                menu = False
    # draw background
    if menu:
        draw_menu()
        screen.blit(menu_surface, menu_surface_rect)
    else:
        draw_background()
        # Exit
        screen.blit(Exit_surface, Exit_surface_rect)
        # show player stats
        draw_health_bar(Player1_spawn.health, 20, 20)
        draw_health_bar(Player2_spawn.health, 1300, 20)
        draw_text("Player1: " + str(score[0]), score_font, black, 20, 60)
        draw_text("Player2: " + str(score[1]), score_font, black, 1300, 60)
        # update countdown
        if intro_count <= 0:
            # move fighters
            Player1_spawn.move(SCREEN_WIDTH, SCREEN_HEIGHT, Player2_spawn, round_over)
            Player2_spawn.move(SCREEN_WIDTH, SCREEN_HEIGHT, Player1_spawn, round_over)
        else:
            # display count
            draw_text(str(intro_count), count_font, red, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
            # update count timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro_count -= 1
                last_count_update = pygame.time.get_ticks()

        # spawn
        Player1_spawn.update()
        Player1_spawn.draw(screen)
        Player2_spawn.update()
        Player2_spawn.draw(screen)

        # check for player defeat
        if round_over == False:
            if not Player1_spawn.alive:
                pygame.mixer.Sound.play(Death_SFX)
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif not Player2_spawn.alive:
                pygame.mixer.Sound.play(Death_SFX)
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else:
            # display victory
            screen.blit(Victory_surface, Victory_surface_rect)
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                round_over = False
                intro_count = 3
                Player1_spawn = Player(1, 200, 1120, False, Player1_data, Player1_spritesheet, Player1_step, Player1_attack)
                Player2_spawn = Player(2, 1800, 1120, True, Player2_data, Player2_spritesheet, Player2_step, Player2_attack)
        # update display
    pygame.display.update()

# exit pygame
pygame.quit()
