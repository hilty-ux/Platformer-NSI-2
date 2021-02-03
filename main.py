import pygame
import game


W = 1920
H = 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Insert name here")

pygame.init()

game = game.Game(screen, W, H)

game.main_loop()

pygame.quit()