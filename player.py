#!/usr/bin/python3
""" player.py | Tue, Jan 02, 2018 | Roman S. Collins
"""
from direct.actor.Actor import Actor

import inspect


# class Player(Actor):
class Player:
    def __init__(self, game):
        # super().__init__(self)
        self.game = game

        self.scale = 0.2
        self.pos = (0, 0, 0)
        self.hpr = (0, 0, 0)

        self.walk_speed = 1.0
        self.run_speed = 1.5
        self.sprint_speed = 2.5
        self.moving = None
        self.sprinting = False

        self.object = Actor("assets/models/figures/gray_boy.egg",
                            {"run": "assets/models/figures/gray_boy.egg",
                             "walk": "assets/models/figures/gray_boy.egg"})
        print(inspect.getargspec(Actor()))

        self.object.reparentTo(self.game.render)
        self.object.setScale(self.scale)

        self.object.setPos(self.pos[0],
                           self.pos[0],
                           self.pos[0])

        self.object.setHpr(self.hpr[0],
                           self.hpr[1],
                           self.hpr[2])

        # Create Player Nodes
        # TODO
        # Aiming node, maybe attach camera node to a
        # location directly behind the player and rotate it
        # to view the aim node using .setHpr()
        # self.aim_node = self.render.attachNewNode("turn_Node")

        # Node for the player
        self.node = self.game.render.attachNewNode("player node")
        self.node.reparentTo(self.object)

    def getPos(self):
        return self.object.getPos()

    def getHpr(self):
        return self.object.getHpr()

    def getX(self):
        return self.object.getX()

    def getY(self):
        return self.object.getY()

    def getZ(self):
        return self.object.getZ()

    def getH(self):
        return self.object.getH()

    def getP(self):
        return self.object.getP()

    def getR(self):
        return self.object.getR()

    def track_player_pos_rotation(self, task):
        # Player position set once a frame
        # rather than many times within
        # multiple function calls
        self.object.pos = self.object.getPos()
        self.object.hpr = self.object.getHpr()

        return task.cont

    def move_forward(self, w):
        if w:
            self.moving = "forward"
        elif not w:
            self.moving = None

    def move_left(self, a):
        if a:
            self.moving = "left"
        elif not a:
            self.moving = None

    def move_backward(self, s):
        if s:
            self.moving = "backward"
        elif not s:
            self.moving = None

    def move_right(self, d):
        if d:
            self.moving = "right"
        elif not d:
            self.moving = None

    def player_sprint_toggle(self, s):
        if s:
            self.sprinting = True
        elif not s:
            self.sprinting = False

    # Movement etc...
    def player_controller(self, task):
        if self.moving == "forward":
            self.object.setY(self.object.getY() + (1 * self.run_speed))

        if self.moving == "backward":
            self.object.setY(self.object.getY() - (1 * self.run_speed))

        if self.moving == "left":
            self.object.setH(self.object.getH() + (1 * self.run_speed))

        if self.moving == "right":
            self.object.setH(self.object.getH() - (1 * self.run_speed))

        if self.sprinting:
            self.player_speed * 2

        return task.cont


