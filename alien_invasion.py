import sys
import pygame
from Settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self)->None:
        pygame.init()
        self.Settings = Settings()

        self.screen =pygame.display.set_mode((self.Settings.screen_w,self.Settings.screen_h))
        pygame.display.set_caption(self.Settings.name)


        self.bg = pygame.image.load(self.Settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
        (self.Settings.screen_w, self.Settings.screen_h)
         )
        self.running = True
        self.clock = pygame.time.Clock()

        self.ship = Ship(self)


    def run_game(self) -> None:
        #Game Loop
        while self.running:
            self._chaeck_events()

            self._update_screen()
            self.clock.tick(self.Settings.FPS) 

    def _update_screen(self):
        self.screen.blit(self.bg,(0,0))
        self.ship.draw()
 
        pygame.display.flip()

            
    def _chaeck_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit
                sys.exit()       
    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

