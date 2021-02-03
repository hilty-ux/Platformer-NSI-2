import pygame


class Shield(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        self.frames = [pygame.image.load("ressource/Shield/test0.png"),
                       pygame.image.load("ressource/Shield/test1.png"),
                       pygame.image.load("ressource/Shield/test2.png"),
                       pygame.image.load("ressource/Shield/test3.png")]
        self.index_anim = 0

        self.image = self.frames[self.index_anim]
        self.rect = self.image.get_rect()

        self.begin_anim_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()

        pygame.draw.rect(self.screen, (0, 255, 0), [160, 530, 800, 20])
        pygame.display.flip()

    def update(self, x_player, y_player):

        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.begin_anim_time > 150:
            if self.index_anim < len(self.frames)-1:
                self.index_anim += 1
                self.begin_anim_time = self.current_time
            else:
                self.index_anim = 0
                self.begin_anim_time = self.current_time

        self.image = self.frames[self.index_anim]
        self.rect = self.image.get_rect()

        self.rect.center = x_player, y_player - 25

        self.screen.blit(self.image, self.rect)