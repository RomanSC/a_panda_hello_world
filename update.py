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

        self.game.taskMgr.add(self.game.player.controller,
                              "player controller")
