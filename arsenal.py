"""
arsenal.py

Lab_13_Rawda Hassanin_1
Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Alien-Invasion-Units-12-14.git
- Pygame documentation: https://www.pygame.org/docs/

This module provides the ShipArsenal class, which manages the player's bullets
in the Alien Invasion game. Responsibilities include:

- Creating and storing active Bullet instances.
- Updating bullet positions and removing bullets that leave the screen.
- Drawing bullets to the game screen.
- Enforcing the configured maximum number of bullets on screen.
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
        """Initialize a ShipArsenal tied to a specific game.

        Args:
            game (AlienInvasion): The main AlienInvasion instance that owns this arsenal.
        """
        self.game = game
        self.Settings = game.Settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self)-> None:
        """Update all bullets and remove those that left the screen.
        
        Iterates through the sprite group, updating each bullet's position.
        Bullets that move past the top of the screen are removed.
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
    """
    Manage the ship's active bullets in the Alien Invasion game.

    Responsibilities:
    - Store and manage active Bullet instances in a pygame.sprite.Group.
    - Update bullet positions each frame and remove bullets that leave the screen.
    - Draw all bullets on the game screen.
    - Enforce the maximum number of bullets allowed simultaneously.

    Attributes:
        game (AlienInvasion): Reference to the main game instance.
        Settings: Shortcut to the game's Settings for configuration values.
        arsenal (pygame.sprite.Group): Group holding all active bullets.
    """
    def __init__(self,game: 'AlienInvasion') -> None:
        """
        Initialize a ShipArsenal tied to the given game instance.

        Args:
            game (AlienInvasion): The main game instance that owns this arsenal.
        """    
        self.game = game
        self.Settings = game.Settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self)-> None:
        """
        Update all bullets in the arsenal and remove bullets that leave the screen.

        Iterates through all bullets, calls their update method, and removes
        any bullet whose rect.bottom is less than or equal to 0.
        """
        self.arsenal.update()
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0: 
                self.arsenal.remove(bullet)


    def draw(self)->None:      
        """
        Draw all active bullets to the game screen.

        Iterates through each bullet in the arsenal and calls its draw method.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """
        Attempt to create and add a new bullet to the arsenal.

        Respects Settings.bullet_amount as the maximum simultaneous bullets.

        Returns:
            bool: True if a new bullet was created and added, False otherwise.
        """
        if len(self.arsenal) < self.Settings.bullet_amount:
            new_bullet = Bullet(self.game) 
            self.arsenal.add(new_bullet)
            return True
        return False
