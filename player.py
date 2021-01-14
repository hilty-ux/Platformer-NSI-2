import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen, W, H):
        
        super().__init__()
        
        # initialisation de l'écran (mis en argument)
        self.screen = screen
        self.W = W
        self.H = H

        # initialisation couleurs
        self.color = (255, 0, 0)

        # largeur et hauteur du joueur
        self.playerW = 50
        self.playerH = 100

        # je définis la surface du joueur (c'est comme une image)
        self.image = pygame.Surface((self.playerW, self.playerH))
        # je remplis cette surface de la couleur choisie (pas utile si image)
        self.image.fill(self.color)
        # récupère le rectangle en fonction de la surface
        self.rect = self.image.get_rect()
        # replace le joueur à une position de base
        self.rect.x, self.rect.y = 100, self.H - 210
        
        # initialisation de la variable vitesse
        self.vitesse = 20
        
        
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
            
    def move_up(self):
        
        self.rect.y -= 50
        
    def collision(self, direction):
        
        if direction == "right":
            
            if self.rect.x + self.playerW > self.W:
                return True
            
            return False
        
        elif direction == "left":
            
            if self.rect.x < 0:
                return True
            
            return False
            
        
        
        