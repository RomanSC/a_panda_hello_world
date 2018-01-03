#!/usr/bin/Python3
""" camera.py | Wed, Jan 03, 2018 | Roman S. Collins
"""


class Camera:
    def __init__(self, game):
        self.game = game
        # TODO:
        # https://www.panda3d.org/forums/viewtopic.php?t=1319

        # Player/Camera Node Setup
        # <self.game.render>
        # |-<player>
        #   |-<player_dummy_node>
        #     |-<camera_dummy_node>
        #       |-camera

        self.start_pos = (0, -60, 50)
        self.start_hpr = (0, -30, 0)

        self.node = self.game.render.attachNewNode("camera node")

        self.node.setPos(*self.start_pos)
        self.node.setHpr(*self.start_hpr)

        self.game.camera.reparentTo(self.node)
        self.node.reparentTo(self.game.player.node)

    def controller(self, task):
        # Zoom
        # camera = self.game.camera
        # if self.game.keymap["zoom-in"]:
        #     camera.setPos(camera.getPos, (0, 1, 0))
        # if self.game.keymap["zoom-out"]:
        #     camera.setPos(camera.getPos, (0, -1, 0))

        # self.game.keymap["zoom-in"] = False
        # self.game.keymap["zoom-out"] = False

        return task.cont
