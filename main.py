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
pygame.display.set_caption("Battle")

# define colors
black = "Black"
green = "Green"
white = (255, 255, 255)
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
Fighter_selected_1 = False
Fighter_selected_2 = False
Shinobi_selected_1 = False
Shinobi_selected_2 = False
Samurai_selected_1 = False
Samurai_selected_2 = False
Gotoku_selected_1 = False
Gotoku_selected_2 = False
Onre_selected_1 = False
Onre_selected_2 = False
# define number of steps in each animation
Fighter_step = [6, 8, 8, 10, 4, 3, 4, 2, 3, 3]
Shinobi_step = [6, 8, 8, 12, 5, 3, 4, 4, 2, 4]
Samurai_step = [6, 8, 8, 12, 6, 4, 3, 2, 2, 3]
Gotoku_step = [5, 6, 7, 8, 4, 4, 4, 3, 4, 6]
Onre_step = [6, 7, 7, 6, 5, 4, 4, 7, 3, 7]
# p1 p2 defaults
p1_Char = "graphics/Fighter/Fighter_Spritelist.png"
p2_Char = "graphics/Shinobi/Shinobi_Spritelist.png"
attack_style_p1 = 0 # default is at zero
attack_style_p2 = 0
Player1_step = [6, 8, 8, 10, 4, 3, 4, 2, 3, 3]
Player2_step = [6, 8, 8, 12, 5, 3, 4, 4, 2, 4]
Player1_character_selected = False
Player2_character_selected = False
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
menu_rendered = "graphics/images/menu/water.jpg"
menu_image = pygame.image.load(menu_rendered).convert_alpha()
start_font = pygame.font.Font("graphics/fonts/Bulletproof.ttf", 100)
start_surface = start_font.render("start", True, "Black")
start_surface_rect = start_surface.get_rect(midbottom=(950, 350))
menu_choose1 = Choose("graphics/fonts/Bulletproof.ttf", "Player1", 700, 450,
                      50, "red")
menu_choose2 = Choose("graphics/fonts/Bulletproof.ttf", "Player2", 1200,
                      450, 50, "red")

# character choose
menu_p1_fighter = Choose("graphics/fonts/Bulletproof.ttf", "Fighter", 700,
                         500, 30)
menu_p1_shinobi = Choose("graphics/fonts/Bulletproof.ttf", "Shinobi", 700,
                         550, 30)
menu_p1_samurai = Choose("graphics/fonts/Bulletproof.ttf", "Samurai", 700,
                         600, 30)
menu_p1_gotoku = Choose("graphics/fonts/Bulletproof.ttf", "Gotoku", 700,
                        650, 30)
menu_p1_Onre = Choose("graphics/fonts/Bulletproof.ttf", "Onre", 700, 700,
                      30)
menu_p2_fighter = Choose("graphics/fonts/Bulletproof.ttf", "Fighter", 1200,
                         500, 30)
menu_p2_shinobi = Choose("graphics/fonts/Bulletproof.ttf", "Shinobi", 1200,
                         550, 30)
menu_p2_samurai = Choose("graphics/fonts/Bulletproof.ttf", "Samurai", 1200,
                         600, 30)
menu_p2_gotoku = Choose("graphics/fonts/Bulletproof.ttf", "Gotoku", 1200,
                        650, 30)
menu_p2_Onre = Choose("graphics/fonts/Bulletproof.ttf", "Onre", 1200, 700,
                      30)
selected = False

# map
menu_map_choose = Choose("graphics/fonts/Bulletproof.ttf", "Map", 950,450, 50, "red")

map1_menu = Choose("graphics/fonts/Bulletproof.ttf", "Shrek", 950,
                         500, 30)
map2_menu = Choose("graphics/fonts/Bulletproof.ttf", "Singapore", 950,
                         550, 30)
map3_menu = Choose("graphics/fonts/Bulletproof.ttf", "Forrest", 950,
                         600, 30)
map4_menu = Choose("graphics/fonts/Bulletproof.ttf", "Lost Island", 950,
                         650, 30)
