import pygame
import game


W = 1800
H = 1000
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Insert name here")

game = game.Game(screen, W, H)

pygame.init()

game.main_loop()

pygame.quit()