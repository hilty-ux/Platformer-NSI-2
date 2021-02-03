import pygame
import json


class KeyChoose:

    def __init__(self, screen):

        self.screen = screen

        # définis un dictionnaire qui servira à afficher les touches correspondantes
        self.keys = {
            pygame.MOUSEBUTTONDOWN: "Mouse",
            pygame.K_ESCAPE: "Esc",
            pygame.K_F1: "F1",
            pygame.K_F2: "F2",
            pygame.K_F3: "F3",
            pygame.K_F4: "F4",
            pygame.K_F5: "F5",
            pygame.K_F6: "F6",
            pygame.K_F7: "F7",
            pygame.K_F8: "F8",
            pygame.K_F9: "F9",
            pygame.K_F10: "F10",
            pygame.K_F11: "F11",
            pygame.K_F12: "F12",
            pygame.K_1: "&",
            pygame.K_2: "é",
            pygame.K_3: '"',
            pygame.K_4: "'",
            pygame.K_5: "(",
            pygame.K_6: "-",
            pygame.K_7: "è",
            pygame.K_8: "_",
            pygame.K_9: "ç",
            pygame.K_0: "à",
            pygame.K_TAB: "Tab",
            pygame.K_CAPSLOCK: "Caps Lock",
            pygame.K_LSHIFT: "Shift",
            pygame.K_RSHIFT: "Shift Right",
            pygame.K_LCTRL: "Ctrl Left",
            pygame.K_RCTRL: "Ctrl Right",
            pygame.K_LALT: "Alt Left",
            pygame.K_RALT: "Alt Right",
            pygame.K_LEFT: "Left",
            pygame.K_RIGHT: "Right",
            pygame.K_UP: "Up",
            pygame.K_DOWN: "Down",
            pygame.K_SPACE: "Space",
            pygame.K_BACKSPACE: "Backspace",
            pygame.K_KP_ENTER: "Enter",
            pygame.K_a: "A",
            pygame.K_b: "B",
            pygame.K_c: "C",
            pygame.K_d: "D",
            pygame.K_e: "E",
            pygame.K_f: "F",
            pygame.K_g: "G",
            pygame.K_h: "H",
            pygame.K_i: "I",
            pygame.K_j: "J",
            pygame.K_k: "K",
            pygame.K_l: "L",
            pygame.K_m: "M",
            pygame.K_n: "N",
            pygame.K_o: "O",
            pygame.K_p: "P",
            pygame.K_q: "Q",
            pygame.K_r: "R",
            pygame.K_s: "S",
            pygame.K_t: "T",
            pygame.K_u: "U",
            pygame.K_v: "V",
            pygame.K_w: "W",
            pygame.K_x: "X",
            pygame.K_y: "Y",
            pygame.K_z: "Z",
            94: "^",
            36: "$",
            13: "Enter",
            249: "ù",
            42: "*",
            44: ",",
            59: ";",
            58: ":",
            33: "!",
            60: "<",
            }
        self.reversed_keys = {value: key for (key, value) in self.keys.items()}

        with open("datas.json") as f:
            self.datas = json.load(f)

        self.key_jump = self.datas["keys"]["jump"]
        self.key_left = self.datas["keys"]["left"]
        self.key_right = self.datas["keys"]["right"]
        self.key_shoot = self.datas["keys"]["shoot"]
        self.key_exit = self.datas["keys"]["exit"]

        self.real_keys = [self.reversed_keys[self.key_jump],
                          self.reversed_keys[self.key_left],
                          self.reversed_keys[self.key_right],
                          self.reversed_keys[self.key_shoot],
                          self.reversed_keys[self.key_exit]]

        self.black_button_exit = pygame.image.load("ressource/Menu Boutons/ExitBlack.gif")
        self.black_button_exit_rect = self.black_button_exit.get_rect()
        self.white_button_exit = pygame.image.load("ressource/Menu Boutons/ExitWhite.gif")
        self.white_button_exit_rect = self.white_button_exit.get_rect()

        self.white_button_exit_rect.x, self.white_button_exit_rect.y = 20, 20
        self.black_button_exit_rect.x, self.black_button_exit_rect.y = 20, 20

        self.blinking = None

        self.background = pygame.image.load("ressource/Background/background_menu.jpg")

        pygame.draw.rect(self.screen, (0, 255, 0), [160, 530, 686, 20])
        pygame.display.flip()

    def return_keys(self):
        return self.real_keys

    def update_keys(self):

        self.datas["keys"]["jump"] = self.key_jump
        self.datas["keys"]["left"] = self.key_left
        self.datas["keys"]["right"] = self.key_right
        self.datas["keys"]["shoot"] = self.key_shoot
        self.datas["keys"]["exit"] = self.key_exit

        with open("datas.json", "w") as f:
            json.dump(self.datas, f, indent=2)

    def print_out(self):

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        if not self.white_button_exit_rect.collidepoint(mouse_pos):
            self.screen.blit(self.white_button_exit, self.white_button_exit_rect)
        else:
            self.screen.blit(self.black_button_exit, self.black_button_exit_rect)

        police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 50)

        text = [police.render("Jump :", True, (255, 255, 255)),
                police.render("Left :", True, (255, 255, 255)),
                police.render("Right :", True, (255, 255, 255)),
                police.render("Shoot :", True, (255, 255, 255)),
                police.render("Exit :", True, (255, 255, 255))]

        text_rect = [i.get_rect() for i in text]

        for i in range(len(text_rect)):
            text_rect[i].right = 500
            text_rect[i].centery = 400 + (100 * i)

        for i in range(len(text)):
            self.screen.blit(text[i], text_rect[i])

        keys = [police.render(self.key_jump, True, (255, 255, 255)),
                police.render(self.key_left, True, (255, 255, 255)),
                police.render(self.key_right, True, (255, 255, 255)),
                police.render(self.key_shoot, True, (255, 255, 255)),
                police.render(self.key_exit, True, (255, 255, 255))]

        keys_rect = [i.get_rect() for i in keys]

        for i in range(len(keys_rect)):
            keys_rect[i].left = 550
            keys_rect[i].centery = 400 + (100 * i)

        if self.blinking is not None:
            pygame.draw.rect(self.screen, (0, 0, 200), keys_rect[self.blinking])

        for i in range(len(keys)):
            if keys_rect[i].collidepoint(mouse_pos) and self.blinking is None:
                pygame.draw.rect(self.screen, (255, 0, 0), keys_rect[i])
            self.screen.blit(keys[i], keys_rect[i])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(keys_rect)):
                    if keys_rect[i].collidepoint(event.pos):
                        self.blinking = i
                        break
                    else:
                        self.blinking = None
                if self.white_button_exit_rect.collidepoint(event.pos):
                    return "return to menu"

            if self.blinking is not None and self.blinking != 3:
                if event.type == pygame.KEYDOWN:
                    self.real_keys[self.blinking] = event.key
                    if self.blinking == 0:
                        self.key_jump = self.keys[event.key]
                    elif self.blinking == 1:
                        self.key_left = self.keys[event.key]
                    elif self.blinking == 2:
                        self.key_right = self.keys[event.key]
                    elif self.blinking == 4:
                        self.key_exit = self.keys[event.key]
                    self.blinking = None
                    break
            elif self.blinking is not None and self.blinking == 3:
                if event.type == pygame.KEYDOWN:
                    self.real_keys[self.blinking] = event.key
                    self.key_shoot = self.keys[event.key]
                    self.blinking = None
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.real_keys[self.blinking] = pygame.MOUSEBUTTONDOWN
                    self.key_shoot = self.keys[pygame.MOUSEBUTTONDOWN]
                    self.blinking = None
                    break