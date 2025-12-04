"""
ship.py

Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Lab12_Rawda-Hassanin_1.git
- Pygame documentation: https://www.pygame.org/docs/

Defines the Ship class which represents the player's ship in the game.
Handles loading the ship sprite, movement, drawing, and delegating firing
and ammunition updates to an Arsenal instance.
"""
import pygame
from Settings import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """A controllable player ship.

    Attributes:
        game: Reference to the main AlienInvasion object.
        Settings: Game settings instance (alias of game.Settings).
        screen: Pygame display Surface.
        boundaries: Rect representing the screen boundaries.
        image: Surface for the ship sprite.
        rect: Rect for the ship position.
        moving_right: Flag for rightward movement.
        moving_left: Flag for leftward movement.
        x: Float x-position for smooth movement.
        arsenal: Arsenal instance that handles bullets/weapons.
    """

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal' ) ->None:
        """Initialize the ship and place it at the bottom center of the screen.

        Loads and scales the ship image, sets up movement flags and position,
        and stores a reference to the provided Arsenal for firing and updates.
        """
        self.game = game
        self.Settings = game.Settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.Settings.ship_file)
        self.image = pygame.transform.scale(self.image, (60,60))
           #(self.Settings.screen_w,self.Settings.screen_h))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x =float(self.rect.x)
        self.arsenal = arsenal

    def update(self)-> None:
        """Update ship position and its arsenal each frame.

        Calls the internal movement updater then delegates to the arsenal's
        update method so bullets/projectiles are updated together with the ship.
        """
         # updating the position of the ship
        self._update_ship_movement() 
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Adjust the ship's x position based on movement flags and speed.

        Constrains movement to the screen boundaries and stores the new x
        coordinate back into the rect for rendering.
        """
        temp_speed = self.Settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed

        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x   

    def draw(self)-> None:
        """Draw the ship and its arsenal to the screen surface."""
        self.screen.blit(self.image, self.rect)
        self.arsenal.draw()

    def fire(self) ->bool:
        """Attempt to fire a bullet via the arsenal.

        Returns:
            bool: True if a shot was fired (arsenal accepted a new bullet),
            False otherwise.
        """
        return self.arsenal.fire_bullet()
        

        