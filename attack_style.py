
class Move_set:
    def __init__(self, attack_style, attack_val, action, attack_cooldown, hit):
        self.attack_style = attack_style
        self.attack_val = attack_val
        self.action1 = action
        self.attacking1 = True
        self.attack_cd1 = 0
        self.attack_cooldown1 = attack_cooldown
        self.hit = hit

    def attack_cd(self):

        if self.attack_style == 0:
            if self.action == 4:
                self.attacking = False
                self.attack_cooldown = 25
            if self.action == 5:
                self.attacking = False
                self.attack_cooldown = 2
            if self.action == 6:
                self.attacking = False
                self.attack_cooldown = 30
            # check if damage was taken
            if self.action == 8:
                self.hit = False
                # is stopped
                self.attacking = False
                self.attack_cooldown = 15

        # shinobi
        elif self.attack_style == 1:
            if self.action == 4:
                self.attacking = False
                self.attack_cooldown = 20
            if self.action == 5:
                self.attacking = False
                self.attack_cooldown = 10
            if self.action == 6:
                self.attacking = False
                self.attack_cooldown = 70
            # check if damage was taken
            if self.action == 8:
                self.hit = False
                # if the player was in the middle of an attack, then the attack
                # is stopped
                self.attacking = False
                self.attack_cooldown = 12
        # samurai
        elif self.attack_style == 2:
            if self.action == 4:
                self.attacking = False
                self.attack_cooldown = 13
            if self.action == 5:
                self.attacking = False
                self.attack_cooldown = 3
            if self.action == 6:
                self.attacking = False
                self.attack_cooldown = 20
            # check if damage was taken
            if self.action == 8:
                self.hit = False
                # if the player was in the middle of an attack, then the attack
                # is stopped
                self.attacking = False
                self.attack_cooldown = 18
        # gotoku
        elif self.attack_style == 3:

            if self.action == 4:
                self.attacking = False
                self.attack_cooldown = 12
            if self.action == 5:
                self.attacking = False
                self.attack_cooldown = 18
            if self.action == 6:
                self.attacking = False
                self.attack_cooldown = 70
            # check if damage was taken
            if self.action == 8:
                self.hit = False
                # if the player was in the middle of an attack, then the attack
                # is stopped
                self.attacking = False
                self.attack_cooldown = 10
        # onre
        elif self.attack_style == 4:
            if self.action == 4:
                self.attacking = False
                self.attack_cooldown = 25
            if self.action == 5:
                self.attacking = False
                self.attack_cooldown = 10
            if self.action == 6:
                self.attacking = False
                self.attack_cooldown = 100
            # check if damage was taken
            if self.action == 8:
                self.hit = False
                # if the player was in the middle of an attack, then the attack
                # is stopped
                self.attacking = False
                self.attack_cooldown = 20
        return self.hit, self.attacking, self.attack_cooldown
    def attack_dmg(self):
        dmg = 0
        if self.attack_style == 0:
            if self.attack_val == 0:
                dmg = 30
            if self.attack_val == 1:
                dmg = 18
            if self.attack_val == 2:
                dmg = 15
        elif self.attack_style == 1:
            if self.attack_val == 0:
                dmg = 28
            if self.attack_val == 1:
                dmg = 14
            if self.attack_val == 2:
                dmg = 26
        elif self.attack_style == 2:
            if self.attack_val == 0:
                dmg = 24
            if self.attack_val == 1:
                dmg = 12
            if self.attack_val == 2:
                dmg = 30
        elif self.attack_style == 3:
            if self.attack_val == 0:
                dmg = 30
            if self.attack_val == 1:
                dmg = 20
            if self.attack_val == 2:
                dmg = 25
        elif self.attack_style == 4:
            if self.attack_val == 0:
                dmg = 30
            if self.attack_val == 1:
                dmg = 15
            if self.attack_val == 2:
                dmg = 20
        return dmg
