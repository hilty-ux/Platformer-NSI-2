import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen, W, H):
        
        # initialisation de la super classe pygame.sprite.Sprite qui va nous offrir de plus grandes possibilités.
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
        
        # dessine un rectangle sur le self.screen, de la couleur self.color, 
        # et de coordonnée et de taille du rectangle self.rect
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
        """Cette fonction fonctionne sur un principe simple : si on détecte une collision dans la direction
        que l'on veut, renvoie vrai, sinon renvoie faux. On pourra ainsi vérifier avant le mouvement si on
        détecte une collision ou non, si oui le mouvement ne sera pas autorisé."""
       
        # si la direction à vérifier est la droite
        if direction == "right":
            
            # comme la coordonnée x du joueur est en haut à droite de son rectangle, pour vérifier si on
            # détecte une collision à droite, il faut ajouter à sa coordonnée x sa largeur, que l'on
            # matérialise avec la variable self.playerW (pour player width ou largeur joueur en français)
            if self.rect.x + self.playerW > self.W:
                return True
            
            return False
        
        # ou si la direction à vérifier est la gauche
        elif direction == "left":
            
            # si le x du joueur est inférieur à 0
            if self.rect.x < 0:
                return True
            
            return False
            
        
        
        
