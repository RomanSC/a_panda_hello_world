#!/usr/bin/python3
""" physics.py | Wed, Jan 03, 2018 | Roman S. Collins
"""
from config import *
from helpers import *

from panda3d.core import Vec3

class Gravity:
    def __init__(self, game):
        self.game = game
        self.player = self.game.player

        # self.player.v = (0.0, 0.0, 0.0)
        # self.player.g = (0.0, 0.0, float(self.g))

    def update(self, task):
        dt = globalClock.getDt()

        # self.game.player.setPos(self.game.player, times_tup(GRAVITY, dt))

        return task.cont
