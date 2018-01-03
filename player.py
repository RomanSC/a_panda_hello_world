#!/usr/bin/python3
""" player.py | Tue, Jan 02, 2018 | Roman S. Collins
"""
from direct.actor.Actor import Actor

from location import Location
from physics import Gravity


# TODO:
# rotate_right should eventually become move_right
# rotate_left should eventually become move_left
# Cursor position should eventually determine
# player rotation

# Keys Q and E should cause the player to strafe
# left and right

class Player(Actor):
    def __init__(self, game):
        super().__init__(self)
        self.game = game

        self.scale = 0.2
        self.start_pos = (0, 0, 0)
        self.start_hpr = (0, 0, 0)

        self.speed_modes = {"walk": 1.0, "run": 1.5, "sprint": 2.5}
        self.speed_default = self.speed_modes["run"]
        self.speed = self.speed_modes["run"]

        self.jump_height = 3

        self.moving = None

        self.loadModel("assets/models/figures/gray_boy.egg",
                       "gray_boy_body")

        self.reparentTo(self.game.render)
        self.setScale(self.scale)

        self.setPos(*self.start_pos)
        self.setHpr(*self.start_hpr)

        # Create Player Nodes

        # TODO
        # Aiming node, maybe attach camera node to a
        # location directly behind the player and rotate it
        # to view the aim node using .setHpr()
        # self.aim_node = self.render.attachNewNode("turn_Node")

        # Node for the player
        self.node = self.game.render.attachNewNode("player node")
        self.node.reparentTo(self)

        self.location = Location(self.game, self)
        self.gravity = Gravity(self.game, self)

    def move_forward(self, w):
        if w:
            self.moving = "forward"
        elif not w:
            self.moving = None

    def rotate_left(self, a):
        if a:
            self.moving = "left"
        elif not a:
            self.moving = None

    def move_backward(self, s):
        if s:
            self.moving = "backward"
        elif not s:
            self.moving = None

    def rotate_right(self, d):
        if d:
            self.moving = "right"
        elif not d:
            self.moving = None

    def toggle_sprint(self):
        if self.speed != self.speed_modes["sprint"]:
            self.speed = self.speed_modes["sprint"]
        else:
            self.speed = self.speed_default

    def jump(self):
        self.setZ(self.getZ() + (1 * self.jump_height))

    # Movement etc...
    def controller(self, task):
        if self.moving == "forward":
            self.setY(self.getY() + (1 * self.speed))

        if self.moving == "backward":
            self.setY(self.getY() - (1 * self.speed))

        if self.moving == "left":
            self.setH(self.getH() + (1 * self.speed))

        if self.moving == "right":
            self.setH(self.getH() - (1 * self.speed))

        return task.cont
