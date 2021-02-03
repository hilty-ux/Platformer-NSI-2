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

        self.police1 = pygame.font.Font("ressource/Police/PIXELITE.ttf", 50)  # crée une police avec pour taille 30
        # crée un rendu de cette police pour le text entre apostrophes avec de l'antialiasing (True)
        # et écrit en noir ((0, 0, 0))
        self.text_ = self.police1.render(f"0/100 PV", True, (0, 0, 0))
        self.text_surf = self.text_.get_rect()
        self.text_surf.right = 710  # aligne le rectangle pour que son coté droit aie pour coo en x : 710
        self.text_surf.y = 40  # met le y du rectangle à 40

        self.police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 35)
        self.text_2 = self.police.render("Space Marine", True, (0, 0, 0))
        self.text_2_surf = self.text_2.get_rect()
        self.text_2_surf.left = 110
        self.text_2_surf.y = 45

        self.police3 = pygame.font.Font("ressource/Police/PIXELITE.ttf", 40)
        self.text_3 = self.police3.render(str(0), True, (0, 0, 0))
        self.text_3_surf = self.text_3.get_rect()
        self.text_3_surf.center = self.W // 2 - 100, 50

        self.police4 = pygame.font.Font("ressource/Police/PIXELITE.ttf", 40)
        self.text_4 = self.police4.render(str(0), True, (0, 0, 0))
        self.text_4_surf = self.text_4.get_rect()
        self.text_4_surf.center = self.W // 2 + 100, 50

        self.police5 = pygame.font.Font("ressource/Police/PIXELITE.ttf", 40)
        self.text5 = self.police5.render(f"Round {0}", True, (0, 0, 0))
        self.text_surf5 = self.text5.get_rect()
        self.text_surf5.center = self.W // 2 + 300, 50

        self.police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
        self.text10 = self.police.render(f"Comet", True, (255, 0, 0))
        self.text_surf10 = self.text10.get_rect()
        self.text_surf10.center = self.W // 2 + 450, 25

        self.police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
        self.text11 = self.police.render(f"Comet", True, (0, 0, 0))
        self.text_surf11 = self.text11.get_rect()
        self.text_surf11.center = self.W // 2 + 450, 25

        self.police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
        self.text21 = self.police.render(f"Space ships invasion", True, (255, 0, 0))
        self.text_surf21= self.text21.get_rect()
        self.text_surf21.center = self.W // 2 + 655, 25

        self.police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
        self.text22 = self.police.render(f"Space ships invasion", True, (0, 0, 0))
        self.text_surf22 = self.text22.get_rect()
        self.text_surf22.center = self.W // 2 + 655, 25

        self.police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
        self.text31 = self.police.render(f"Jump", True, (255, 0, 0))
        self.text_surf31 = self.text31.get_rect()
        self.text_surf31.center = self.W // 2 + 850, 25

        self.police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 25)
        self.text32 = self.police.render(f"Jump", True, (0, 0, 0))
        self.text_surf32 = self.text32.get_rect()
        self.text_surf32.center = self.W // 2 + 850, 25

        pygame.draw.rect(self.screen, (0, 255, 0), [160, 530, 344, 20])
        pygame.display.flip()

    def update(self, life, time, score, present_round, state, update_, shield_cooldown, chock_cooldown, last_cooldown):

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

        # Ecritures ------------------------------------------- #

        # redéfinis les textes ayant des valueurs à mettre a jour

        self.text_ = self.police1.render(f"{life}/100 PV", True, (0, 0, 0))
        self.text_3 = self.police3.render(str(time), True, (0, 0, 0))
        self.text_4 = self.police4.render(str(score), True, (0, 0, 0))

        # affiche tous les éléments texts créés avec pour coordonnées leurs rectangles respectifs
        self.screen.blit(self.text_, self.text_surf)
        self.screen.blit(self.text_2, self.text_2_surf)
        self.screen.blit(self.text_3, self.text_3_surf)

        # Score ----------------------------------------------- #

        self.screen.blit(self.text_4, self.text_4_surf)

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

        # redéfinis le texte ayant une variable à redéfinir en temps réel
        self.text5 = self.police5.render(f"Round {present_round}", True, (0, 0, 0))
        self.screen.blit(self.text5, self.text_surf5)

        if state == 0:
            self.screen.blit(self.text10, self.text_surf10)
        else:
            self.screen.blit(self.text11, self.text_surf11)

        if state == 1:
            self.screen.blit(self.text21, self.text_surf21)
        else:
            self.screen.blit(self.text22, self.text_surf22)

        if state == 2:
            self.screen.blit(self.text31, self.text_surf31)
        else:
            self.screen.blit(self.text32, self.text_surf32)

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

        cooldowns = [shield_cooldown, chock_cooldown, last_cooldown]
        police = pygame.font.Font("ressource/Police/PIXELITE.TTF", 25)
        texts = [police.render(str(i), True, (255, 255, 255)) for i in cooldowns]
        rect = [i.get_rect() for i in texts]
        for i in range(len(rect)):
            rect[i].left = 50
            rect[i].centery = i * 50 + 115
            self.screen.blit(texts[i], rect[i])