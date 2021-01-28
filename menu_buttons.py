import pygame


class ButtonMenu:

    def __init__(self, screen):

        self.screen = screen

        # charge toutes les icones de boutons et leur assigne un rectangle chacune
        self.black_button_play = pygame.image.load("ressource/Menu Boutons/BlackPlayButton.png")
        self.black_button_rect = self.black_button_play.get_rect()
        self.white_button_play = pygame.image.load("ressource/Menu Boutons/WhitePlayButton.png")
        self.white_button_rect = self.white_button_play.get_rect()
        
        self.black_button_keys = pygame.image.load("ressource/Menu Boutons/BlackKeysButton.png")
        self.black_button_keys_rect = self.black_button_keys.get_rect()
        self.white_button_keys = pygame.image.load("ressource/Menu Boutons/WhiteKeysButton.png")
        self.white_button_keys_rect = self.white_button_keys.get_rect()

        self.black_button_exit = pygame.image.load("ressource/Menu Boutons/ExitBlack.gif")
        self.black_button_exit_rect = self.black_button_exit.get_rect()
        self.white_button_exit = pygame.image.load("ressource/Menu Boutons/ExitWhite.gif")
        self.white_button_exit_rect = self.white_button_exit.get_rect()

        # place les rectangles pour placer les boutons sur l'écran
        self.black_button_rect.x, self.black_button_rect.y = 1625, 725
        self.white_button_rect.x, self.white_button_rect.y = 1625, 725
        
        self.black_button_keys_rect.x, self.black_button_keys_rect.y = 1625, 825
        self.white_button_keys_rect.x, self.white_button_keys_rect.y = 1625, 825

        self.black_button_exit_rect.x, self.black_button_exit_rect.y = 1625, 925
        self.white_button_exit_rect.x, self.white_button_exit_rect.y = 1625, 925
        

    def print_out(self):

        # récupère les coordonnées de la souris pour vérifier si la souris passe par dessus le bouton
        mouse_coo = pygame.mouse.get_pos()

        # si les coordonnées de la souris ne collisionnent pas avec le rectangle du bouton, affiche le bouton 
        # en blanc, si oui, l'affiche en noir
        if not self.white_button_rect.collidepoint(mouse_coo):
            self.screen.blit(self.white_button_play, self.white_button_rect)
        else:
            self.screen.blit(self.black_button_play, self.black_button_rect)
            
        if not self.white_button_keys_rect.collidepoint(mouse_coo):
            self.screen.blit(self.white_button_keys, self.white_button_keys_rect)
        else:
            self.screen.blit(self.black_button_keys, self.black_button_keys_rect)

        if not self.white_button_exit_rect.collidepoint(mouse_coo):
            self.screen.blit(self.white_button_exit, self.white_button_exit_rect)
        else:
            self.screen.blit(self.black_button_exit, self.black_button_exit_rect)