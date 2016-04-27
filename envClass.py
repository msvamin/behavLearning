__author__ = 'Amin'

"""
Example usage:
from benavLearning.envClass import EnvClass
envObj = envClass()
"""

import numpy as np
import random


class EnvClass(object):
    LENGTH = 20
    WIDTH = 20
    OBSTACLES = np.zeros((WIDTH, LENGTH))
    GOAL = (20, 20)

    def __init__(self):
        self._x_position = None
        self._y_position = None

    def setPosition(self, x_position, y_position):
        self._x_position = x_position
        self._y_position = y_position

    def getPosition(self):
        return self._x_position, self._y_position

    def randPosition(self):
        self._x_position = random.randint(1, self.WIDTH)
        self._y_position = random.randint(1, self.LENGTH)