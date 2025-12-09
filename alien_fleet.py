import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manages a fleet of alien ships.

    Attributes:
        aliens: A list of Alien instances in the fleet.
        settings: Game settings instance for configuration.
        screen: Pygame display Surface.
    """

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the alien fleet.

        Args:
            game: The AlienInvasion instance that created this fleet.
        """
        self.aliens = []
        self.settings = game.Settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        self.game = game
        
        self.create_fleet()
    
    def create_fleet(self) -> None:
        alien_w = self.settings.alien_w
        screen_w = self.settings.screen_w
        fleet_w = self.calculate_fleet_size(alien_w, screen_w)
        
       # half_screen = self.settings.screen_w 
        fleet_horizantle_space = (fleet_w * alien_w)
        x_offset = int((screen_w - fleet_horizantle_space) // 2)
        
        for col in range(fleet_w):
            current_x = alien_w * col + x_offset 
            """y = 50  # Starting y position for the fleet
            alien = Alien(game=None, x=x, y=y)  # Pass None for game, adjust as needed
            self.fleet.add(alien)
        """
            self._creat_alien(current_x, 10)
        #self.calculate_fleet_size(alien_w, screen_w)

    def calculate_fleet_size(self, alien_w, screen_w):
        
        
        fleet_w = (screen_w//alien_w)
        if fleet_w %2 == 0:
            # Make fleet width odd for centering
            fleet_w -= 1
        else: 
            fleet_w -= 2
        return fleet_w    
            
    def _creat_alien(self, current_x: int, current_y: int) -> None: 
        new_alien = Alien(self, current_x, current_y)   
        
        self.fleet.add(new_alien)
    def draw(self)-> None:
        """Draw all aliens in the fleet to the screen."""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()   
         