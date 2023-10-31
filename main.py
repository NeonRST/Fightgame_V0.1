import pygame
from Playable import Player
from pygame import mixer
from choose import Choose

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
# character select:
Fighter = "graphics/Fighter/Fighter_Spritelist.png"
Shinobi = "graphics/Shinobi/Shinobi_Spritelist.png"
Samurai = "graphics/Samurai/Samurai_Spritelist.png"
Gotoku = "graphics/Gotoku/Gotoku_spritelist.png"
Onre = "graphics/Onre/Onre_spritelist.png"
# define number of steps in each animation
Fighter_step = [6, 8, 8, 10, 4, 3, 4, 2, 3, 3]
Shinobi_step = [6, 8, 8, 12, 5, 3, 4, 4, 2, 4]
Samurai_step = [6, 8, 8, 12, 6, 4, 3, 2, 2, 3]
Gotoku_step = [5, 6, 7, 8, 4, 4, 4, 3, 4, 6]
Onre_step = [6, 7, 7, 6, 4, 4, 5, 7, 3, 7]
# p1 p2 defaults
p1_Char = "graphics/Fighter/Fighter_Spritelist.png"
p2_Char = "graphics/Shinobi/Shinobi_Spritelist.png"
attack_style_p1 = 0 # default is at zero
attack_style_p2 = 0
Player1_step = [6, 8, 8, 10, 4, 3, 4, 2, 3, 3]
Player2_step = [6, 8, 8, 12, 5, 3, 4, 4, 2, 4]
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

# menu
menu_image = pygame.image.load("graphics/images/menu/menu.jpg").convert_alpha()
start_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 100)
start_surface = start_font.render("start", True, "Black")
start_surface_rect = start_surface.get_rect(midbottom=(870, 300))
menu_choose1 = Choose("graphics/fonts/Bulletproof.ttf", "Player1", 600, 450, 50, "red")
menu_choose2 = Choose("graphics/fonts/Bulletproof.ttf", "Player2", 1100, 450, 50, "red")

# load background image
background_image = pygame.image.load("graphics/images/background/shrek.jpg").convert_alpha()
# character choose
menu_p1_fighter = Choose("graphics/fonts/Bulletproof.ttf", "Fighter", 600,
                         500, 30)
menu_p1_shinobi = Choose("graphics/fonts/Bulletproof.ttf", "Shinobi", 600,
                         550, 30)
menu_p1_samurai = Choose("graphics/fonts/Bulletproof.ttf", "Samurai", 600,
                         600, 30)
menu_p1_gotoku = Choose("graphics/fonts/Bulletproof.ttf", "Gotoku", 600,
                        650, 30)
menu_p1_Onre = Choose("graphics/fonts/Bulletproof.ttf", "Onre", 600, 700,
                      30)
menu_p2_fighter = Choose("graphics/fonts/Bulletproof.ttf", "Fighter", 1100,
                         500, 30)
menu_p2_shinobi = Choose("graphics/fonts/Bulletproof.ttf", "Shinobi", 1100,
                         550, 30)
menu_p2_samurai = Choose("graphics/fonts/Bulletproof.ttf", "Samurai", 1100,
                         600, 30)
menu_p2_gotoku = Choose("graphics/fonts/Bulletproof.ttf", "Gotoku", 1100,
                        650, 30)
menu_p2_Onre = Choose("graphics/fonts/Bulletproof.ttf", "Onre", 1100, 700,
                      30)

# load sprite sheets
Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()

# define font
Exit_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 50)
count_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 80)
score_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 30)
Victory_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 150)
Victory_surface = Victory_font.render("Fatality", True, "Red")
Victory_surface_rect = Victory_surface.get_rect(midbottom=(960, 550))
Exit_surface = Exit_font.render("Exit", True, "Black")
Exit_surface_rect = Exit_surface.get_rect(midbottom=(960, 80))


