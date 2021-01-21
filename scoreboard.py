import pygame
import json


class ScoreBoard:

    def __init__(self, screen, W, H):

        # ouvre le fichier contenant les variables de high score
        with open('datas.json') as d:
            self.data = json.load(d)

        # recupere toutes les variables
        self.high_score = self.data["scores"]["high-score"]
        self.high_score_time = self.data["scores"]["high-score-time"]
        self.precedent_scores = self.data["scores"]["precedent-game-score"]
        self.precedent_times = self.data["scores"]["precedent-game-time"]

        self.screen = screen
        self.W = W
        self.H = H

    def update(self):

        with open('datas.json') as d:
            self.data = json.load(d)

        self.high_score = self.data["scores"]["high-score"]
        self.high_score_time = self.data["scores"]["high-score-time"]
        self.precedent_scores = self.data["scores"]["precedent-game-score"]
        self.precedent_times = self.data["scores"]["precedent-game-time"]

    def add_precedent_score(self, score, time):

        # on descends chaque valeur d'un rang
        self.precedent_scores[6] = self.precedent_scores[5]
        self.precedent_scores[5] = self.precedent_scores[4]
        self.precedent_scores[4] = self.precedent_scores[3]
        self.precedent_scores[3] = self.precedent_scores[2]
        self.precedent_scores[2] = self.precedent_scores[1]
        self.precedent_scores[1] = self.precedent_scores[0]

        self.precedent_times[6] = self.precedent_times[5]
        self.precedent_times[5] = self.precedent_times[4]
        self.precedent_times[4] = self.precedent_times[3]
        self.precedent_times[3] = self.precedent_times[2]
        self.precedent_times[2] = self.precedent_times[1]
        self.precedent_times[1] = self.precedent_times[0]

        # on assigne les nouvelles valeurs au rang 1
        self.precedent_scores[0] = score
        self.precedent_times[0] = time

        with open('datas.json', 'w') as d:
            json.dump(self.data, d, indent=2)

    def add_high_score(self, high_score, high_score_time):

        self.data["scores"]["high-score"] = high_score
        self.data["scores"]["high-score-time"] = high_score_time

        with open('datas.json', 'w') as d:
            json.dump(self.data, d, indent=2)

    def score_board(self):

        self.screen.fill((255, 255, 255))
        police = pygame.font.Font('ressource/Police/PIXELITE.ttf', 75)
        text = police.render("Score Board", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = 675 - 302, 150
        self.screen.blit(text, text_rect)

        # dessine le rectangle principal contenant les valeurs du scoreboard
        pygame.draw.line(self.screen, (0, 0, 0), (100, 200), (self.W // 2 - 260, 200), width=10)
        pygame.draw.line(self.screen, (0, 0, 0), (100, 196), (100, self.H - 105), width=10)
        pygame.draw.line(self.screen, (0, 0, 0), (100, self.H - 110), (self.W // 2 - 260, self.H - 110), width=10)
        pygame.draw.line(self.screen, (0, 0, 0), (self.W // 2 - 260, 196), (self.W // 2 - 260, self.H - 105), width=10)

        # dessine toutes les lignes horizontales
        pygame.draw.line(self.screen, (0, 0, 0), (100, 275), (self.W // 2 - 260, 275), width=10)
        pygame.draw.line(self.screen, (0, 0, 0), (100, 362), (self.W // 2 - 260, 362), width=3)
        pygame.draw.line(self.screen, (0, 0, 0), (100, 449), (self.W // 2 - 260, 449), width=3)
        pygame.draw.line(self.screen, (0, 0, 0), (100, 536), (self.W // 2 - 260, 536), width=3)
        pygame.draw.line(self.screen, (0, 0, 0), (100, 623), (self.W // 2 - 260, 623), width=3)
        pygame.draw.line(self.screen, (0, 0, 0), (100, 710), (self.W // 2 - 260, 710), width=3)
        pygame.draw.line(self.screen, (0, 0, 0), (100, 797), (self.W // 2 - 260, 797), width=3)

        # dessine toutes les lignes verticales
        pygame.draw.line(self.screen, (0, 0, 0), ((self.W // 2 - 260 + 100) // 2, 200),
                         ((self.W // 2 - 260 + 100) // 2, self.H - 105), width=10)
        pygame.draw.line(self.screen, (0, 0, 0), (((self.W // 2 - 260 + 100) // 4) * 2.75, 200),
                         (((self.W // 2 - 260 + 100) // 4) * 2.75, self.H - 105), width=3)

        police = pygame.font.Font('ressource/Police/PIXELITE.ttf', 25)
        text = police.render("Highest Score", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = 235, 362-275 + 155
        self.screen.blit(text, text_rect)

        police = pygame.font.Font('ressource/Police/PIXELITE.ttf', 40)
        if self.high_score < 1000:
            text = police.render(str(self.high_score), True, (0, 0, 0))
        else:
            text = police.render(f"{round(self.high_score / 1000, 1)}k", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = 445, 362 - 275 + 155
        self.screen.blit(text, text_rect)

        high_score_time_min = self.high_score_time // 60000
        high_score_time_sec = round((self.high_score_time - (high_score_time_min * 60000)) / 1000, 2)

        police = pygame.font.Font('ressource/Police/PIXELITE.ttf', 25)
        text = police.render(f"{high_score_time_min} : {high_score_time_sec}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = 580, 362 - 275 + 155
        self.screen.blit(text, text_rect)

        for i in range(7):
            police = pygame.font.Font('ressource/Police/PIXELITE.ttf', 20)
            text = police.render(f"Last game {i + 1}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = 235, 362 - 275 + 242 + (87 * i)
            self.screen.blit(text, text_rect)

        for i in range(7):
            police = pygame.font.Font('ressource/Police/PIXELITE.ttf', 40)
            if self.precedent_scores[i] < 1000:
                text = police.render(str(self.precedent_scores[i]), True, (0, 0, 0))
            else:
                text = police.render(f"{round(self.precedent_scores[i] / 1000, 2)}k", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = 445, 362 - 275 + 242 + (87 * i)
            self.screen.blit(text, text_rect)

        for i in range(7):
            time_min = self.precedent_times[i] // 60000
            time_sec = round((self.precedent_times[i] - (time_min * 60000)) / 1000, 2)

            police = pygame.font.Font('ressource/Police/PIXELITE.ttf', 25)
            if time_sec < 10:
                text = police.render(f"{time_min} : 0{time_sec}", True, (0, 0, 0))
            else:
                text = police.render(f"{time_min} : {time_sec}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = 570, 362 - 275 + 242 + (87 * i)
            self.screen.blit(text, text_rect)
