import pygame, random
import player
import ground
import mouse
import bullet
import comet


class Game:

    def __init__(self, screen, W, H):

        # récupère la fenêtre
        self.screen = screen

        # initialise les variables de stade de jeu
        self.running = True
        self.menu = True
        self.jeu = False

        # initialise les variables de couleur
        self.background_menu = (200, 200, 200)
        self.background_game = (0, 100, 100)

        # définis une liste des touches préssées (vide)
        self.pressed = {}

        # définit l'horloge du jeu afin de pouvoir gérer les fps
        self.clock = pygame.time.Clock()

        self.W = W
        self.H = H

        # crée un groupe de sprite qui contiendra toutes les plateformes
        self.platform_group = pygame.sprite.Group()
        self.platform_group.add(ground.Ground(self.screen, self.W, self.H))
        self.platform_group.add(ground.Platform(random.randint(0, self.W - 200), random.randint(200, 800)))

        # lambda est une fonction écrite en une ligne, pour éviter de définir une fonction qui prendra une seule ligne
        # cette fonction ajoute une plateforme au groupe des plateformes
        self.add_platform = lambda : self.platform_group.add(ground.Platform(random.randint(0, self.W - 200),
                                                                             random.randint(200, 800)))

        # crée un groupe pour toutes les balles qui vont être tirées par le joueur
        self.bullet_group = pygame.sprite.Group()
        # lambda est une fonction écrite en une ligne, pour éviter de définir une fonction qui prendra une seule ligne
        # cette fonction ajoute une balle au groupe des balles tirées par le joueur
        self.add_bullet = lambda x, y, target_x, target_y : self.bullet_group.add(bullet.Bullet(x, y, target_x, target_y))

        # crée un groupe pour toutes les comètes
        self.comet_group = pygame.sprite.Group()

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
            self.comet_group.add(comet.Comet(self.screen, self.W, self.H, self.pl.rect.x, self.pl.rect.y))

    def gravity_player(self):
        self.pl.rect.y += self.gravity[1] + self.resistance[1]

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

                    #si l'évènement est de type bouton de souris pressé:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.add_bullet(self.pl.rect.x + (self.pl.playerW // 2),
                                        self.pl.rect.y + (self.pl.playerH // 2),
                                        event.pos[0]+13, event.pos[1]+13)

                    # si l'événement est de type touche préssée
                    if event.type == pygame.KEYDOWN:

                        # ajoute à la liste des touches préssées la touche actuellement préssée
                        self.pressed[event.key] = True

                        # si la touche préssée est la touche ESCAPE
                        if event.key == pygame.K_ESCAPE:
                            # initialise la boucle menu et ferme la boucle jeu
                            self.menu = True
                            self.jeu = False

                        if event.key == pygame.K_t:
                            self.add_platform()

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

                # dessine toutes les sprites contenues dans le groupe self.bullet
                self.bullet_group.draw(self.screen)
                # update all sprites of the group (class method)
                self.bullet_group.update()

                # dessine les comètes
                self.comet_group.draw(self.screen)
                self.comet_group.update()
                self.add_comet()

                # check for collisions between sprites in the group self.bullet_group and the group self.comet_group,
                # the first group won't kill the sprite wich collided ('False'), but the second one does ('True')
                pygame.sprite.groupcollide(self.bullet_group, self.comet_group, False, True, None)

                # dessine les plateformes
                self.platform_group.draw(self.screen)

                for sprite in self.platform_group:
                    get_hits = pygame.sprite.spritecollideany(self.pl, self.platform_group)
                    if get_hits:
                        self.resistance = (0, -10)
                        break
                    else:
                        self.resistance = (0, 0)

                ########################################################################################################

                self.gravity_player()

                # rends la souris invisible pour la remplacer par un curseur personnalisé
                pygame.mouse.set_visible(False)
                self.mo.update()

                # met à jour l'écran
                pygame.display.flip()
                # met les fps à 40
                self.clock.tick(40)
