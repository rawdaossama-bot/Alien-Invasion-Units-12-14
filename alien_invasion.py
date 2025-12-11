"""
alien_invasion.py
alien_invasion module for Alien Invasion game.

Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Lab12_Rawda-Hassanin_1.git
- Pygame documentation: https://www.pygame.org/docs/

Main module to run the Alien Invasion game.
Provides the AlienInvasion class which initializes the game, handles the
main loop, events, and screen updates.
"""
import sys
import pygame
from Settings import Settings
from ship import Ship
from arsenal import ShipArsenal
#from alien import Alien
from alien_fleet import AlienFleet


class AlienInvasion:
    """Manage game assets and behavior for Alien Invasion.

    Responsible for initializing pygame, loading settings and resources,
    creating the main Ship object, running the game loop, processing
    events, and updating the display.
    """

    def __init__(self)->None:
        """Initialize game, create screen, load resources, and create ship."""
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
        
        
        self.impact_sound = pygame.mixer.Sound(self.Settings.impact_sound)
        self.impact_sound.set_volume(0.5)

        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()


    def run_game(self) -> None:
        """Start the main game loop.

        The loop continues while self.running is True. Each iteration:
        - handles input events
        - updates the ship
        - redraws the screen
        - enforces the target FPS
        """
        #Game Loop
        while self.running:
            self._chaeck_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._check_collision()
            self._update_screen()
            self.clock.tick(self.Settings.FPS)  
            
    def _check_collision(self) -> None:
        #check colloson for ship
        if self.ship.check_collision(self.alien_fleet.fleet):
           self._reset_level()
            # subtract one lif eif possible
            
        #Check for collisions for aliens and bottom of screen.
        if self.alien_fleet.check_bottom():
            self._reset_level()
        
        #check collision of projectiles and aliens
        collision = self.alien_fleet.check_collision(self.ship.arsenal.arsenal)
        if collision:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
          
    
    def _reset_level(self) -> None:
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
            
            

    def _update_screen(self)-> None:
        """Redraw the screen and flip to the new display.

            s the background and the ship, then updates the display buffer.
        """
        self.screen.blit(self.bg,(0,0))
        self.ship.draw()
        self.alien_fleet.draw()
 
        pygame.display.flip()

            
    def _chaeck_events(self)-> None:
        """Respond to keypresses and mouse events.

        Processes the pygame event queue and dispatches to specific handlers.
        """
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
        """Handle key release events.

        Updates ship movement flags when arrow keys are released.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False              

    
    def _check_keydown_events(self, event)-> None:
        """Handle key press events.

        Sets movement flags, fires ship weapons on space, and quits on 'q'.
        """
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

