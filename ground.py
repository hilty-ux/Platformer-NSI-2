import pygame
from random import randint


class Ground(pygame.sprite.Sprite):
    """Hérite de la super classe Sprite de pygame, cela va permettre de faire des groupes de sprites notamment"""

    def __init__(self, screen, W, H):
        super().__init__()  # initialise la super classe

        # récupère les variables mises en argument
        self.screen = screen
        self.W = W
        self.H = H

        self.color = (0, 200, 0)  # définit une couleur

        self.image = pygame.Surface((self.W, 100))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = 0, self.H - 100



class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # chargement des différente frames
        self.sprites = [pygame.image.load('ressource/Plateforme_frame/sprite_0_250.png'),
                        pygame.image.load('ressource/Plateforme_frame/sprite_1_250.png')]
        # index d'animation
        self.index_animation = randint(0, 1)
        self.image = self.sprites[self.index_animation]
        # self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x, y

    def update(self, move, anim):

        if anim:
            if self.index_animation == 0:
                self.index_animation += 1
                self.image = self.sprites[self.index_animation]
            else:
                self.index_animation -= 1
                self.image = self.sprites[self.index_animation]

        if move:
            self.rect.y += 10


class Flame(pygame.sprite.Sprite):

    def __init__(self, x, y, begining_index):
        super().__init__()

        self.sprites = [pygame.image.load('ressource/Flamme/frame0-83.png'),
                        pygame.image.load('ressource/Flamme/frame1-83.png')]
        self.index_animation = begining_index
        self.image = self.sprites[self.index_animation]

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x, y

    def update(self):

        if self.index_animation == 0:
            self.index_animation += 1
            self.image = self.sprites[self.index_animation]
        else:
            self.index_animation -= 1
            self.image = self.sprites[self.index_animation]
