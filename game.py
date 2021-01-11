import pygame


class Game:
    
    def __init__(self):
        
        self.running  = True
        self.menu = True
        self.jeu = False
        
    def main_loop(self):
        
        while self.running:
            
            while self.menu:
                
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.menu = False
                
            while self.jeu: