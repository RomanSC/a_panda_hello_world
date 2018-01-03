#!/usr/bin/python3
""" physics.py | Wed, Jan 03, 2018 | Roman S. Collins
"""


class Gravity:
    def __init__(self, game, obj):
        self.game = game
        self.obj = obj

        # Limit to falling
        self.gravity_floor = 0
        self.gravity_force = -8

    def update(self, task):
        # Pin to floor
        if self.obj.getZ() <= self.gravity_floor:
            self.obj.setZ(self.gravity_floor)

        elif self.obj.getZ() >= self.gravity_floor:
            self.obj.setZ(self.obj.getZ() + (1 * self.gravity_force))

        return task.cont


class Velocity:
    def __init__(self, game, obj):
        self.game = game
        self.obj = obj

# Other realistic physics stuff I plan to add later...
# This whole file:
# TODO
