import sys
import pygame
from Settings import Settings
from ship import Ship
from arsenal import ShipArsenal


class AlienInvasion:
    def __init__(self)->None:
        pygame.init()
        pygame.mixer.init()
        self.Settings = Settings()

        self.screen =pygame.display.set_mode((self.Settings.screen_w,self.Settings.screen_h))
        pygame.display.set_caption(self.Settings.name)


        self.bg = pygame.image.load(self.Settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
        (self.Settings.screen_w, self.Settings.screen_h)
         )
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.Settings.sound_file)
        self.laser_sound.set_volume(0.5)


        self.ship = Ship(self, ShipArsenal(self))


    def run_game(self) -> None:
        #Game Loop
        while self.running:
            self._chaeck_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.Settings.FPS) 

    def _update_screen(self)-> None:
        self.screen.blit(self.bg,(0,0))
        self.ship.draw()
 
        pygame.display.flip()

            
    def _chaeck_events(self)-> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keyup_events(self, event)-> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False              

    
    def _check_keydown_events(self, event)-> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True 

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  
        elif event.key == pygame.K_SPACE:
             if self.ship.fire():
                 self.laser_sound.play()
                 self.laser_sound.fadeout(250)
                
        elif event.key == pygame.K_q:
             self.running = False
             pygame.quit
             sys.exit()

    
    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

