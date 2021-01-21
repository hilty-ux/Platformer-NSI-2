import pygame
import random
import math


class Comet(pygame.sprite.Sprite):

    def __init__(self, screen, W, H, player_pos_x, player_pos_y):
        super().__init__()
        
        self.W = W
        self.H = H

        self.screen = screen

        self.image = pygame.Surface((75, 75))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()

        # choisi le côté d'ou viendra la comète
        self.cote = random.randint(1, 4)

        # haut de l'écran
        if self.cote == 1:
            self.rect.x = random.randint(0, self.W)
            self.rect.y = 0
        # droite de l'écran
        elif self.cote == 2:
            self.rect.x = self.W - self.image.get_width()
            self.rect.y = random.randint(0, self.H)
        # bas de l'écran
        elif self.cote == 3:
            self.rect.x = random.randint(0, self.W)
            self.rect.y = self.H
        # gauche de l'écran
        elif self.cote == 4:
            self.rect.x = 0
            self.rect.y = random.randint(0, self.H)

        self.angle = math.atan2(player_pos_y - self.rect.y, player_pos_x - self.rect.x)

        self.dx = math.cos(self.angle) * 10
        self.dy = math.sin(self.angle) * 10

    def update(self):

        self.rect.y += self.dy
        self.rect.x += self.dx

        if self.rect.y > self.H:
            self.kill()
        elif self.rect.y < 0:
            self.kill()
        elif self.rect.x > self.W:
            self.kill()
        elif self.rect.x < 0:
            self.kill()


class SpaceShip(pygame.sprite.Sprite):

    def __init__(self, x_player, y_player, W, H, screen):
        super().__init__()

        self.sprites = [pygame.image.load('ressource/SpaceShip/spaceleft.png'),
                        pygame.image.load('ressource/SpaceShip/spaceright.png')]
        self.index_anim = 1
        self.image = self.sprites[self.index_anim]
        self.rect = self.image.get_rect()

        self.velocity = 6
        self.life = 100

        self.target_x = x_player
        self.target_y = y_player

        self.screen = screen
        self.W = W
        self.H = H

        # ici il va s'agir de vérifier dans quelle partie de l'écran le joueur se trouve,
        # dans quel quart de l'écran il se trouve, pour situer au mieux le vaisseau
        """                                                   # ceci est un écran
        if self.target_x < W // 2:                                #  quart 1      |      quart 3
            if self.target_y < H // 2:                            #               |
                self.quart = 1                                    #  -------------|-------------
                self.rect.x, self.rect.y = 10, self.H // 2 - 250  #               |
                self.index_anim = 1                               #  quart 2      |      quart 4
                self.image = self.sprites[self.index_anim]
            elif self.target_y > H // 2:
                self.quart = 2
                self.rect.x, self.rect.y = 10, self.H // 2 + 250
                self.index_anim = 1
                self.image = self.sprites[self.index_anim]
        elif self.target_x > W // 2:
            if self.target_y < H // 2:
                self.quart = 3
                self.rect.x, self.rect.y = W - self.image.get_width(), H // 2 - 250
                self.index_anim = 0
                self.image = self.sprites[self.index_anim]
            elif self.target_y > H // 2:
                self.quart = 4
                self.rect.x, self.rect.y = W - self.image.get_width(), H // 2 + 250
                self.index_anim = 0
                self.image = self.sprites[self.index_anim]
        """

        self.quart = random.randint(1, 4)
        if self.quart == 1:
            self.rect.x, self.rect.y = 10, self.H // 2 - 250
            self.index_anim = 1
            self.image = self.sprites[self.index_anim]
        elif self.quart == 2:
            self.rect.x, self.rect.y = 10, self.H // 2 + 250
            self.index_anim = 1
            self.image = self.sprites[self.index_anim]
        elif self.quart == 3:
            self.rect.x, self.rect.y = W - self.image.get_width(), H // 2 - 250
            self.index_anim = 0
            self.image = self.sprites[self.index_anim]
        elif self.quart == 4:
            self.rect.x, self.rect.y = W - self.image.get_width(), H // 2 + 250
            self.index_anim = 0
            self.image = self.sprites[self.index_anim]
        self.movement = "up"

    def update(self, life_switch, move):

        if life_switch:
            self.life -= 25
            return self.life, None

        if self.life <= 0:
            last_x, last_y = self.rect.x, self.rect.y
            self.kill()
            return "dead", last_x, last_y

        self.velocity = move

        # si le vaisseau a apparu dans le quart n°1, effectue cette routine de mouvement
        if self.quart == 1:
            if self.movement == "up":
                if self.rect.y - self.velocity > 100:
                    self.rect.y -= self.velocity
                else: self.movement = "down"

            if self.movement == "down":
                if self.rect.y + self.velocity < self.H // 2:
                    self.rect.y += self.velocity
                else: self.movement = "up"

        # si le vaisseau a apparu dans le quart n°2, effectue cette routine de mouvement
        elif self.quart == 2:
            if self.movement == "up":
                if self.rect.y - self.velocity > self.H // 2:
                    self.rect.y -= self.velocity
                else:
                    self.movement = "down"

            if self.movement == "down":
                if self.rect.y + self.velocity < self.H:
                    self.rect.y += self.velocity
                else:
                    self.movement = "up"

        # si le vaisseau a apparu dans le quart n°3, effectue cette routine de mouvement
        elif self.quart == 3:
            if self.movement == "up":
                if self.rect.y - self.velocity > 100:
                    self.rect.y -= self.velocity
                else:
                    self.movement = "down"

            if self.movement == "down":
                if self.rect.y + self.velocity < self.H // 2:
                    self.rect.y += self.velocity
                else:
                    self.movement = "up"

        # si le vaisseau a apparu dans le quart n°4, effectue cette routine de mouvement
        elif self.quart == 4:
            if self.movement == "up":
                if self.rect.y - self.velocity > self.H // 2:
                    self.rect.y -= self.velocity
                else:
                    self.movement = "down"

            if self.movement == "down":
                if self.rect.y + self.velocity < self.H:
                    self.rect.y += self.velocity
                else:
                    self.movement = "up"

        pygame.draw.rect(self.screen, (0, 0, 0), [
            self.rect.x,
            self.rect.y + self.image.get_height() + 20,
            self.image.get_width(),
            5
        ])

        pygame.draw.rect(self.screen, (205, 0, 0), [
            self.rect.x,
            self.rect.y + self.image.get_height() + 20,
            (self.image.get_width() / 100) * self.life,
            5
        ])

        return "successfully updated", None

    def hit(self):

        self.life -= 5