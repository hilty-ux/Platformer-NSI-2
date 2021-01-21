import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen, W, H):
        
        super().__init__()
        
        self.player_score = 0
        
        # initialisation de l'écran (mis en argument)
        self.screen = screen
        self.W = W
        self.H = H

        # largeur et hauteur du joueur
        self.playerW = 25
        self.playerH = 50

        # je définis la surface du joueur (c'est comme une image)
        self.image = pygame.image.load("ressource/Player/basic-50.png")
        # récupère le rectangle en fonction de la surface
        self.rect = self.image.get_rect()
        # replace le joueur à une position de base
        self.rect.x, self.rect.y = self.W // 2, self.H - 300
        
        # initialisation de la variable vitesse
        self.vitesse = 20

    def update(self):
        self.screen.blit(self.image, self.rect)
        
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
        if self.rect.y > 100:
            self.rect.y -= 5

    def jump(self):

        if self.rect.y > 150:
            self.rect.y -= 200
        
    def collision(self, direction):
        
        if direction == "right":
            
            if self.rect.x + self.playerW > self.W:
                return True
            
            return False
        
        elif direction == "left":
            
            if self.rect.x < 0:
                return True
            
            return False
            
        
        
        