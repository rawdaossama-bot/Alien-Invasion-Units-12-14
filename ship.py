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
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.Settings.ship_file)
        self.image = pygame.transform.scale(self.image, (60,60))
           #(self.Settings.screen_w,self.Settings.screen_h))
        
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self)-> None:
        self.screen.blit(self.image, self.rect)    

        