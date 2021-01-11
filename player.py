import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen, W, H):
        
        super().__init__()
        
        # initialisation de l'écran (mis en argument)
        self.screen = screen
        self.W = W
        self.H = H
        
        # je définis le rectangle du joueur : x: 100, y: 100 et largeur: 50, hauteur : 100
        self.rect = pygame.Rect((100, self.H - 100 - 100), (50, 100))
        self.playerW = 50
        self.playerH = 100
        
        # initialisation de la variable vitesse
        self.vitesse = 20
        
        # initialisation couleurs
        self.color = (255, 0, 0)
        
        
    def update(self):
        
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def move_right(self):
        
        # si il ne détecte pas de collision à droite
        if not self.collision("right"):
            # ajoute la valeur de la vitesse au coordonnée x du joueur
            self.rect.x += self.vitesse
        
    def move_left(self):
        
        # si il ne détecte pas de collision à la gauche
        if not self.collision("left"):
            # enlève la valeur de la vitesse au coordonnée x du joueur
            self.rect.x -= self.vitesse
        
    def collision(self, direction):
        
        if direction == "right":
            
            if self.rect.x + self.playerW > self.W:
                return True
            
            return False
        
        elif direction == "left":
            
            if self.rect.x < 0:
                return True
            
            return False
            
        
        
        