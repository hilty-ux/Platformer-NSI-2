import pygame
import random
import math


class Comet(pygame.sprite.Sprite):

    def __init__(self, screen, W, H, player_pos_x, player_pos_y):
        super().__init__()

        self.W = W
        self.H = H

        self.screen = screen

        self.image = pygame.Surface((100, 100))
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

        self.dx = math.cos(self.angle) * 15
        self.dy = math.sin(self.angle) * 15

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