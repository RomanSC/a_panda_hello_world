#!/usr/bin/python3
""" keymap.py | Wed, Jan 03, 2018 | Roman S. Collins

    This holds the key press settings for the game.

"""
import sys

class Keymap:
    def __init__(self, game):
        self.game = game
        # TODO:
        # Fix bug where "escape": sys.exit(1) in self.keymap
        # gets executed (for no apparent reason...) when
        # the keymap is loaded in a loop during init process
        # ...
        # lol

        self.game.accept("escape", sys.exit, extraArgs=[1])
        self.map = {  # "escape":
                      # [sys.exit, 1],
                    "w":
                    [self.game.player.move_forward, [True]],

                    "w-up":
                    [self.game.player.move_forward, [False]],

                    "a":
                    [self.game.player.rotate_left, [True]],

                    "a-up":
                    [self.game.player.rotate_left, [False]],

                    "s":
                    [self.game.player.move_backward, [True]],

                    "s-up":
                    [self.game.player.move_backward, [False]],

                    "d":
                    [self.game.player.rotate_right, [True]],

                    "d-up":
                    [self.game.player.rotate_right, [False]],

                    "arrow_up":
                    [self.game.player.move_forward, [True]],

                    "arrow_up-up":
                    [self.game.player.move_forward, [False]],

                    "arrow_left":
                    [self.game.player.rotate_left, [True]],

                    "arrow_left-up":
                    [self.game.player.rotate_left, [False]],

                    "arrow_down":
                    [self.game.player.move_backward, [True]],

                    "arrow_down-up":
                    [self.game.player.move_backward, [False]],

                    "arrow_right":

                    [self.game.player.rotate_right, [True]],
                    "arrow_right-up":

                    [self.game.player.rotate_right, [False]]}

        for key, val in self.map.items():
            # self.accept(<keystr>, <function>, <args>)
            print(key,
                  self.map[key][0],
                  self.map[key][1])

            self.game.accept(key,
                             self.map[key][0],
                             extraArgs=list(self.map[key][1]))
