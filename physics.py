#!/usr/bin/python3
""" physics.py | Wed, Jan 03, 2018 | Roman S. Collins
"""
from panda3d.core import Vec3

class Gravity:
    def __init__(self, game):
        self.game = game
        self.player = self.game.player

        self.g = 8.0

        # self.player.v = (0.0, 0.0, 0.0)
        # self.player.g = (0.0, 0.0, float(self.g))

    def update(self, task):
        dt = globalClock.getDt()

        # if self.player.v[2] > 200.00:
        #     self.player.v = (self.player.v[0], self.player.v[1], 200.00)

        # print("PLAYER VELOCITY: {}".format(self.player.v))
        # print("PLAYER GRAVITY: {}".format(self.player.g))
        # print("APPLIED GRAVITY: {}".format((0.0, 0.0, -((1.0 * (self.player.v[2]
        #     - self.player.g[2]) * dt)))))

        # Player gravity

        pos = self.player.getPos()
        print(pos)

        # if pos[2] == 0.0:
        #     pass 

        # elif pos[2] > 0.0:
        #     self.player.setPos(self.player, (pos[0], pos[1], -self.g))

        #     pos = self.player.getPos()

        #     if pos[2] < 0.0:
        #         self.player.setPos(self.player, (pos[0], pos[1], 0.0))

        return task.cont
