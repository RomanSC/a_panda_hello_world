#!/usr/bin/python3
""" physics.py | Wed, Jan 03, 2018 | Roman S. Collins
"""


class Gravity:
    def __init__(self, game, obj):
        self.game = game
        self.obj = obj

        # Limit to falling
        self.ground = (self.game.ground_object.getZ() + 0.80)
        self.gravity_force = -9.81

        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity_z = 0

    def update(self, task):
        dt = globalClock.getDt()

        if self.obj.getZ() >= self.ground:
            self.obj.setZ(self.obj.getZ() + self.velocity_z * dt)

        if self.obj.getZ() <= self.ground:
            self.obj.setZ(self.ground)

        self.velocity_z += self.gravity_force * dt
        return task.cont


class Velocity:
    def __init__(self, game, obj):
        self.game = game
        self.obj = obj

# Other realistic physics stuff I plan to add later...
# This whole file:
# TODO
