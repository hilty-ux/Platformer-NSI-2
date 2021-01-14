import pygame


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

        self.image = pygame.image.load('ressource/plateforme.png')
        # self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x, y
