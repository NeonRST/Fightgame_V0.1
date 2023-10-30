import pygame



pygame.init()
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("shoot me")

fly = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
snail = pygame.image.load("graphics/snail/snail1r.png").convert_alpha()
fly_rect = fly.get_rect(midleft=(700, 700))
snail_rect = snail.get_rect(midright=(100, 100))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.image.load("graphics/snail/snail1_r.png").convert_alpha()
                bullet_rect = bullet.get_rect(topleft=(snail_rect.x,snail_rect.y))
                screen.blit(bullet, bullet_rect)
                bullet_rect.x += 2
    screen.fill("brown")
    screen.blit(snail, snail_rect)
    screen.blit(fly, fly_rect)
    key = pygame.key.get_pressed()
    key_r = pygame.key.get_focused()
    if key[pygame.K_a]:
        snail_rect.x -= 1
    if key[pygame.K_d]:
        snail_rect.x += 1
    if key[pygame.K_s]:
        snail_rect.y += 1
    if key[pygame.K_w]:
        snail_rect.y -= 1
    if key[pygame.K_LEFT]:
        fly_rect.x -= 1
    if key[pygame.K_RIGHT]:
        fly_rect.x += 1
    if key[pygame.K_DOWN]:
        fly_rect.y += 1
    if key[pygame.K_UP]:
        fly_rect.y -= 1
    pygame.display.update()
