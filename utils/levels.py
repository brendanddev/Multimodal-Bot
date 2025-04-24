"""
levels.py

Brendan Dileo, April 2025
"""

from enum import Enum

# Level enum for tracking xp thresholds
class Level(Enum):
    Noob = 0
    Middleman = 50
    Veteran = 150
    Elite = 300
    Legend = 750

    # Retreives the users current level
    @classmethod
    def get_level(cls, xp: int) -> 'Level':
        levels = sorted(cls, key=lambda l: l.value)
        current_level = levels[0]
        for level in levels:
            if xp >= level.value:
                current_level = level
            else:
                break 

        return current_level
    
    # Determines the users next level and how much xp is needed to reach it
    @classmethod
    def get_next_level(cls, xp: int) -> tuple['Level', int] | None:
        levels = sorted(cls, key=lambda l: l.value)
        for level in levels:
            if xp < level.value:
                return level, level.value - xp
        return None 

