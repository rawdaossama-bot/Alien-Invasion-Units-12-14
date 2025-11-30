from pathlib import Path

class Settings:

    def __init__(self)->None:
        self.name: str = 'Alien Invasion'
        self.screen_w = 1100
        self.screen_h = 600
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets'/ 'images' / 'Starbasesnow.png'


        self.ship_file = Path.cwd() / 'Assets'/ 'images'/ 'ship2(no bg).png'
        self.ship_w = 30
        self.ship_h = 40