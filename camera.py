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

        self.start_pos = (0, -35, 18)
        self.start_hpr = (0, -25, 0)

        self.node = self.game.render.attachNewNode("camera node")

        self.node.setPos(*self.start_pos)
        self.node.setHpr(*self.start_hpr)

        self.game.camera.reparentTo(self.node)
        self.node.reparentTo(self.game.player.node)
