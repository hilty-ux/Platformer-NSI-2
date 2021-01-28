import pygame


class TopBar:

    def __init__(self, screen, W, H, life):

        self.screen = screen
        self.W = W
        self.H = H

        self.main_surface = pygame.Surface((self.W, 100))
        self.main_surface.fill((255, 255, 255))
        self.main_surface.set_alpha(125)
        self.main_rect = self.main_surface.get_rect()
        self.main_rect.x, self.main_rect.y = 0, 0
        self.image_player = pygame.Surface((90, 90))
        self.image_player.fill((0, 0, 0))
        self.image_player_rect = self.image_player.get_rect()
        self.image_player_rect.center = 50, 50

        self.state_index = 0
        self.present_time = pygame.time.get_ticks()
        self.start_round = pygame.time.get_ticks()

    def update(self, life, time, score, present_round, state, update_):

        # Rectangles ----------------------------------------------- #

        # dessine le rectangle principal
        self.screen.blit(self.main_surface, self.main_rect)
        self.screen.blit(self.image_player, self.image_player_rect)

        # dessine le rectangle de vie (le noir qui représente les pv max)
        pygame.draw.rect(self.screen, (0, 0, 0), [
            110, 20, 600, 15
        ])

        # dessine le rectangle de vie (le rouge qui représente les pv actuels)
        pygame.draw.rect(self.screen, (255, 0, 0), [
            110, 20, 6 * life, 15
        ])

        # Ecriture ----------------------------------------------- #

        police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 50)  # crée une police avec pour taille 30
        # crée un rendu de cette police pour le text entre apostrophes avec de l'antialiasing (True)
        # et écrit en noir ((0, 0, 0))
        text_ = police.render(f"{life}/100 PV", True, (0, 0, 0))
        text_surf = text_.get_rect()
        text_surf.right = 710  # aligne le rectangle pour que son coté droit aie pour coo en x : 710
        text_surf.y = 40  # met le y du rectangle à 40

        # pareil mais avec des valeurs différentes
        police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 35)
        text_2 = police.render("Space Marine", True, (0, 0, 0))
        text_2_surf = text_2.get_rect()
        text_2_surf.left = 110
        text_2_surf.y = 45

        # pareil mais avec des valeurs différentes
        police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 40)
        text_3 = police.render(str(time), True, (0, 0, 0))
        text_3_surf = text_3.get_rect()
        text_3_surf.center = self.W // 2 - 100, 50

        # affiche tous les éléments texts créés avec pour coordonnées leurs rectangles respectifs
        self.screen.blit(text_, text_surf)
        self.screen.blit(text_2, text_2_surf)
        self.screen.blit(text_3, text_3_surf)

        # Score ----------------------------------------------- #

        police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 40)
        text_4 = police.render(str(score), True, (0, 0, 0))
        text_4_surf = text_4.get_rect()
        text_4_surf.center = self.W // 2 + 100, 50

        self.screen.blit(text_4, text_4_surf)

        # Round/State ----------------------------------------- #

        pygame.draw.rect(self.screen, (0, 0, 0), [
            self.W // 2 + 400, 45, 500, 10
            ])
        pygame.draw.rect(self.screen, (255, 0, 0), [
            self.W // 2 + 400 + 166, 45, 10, 10
            ])
        pygame.draw.rect(self.screen, (255, 0, 0), [
            self.W // 2 + 400 + 166 + 166, 45, 10, 10
            ])

        police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 40)
        text = police.render(f"Round {present_round}", True, (0, 0, 0))
        text_surf = text.get_rect()
        text_surf.center = self.W // 2 + 300, 50

        self.screen.blit(text, text_surf)

        if state == 0:
            police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
            text = police.render(f"Comet", True, (255, 0, 0))
            text_surf = text.get_rect()
            text_surf.center = self.W // 2 + 450, 25

            self.screen.blit(text, text_surf)
        else:
            police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
            text = police.render(f"Comet", True, (0, 0, 0))
            text_surf = text.get_rect()
            text_surf.center = self.W // 2 + 450, 25

            self.screen.blit(text, text_surf)

        if state == 1:
            police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
            text = police.render(f"Space ships invasion", True, (255, 0, 0))
            text_surf = text.get_rect()
            text_surf.center = self.W // 2 + 655, 25

            self.screen.blit(text, text_surf)
        else:
            police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
            text = police.render(f"Space ships invasion", True, (0, 0, 0))
            text_surf = text.get_rect()
            text_surf.center = self.W // 2 + 655, 25

            self.screen.blit(text, text_surf)

        if state == 2:
            police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
            text = police.render(f"Jump", True, (255, 0, 0))
            text_surf = text.get_rect()
            text_surf.center = self.W // 2 + 850, 25

            self.screen.blit(text, text_surf)
        else:
            police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
            text = police.render(f"Jump", True, (0, 0, 0))
            text_surf = text.get_rect()
            text_surf.center = self.W // 2 + 850, 25

            self.screen.blit(text, text_surf)

        # dessine l'avancement du round

        if update_:
            if self.state_index > 120:
                self.state_index = 0
            self.state_index += 1


        try:
            pygame.draw.rect(self.screen, (255, 0, 0), [
                self.W // 2 + 400, 45, 4 * self.state_index, 10])   
            print("coucou")         
        except Exception as e:
            print(e)