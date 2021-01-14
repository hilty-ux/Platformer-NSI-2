import pygame


class Ground(pygame.sprite.Sprite):
    
    """Hérite de la super classe Sprite de pygame, cela va permettre de faire des groupes de sprites notamment"""
    
    def __init__(self, screen, W, H):
        
        super().__init__() # initialise la super classe
        
        self.screen = screen
        self.W = W
        self.H = H
        
        self.rect = pygame.Rect((0, self.H - 100), (W, H)) # définit un rectangle
        
        self.color = (0, 200, 0) # définit une couleur
        
    def update(self):
        
        # déssine un rectangle sur la fenetre : 'self.screen', dans la couleur: 'self.color', dans le rectangle : 'self.rect'
        pygame.draw.rect(self.screen, self.color, self.rect)
        

class Platform(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        super().__init__()
        
        self.image = pygame.Surface((200, 50))
        self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = x, y
        
    