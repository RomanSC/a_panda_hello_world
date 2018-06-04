#!/usr/bin/python3
""" physics.py | Wed, Jan 03, 2018 | Roman S. Collins
"""
from config import *
from constants import *
from helpers import *

from panda3d.core import Vec3

class Gravity:
    def __init__(self, game):
        self.game = game
        self.player = self.game.player

    def update(self, task):
        dt = globalClock.getDt()

        if self.game.player.getZ() > 1:
            self.game.player.velocity[2] -= abs(GRAVITY)

        return task.cont
