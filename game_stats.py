"""
game_stats.py

Lab_13_Rawda Hassanin_1
Author: Rawda Hassanin
Date: 11/30/2025
Resources:
- Starter repo: https://github.com/rawdaossama-bot/Alien-Invasion-Units-12-14.git

Defines the GameStats class which tracks game state information.
Manages the player's remaining ships and other game statistics.
"""


class GameStats:
    """Track game statistics and state.

    Attributes:
        ship_left: Number of ships remaining for the player.
    """

    def __init__(self, ship_limit: int) -> None:
        """Initialize game statistics.

        Args:
            ship_limit: The initial number of ships available to the player.
        """
        self.ship_left = ship_limit
