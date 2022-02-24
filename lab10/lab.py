"""6.009 Fall 2019 Lab 10 -- 6.009 Zoo"""

from math import ceil
from math import acos
# NO OTHER IMPORTS ALLOWED!

class Constants:
    """
    A collection of game-specific constants.

    You can experiment with tweaking these constants, but
    remember to revert the changes when running the test suite!
    """
    # width and height of keepers
    KEEPER_WIDTH = 30
    KEEPER_HEIGHT = 30

    # width and height of animals
    ANIMAL_WIDTH = 30
    ANIMAL_HEIGHT = 30

    # width and height of food
    FOOD_WIDTH = 10
    FOOD_HEIGHT = 10

    # width and height of rocks
    ROCK_WIDTH = 50
    ROCK_HEIGHT = 50

    # thickness of the path
    PATH_THICKNESS = 30

    CRAZY_NAP_LENGTH = 125

    CRAZY_ENDURANCE = 6

    TRAINEE_THRESHOLD = 3

    TEXTURES = {
        'rock': '1f5ff',
        'animal': '1f418',
        'SpeedyZookeeper': '1f472',
        'ThriftyZookeeper': '1f46e',
        'CheeryZookeeper': '1f477',
        'food': '1f34e',
        'Demon': '1f479',
        'VHS': '1f4fc',
        'TraineeZookeeper': '1f476',
        'CrazyZookeeper': '1f61c',
        'SleepingZookeeper': '1f634'
    }

    FORMATION_INFO = {'SpeedyZookeeper':
                       {'price': 9,
                        'interval': 55,
                        'throw_speed_mag': 20},
                      'ThriftyZookeeper':
                       {'price': 7,
                        'interval': 45,
                        'throw_speed_mag': 7},
                      'CheeryZookeeper':
                       {'price': 10,
                        'interval': 35,
                        'throw_speed_mag': 2}, 

                      'TraineeZookeeper':
                       {'price': 4,
                        'interval': 65,
                        'throw_speed_mag': 1},
                      'CrazyZookeeper':
                        {'price': 11,
                         'interval': 10,
                         'throw_speed_mag': 13},

                      'Demon': 
                       {'width': 50,
                        'height': 50,
                        'radius': 75,
                        'multiplier': 2,
                        'price': 8},
                      'VHS':
                       {'width': 30,
                        'height': 30,
                        'radius': 75, 
                        'multiplier': 0.5,
                        'price': 5}}

# New spec for timestep(self, mouse):
# 
# (0. Do not take any action if the player is already defeated.)
#  1. Compute the new speed of animals based on the presence of nearby VHS cassettes or demons.
#  2. Compute any changes in formation locations and remove any off-board formations.
#  3. Handle any food-animal collisions, and remove the fed animals and the eaten food.
#  4. Upgrade trainee zookeeper if needed.
#  5. Throw new food if possible.
#  6. Spawn a new animal from the path's start if needed.
#  7. Handle mouse input, which is the integer tuple coordinate of a player's click, the string 
#     label of a particular particular zookeeper type, `'Demon'`, `'VHS'`, or `None`.
#  8. Redeem one dollar per animal fed this timestep.
#  9. Check for the losing condition.

################################################################################
##  Copy and paste your code from lab9 below EXCEPT for the Constants class.  ##
##  The Constants class above contains the changes needed for the lab.        ##
################################################################################

### lab9 code here ###

if __name__ == '__main__':
    pass