def draw_menu():
    scaled_menu = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_menu, (0, 0))
    Choose.draw_menu(menu_choose1, screen)
    # p1
    Choose.draw_menu(menu_choose2, screen)
    Choose.draw_menu(menu_p1_fighter, screen)
    Choose.draw_menu(menu_p1_shinobi, screen)
    Choose.draw_menu(menu_p1_samurai, screen)
    Choose.draw_menu(menu_p1_gotoku, screen)
    Choose.draw_menu(menu_p1_Onre, screen)
    # p2
    Choose.draw_menu(menu_p2_fighter, screen)
    Choose.draw_menu(menu_p2_shinobi, screen)
    Choose.draw_menu(menu_p2_samurai, screen)
    Choose.draw_menu(menu_p2_gotoku, screen)
    Choose.draw_menu(menu_p2_Onre, screen)


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

menu = True
run = False
while menu:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_surface_rect.collidepoint(pygame.mouse.get_pos()):
                menu = False
                run = True
            if menu_p1_fighter[3].collidepoint(pygame.mouse.get_pos()):
                p1_Char = Fighter
                Player1_step = Fighter_step
                Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                attack_style_p1 = 0
            if menu_p1_shinobi[3].collidepoint(pygame.mouse.get_pos()):
                p1_Char = Shinobi
                Player1_step = Shinobi_step
                Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                attack_style_p1 = 1
            if menu_p1_samurai[3].collidepoint(pygame.mouse.get_pos()):
                p1_Char = Samurai
                Player1_step = Samurai_step
                Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                attack_style_p1 = 2
            if menu_p1_gotoku[3].collidepoint(pygame.mouse.get_pos()):
                p1_Char = Gotoku
                Player1_step = Gotoku_step
                Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                attack_style_p1 = 3
            if menu_p1_Onre[3].collidepoint(pygame.mouse.get_pos()):
                p1_Char = Onre
                Player1_step = Onre_step
                Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                attack_style_p1 = 4

            # player 2
            if menu_p2_fighter[3].collidepoint(pygame.mouse.get_pos()):
                p2_Char = Fighter
                Player2_step = Fighter_step
                Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                attack_style_p2 = 0
            if menu_p2_shinobi[3].collidepoint(pygame.mouse.get_pos()):
                p2_Char = Shinobi
                Player2_step = Shinobi_step
                Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                attack_style_p2 = 1
            if menu_p2_samurai[3].collidepoint(pygame.mouse.get_pos()):
                p2_Char = Samurai
                Player2_step = Samurai_step
                Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                attack_style_p2 = 2
            if menu_p2_gotoku[3].collidepoint(pygame.mouse.get_pos()):
                p2_Char = Gotoku
                Player2_step = Gotoku_step
                Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                attack_style_p2 = 3
            if menu_p2_Onre[3].collidepoint(pygame.mouse.get_pos()):
                p2_Char = Onre
                Player2_step = Onre_step
                Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                attack_style_p2 = 4

    draw_menu()
    screen.blit(start_surface, start_surface_rect)
    pygame.display.update()

Player1_spawn = Player(1, 200, 1120, False, Player1_data, Player1_spritesheet,
                       Player1_step, Player1_attack, attack_style_p1)
Player2_spawn = Player(2, 1800, 1120, True, Player2_data, Player2_spritesheet,
                       Player2_step, Player2_attack, attack_style_p2)
while run:
    clock.tick(FPS)
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Exit_surface_rect.collidepoint(pygame.mouse.get_pos()):
                run = False

    # draw background
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
    Player2_spawn.update()
    Player1_spawn.draw(screen)
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
            Player1_spawn = Player(1, 200, 1120, False, Player1_data,
                                   Player1_spritesheet, Player1_step,
                                   Player1_attack, attack_style_p1)
            Player2_spawn = Player(2, 1800, 1120, True, Player2_data,
                                   Player2_spritesheet, Player2_step,
                                   Player2_attack, attack_style_p2)
    # update display
    pygame.display.update()

# exit pygame
pygame.quit()
