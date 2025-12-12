"""
alien.py
Lab13_Rawda-Hassanin_1 module for Alien Invasion game.

Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Alien-Invasion-Units-12-14.git
- Pygame documentation: https://www.pygame.org/docs/

Defines the Alien class which represents an enemy sprite in the game.
Handles alien sprite loading, positioning, movement, and rendering.
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """An enemy alien sprite controlled by the fleet.

    Attributes:
        fleet: Reference to the AlienFleet that manages this alien.
        screen: Pygame display Surface.
        settings: Game settings instance for alien configuration.
        image: Surface for the alien sprite.
        rect: Rect for the alien position.
        x: Float x-position for smooth horizontal movement.
        y: Float y-position for vertical positioning.
    """

    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initialize an alien at the specified position.

        Loads and scales the alien image, positions it at the given coordinates,
        and initializes movement tracking.

        Args:
            fleet: The AlienFleet instance that created this alien.
            x: Initial x-coordinate for the alien.
            y: Initial y-coordinate for the alien.
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.Settings
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
          (self.settings.alien_w, self.settings.alien_h))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
      

    def update(self) -> None:
        """Update alien position each frame.

        Moves the alien horizontally at the configured fleet_speed in the
        direction set by the fleet, and updates the rect for rendering.
        """
        temp_speed = self.settings.fleet_speed    
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self) -> bool:
        """Check if the alien has reached the screen edge.

        Returns:
            True if the alien's rect has reached or passed the right or left
            screen boundary, False otherwise.
        """
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self) -> None:
        """Draw the alien sprite to the screen surface."""
        self.screen.blit(self.image, self.rect)

