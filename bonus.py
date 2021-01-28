import pygame
import random

# PAS TERMINE !

class Bonus(pygame.sprite.sprite):
	"""Création d'une classe bonus pour faire apparaitre des bonus"""

	def __init__(self, screen, W, H):

		self.scren = screen
		self.W = W
		self.H = H

		self.image = pygame.Surface((100, 100))
		self.image.fill((255, 100, 20))
		self.rect = self.image.get_rect()

	def spawn(self):

		self.rect.x = random.randint(self.W // 4, self.W // 2 + self.W // 4)
		self.rect.y = random.randint(self.H // 4, self.H // 2 + self.H // 4)
