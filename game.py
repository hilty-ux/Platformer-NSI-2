import pygame
import player
import ground


class Game:
    
    def __init__(self, screen, W, H):
        
        # récupère la fenêtre
        self.screen = screen
        
        self.pl = player.Player(self.screen, W, H)
        self.gr = ground.Ground(self.screen, W, H)
        
        # initialise les variables de stade de jeu
        self.running  = True
        self.menu = True
        self.jeu = False
        
        # initialise les variables de couleur
        self.background_menu = (200, 200, 200)
        self.background_game = (0, 0, 0)
        
        # définis une liste des touches préssées (vide)
        self.pressed = {}
        
        # définit l'horloge du jeu afin de pouvoir gérer les fps
        self.clock = pygame.time.Clock()
        
    def main_loop(self):
        
        while self.running:
            
            while self.menu:
                
                # récupère tous les évènements
                for event in pygame.event.get():
                    
                    # si le joueur ferme la fenetre, casse la boucle de lancement et ferme la boucle actuelle, la boucle menu
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.menu = False
                        
                    if event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_p:
                            self.menu = False
                            self.jeu = True
                        
                self.screen.fill(self.background_menu)
                
                pygame.display.flip()
                
            while self.jeu:
                
                # récupère tous les évènements
                for event in pygame.event.get():
                    
                    # si le joueur ferme la fenetre, casse la boucle de lancement et ferme la boucle actuelle, la boucle jeu
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.jeu = False
                        
                    # si l'événement est de type touche préssée
                    if event.type == pygame.KEYDOWN:
                        
                        # ajoute à la liste des touches préssées la touche actuellement préssée
                        self.pressed[event.key] = True
                        
                        # si la touche préssée est la touche ESCAPE
                        if event.key == pygame.K_ESCAPE:
                            
                            # initialise la boucle menu et ferme la boucle jeu
                            self.menu = True
                            self.jeu = False
                            
                            
                    if event.type == pygame.KEYUP:
                        
                        self.pressed[event.key] = False
                
                # si le joueur appuies sur la flèche de gauche, utilise la fonction du joueur 'bouger à gauche'
                if self.pressed.get(pygame.K_LEFT):
                   self.pl.move_left()
                
                # si le joueur appuies sur la flèche de droite, utilise la fonction du joueur 'bouger à droite'
                if self.pressed.get(pygame.K_RIGHT):
                    self.pl.move_right()
                
                # colore l'écran dans la couleur définit plus haut
                self.screen.fill(self.background_game)
                # met à jour le sol
                self.gr.update()
                # met à jour le joueur
                self.pl.update()
                
                # met à jour l'écran
                pygame.display.flip()
                # met les fps à 40
                self.clock.tick(40)