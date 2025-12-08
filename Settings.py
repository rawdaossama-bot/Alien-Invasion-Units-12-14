"""
Settings.py

Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Lab12_Rawda-Hassanin_1.git
- Pygame documentation: https://www.pygame.org/docs/

Defines the Settings class which centralizes all game configuration values.
Includes screen dimensions, file paths for assets, and gameplay parameters.
"""
from pathlib import Path


class Settings:
    """Game configuration and asset paths.

    Attributes:
        name: Game window title.
        screen_w: Screen width in pixels.
        screen_h: Screen height in pixels.
        FPS: Target frames per second.
        bg_file: Path to background image file.
        ship_file: Path to ship sprite image file.
        ship_w: Ship sprite width in pixels.
        ship_h: Ship sprite height in pixels.
        ship_speed: Ship movement speed in pixels per frame.
        bullet_file: Path to bullet sprite image file.
        sound_file: Path to laser sound effect file.
        bullet_speed: Bullet movement speed in pixels per frame.
        bullet_w: Bullet sprite width in pixels.
        bullet_h: Bullet sprite height in pixels.
        bullet_amount: Maximum number of simultaneous bullets allowed.
    """

    def __init__(self) -> None:
        """Initialize all game settings and asset file paths."""
        self.name: str = 'Alien Invasion'
        self.screen_w = 1100
        self.screen_h = 600
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets'/ 'images' / 'Galaxy.png'

        self.ship_file = Path.cwd() / 'Assets'/ 'images'/ 'Ship3.png'
        self.ship_w = 80
        self.ship_h = 100
        self.ship_speed = 15

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.sound_file = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5
from pathlib import Path

