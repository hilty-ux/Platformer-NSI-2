import pygame
import random

import bullet
import ground
import hostile
import mouse
import player
import border_top
import scoreboard
import menu_buttons
import keys
import chock_wave
import shield
import abilities_menu


class Game:

    def __init__(self, screen, W, H):
        
        self.background_menu = pygame.image.load("ressource/Background/background_menu.jpg")
        self.background_game = pygame.image.load("ressource/Background/background_game.jpg")

        # récupère la fenêtre
        self.screen = screen

        # initialise les variables de stade de jeu
        self.running = True
        self.menu = True
        self.jeu = False
        self.keys_set = False
        self.abi_menu = False

        self.life = 100
        self.score = 0

        # définis la phase du jeu, si ce sont des comètes qui tombent ou des lasers lattéraux,
        # ou encore des vaisseau qui attaquent
        self.phase = ["comet", "space ships", "laser"]
        self.state = 0
        self.beginning_phase = pygame.time.get_ticks()
        self.present_round = 1

        # définis une liste des touches préssées (vide)
        self.pressed = {}

        # définit l'horloge du jeu afin de pouvoir gérer les fps
        self.clock = pygame.time.Clock()
        self.actual_time = pygame.time.get_ticks()
        self.beginning_game = pygame.time.get_ticks()
        self.begin_time_frame_platform = pygame.time.get_ticks()
        self.begin_time_frame_flames = pygame.time.get_ticks()

        self.W = W
        self.H = H

        # crée un groupe de sprite qui contiendra toutes les plateformes
        self.platform_group = pygame.sprite.Group()

        # lambda est une fonction écrite en une ligne, pour éviter de définir une fonction qui prendra une seule ligne
        # cette fonction ajoute une plateforme au groupe des plateformes
        self.add_platform = lambda x, y: self.platform_group.add(ground.Platform(x, y))

        # crée un groupe pour toutes les balles qui vont être tirées par le joueur
        self.bullet_group_player = pygame.sprite.Group()
        self.bullet_group_hostile = pygame.sprite.Group()
        # lambda est une fonction écrite en une ligne, pour éviter de définir une fonction qui prendra une seule ligne
        # cette fonction ajoute une balle au groupe des balles tirées par le joueur
        self.add_blue_bullet = lambda x, y, target_x, target_y: self.bullet_group_player.add(bullet.Bullet(
            x, y, target_x, target_y, (0, 255, 255), 100))
        self.add_red_bullet = lambda x, y, target_x, target_y: self.bullet_group_hostile.add(bullet.Bullet(
            x, y, target_x, target_y, (255, 0, 0), 10))

        # crée un groupe pour toutes les comètes
        self.comet_group = pygame.sprite.Group()

        # crée le groupe des flammes (uniquement visuel)
        # self.flames_group = pygame.sprite.Group()
        # self.add_flames = lambda x, y, begining_index: self.flames_group.add(ground.Flame(x, y, begining_index))

        # crée le groupe de vaisseau
        self.spaceship_group = pygame.sprite.Group()
        self.add_spaceship = lambda x, y: self.spaceship_group.add(hostile.SpaceShip(x, y, W, H, self.screen))

        # crée une instance du joueur
        self.pl = player.Player(self.screen, W, H)
        # crée une instance de la classe souris
        self.mo = mouse.MouseCursor(self.screen)
        # crée une instance de la classe TobBar qui sera la classe affichant l'overlay supérieur
        self.tb = border_top.TopBar(self.screen, self.W, self.H, self.life)
        # crée une instance de la classe ScoreBoard qui sera la pour afficher le menu des meilleurs scores
        self.sb = scoreboard.ScoreBoard(self.screen, self.W, self.H)
        # crée une instance de la classe ButtonMenu qui sera la pour afficher les boutons du menu
        self.but = menu_buttons.ButtonMenu(self.screen)
        # crée une instance de la classe KeyChoose qui sera la pour afficher la fenetre des touches
        self.ke = keys.KeyChoose(self.screen)
        # crée une instance de la classe Shield contenue dans le fichier shield
        self.sh = shield.Shield(self.screen)
        # crée une instance de la classe AbilityMenu qui servira a afficher le menu des abilités
        self.am = abilities_menu.AbilityMenu(self.screen)

        # création de deux vecteurs : un qui représentera la gravité et l'autre la resistance du support.
        # lorsque une detection avec le sol sera detecté, les deux vecteurs s'annuleront.
        self.gravity = (0, 10)
        self.resistance = (0, 0)
        self.in_the_air = True

        self.jump_number = 0

        self.score_pop_up_list = {}

        # toutes les variables pour la phase 3
        self.platform_group = pygame.sprite.Group()
        self.add_platform_random_1 = lambda: self.platform_group.add(ground.Platform(random.randint(0, W // 2 - 200),
                                                                                     random.randint(-150, 0)))
        self.add_platform_random_2 = lambda: self.platform_group.add(ground.Platform(random.randint(W // 2 - 200,
                                                                                                    W - 200),
                                                                                     random.randint(-150, 0)))

        self.clock = pygame.time.Clock()

        self.actual_time = pygame.time.get_ticks()
        self.begin_jump_time = pygame.time.get_ticks()
        self.begin_updating_time = pygame.time.get_ticks()
        self.platform_spawning_delay = pygame.time.get_ticks()
        self.score_pop_up_delay = pygame.time.get_ticks()
        self.state_delay = pygame.time.get_ticks()
        self.anim_char_delay = pygame.time.get_ticks()
        self.shield_delay = pygame.time.get_ticks()
        self.jumping = False
        self.updating_platforms = False
        
        self.click = False

        # crée un groupe qui contiendra l'onde de choc
        self.chock_wave_group = pygame.sprite.Group()
        # crée une fonction lambda qui rajoute une onde de choc au groupe
        self.add_chock_wave = lambda x, y: self.chock_wave_group.add(chock_wave.ChockWave(self.screen, x, y))

        # toutes les variables relatives aux capacités
        self.shielded = False
        self.chocked = False
        self.last_power = False
        self.shield_cooldown = pygame.time.get_ticks()
        self.chock_cooldown = pygame.time.get_ticks()
        self.last_ability_cooldown = pygame.time.get_ticks()

    def pin_up_life(self):
        police = pygame.font.Font('ressource/Police/PIXELITE.ttf', 25)
        text = police.render(f"Lives : {self.life}", True, (0, 0, 0))
        text_surf = text.get_rect()
        text_surf.center = self.W // 2, 15

        self.screen.blit(text, text_surf)

    def add_comet(self):
        if self.present_round == 1:
            difficulty = 50
        elif self.present_round == 2:
            difficulty = 25
        elif self.present_round == 3:
            difficulty = 15
        else:
            difficulty = 10
        if random.randint(1, difficulty) == 1 and len(self.comet_group) < 10:
            self.comet_group.add(hostile.Comet(self.screen, self.W, self.H, self.pl.rect.x, self.pl.rect.y))

    def gravity_player(self):
        self.pl.rect.y += self.gravity[1] + self.resistance[1]

    def spaceship_shooting(self, x, y, side, sprite):
        if side == "right":
            self.add_red_bullet(x - 10, y + 24, 0, random.randint(y - 100, y + 100))
        else:
            self.add_red_bullet(x + sprite.image.get_width() + 10, y + 24, self.W, random.randint(y - 100, y + 100))

    def space_ship_update(self):
        if self.present_round == 1:
            difficulty = 110
            difficulty2 = 50
        elif self.present_round == 2:
            difficulty = 75
            difficulty2 = 25
        elif self.present_round == 3:
            difficulty = 50
            difficulty2 = 15
        else:
            difficulty = 20
            difficulty2 = 10

        if random.randint(1, difficulty) == 1 and len(self.spaceship_group) < 6:
            print("ship added")
            self.add_spaceship(self.pl.rect.x, self.pl.rect.y)
        if random.randint(1, difficulty2) == 1:
            for sprite in self.spaceship_group:
                if sprite.rect.x > self.W // 2:
                    self.spaceship_shooting(sprite.rect.x, sprite.rect.y, "right", sprite)
                else:
                    self.spaceship_shooting(sprite.rect.x, sprite.rect.y, "left", sprite)

        for sprite in self.spaceship_group:
            if random.randint(1, 5) == 1:
                move = 6
            else:
                move = 3
            sprite.update(life_switch=False, move=move)

            # si un sprite renvoies qu'il est mort, ajoute dans le dictionnaire des sprites mort, en argument
            # 1: sa position en x, en argument 2: sa position en y, et en argument 3: la seconde à laquelle
            # il est mort pour afficher pendant 0.5 sec un message de score
            if sprite.update(life_switch=False, move=0)[0] == "dead":
                self.score_pop_up_list[sprite] = (sprite.update(life_switch=False, move=0)[1],
                                                  sprite.update(life_switch=False, move=0)[2],
                                                  pygame.time.get_ticks())
                try:
                    self.spaceship_group.remove(sprite)
                except Exception as e:
                    print(e)
                self.score += 10

    def all_collisions(self):
        """Detectes toutes les collisions sur tous les sprites"""
        # Collision entre les balles du joueur et les vaisseaux ---------------------------------------------- #
        if self.state == 1:
            for bullet_sprite in self.bullet_group_player:
                for space_ship in self.spaceship_group:
                    get_hits = bullet_sprite.rect.colliderect(space_ship.rect)
                    if get_hits:
                        self.bullet_group_player.remove(bullet_sprite)
                        space_ship.update(life_switch=True, move=6)

            # Collision entre les balles hostiles et le joueur --------------------------------------------------- #
            for sprite in self.bullet_group_hostile:
                get_hits = self.pl.rect.colliderect(sprite.rect)
                if get_hits:
                    self.bullet_group_hostile.remove(sprite)
                    if not self.shielded:
                        self.life -= 2

        # Collision entre les comètes et le joueur ----------------------------------------------------------- #
        if self.state == 0 or self.state == 2:
            for sprite in self.comet_group:
                get_hits = self.pl.rect.colliderect(sprite.rect)
                if get_hits:
                    if not self.shielded:
                        self.life -= 1
                    self.comet_group.remove(sprite)

        # Collision avec les plateformes --------------------------------------------------------------------- #
        if self.state != 2:
            for sprite in self.platform_group:
                get_hits = pygame.sprite.spritecollideany(self.pl, self.platform_group)
                if get_hits:
                    self.resistance = (0, -10)
                    self.jump_number = 0
                    self.in_the_air = False
                    # s'il détecte une collision, il casse la boucle pour éviter de vérifier une autre plateformes
                    # et que cela change les variables comme si le joueur ne touchait pas le sol alors que si
                    # mais simplement sur une autre plateforme (une plateforme avec un index inférieur dans la
                    # liste des plateformes)
                    break
                else:
                    self.resistance = (0, 0)
                    self.in_the_air = True

        # Collision entre les balles et les comètes ---------------------------------------------------------- #
        if self.state == 0 or self.state == 2:
            for sprite in self.bullet_group_player:
                for sprite2 in self.comet_group:
                    get_hits = sprite.rect.colliderect(sprite2.rect)
                    if get_hits:
                        self.score_pop_up_list[sprite2] = (sprite2.rect.centerx,
                                                           sprite2.rect.centery,
                                                           pygame.time.get_ticks())
                        self.score += 10 * self.present_round
                        self.bullet_group_player.remove(sprite)
                        self.comet_group.remove(sprite2)

        try:
            pygame.sprite.groupcollide(self.chock_wave_group, self.comet_group, False, True)
            pygame.sprite.groupcollide(self.chock_wave_group, self.spaceship_group, False, True)
            pygame.sprite.groupcollide(self.chock_wave_group, self.bullet_group_hostile, False, True)
        except Exception as e:
            print(e)

    def pop_up_list_update(self):

        if self.actual_time - self.score_pop_up_delay > 750:
            self.score_pop_up_list = {}
            self.score_pop_up_delay = self.actual_time

        for score in self.score_pop_up_list:
            self.screen.blit(
                self.print_out_text(font="ressource/Police/PIXELITE.ttf", size_font=15,
                                    text=f"+ {10*self.present_round}",
                                    color=(255, 255, 255), pos_x=self.score_pop_up_list[score][0],
                                    pos_y=self.score_pop_up_list[score][1])[0],
                self.print_out_text(font="ressource/Police/PIXELITE.ttf", size_font=15,
                                    text=f"+ {10*self.present_round}", color=(255, 255, 255),
                                    pos_x=self.score_pop_up_list[score][0] + 10,
                                    pos_y=self.score_pop_up_list[score][1])[1])

    # Platforms Patterns ------------------------------------ #

    def pattern_1(self):
        # supprime toutes les plateformes précédentes
        for sprite in self.platform_group:
            self.platform_group.remove(sprite)

        # utilise la fonction lambda plusieurs fois pour créer des plateformes
        self.add_platform((self.W // 2) - 400 - 250, (self.H // 2) - 200)  # plateforme en haut à gauche
        self.add_platform((self.W // 2) + 400, (self.H // 2) - 200)  # plateforme en haut à droite
        self.add_platform((self.W // 2) - 500 - 250, (self.H // 2) + 100)  # plateforme au milieu à gauche
        self.add_platform((self.W // 2) + 500, (self.H // 2) + 100)  # plateforme au milieu à droite
        self.add_platform((self.W // 2) - (250 // 2), (self.H // 2) + 300)  # plateforme tout en bas

    def pattern_2(self):
        # supprime toutes les plateformes précédentes
        for sprite in self.platform_group:
            self.platform_group.remove(sprite)

        self.add_platform((self.W // 2) - (250 // 2) - 400, (self.H // 2) + 125)  # plateforme de gauche
        self.add_platform((self.W // 2) - (250 // 2) + 400, (self.H // 2) + 125)  # plateforme de droite
        self.add_platform((self.W // 2) - (250 // 2), (self.H // 2) - 50)  # plateforme tout au milieu
        self.add_platform((self.W // 2) - (250 // 2), (self.H // 2) + 300)  # plateforme tout en bas au milieu

    def print_out_text(self, font, size_font, text, pos_x, pos_y, color):
        Police = pygame.font.Font(font, size_font)
        text_ = Police.render(text, True, color)
        text_surf = text_.get_rect()
        text_surf.center = (pos_x, pos_y)
        return text_, text_surf

    def main_loop(self):

        print("Ouverture du client.")

        while self.running:

            while self.menu:

                pygame.mouse.set_visible(True)

                self.screen.blit(self.background_menu, (0, 0))
                self.sb.update()

                # récupère tous les évènements
                for event in pygame.event.get():

                    # si le joueur ferme la fenetre, casse la boucle de lancement et
                    # ferme la boucle actuelle, la boucle menu
                    if event.type == pygame.QUIT:
                        # met a jour les touches dans le fichier json
                        self.ke.update_keys()
                        self.running = False
                        self.menu = False

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if self.but.white_button_rect.collidepoint(event.pos):
                            self.menu = False
                            self.jeu = True

                            # remet à zéro toutes les variables du jeu
                            self.life = 100

                            # retire tous les sprites de tous les groupes
                            for sprite in self.spaceship_group:
                                self.spaceship_group.remove(sprite)
                            for sprite in self.comet_group:
                                self.comet_group.remove(sprite)
                            for sprite in self.bullet_group_player:
                                self.bullet_group_player.remove(sprite)
                            for sprite in self.bullet_group_hostile:
                                self.bullet_group_hostile.remove(sprite)

                            # vide le dictionnaire des touches pouur éviter qu'une touche reste sur True quand le joueur
                            # meurt et que le client continue d'appuyer (un bug récurent qui venait à faire continuer de
                            # bouger le joueur car le client était en train d'appuyer sur une touche lorsque son joueur
                            # est mort et la touche n'était ainsi pas remise sur False)
                            self.pressed = {}

                            # vide le dictionnaire contenant toutes les pop up de score
                            self.score_pop_up_list = {}

                            self.beginning_game = pygame.time.get_ticks()

                            self.state = 0
                            self.beginning_phase = pygame.time.get_ticks()

                            # ici, en fonction du niveau qui sera cliqué, le pattern changera
                            if random.randint(0, 1) == 0:
                                self.pattern_2()
                            else:
                                self.pattern_1()

                        elif self.but.white_button_exit_rect.collidepoint(event.pos):
                            # met a jour les touches dans le fichier json
                            self.ke.update_keys()
                            print("Fermeture du client.")
                            self.menu = False
                            self.running = False

                        elif self.but.white_button_keys_rect.collidepoint(event.pos):
                            self.menu = False
                            self.keys_set = True

                    if event.type == pygame.KEYDOWN:
                        self.abi_menu = True
                        self.menu = False

                self.sb.score_board()
                self.but.print_out()

                pygame.display.flip()

            while self.keys_set:

                # ici pas besoin de mettre une boucle d'évèneemnts car la fonction suivante les gere deja
                self.ke.print_out()

                if self.ke.print_out() == "quit":
                    # met a jour les touches dans le fichier json
                    self.ke.update_keys()
                    self.keys_set = False
                    self.running = False
                elif self.ke.print_out() == "return to menu":
                    self.keys_set = False
                    self.menu = True

                pygame.display.flip()

            while self.abi_menu:

                self.am.update_screen()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.abi_menu = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.am.button_exit_rect.collidepoint(event.pos):
                            self.menu = True
                        self.abi_menu = False

                pygame.display.flip()

            while self.jeu:

                # index 0 = jump
                # index 1 = left
                # index 2 = right
                # index 3 = shoot
                # index 4 = exit
                key_bind = self.ke.return_keys()

                # récupère tous les évènements
                for event in pygame.event.get():

                    # si le joueur ferme la fenetre, casse la boucle de lancement et
                    # ferme la boucle actuelle, la boucle jeu
                    if event.type == pygame.QUIT:
                        # met a jour les touches dans le fichier json
                        self.ke.update_keys()
                        self.running = False
                        self.jeu = False

                    # si l'évènement est de type bouton de souris pressé:
                    if event.type == key_bind[3]:
                        self.add_blue_bullet(self.pl.rect.x + (self.pl.playerW // 2),
                                             self.pl.rect.y + (self.pl.playerH // 2),
                                             event.pos[0] + 13, event.pos[1] + 13)
                    # si l'événement est de type touche préssée
                    if event.type == pygame.KEYDOWN:

                        # ajoute à la liste des touches préssées la touche actuellement préssée
                        self.pressed[event.key] = True

                        if event.key == key_bind[0] and self.jump_number < 2:
                            self.pl.jump()
                            self.jump_number += 1

                        # si la touche préssée est la touche ESCAPE
                        if event.key == key_bind[4]:
                            # enregistre toutes les valeurs liées à la parties qui vient d'être jouée
                            if self.score > self.sb.high_score:
                                self.sb.add_high_score(self.score, self.actual_time)
                            self.jeu = False
                            self.menu = True

                            self.sb.add_precedent_score(self.score, self.actual_time)
                            # initialise la boucle menu et ferme la boucle jeu
                            self.menu = True
                            self.jeu = False

                        if event.key == pygame.K_e and not self.chocked:
                            self.chocked = True
                            self.add_chock_wave(self.pl.rect.x, self.pl.rect.y)
                            self.chock_cooldown = self.actual_time

                        if event.key == pygame.K_a and not self.shielded:
                            self.shielded = True
                            self.shield_delay = self.actual_time
                            self.shield_cooldown = self.actual_time

                    if event.type == pygame.KEYUP:
                        self.pressed[event.key] = False

                # si le joueur appuies sur la flèche de gauche, utilise la fonction du joueur 'bouger à gauche'
                if self.pressed.get(key_bind[1]):
                    self.pl.move_left()

                # si le joueur appuies sur la flèche de droite, utilise la fonction du joueur 'bouger à droite'
                if self.pressed.get(key_bind[2]):
                    self.pl.move_right()

                # colore l'écran dans la couleur définit plus haut
                self.screen.blit(self.background_game, (0, 0))
                # met à jour le joueur
                self.pl.update()

                # Cooldowns ------------------------------------------ #

                if self.chocked:
                    if self.actual_time - self.chock_cooldown > 30000:
                        self.chocked = False
                    chock_cd = round(30-((self.actual_time - self.chock_cooldown)/1000))
                else:
                    chock_cd = "RDY"

                if self.shielded:
                    if self.actual_time - self.shield_cooldown > 17000:
                        self.shielded = False
                    shield_cd = round(17-((self.actual_time - self.shield_cooldown)/1000))
                else:
                    shield_cd = "RDY"

                if self.last_power:
                    if self.actual_time - self.last_ability_cooldown > 10000:
                        self.last_power = False
                    last_power_cd = (self.actual_time - self.last_ability_cooldown)/1000
                else:
                    last_power_cd = "RDY"

                # Sprites -------------------------------------------- #

                # dessine toutes les sprites contenues dans le groupe self.bullet_group_player
                self.bullet_group_player.draw(self.screen)
                # update all sprites of the group (class method)
                self.bullet_group_player.update()

                # dessine toutes les sprites contenues dans le groupe self.bullet_group_hostile
                self.bullet_group_hostile.draw(self.screen)
                # met a jour tous les sprites de ce groupe
                self.bullet_group_hostile.update()

                # dessine l'onde de choc (si elle existe)
                try:
                    self.chock_wave_group.draw(self.screen)
                except Exception as e:
                    print(e)
                # met a jour l'onde de choc
                try:
                    self.chock_wave_group.update()
                except Exception as e:
                    print(e)

                # manage the shield
                if self.shielded:
                    if self.actual_time - self.shield_delay < 5000:
                        self.sh.update(self.pl.rect.centerx, self.pl.rect.centery)

                # dessine les comètes
                self.comet_group.draw(self.screen)
                self.comet_group.update()
                if self.phase[self.state] == "comet":
                    self.add_comet()

                # dessine les vaisseaux
                self.spaceship_group.draw(self.screen)
                if self.phase[self.state] == "space ships":
                    self.space_ship_update()

                self.pop_up_list_update()

                # dessine les plateformes
                self.platform_group.draw(self.screen)
                # toutes les demi secondes, change la frame des plateformes
                if self.actual_time - self.begin_time_frame_platform > 500:
                    self.platform_group.update(False, True)
                    self.begin_time_frame_platform = pygame.time.get_ticks()

                if self.pl.rect.y > self.H:
                    self.life -= 50
                    self.pl.rect.x, self.pl.rect.y = self.W // 2, self.H // 2

                if self.state == 2:
                    if self.actual_time - self.platform_spawning_delay > 1000:
                        choice = random.randint(1, 5)
                        if choice >= 3:
                            self.add_platform_random_1()
                            self.add_platform_random_2()
                        elif choice == 1:
                            self.add_platform_random_1()
                        elif choice == 2:
                            self.add_platform_random_2()

                        self.platform_spawning_delay = self.actual_time

                    if not self.jumping:
                        if pygame.sprite.spritecollideany(self.pl, self.platform_group):
                            self.begin_updating_time = self.actual_time
                            self.begin_jump_time = self.actual_time

                    if self.actual_time - self.begin_updating_time < 1000:
                        self.updating_platforms = True
                    else:
                        self.updating_platforms = False

                    if self.updating_platforms:
                        self.platform_group.update(True, False)

                    if self.actual_time - self.begin_jump_time < 1500:
                        self.jumping = True
                    else:
                        self.jumping = False

                    if self.jumping:
                        self.pl.move_up()
                        self.resistance = (0, -10)
                        self.in_the_air = True
                    else:
                        self.resistance = (0, 0)
                        self.in_the_air = False

                    self.add_comet()

                ########################################################################################################
                # Game phase ----------------------------------------------------------------------------------------- #

                # passage à la phase 2 du jeu
                if self.actual_time - self.beginning_phase > 20000 and self.state == 0:
                    self.state += 1
                    self.beginning_phase = self.actual_time
                    self.add_spaceship(self.pl.rect.x, self.pl.rect.y)

                # passage à la phase 3 du jeu
                if self.actual_time - self.beginning_phase > 20000 and self.state == 1:
                    self.state = 2
                    self.beginning_phase = self.actual_time

                    for sprite in self.spaceship_group:
                        self.spaceship_group.remove(sprite)
                    for sprite in self.bullet_group_player:
                        self.bullet_group_player.remove(sprite)
                    for sprite in self.bullet_group_hostile:
                        self.bullet_group_hostile.remove(sprite)
                    for sprite in self.comet_group:
                        self.comet_group.remove(sprite)

                    self.add_platform(random.randint(self.W // 4, (self.W // 4) * 3), 300)

                # retourne à la phase 1 du jeu
                if self.actual_time - self.beginning_phase > 20000 and self.state == 2:
                    self.state = 0
                    self.beginning_phase = self.actual_time

                    for sprite in self.platform_group:
                        self.platform_group.remove(sprite)
                    if random.randint(0, 1) == 1:
                        self.pattern_1()
                    else:
                        self.pattern_2()

                    self.present_round += 1

                ########################################################################################################

                # Overlay --------------------------------- #
                if self.actual_time - self.state_delay > 500:
                    update_ = True
                    self.state_delay = self.actual_time
                else:
                    update_ = False

                self.tb.update(self.life, round(self.actual_time / 1000, 2), self.score,
                               self.present_round, self.state, update_, shield_cd, chock_cd, last_power_cd)

                self.gravity_player()

                # rends la souris invisible pour la remplacer par un curseur personnalisé
                pygame.mouse.set_visible(False)
                self.mo.update()

                if self.life <= 0:
                    if self.score > self.sb.high_score:
                        self.sb.add_high_score(self.score, self.actual_time)
                    self.jeu = False
                    self.menu = True

                    self.sb.add_precedent_score(self.score, self.actual_time)

                # anime le personnage 
                if self.in_the_air:
                    if self.actual_time - self.anim_char_delay > 250:
                        self.pl.anim_jump()
                        self.anim_char_delay = pygame.time.get_ticks()
                elif self.resistance == (0, -10):
                    self.pl.reset_anim()

                # appelle la fonction all_collision qui vérifie toutes les collisions de tous les sprites
                self.all_collisions()
                # met à jour l'écran
                pygame.display.flip()
                # met les fps à 40
                self.clock.tick(40)
                # met à jour le temps actuel
                self.actual_time = pygame.time.get_ticks() - self.beginning_game