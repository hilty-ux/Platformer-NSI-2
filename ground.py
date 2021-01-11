import pygame


class Ground(pygame.sprite.Sprite):
    
    def __init__(self, screen, W, H):
        
        super().__init__()
        
        self.screen = screen
        self.W = W
        self.H = H
        
        self.rect = pygame.Rect((0, self.H - 100), (W, H))
        
        self.color = (0, 200, 0)
        
    def update(self):
        
        pygame.draw.rect(self.screen, self.color, self.rect)
    