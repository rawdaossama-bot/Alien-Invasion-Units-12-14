"""
arsenal.py

Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Lab12_Rawda-Hassanin_1.git
- Pygame documentation: https://www.pygame.org/docs/

Provides ShipArsenal, a thin wrapper around a pygame.sprite.Group that
manages the ship's bullets. Responsibilities:
- create and store active Bullet instances
- update and remove off-screen bullets
- draw bullets to the screen
- enforce the configured maximum number of bullets
"""
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    


class ShipArsenal:
    """Manage the ship's active bullets.

    Attributes:
        game: Reference to the main AlienInvasion instance.
        Settings: Shortcut to game.Settings for configuration values.
        arsenal: pygame.sprite.Group holding active Bullet sprites.
    """

    def __init__(self,game: 'AlienInvasion') -> None:
        """Create a ShipArsenal tied to the given game.

        Args:
            game: The AlienInvasion instance that owns this arsenal.
        """
        self.game = game
        self.Settings = game.Settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self)-> None:
        """Update all bullets and remove those that left the screen.

        Calls the sprite Group update method and then removes bullets whose
        rect.bottom has moved past the top of the display.
        """
        self.arsenal.update()
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)


    def draw(self)->None:
        """Draw each active bullet to the game's screen.

        Iterates the active bullets and calls their draw method.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Attempt to create and add a new Bullet.

        Respects Settings.bullet_amount as the maximum simultaneous bullets.

        Returns:
            True if a new Bullet was created and added, False otherwise.
        """
        if len(self.arsenal) < self.Settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
# ...existing code...
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class ShipArsenal:
    def __init__(self,game: 'AlienInvasion') -> None:    
        self.game = game
        self.Settings = game.Settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self)-> None:
        self.arsenal.update()
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0: 
                self.arsenal.remove(bullet)


    def draw(self)->None:      
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.Settings.bullet_amount:
            new_bullet = Bullet(self.game) 
            self.arsenal.add(new_bullet)
            return True
        return False
