#!/usr/bin/python3
""" player.py | Tue, Jan 02, 2018 | Roman S. Collins
"""
from direct.actor.Actor import Actor

import inspect


class Player(Actor):
    def __init__(self, game):
        super().__init__(self)
        self.game = game

        self.scale = 0.2
        self.pos = (0, 0, 0)
        self.hpr = (0, 0, 0)

        self.walk_speed = 1.0
        self.run_speed = 1.5
        self.sprint_speed = 2.5
        self.moving = None
        self.sprinting = False

        # self = Actor("assets/models/figures/gray_boy.egg",
        #                     {"run": "assets/models/figures/gray_boy.egg",
        #                      "walk": "assets/models/figures/gray_boy.egg"})

        self.reparentTo(self.game.render)
        self.setScale(self.scale)

        self.setPos(self.pos[0],
                    self.pos[0],
                    self.pos[0])

        self.setHpr(self.hpr[0],
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
        self.node.reparentTo(self)

    # def getPos(self):
    #     return self.getPos()

    # def getHpr(self):
    #     return self.getHpr()

    # def getX(self):
    #     return self.getX()

    # def getY(self):
    #     return self.getY()

    # def getZ(self):
    #     return self.getZ()

    # def getH(self):
    #     return self.getH()

    # def getP(self):
    #     return self.getP()

    # def getR(self):
    #     return self.getR()

    def track_player_pos_rotation(self, task):
        # Player position set once a frame
        # rather than many times within
        # multiple function calls
        self.pos = self.getPos()
        self.hpr = self.getHpr()

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
            self.setY(self.getY() + (1 * self.run_speed))

        if self.moving == "backward":
            self.setY(self.getY() - (1 * self.run_speed))

        if self.moving == "left":
            self.setH(self.getH() + (1 * self.run_speed))

        if self.moving == "right":
            self.setH(self.getH() - (1 * self.run_speed))

        if self.sprinting:
            self.player_speed * 2

        return task.cont


