import pygame, random
import player
import ground
import mouse
import bullet
import hostile


class Game:

    def __init__(self, screen, W, H):

        # récupère la fenêtre
        self.screen = screen

        # initialise les variables de stade de jeu
        self.running = True
        self.menu = True
        self.jeu = False

        # définis la phase du jeu, si ce sont des comètes qui tombent ou des lasers lattéraux,
        # ou encore des vaisseau qui attaquent
        self.phase = ["comet", "space ships", "laser"]
        self.state = 0
        self.beginning_phase = pygame.time.get_ticks()

        # initialise les variables de couleur
        self.background_menu = (200, 200, 200)
        self.background_game = (0, 100, 100)

        # définis une liste des touches préssées (vide)
        self.pressed = {}

        # définit l'horloge du jeu afin de pouvoir gérer les fps
        self.clock = pygame.time.Clock()
        self.actual_time = pygame.time.get_ticks()
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
        self.flames_group = pygame.sprite.Group()
        self.add_flames = lambda x, y, begining_index: self.flames_group.add(ground.Flame(x, y, begining_index))

        # crée le groupe de vaisseau
        self.spaceship_group = pygame.sprite.Group()
        self.add_spaceship = lambda x, y: self.spaceship_group.add(hostile.SpaceShip(x, y, W, H, self.screen))

        # crée une instance du joueur
        self.pl = player.Player(self.screen, W, H)
        # crée une instance de la classe souris
        self.mo = mouse.MouseCursor(self.screen)

        # création de deux vecteurs : un qui représentera la gravité et l'autre la resistance du support.
        # lorsque une detection avec le sol sera detecté, les deux vecteurs s'annuleront.
        self.gravity = (0, 10)
        self.resistance = (0, 0)

    def add_comet(self):
        if random.randint(1, 30) == 1:
            self.comet_group.add(hostile.Comet(self.screen, self.W, self.H, self.pl.rect.x, self.pl.rect.y))

    def gravity_player(self):
        self.pl.rect.y += self.gravity[1] + self.resistance[1]

    def spaceship_shooting(self, x, y, side, sprite):
        if side == "right":
            self.add_red_bullet(x - 10, y + 24, 0, random.randint(y - 100, y + 100))
        else:
            self.add_red_bullet(x + sprite.image.get_width() + 10, y + 24, self.W, random.randint(y - 100, y + 100))

    # Platforms Patterns ------------------------------------ #

    def pattern_1(self):
        # utilise la fonction lambda plusieurs fois pour créer des plateformes
        self.add_platform((self.W // 2) - 400 - 250, (self.H // 2) - 200)  # plateforme en haut à gauche
        self.add_platform((self.W // 2) + 400, (self.H // 2) - 200)  # plateforme en haut à droite
        self.add_platform((self.W // 2) - 500 - 250, (self.H // 2) + 100)  # plateforme au milieu à gauche
        self.add_platform((self.W // 2) + 500, (self.H // 2) + 100)  # plateforme au milieu à droite
        self.add_platform((self.W // 2) - (250 // 2), (self.H // 2) + 300)  # plateforme tout en bas

        for i in range(22):
            if i % 2 == 0:
                index = 0
            else:
                index = 1
            self.add_flames(i * 83, self.H - 75, index)

    def main_loop(self):

        while self.running:

            while self.menu:

                # récupère tous les évènements
                for event in pygame.event.get():

                    # si le joueur ferme la fenetre, casse la boucle de lancement et
                    # ferme la boucle actuelle, la boucle menu
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.menu = False

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_p:
                            self.menu = False
                            self.jeu = True

                            # ici, en fonction du niveau qui sera cliqué, le pattern changera
                            self.pattern_1()

                self.screen.fill(self.background_menu)

                pygame.display.flip()

            while self.jeu:

                # récupère tous les évènements
                for event in pygame.event.get():

                    # si le joueur ferme la fenetre, casse la boucle de lancement et
                    # ferme la boucle actuelle, la boucle jeu
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.jeu = False

                    # si l'évènement est de type bouton de souris pressé:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.add_blue_bullet(self.pl.rect.x + (self.pl.playerW // 2),
                                             self.pl.rect.y + (self.pl.playerH // 2),
                                             event.pos[0] + 13, event.pos[1] + 13)

                    # si l'événement est de type touche préssée
                    if event.type == pygame.KEYDOWN:

                        # ajoute à la liste des touches préssées la touche actuellement préssée
                        self.pressed[event.key] = True

                        # si la touche préssée est la touche ESCAPE
                        if event.key == pygame.K_ESCAPE:
                            # initialise la boucle menu et ferme la boucle jeu
                            self.menu = True
                            self.jeu = False

                    if event.type == pygame.KEYUP:
                        self.pressed[event.key] = False

                # si le joueur appuies sur la flèche de gauche, utilise la fonction du joueur 'bouger à gauche'
                if self.pressed.get(pygame.K_LEFT):
                    self.pl.move_left()

                # si le joueur appuies sur la flèche de droite, utilise la fonction du joueur 'bouger à droite'
                if self.pressed.get(pygame.K_RIGHT):
                    self.pl.move_right()

                if self.pressed.get(pygame.K_UP):
                    self.pl.move_up()

                # colore l'écran dans la couleur définit plus haut
                self.screen.fill(self.background_game)
                # met à jour le joueur
                self.pl.update()

                ##########################################SPRITES#######################################################

                # dessine toutes les sprites contenues dans le groupe self.bullet_group_player
                self.bullet_group_player.draw(self.screen)
                # update all sprites of the group (class method)
                self.bullet_group_player.update()

                # dessine toutes les sprites contenues dans le groupe self.bullet_group_hostile
                self.bullet_group_hostile.draw(self.screen)
                # met a jour tous les sprites de ce groupe
                self.bullet_group_hostile.update()

                # dessine les comètes
                self.comet_group.draw(self.screen)
                self.comet_group.update()
                if self.phase[self.state] == "comet":
                    self.add_comet()

                # dessine les vaisseaux
                self.spaceship_group.draw(self.screen)
                if self.phase[self.state] == "space ships":
                    if random.randint(1, 110) == 1:
                        print("ship added")
                        self.add_spaceship(self.pl.rect.x, self.pl.rect.y)
                    if random.randint(1, 25) == 1:
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

                # dessine toutes les flammes
                self.flames_group.draw(self.screen)
                if self.actual_time - self.begin_time_frame_flames > 250:
                    self.flames_group.update()
                    self.begin_time_frame_flames = pygame.time.get_ticks()

                # check for collisions between sprites in the group self.bullet_group and the group self.comet_group,
                # the first group won't kill the sprite wich collided ('False'), but the second one does ('True')
                pygame.sprite.groupcollide(self.bullet_group_player, self.comet_group, False, True, None)

                # dessine les plateformes
                self.platform_group.draw(self.screen)
                # toutes les demi secondes, change la frame des plateformes
                if self.actual_time - self.begin_time_frame_platform > 500:
                    self.platform_group.update()
                    self.begin_time_frame_platform = pygame.time.get_ticks()

                for bullet_sprite in self.bullet_group_player:
                    for space_ship in self.spaceship_group:
                        get_hits = bullet_sprite.rect.colliderect(space_ship.rect)
                        if get_hits:
                            self.bullet_group_player.remove(bullet_sprite)
                            space_ship.update(life_switch=True)

                for sprite in self.platform_group:
                    get_hits = pygame.sprite.spritecollideany(self.pl, self.platform_group)
                    if get_hits:
                        self.resistance = (0, -10)
                        break
                    else:
                        self.resistance = (0, 0)

                # ces lignes représentent le milieu, le quart et les trois quarts de l'écran, pour vérifier si les
                # plateformes sont bien alignées
                """pygame.draw.line(self.screen, (0, 0, 0), (self.W // 2, 0), (self.W // 2, self.H))
                pygame.draw.line(self.screen, (0, 0, 0), (self.W // 4, 0), (self.W // 4, self.H))
                pygame.draw.line(self.screen, (0, 0, 0), (self.W // 2 + (self.W // 4), 0), (self.W // 2 + (self.W // 4), self.H))"""

                ########################################################################################################

                ########################################GAME PHASE######################################################

                # passage à la phase 2 du jeu
                if self.actual_time - self.beginning_phase > 3000 and self.state == 0:
                    self.state += 1
                    self.beginning_phase = self.actual_time
                    self.add_spaceship(self.pl.rect.x, self.pl.rect.y)

                # passage à la phase 3 du jeu
                if self.actual_time - self.beginning_phase > 30000 and self.state == 1:
                    self.state = 0
                    self.beginning_phase = self.actual_time

                ########################################################################################################

                self.gravity_player()

                # rends la souris invisible pour la remplacer par un curseur personnalisé
                pygame.mouse.set_visible(False)
                self.mo.update()

                # met à jour l'écran
                pygame.display.flip()
                # met les fps à 40
                self.clock.tick(40)
                # met à jour le temps actuel
                self.actual_time = pygame.time.get_ticks()
