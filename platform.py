import pygame

class Plateform(pygame.sprite.Sprite):
    
    def __init__(self, screen, W, H,X,Y):
        
        super().__init__()# initialisation de la super classe pygame.sprite.Sprite qui va nous offrir de plus grandes possibilités.
        
        self.screen = screen
        self.W = W
        self.H = H
        
        
    # je définis le rectangle de la plateforme : x: 100, y: 100 et largeur: 100, hauteur : 20
        self.image = pygame.Surface((200, 50))
        self.image.fill((255, 0, 0))
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = X, Y