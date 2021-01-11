import pygame
import game # import le fichier game


W = 1800 # définit une variable désignant la largeur de l'écran
H = 1000 # définit une variable désignant la hauteur de l'écran
screen = pygame.display.set_mode((W, H)) # crée l'écran avec pour largeur W et hauteur H

game = game.Game(screen, W, H) # initialise la classe Game provenant du fichier game

pygame.init() # initialise pygame

game.main_loop() # appelle la fonction main_loop de la classe Game, elle désigne les boucles de jeu

pygame.quit() # quitte pygame, quand la boucle de jeu est finie/cassée
            
            
            
