import pygame


class ChockWave(pygame.sprite.Sprite):

    def __init__(self, screen, x_dep, y_dep):
        super().__init__()

        self.screen = screen
        self.x_dep = x_dep
        self.y_dep = y_dep

        self.frames = [pygame.image.load("ressource/Onde de choc/frame_00_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_01_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_02_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_03_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_04_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_05_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_06_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_07_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_08_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_09_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_10_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_11_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_12_delay-0.13s.gif"),
                       pygame.image.load("ressource/Onde de choc/frame_13_delay-0.13s.gif")]
        self.index_anim = 0
        self.image = self.frames[self.index_anim]
        self.rect = self.frames[self.index_anim].get_rect()
        self.rect.center = x_dep, y_dep

        self.begin_anim_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()

    def update(self):

        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.begin_anim_time > 60:
            self.begin_anim_time = self.current_time
            if self.index_anim < len(self.frames)-1:
                self.index_anim += 1
            else:
                self.kill()

        self.image = self.frames[self.index_anim]
        self.rect = self.image.get_rect()
        self.rect.center = self.x_dep, self.y_dep