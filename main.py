import pygame
import game


W = 1920
H = 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Insert name here")

game = game.Game(screen, W, H)

pygame.init()

game.main_loop()

pygame.quit()