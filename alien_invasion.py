import sys
import pygame
from Settings import Settings

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

    def run_game(self) -> None:
        #Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit
                    sys.exit()

            self.screen.blit(self.bg,(0,0))



            pygame.display.flip()
            self.clock.tick(self.Settings.FPS)        
    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

