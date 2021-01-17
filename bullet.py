import pygame
import math


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, target_x, target_y, color, velocity):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        # get angle of bullet direction
        self.angle = math.atan2(target_y-pos_y, target_x-pos_x)

        self.dx = math.cos(self.angle)*velocity
        self.dy = math.sin(self.angle)*velocity

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        if self.rect.x > 1920:
            self.kill()
        elif self.rect.y > 1080:
            self.kill()
        elif self. rect.x < 0:
            self.kill()
        elif self.rect.y < 0:
            self.kill()