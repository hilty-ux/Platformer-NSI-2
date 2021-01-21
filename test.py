"""Ce test est le programme servant à faire le bunny jump (phase 3 du jeu final)"""


import pygame
import random

W = 1000
H = 1000
screen = pygame.display.set_mode((W, H))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.rect = pygame.Rect((W // 2, H - 200), (50, 50))
        self.color = (255, 0, 0)

        self.velocity = 10

        self.rect.x, self.rect.y = W // 2, H // 2

    def update(self):

        pygame.draw.rect(screen, self.color, self.rect)

    def move_right(self):
        if self.rect.x < W - 10:
            self.rect.x += self.velocity

    def move_left(self):
        if self.rect.x > 10:
            self.rect.x -= self.velocity

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 5


class BasicGround(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((W, 100))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = H - 100

    def update(self):

        screen.blit(self.image, self.rect)


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((200, 50))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x, y

    def update(self):
        self.rect.y += 15


class Game:

    def __init__(self):

        self.running = True

        self.pl = Player()
        self.ba = BasicGround()

        self.platform_group = pygame.sprite.Group()
        self.add_platform = lambda: self.platform_group.add(Platform(random.randint(0, W - 200), - 100))

        self.gravity_vector = (0, 10)
        self.resistance_vector = (0, 0)

        self.clock = pygame.time.Clock()

        self.actual_time = pygame.time.get_ticks()
        self.begin_jump_time = pygame.time.get_ticks()
        self.begin_updating_time = pygame.time.get_ticks()
        self.platform_spawning_delay = pygame.time.get_ticks()
        self.jumping = False
        self.updating_platforms = False

        self.pressed = {}

    def gravity(self):
        self.pl.rect.y += self.gravity_vector[1] + self.resistance_vector[1]

    def main_loop(self):

        self.platform_group.add(Platform(random.randint(0, W - 200), 100))

        while self.running:

            screen.fill((255, 255, 255))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True
                if event.type == pygame.KEYUP:
                    self.pressed[event.key] = False

            if self.pressed.get(pygame.K_q):
                self.pl.move_left()
            if self.pressed.get(pygame.K_d):
                self.pl.move_right()

            self.platform_group.draw(screen)

            self.pl.update()

            if self.actual_time - self.platform_spawning_delay > 1000:
                self.add_platform()
                self.platform_spawning_delay = pygame.time.get_ticks()

            if not self.jumping:
                if pygame.sprite.spritecollideany(self.pl, self.platform_group):
                    self.begin_updating_time = pygame.time.get_ticks()
                    self.begin_jump_time = pygame.time.get_ticks()

            if self.actual_time - self.begin_updating_time < 1000:
                self.updating_platforms = True
            else:
                self.updating_platforms = False

            if self.updating_platforms:
                self.platform_group.update()

            if self.actual_time - self.begin_jump_time < 1300:
                self.jumping = True
            else:
                self.jumping = False

            if self.jumping:
                self.pl.move_up()
                self.resistance_vector = (0, -10)
            else:
                self.resistance_vector = (0, 0)

            self.gravity()

            self.actual_time = pygame.time.get_ticks()
            self.clock.tick(40)
            pygame.display.flip()


game = Game()

pygame.init()

game.main_loop()

pygame.quit()