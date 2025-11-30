import pygame
from Settings import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship:
    

    def __init__(self, game: 'AlienInvasion' ) ->None:
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


    def update(self)-> None:
         # updating the position of the ship
        temp_speed = self.Settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed

        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x    


    def draw(self)-> None:
        self.screen.blit(self.image, self.rect)    

        