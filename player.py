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

        # Based on human average walk, jog, and run speeds
        self.speed_modes = {"walk": 1.4, "run": 2.68224, "sprint": 12.5171}
        self.speed_default = self.speed_modes["run"]
        self.speed = self.speed_modes["run"]

        self.turn_speed = 60

        # Based on human average of 20"
        # TODO: Fine tune to be more
        # 'athletic' and playable
        self.jump_height = 0.508

        # self.moving = None

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

    # def toggle_sprint(self):
    #     if self.speed != self.speed_modes["sprint"]:
    #         self.speed = self.speed_modes["sprint"]
    #     else:
    #         self.speed = self.speed_default

    def jump(self):
        if self.getZ() <= self.gravity.gravity_floor:
            self.setPos(self, (0, 0, (1 * self.jump_height)))

        self.game.keymap.map["jump"] = False

    # Movement etc...
    def controller(self, task):
        dt = globalClock.getDt()
        # Navigation
        if self.game.keymap.map["forward"]:
            # self.setY(self.getY() + (1 * self.speed))
            self.setPos(self, (0, ((1 * self.speed) * dt), 0))

        if self.game.keymap.map["left"]:
            self.setH(self.getH() + ((1 * self.speed) * dt))
            # For move_left
            # self.setPos(self, (((1 * self.speed) * dt), 0, 0))

        if self.game.keymap.map["backward"]:
            # self.setY(self.getY() - (1 * self.speed))
            self.setPos(self, (0, -((1 * self.turn_speed) * dt), 0))

        if self.game.keymap.map["right"]:
            self.setH(self.getH() + -((1 * self.turn_speed) * dt))
            # For move_right
            # self.setPos(self, (-((1 * self.speed) * dt), 0, 0))

        # Jump
        if self.game.keymap.map["jump"]:
            self.jump()

        # Sprint
        if self.game.keymap.map["sprint"]:
            # self.toggle_sprint()
            self.speed = self.speed_modes["sprint"]
        else:
            self.speed = self.speed_default

        return task.cont
