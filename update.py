#!/usr/bin/python3

""" update.py | Wed, Jan 03, 2018 | Roman S. Collins

    This class manages all of the update actions for game
    initializing all class update methods within the game.

"""
# from direct.task import taskMgr
# from direct.task import Task


class Update:
    def __init__(self, game):
        self.game = game

        # Order matters
        self.game.taskMgr.add(self.game.camera_controller.mouse_pointer.get_point,
                              "get 3d mouse position")

        self.game.taskMgr.add(self.game.player.controller,
                              "player controller")

        self.game.taskMgr.add(self.game.player.is_moving,
                              "is player moving")

        self.game.taskMgr.add(self.game.player.animate,
                              "player animations")

        self.game.taskMgr.add(self.game.player.update,
                              "player update")

        self.game.taskMgr.doMethodLater(0.1, self.game.collision_controller.update,
                                        "collision controller")

        self.game.taskMgr.doMethodLater(0.3, self.game.gravity.update,
                                        "player gravity")

        self.game.taskMgr.doMethodLater(0.5, self.game.camera_controller.update,
                                        "camera controller")
