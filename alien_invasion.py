"""
alien_invasion.py
alien_invasion module for Alien Invasion game.

Lab_13_Rawda Hassanin_1
Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Alien-Invasion-Units-12-14.git
- Pygame documentation: https://www.pygame.org/docs/

Main module to run the Alien Invasion game.
Provides the AlienInvasion class which initializes the game, handles the
main loop, events, and screen updates.
"""
import sys
import pygame
from Settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from time import sleep


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
        self.game_stats = GameStats(self.Settings.startign_ship_count)

        self.screen = pygame.display.set_mode((self.Settings.screen_w, self.Settings.screen_h))
        pygame.display.set_caption(self.Settings.name)

        self.bg = pygame.image.load(self.Settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.Settings.screen_w, self.Settings.screen_h))
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
        self.game_active = True


    def run_game(self) -> None:
        """Start the main game loop.

        The loop continues while self.running is True. Each iteration:
        - handles input events
        - updates the ship and alien fleet if game is active
        - checks for collisions
        - redraws the screen
        - enforces the target FPS
        """
        while self.running:
            self._chaeck_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collision()
            self._update_screen()
            self.clock.tick(self.Settings.FPS)  
            
    def _check_collision(self) -> None:
        """Check all collision events in the game.

        Tests for:
        - Ship colliding with aliens
        - Aliens reaching the bottom of the screen
        - Bullets colliding with aliens
        - All aliens destroyed
        """
        # Check collision for ship
        if self.ship.check_collision(self.alien_fleet.fleet):
            self.check_game_stats()
            
        # Check for collisions for aliens and bottom of screen.
        if self.alien_fleet.check_bottom():
            self.check_game_stats()
        
        # Check collision of projectiles and aliens
        collision = self.alien_fleet.check_collision(self.ship.arsenal.arsenal)
        if collision:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            
        if self.alien_fleet.check_destroyed_stats():  
            self._reset_level()
            
    def check_game_stats(self) -> None:
        """Update game stats after collision and handle ship loss.

        Decrements ship count if ships remain, resets the level,
        and waits before resuming. Sets game_active to False if no ships left.
        """
        if self.game_stats.ship_left > 0:
            self.game_stats.ship_left -= 1
            self._reset_level()   
            pygame.time.delay(500)
            sleep(0.5)
        else:
            self.game_active = False  
            print("Game Over!")  
    
    def _reset_level(self) -> None:
        """Reset the level after aliens are destroyed or ship is hit.

        Clears all bullets and aliens, then creates a new alien fleet.
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _update_screen(self) -> None:
        """Redraw the screen and flip to the new display.

        Draws the background, ship, and alien fleet, then updates 
        the display buffer.
        """
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

            
    def _chaeck_events(self) -> None:
        """Respond to keypresses and mouse events.

        Processes the pygame event queue and dispatches to specific handlers
        for key down, key up, and quit events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keyup_events(self, event) -> None:
        """Handle key release events.

        Updates ship movement flags when arrow keys are released.

        Args:
            event: Pygame key event object.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False              

    
    def _check_keydown_events(self, event) -> None:
        """Handle key press events.

        Sets movement flags, fires ship weapons on space, and quits on 'q'.

        Args:
            event: Pygame key event object.
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
            pygame.quit()
            sys.exit()

    
    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

