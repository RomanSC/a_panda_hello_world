#!/usr/bin/python3
""" keymap.py | Wed, Jan 03, 2018 | Roman S. Collins

    This holds the key press settings for the game.

"""
import sys
from panda3d.core import ModifierButtons


class Keymap:
    def __init__(self, game):
        self.game = game

        self.game.mouseWatcherNode.set_modifier_buttons(ModifierButtons())
        self.game.buttonThrowers[0].node().set_modifier_buttons(ModifierButtons())

        self.map = {"forward": False, "left": False, "backward": False,
                    "right": False, "sprint": False, "jump": False,
                    "zoom-in": False, "zoom-out": False}

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
        self.game.accept("space", self.setKey, ["jump", True])
        self.game.accept("space-up", self.setKey, ["jump", False])

        # Zoom
        self.game.accept("wheel_up-up", self.setKey, ["zoom-in", True])
        self.game.accept("wheel_down-up", self.setKey, ["zoom-out", True])
        # self.game.accept("wheel_up-up", self.setKey, ["zoom-in", False])
        # self.game.accept("wheel_down-up", self.setKey, ["zoom-out", False])

    def setKey(self, key, val):
        self.map[key] = val
