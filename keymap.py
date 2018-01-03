#!/usr/bin/python3
""" keymap.py | Wed, Jan 03, 2018 | Roman S. Collins

    This holds the key press settings for the game.

"""
import sys


class Keymap:
    def __init__(self, game):
        self.game = game
        # TODO:
        # Fix bug where "escape": sys.exit(1) in self.map
        # gets executed (for no apparent reason...) when
        # the keymap is loaded in a loop during init process
        # ...
        # lol
        self.map = {"forward": None, "left": None, "backward": None,
                    "right": None, "sprint": None, "jump": None}

        self.game.accept("escape", sys.exit, extraArgs=[1])

        # Keys down
        self.game.accept("w", self.setKey, ["forward", True])
        self.game.accept("a", self.setKey, ["left", True])
        self.game.accept("s", self.setKey, ["backward", True])
        self.game.accept("d", self.setKey, ["right", True])
        self.game.accept("arrow_up", self.setKey, ["forward", True])
        self.game.accept("arrow_left", self.setKey, ["left", True])
        self.game.accept("arrow_down", self.setKey, ["backward", True])
        self.game.accept("arrow_right", self.setKey, ["right", True])
        self.game.accept("w", self.setKey, ["forward", True])
        self.game.accept("a", self.setKey, ["left", True])
        self.game.accept("s", self.setKey, ["backward", True])
        self.game.accept("d", self.setKey, ["right", True])
        self.game.accept("arrow_up", self.setKey, ["forward", True])
        self.game.accept("arrow_left", self.setKey, ["left", True])
        self.game.accept("arrow_down", self.setKey, ["backward", True])
        self.game.accept("arrow_right", self.setKey, ["right", True])
        self.game.accept("shift", self.setKey, ["sprint", True])

        # Shift + Keys down
        # self.game.accept("shift-w", self.setKey, ["forward", True])
        # self.game.accept("shift-w", self.setKey, ["sprint", True])
        # self.game.accept("shift-a", self.setKey, ["left", True])
        # self.game.accept("shift-a", self.setKey, ["sprint", True])
        # self.game.accept("shift-s", self.setKey, ["backward", True])
        # self.game.accept("shift-s", self.setKey, ["sprint", True])
        # self.game.accept("shift-d", self.setKey, ["right", True])
        # self.game.accept("shift-d", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_up", self.setKey, ["forward", True])
        # self.game.accept("shift-arrow_up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_left", self.setKey, ["left", True])
        # self.game.accept("shift-arrow_left", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_down", self.setKey, ["backward", True])
        # self.game.accept("shift-arrow_down", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_right", self.setKey, ["right", True])
        # self.game.accept("shift-arrow_right", self.setKey, ["sprint", True])
        # self.game.accept("shift-w", self.setKey, ["forward", True])
        # self.game.accept("shift-w", self.setKey, ["sprint", True])
        # self.game.accept("shift-a", self.setKey, ["left", True])
        # self.game.accept("shift-a", self.setKey, ["sprint", True])
        # self.game.accept("shift-s", self.setKey, ["backward", True])
        # self.game.accept("shift-s", self.setKey, ["sprint", True])
        # self.game.accept("shift-d", self.setKey, ["right", True])
        # self.game.accept("shift-d", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_up", self.setKey, ["forward", True])
        # self.game.accept("shift-arrow_up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_left", self.setKey, ["left", True])
        # self.game.accept("shift-arrow_left", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_down", self.setKey, ["backward", True])
        # self.game.accept("shift-arrow_down", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_right", self.setKey, ["right", True])
        # self.game.accept("shift-arrow_right", self.setKey, ["sprint", True])

        # Keys up
        self.game.accept("w-up", self.setKey, ["forward", False])
        self.game.accept("a-up", self.setKey, ["left", False])
        self.game.accept("s-up", self.setKey, ["backward", False])
        self.game.accept("d-up", self.setKey, ["right", False])
        self.game.accept("arrow_up-up", self.setKey, ["forward", False])
        self.game.accept("arrow_left-up", self.setKey, ["left", False])
        self.game.accept("arrow_down-up", self.setKey, ["backward", False])
        self.game.accept("arrow_right-up", self.setKey, ["right", False])
        self.game.accept("w-up", self.setKey, ["forward", False])
        self.game.accept("a-up", self.setKey, ["left", False])
        self.game.accept("s-up", self.setKey, ["backward", False])
        self.game.accept("d-up", self.setKey, ["right", False])
        self.game.accept("arrow_up-up", self.setKey, ["forward", False])
        self.game.accept("arrow_left-up", self.setKey, ["left", False])
        self.game.accept("arrow_down-up", self.setKey, ["backward", False])
        self.game.accept("arrow_right-up", self.setKey, ["right", False])
        self.game.accept("shift-up", self.setKey, ["sprint", False])
        self.game.accept("space-up", self.setKey, ["jump", True])

        # Shift + Keys up
        # self.game.accept("shift-w-up", self.setKey, ["forward", True])
        # self.game.accept("shift-w-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-a-up", self.setKey, ["left", True])
        # self.game.accept("shift-a-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-s-up", self.setKey, ["backward", True])
        # self.game.accept("shift-s-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-d-up", self.setKey, ["right", True])
        # self.game.accept("shift-d-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_up-up", self.setKey, ["forward", True])
        # self.game.accept("shift-arrow_up-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_left-up", self.setKey, ["left", True])
        # self.game.accept("shift-arrow_left-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_down-up", self.setKey, ["backward", True])
        # self.game.accept("shift-arrow_down-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_right-up", self.setKey, ["right", True])
        # self.game.accept("shift-arrow_right-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-w-up", self.setKey, ["forward", True])
        # self.game.accept("shift-w-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-a-up", self.setKey, ["left", True])
        # self.game.accept("shift-a-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-s-up", self.setKey, ["backward", True])
        # self.game.accept("shift-s-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-d-up", self.setKey, ["right", True])
        # self.game.accept("shift-d-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_up-up", self.setKey, ["forward", True])
        # self.game.accept("shift-arrow_up-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_left-up", self.setKey, ["left", True])
        # self.game.accept("shift-arrow_left-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_down-up", self.setKey, ["backward", True])
        # self.game.accept("shift-arrow_down-up", self.setKey, ["sprint", True])
        # self.game.accept("shift-arrow_right-up", self.setKey, ["right", True])
        # self.game.accept("shift-arrow_right-up", self.setKey, ["sprint", True])

    def setKey(self, key, val):
        self.map[key] = val
