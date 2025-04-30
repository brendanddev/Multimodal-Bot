"""
levels.py

Defines a Enum class to represent the different levels a user can have within the discord server.
There are 5 different levels, and the users level is based on the amount of experience points they 
have (XP). 

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

    # Class level method that retreives the users current level
    # Takes a reference to the class itself and the amount of xp to determine level
    @classmethod
    def get_level(cls, xp: int) -> 'Level':
        # Sorts each enum by its value
        levels = sorted(cls, key=lambda lvl: lvl.value)
        # Checks which level the user is based on xp, starts at lowest level
        current_level = levels[0]
        for level in levels:
            if xp >= level.value:
                current_level = level
            else:
                break 
        return current_level
    

    # Class level method that determines the users next level, and how much xp is required to reach it
    # Takes a reference to the class itself and the amount of xp the user has
    @classmethod
    def get_next_level(cls, xp: int) -> tuple['Level', int] | None:
        levels = sorted(cls, key=lambda l: l.value)
        for level in levels:
            if xp < level.value:
                return level, level.value - xp
        return None 