map5_menu = Choose("graphics/fonts/Bulletproof.ttf", "Hanamura", 950,
                         700, 30)

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
Exit_to_menu_surface = Exit_font.render("Exit", True, "White")
Exit_to_menu_surface_rect = Exit_to_menu_surface.get_rect(midbottom=(960, 80))
bg_image_load = "graphics/images/background/forrest.png"
render_map_selected = False
map1_selected = False
map2_selected = False
map3_selected = False
map4_selected = False
map5_selected = False

# load background image
background_image = pygame.image.load(bg_image_load).convert_alpha()


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

    # map
    Choose.draw_menu(menu_map_choose, screen)
    Choose.draw_menu(map1_menu, screen)
    Choose.draw_menu(map2_menu, screen)
    Choose.draw_menu(map3_menu, screen)
    Choose.draw_menu(map4_menu, screen)
    Choose.draw_menu(map5_menu, screen)


# draw background
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
    screen.blit(Exit_surface, Exit_surface_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_surface_rect.collidepoint(pygame.mouse.get_pos()):
                menu = False
                run = True
            if menu_p1_fighter[3].collidepoint(pygame.mouse.get_pos()):
                if Player1_character_selected == False or Fighter_selected_1:
                    if not Fighter_selected_1:
                        p1_Char = Fighter
                        Player1_step = Fighter_step
                        Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                        attack_style_p1 = 0
                        menu_p1_fighter = Choose("graphics/fonts/Bulletproof.ttf", "Fighter", 700, 500, 30, white)
                        Player1_character_selected = True
                        Fighter_selected_1 = True
                    elif Fighter_selected_1:
                        menu_p1_fighter = Choose(
                            "graphics/fonts/Bulletproof.ttf",
                            "Fighter", 700,
                            500, 30, black)
                        Player1_character_selected = False
                        Fighter_selected_1 = False

            if menu_p1_shinobi[3].collidepoint(pygame.mouse.get_pos()):
                if Player1_character_selected == False or Shinobi_selected_1:
                    if not Shinobi_selected_1:
                        p1_Char = Shinobi
                        Player1_step = Shinobi_step
                        Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                        attack_style_p1 = 1
                        menu_p1_shinobi = Choose("graphics/fonts/Bulletproof.ttf","Shinobi", 700, 550, 30, white)
                        Player1_character_selected = True
                        Shinobi_selected_1 = True
                    elif Shinobi_selected_1:
                        menu_p1_shinobi = Choose(
                            "graphics/fonts/Bulletproof.ttf",
                            "Shinobi", 700,
                            550, 30, black)
                        Player1_character_selected = False
                        Shinobi_selected_1 = False

            if menu_p1_samurai[3].collidepoint(pygame.mouse.get_pos()):
                if Player1_character_selected == False or Samurai_selected_1:
                    if not Samurai_selected_1:
                        p1_Char = Samurai
                        Player1_step = Samurai_step
                        Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                        attack_style_p1 = 2
                        menu_p1_samurai = Choose("graphics/fonts/Bulletproof.ttf",
                                                 "Samurai", 700,
                                                 600, 30, white)
                        Player1_character_selected = True
                        Samurai_selected_1 = True
                    elif Samurai_selected_1:
                        menu_p1_samurai = Choose(
                            "graphics/fonts/Bulletproof.ttf",
                            "Samurai", 700,
                            600, 30, black)
                        Player1_character_selected = False
                        Samurai_selected_1 = False

            if menu_p1_gotoku[3].collidepoint(pygame.mouse.get_pos()):
                if Player1_character_selected == False or Gotoku_selected_1:
                    if not Gotoku_selected_1:
                        p1_Char = Gotoku
                        Player1_step = Gotoku_step
                        Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                        attack_style_p1 = 3
                        menu_p1_gotoku = Choose("graphics/fonts/Bulletproof.ttf",
                                                "Gotoku", 700,
                                                650, 30, white)
                        Player1_character_selected = True
                        Gotoku_selected_1 = True
                    elif Gotoku_selected_1:
                        menu_p1_gotoku = Choose(
                            "graphics/fonts/Bulletproof.ttf",
                            "Gotoku", 700,
                            650, 30, black)
                        Player1_character_selected = False
                        Gotoku_selected_1 = False
            if menu_p1_Onre[3].collidepoint(pygame.mouse.get_pos()):
                if Player1_character_selected == False or Onre_selected_1:
                    if not Onre_selected_1:
                        p1_Char = Onre
                        Player1_step = Onre_step
                        Player1_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                        attack_style_p1 = 4
                        menu_p1_Onre = Choose("graphics/fonts/Bulletproof.ttf", "Onre",
                                              700, 700,
                                              30, white)
                        Player1_character_selected = True
                        Onre_selected_1 = True
                    elif Onre_selected_1:
                        menu_p1_Onre = Choose("graphics/fonts/Bulletproof.ttf",
                                              "Onre",
                                              700, 700,
                                              30, black)
                        Player1_character_selected = False
                        Onre_selected_1 = False

            if menu_p2_fighter[3].collidepoint(pygame.mouse.get_pos()):
                if Player2_character_selected == False or Fighter_selected_2:
                    if not Fighter_selected_2:
                        p2_Char = Fighter
                        Player2_step = Fighter_step
                        Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                        attack_style_p1 = 0
                        menu_p2_fighter = Choose("graphics/fonts/Bulletproof.ttf", "Fighter", 1200, 500, 30, white)
                        Player2_character_selected = True
                        Fighter_selected_2 = True
                    elif Fighter_selected_2:
                        menu_p2_fighter = Choose(
                            "graphics/fonts/Bulletproof.ttf",
                            "Fighter", 1200,
                            500, 30, black)
                        Player2_character_selected = False
                        Fighter_selected_2 = False

            if menu_p2_shinobi[3].collidepoint(pygame.mouse.get_pos()):
                if Player2_character_selected == False or Shinobi_selected_2:
                    if not Shinobi_selected_2:
                        p2_Char = Shinobi
                        Player2_step = Shinobi_step
                        Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                        attack_style_p2 = 1
                        menu_p2_shinobi = Choose("graphics/fonts/Bulletproof.ttf","Shinobi", 1200, 550, 30, white)
                        Player2_character_selected = True
                        Shinobi_selected_2 = True
                    elif Shinobi_selected_2:
                        menu_p2_shinobi = Choose(
                            "graphics/fonts/Bulletproof.ttf",
                            "Shinobi", 1200,
                            550, 30, black)
                        Player2_character_selected = False
                        Shinobi_selected_2 = False

            if menu_p2_samurai[3].collidepoint(pygame.mouse.get_pos()):
                if Player2_character_selected == False or Samurai_selected_2:
                    if not Samurai_selected_2:
                        p2_Char = Samurai
                        Player2_step = Samurai_step
                        Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                        attack_style_p2 = 2
                        menu_p2_samurai = Choose("graphics/fonts/Bulletproof.ttf",
                                                 "Samurai", 1200,
                                                 600, 30, white)
                        Player2_character_selected = True
                        Samurai_selected_2 = True
                    elif Samurai_selected_2:
                        menu_p2_samurai = Choose(
                            "graphics/fonts/Bulletproof.ttf",
                            "Samurai", 1200,
                            600, 30, black)
                        Player2_character_selected = False
                        Samurai_selected_2 = False

            if menu_p2_gotoku[3].collidepoint(pygame.mouse.get_pos()):
                if Player2_character_selected == False or Gotoku_selected_2:
                    if not Gotoku_selected_2:
                        p2_Char = Gotoku
                        Player2_step = Gotoku_step
                        Player2_spritesheet = pygame.image.load(p2_Char).convert_alpha()
                        attack_style_p2 = 3
                        menu_p2_gotoku = Choose("graphics/fonts/Bulletproof.ttf",
                                                "Gotoku", 1200,
                                                650, 30, white)
                        Player2_character_selected = True
                        Gotoku_selected_2 = True
                    elif Gotoku_selected_2:
                        menu_p2_gotoku = Choose(
                            "graphics/fonts/Bulletproof.ttf",
                            "Gotoku", 1200,
                            650, 30, black)
                        Player2_character_selected = False
                        Gotoku_selected_2 = False
            if menu_p2_Onre[3].collidepoint(pygame.mouse.get_pos()):
                if Player2_character_selected == False or Onre_selected_2:
                    if not Onre_selected_2:
                        p2_Char = Onre
                        Player2_step = Onre_step
                        Player2_spritesheet = pygame.image.load(p1_Char).convert_alpha()
                        attack_style_p2 = 4
                        menu_p2_Onre = Choose("graphics/fonts/Bulletproof.ttf", "Onre",
                                              1200, 700,
                                              30, white)
                        Player2_character_selected = True
                        Onre_selected_2 = True
                    elif Onre_selected_2:
                        menu_p2_Onre = Choose("graphics/fonts/Bulletproof.ttf",
                                              "Onre",
                                              1200, 700,
                                              30, black)
                        Player2_character_selected = False
                        Onre_selected_2 = False
            # map selection
            if map1_menu[3].collidepoint(pygame.mouse.get_pos()):
                if not render_map_selected or map1_selected:
                    if not map1_selected:
                        background_image = "graphics/images/background/shrek.jpg"
                        map1_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Shrek", 950, 500, 30, white)
                        background_image = pygame.image.load(background_image).convert_alpha()
                        render_map_selected = True
                        map1_selected = True
                    elif map1_selected:
                        map1_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Shrek", 950,
                                           500, 30, black)
                        map1_selected = False
                        render_map_selected = False
            if map2_menu[3].collidepoint(pygame.mouse.get_pos()):
                if not render_map_selected or map2_selected:
                    if not map2_selected:
                        background_image = "graphics/images/background/merlion.jpg"
                        map2_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Singapore", 950, 550, 30, white)
                        background_image = pygame.image.load(background_image).convert_alpha()
                        render_map_selected = True
                        map2_selected = True
                    elif map2_selected:
                        map2_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Singapore", 950,
                                           550, 30, black)
                        map2_selected = False
                        render_map_selected = False
            if map3_menu[3].collidepoint(pygame.mouse.get_pos()):
                if not render_map_selected or map3_selected:
                    if not map3_selected:
                        background_image = "graphics/images/background/forrest.png"
                        map3_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Forrest", 950, 600, 30, white)
                        background_image = pygame.image.load(background_image).convert_alpha()
                        render_map_selected = True
                        map3_selected = True
                    elif map3_selected:
                        map3_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Forrest", 950,
                                           600, 30, black)
                        map3_selected = False
                        render_map_selected = False
            if map4_menu[3].collidepoint(pygame.mouse.get_pos()):
                if not render_map_selected or map4_selected:
                    if not map4_selected:
                        background_image = "graphics/images/background/lost_island.jpg"
                        map4_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Lost Island", 950, 650, 30, white)
                        background_image = pygame.image.load(background_image).convert_alpha()
                        render_map_selected = True
                        map4_selected = True
                    elif map4_selected:
                        map4_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Lost Island", 950,
                                           650, 30, black)
                        map4_selected = False
                        render_map_selected = False

            if map5_menu[3].collidepoint(pygame.mouse.get_pos()):
                if not render_map_selected or map5_selected:
                    if not map5_selected:
                        background_image = "graphics/images/background/hanamura.jpg"
                        map5_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Hanamura", 950, 700, 30, white)
                        background_image = pygame.image.load(background_image).convert_alpha()
                        render_map_selected = True
                        map5_selected = True
                    elif map5_selected:
                        map5_menu = Choose("graphics/fonts/Bulletproof.ttf",
                                           "Hanamura", 950,
                                           700, 30, black)
                        map5_selected = False
                        render_map_selected = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Exit_to_menu_surface_rect.collidepoint(pygame.mouse.get_pos()):
                    menu = False

    draw_menu()
    screen.blit(start_surface, start_surface_rect)
    screen.blit(Exit_surface, Exit_surface_rect)
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
            if Exit_to_menu_surface_rect.collidepoint(pygame.mouse.get_pos()):
                menu = True
                run = False

    # draw background
    draw_background()
    # Exit
    screen.blit(Exit_to_menu_surface, Exit_to_menu_surface_rect)
    # show player stats
    draw_health_bar(Player1_spawn.health, 20, 20)
    draw_health_bar(Player2_spawn.health, 1300, 20)
    draw_text("Player1: " + str(score[0]), score_font, white, 20, 60)
    draw_text("Player2: " + str(score[1]), score_font, white, 1300, 60)
    # update countdown
    if intro_count <= 0:
        # move fighters544433
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
