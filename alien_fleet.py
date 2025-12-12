"""
alien_fleet.py

Lab_13_Rawda Hassanin_1
Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Alien-Invasion-Units-12-14.git

Defines the AlienFleet class which manages a fleet of alien enemies.
Handles fleet creation, movement, collision detection, and rendering.
"""
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manages a fleet of alien ships.

    Attributes:
        game: Reference to the AlienInvasion instance.
        settings: Game settings instance for configuration.
        fleet: pygame.sprite.Group containing all active Alien sprites.
        fleet_direction: Current direction of fleet movement (1 for right, -1 for left).
        fleet_drop_speed: Vertical distance fleet drops when hitting screen edge.
    """

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the alien fleet.

        Args:
            game: The AlienInvasion instance that created this fleet.
        """
        self.game = game
        self.settings = game.Settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        
    def create_fleet(self) -> None:
        """Create and populate the alien fleet in a grid pattern.

        Calculates fleet dimensions and offset to center it on screen,
        then creates aliens in a checkerboard pattern.
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h
        
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)
         
        self._create_rectangle(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle(self, alien_w: int, alien_h: int, fleet_w: int, 
                         fleet_h: int, x_offset: int, y_offset: int) -> None:
        """Create aliens in a rectangular grid pattern with checkerboard spacing.

        Args:
            alien_w: Width of each alien sprite.
            alien_h: Height of each alien sprite.
            fleet_w: Number of columns in the fleet.
            fleet_h: Number of rows in the fleet.
            x_offset: Horizontal offset for centering the fleet.
            y_offset: Vertical offset for centering the fleet.
        """
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset 
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._creat_alien(current_x, current_y)

    def calculate_offsets(self, alien_w: int, alien_h: int, screen_w: int, 
                         fleet_w: int, fleet_h: int) -> tuple:
        """Calculate x and y offsets to center the fleet on screen.

        Args:
            alien_w: Width of each alien sprite.
            alien_h: Height of each alien sprite.
            screen_w: Screen width in pixels.
            fleet_w: Number of columns in the fleet.
            fleet_h: Number of rows in the fleet.

        Returns:
            A tuple of (x_offset, y_offset) for fleet positioning.
        """
        half_screen = self.settings.screen_h // 2
        fleet_horizantle_space = (fleet_w * alien_w)
        fleet_vertical_space = (fleet_h * alien_h)
        x_offset = int((screen_w - fleet_horizantle_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w: int, screen_w: int, alien_h: int, 
                            screen_h: int) -> tuple:
        """Calculate the number of aliens that fit on screen in a grid.

        Makes fleet dimensions odd numbers for proper centering.

        Args:
            alien_w: Width of each alien sprite.
            screen_w: Screen width in pixels.
            alien_h: Height of each alien sprite.
            screen_h: Screen height in pixels.

        Returns:
            A tuple of (fleet_width, fleet_height) in alien count.
        """
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h / 2) // alien_h)
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else: 
            fleet_w -= 2
            
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2
               
        return int(fleet_w), int(fleet_h)  
            
    def _creat_alien(self, current_x: int, current_y: int) -> None:
        """Create a single alien and add it to the fleet.

        Args:
            current_x: X-coordinate for the new alien.
            current_y: Y-coordinate for the new alien.
        """
        new_alien = Alien(self, current_x, current_y) 
        self.fleet.add(new_alien)  
        
    def _check_fleet_egdges(self) -> None:
        """Check if any alien has hit the screen edge and reverse direction if so.

        When an edge is detected, reverses fleet direction and drops the fleet.
        """
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1
                self._drop_alien_fleet()
                break
        
    def _drop_alien_fleet(self) -> None:
        """Move all aliens down by fleet_drop_speed when hitting screen edges."""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed
        
    def update_fleet(self) -> None:
        """Update fleet movement and check for edge collisions each frame.

        Calls edge checking and then updates all aliens.
        """
        self._check_fleet_egdges()
        self.fleet.update()    
        
    def draw(self) -> None:
        """Draw all aliens in the fleet to the screen."""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()   
            
    def check_collision(self, other_group) -> dict:
        """Check collisions between fleet and another sprite group.

        Args:
            other_group: A pygame sprite group to check collisions with (typically bullets).

        Returns:
            A dict of collisions (pygame.sprite.groupcollide format).
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)      
    
    def check_bottom(self) -> bool:
        """Check if any alien has reached the bottom of the screen.

        Returns:
            True if any alien's bottom edge is at or past screen height, False otherwise.
        """
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
         
    def check_destroyed_stats(self) -> bool:
        """Check if the entire fleet has been destroyed.

        Returns:
            True if no aliens remain in the fleet, False otherwise.
        """
        return not self.fleet
