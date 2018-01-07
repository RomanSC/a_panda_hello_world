#!/usr/bin/Python3
""" camera.py | Wed, Jan 03, 2018 | Roman S. Collins
"""


class CameraController:
    # def __init__(self, game):
    #     self.game = game

    #     self.game.camera.setPos(self.game.player.getX() + 10,
    #                             self.game.player.getY() + 10,
    #                             2)

    #     self.game.camLens.setFov(120)

    # def update(self, task):
    #     self.game.camera.lookAt(self.game.player)

    #     self.game.camera.setPos(self.game.player.getX() + 10,
    #                             self.game.player.getY() + 10,
    #                             2)

    #     return task.cont

    def __init__(self, game):
        self.game = game

        self.game.disableMouse()

        self.start_pos = (0, -60, 50)
        self.start_hpr = (0, -30, 0)

        self.node = self.game.render.attachNewNode("camera node")

        self.node.setPos(*self.start_pos)
        self.node.setHpr(*self.start_hpr)

        self.game.camera.reparentTo(self.node)
        self.node.reparentTo(self.game.player.node)

        # TODO:
        # Find out why self.game.camera has no camLens
        # self.game.camera.camLens.setFov(120)

    def update(self, task):
        # Zoom
        # camera = self.game.camera
        # if self.game.keymap["zoom-in"]:
        #     camera.setPos(camera.getPos, (0, 1, 0))
        # if self.game.keymap["zoom-out"]:
        #     camera.setPos(camera.getPos, (0, -1, 0))

        # self.game.keymap["zoom-in"] = False
        # self.game.keymap["zoom-out"] = False

        return task.cont

