"""
alien.py
Lab13_Rawda-Hassanin_1 module for Alien Invasion game.
Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Lab12_Rawda-Hassanin_1.git
- Pygame documentation: https://www.pygame.org/docs/

Defines the Bullet class which represents a projectile fired by the player's ship.
Handles bullet sprite loading, positioning, movement, and rendering.
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """A projectile fired by the player's ship.

    Attributes:
        screen: Pygame display Surface.
        settings: Game settings instance for bullet configuration.
        image: Surface for the bullet sprite.
        rect: Rect for the bullet position.
        y: Float y-position for smooth upward movement.
    """

    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initialize a bullet at the ship's top-center position.

        Loads and scales the bullet image, positions it at the ship's midtop,
        and initializes movement tracking.

        Args:
            game: The AlienInvasion instance that created this bullet.
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.Settings
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
          (self.settings.alien_w, self.settings.alien_h))
        #self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        #self.laser_sound.set_volume(0.5)

        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
       

    def update(self) -> None:
        """Update bullet position each frame.

        Moves the bullet upward at the configured bullet_speed and updates
        the rect for rendering.
        """
        temp_speed = self.settings.fleet_speed    
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y
    
        #self.y -= self.settings.bullet_speed
        #self.rect.y = self.y  
    def check_edges(self):
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)
        
    
    def draw_alien(self) -> None:
        """Draw the bullet to the screen surface."""
        self.screen.blit(self.image, self.rect)

