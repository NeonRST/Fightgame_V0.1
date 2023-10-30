import pygame


class Player():
    def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 40, 40))
        self.vel_y = 0
        self.walking = False
        self.running = False
        self.jump = False
        self.attacking = False
        self.blocking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attack_val = 0
        self.attack_sound = sound
        self.hit = False
        self.health = 200
        self.alive = True
        self.menu = False

    def load_images(self, sprite_sheet, animation_steps):
        # extract images from sprite sheet
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, target, round_over):
        speed = 10
        gravity = 2
        dx = 0
        dy = 0
        self.running = False
        self.blocking = False
        self.attack_type = 0

        # get key press
        key = pygame.key.get_pressed()
        # can only perform other actions if not currently attacking
        if self.attacking == False and self.alive == True and not round_over:
            # check player 1 controls
            if self.player == 1:
                # movement
                if key[pygame.K_a]:
                    dx = -speed
                    self.running = True
                elif key[pygame.K_d]:
                    dx = speed
                    self.running = True
                    # jump
                if (key[pygame.K_SPACE] or key[pygame.K_w]) and not self.jump:
                    self.vel_y = -30
                    self.jump = True
                if key[pygame.K_s] and not self.running:
                    self.blocking = True
                # attack
                if key[pygame.K_j] or key[pygame.K_k] or key[pygame.K_l]:
                    # determine which attack type was used
                    if key[pygame.K_j]:
                        self.attack_type = 1
                        self.attack_val = 0
                    if key[pygame.K_k]:
                        self.attack_type = 2
                        self.attack_val = 1
                    if key[pygame.K_l]:
                        self.attack_type = 3
                        self.attack_val = 2
                    self.attack(target)

            # check player 2 controls
            if self.player == 2:
                # movement
                if key[pygame.K_LEFT]:
                    dx = -speed
                    self.running = True
                elif key[pygame.K_RIGHT]:
                    dx = speed
                    self.running = True
                # jump
                if key[pygame.K_UP] and not self.jump:
                    self.vel_y = -30
                    self.jump = True
                if key[pygame.K_DOWN] and not self.running:
                    self.blocking = True
                # attack
                if key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]:
                    # determine which attack type was used
                    if key[pygame.K_KP1]:
                        self.attack_type = 1
                        self.attack_val = 0
                    if key[pygame.K_KP2]:
                        self.attack_type = 2
                        self.attack_val = 1
                    if key[pygame.K_KP3]:
                        self.attack_type = 3
                        self.attack_val = 2
                    self.attack(target)

        # apply gravity
        self.vel_y += gravity
        dy += self.vel_y
        #
        # # ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height + 80:
            self.vel_y = 0
            self.jump = False
            dy = screen_height + 80 - self.rect.bottom

        # ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # apply attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # update player position
        self.rect.x += dx
        self.rect.y += dy

    # handle animation updates
    def update(self):
        # check what action the player is performing
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(9)  # 9:death
        elif self.hit == True:
            self.update_action(8)  # 8:hit
        elif self.blocking == True:
            self.update_action(7)  # 7:block
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(4)  # 4:attack1
            elif self.attack_type == 2:
                self.update_action(5)  # 5:attack2
            elif self.attack_type == 3:
                self.update_action(6)  # 6:attack2
        elif self.jump == True:
            self.update_action(3)  # 3:jump
        elif self.walking == True:
            self.update_action(1)  # 1:walk
        elif self.running == True:
            self.update_action(2) # 2:run
        else:
            self.update_action(0)  # 0:idle

        animation_cooldown = 50
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # check if the animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            # if the player is dead then end the animation
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                # check if an attack was executed
                if self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 10
                if self.action == 5:
                    self.attacking = False
                    self.attack_cooldown = 1
                if self.action == 6:
                    self.attacking = False
                    self.attack_cooldown = 30
                # check if damage was taken
                if self.action == 8:
                    self.hit = False
                # if the player was in the middle of an attack, then the attack
                    # is stopped
                    self.attacking = False
                    self.attack_cooldown = 20

    def attack(self, target):

        if self.attack_cooldown == 0:
            # execute attack
            self.attacking = True
            self.blocking = False
            self.attack_sound.play()
            attacking_rect = pygame.Rect(self.rect.centerx -
                                         (2 * self.rect.width * self.flip),
                                         self.rect.y, 2 * self.rect.width,
                                         self.rect.height)
            if attacking_rect.colliderect(target.rect):
                dmg = 0
                if target.blocking and self.attack_val != 2:
                    dmg = 0.5
                else:
                    if self.attack_val == 0:
                        dmg = 200
                    if self.attack_val == 1:
                        dmg = 5
                    if self.attack_val == 2:
                        dmg = 15
                    target.hit = True
                target.health -= dmg

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale),
                           self.rect.y - (self.offset[1] * self.image_scale)))


