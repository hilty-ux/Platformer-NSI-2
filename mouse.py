import pygame


class MouseCursor(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()

        self.mouse_image = pygame.image.load('ressource/scope.png')
        self.rect = self.mouse_image.get_rect()

        self.screen = screen

        pygame.draw.rect(self.screen, (0, 255, 0), [160, 530, 230, 20])
        pygame.display.update()

    def update(self):

        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = pygame.mouse.get_pos()[1]

        self.screen.blit(self.mouse_image, self.rect)