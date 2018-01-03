#!/usr/bin/python3
""" debug_hud.py | Tue, Jan 02, 2018 | Roman S. Collins

    Onscreen debugging HUD.

"""
# import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import DirectOptionMenu
from direct.gui.DirectGui import DirectScrolledList
# from panda3d.core import *
from panda3d.core import TextNode


class Debug_HUD:
    def __init__(self, game):
        self.game = game
        self.player_position = (0, 0, 0)
        self.player_hpr = (0, 0, 0)
        self.camera_position = (0, 0, 0)
        self.camera_hpr = (0, 0, 0)

        # TODO
        # Remove this and create a tracking function in __main__
        # self.game.camera_position = (0, 0, 0)
        # self.game.camera_hpr = (0, 0, 0)

        self.font = self.game.loader.loadFont("assets/fonts/teks-regular.otf")

        # TODO
        # self.font_bold
        # self.font_italic
        # self.font_bold_italic

    def init_HUD(self):
        # self.display_text =  "player_position = (x = {}, y = {}, z = {})" +
        #                      "player_position = (x = {}, y = {}, z = {})" +
        #                      "player_position = (x = {}, y = {}, z = {})" +
        #                      "player_position = (x = {}, y = {}, z = {})")\
        #                      .format(
        #                      self.player_position[0],
        #                      self.player_position[1],
        #                      self.player_position[2],
        #                      self.player_hpr[0],
        #                      self.player_hpr[1],
        #                      self.player_hpr[2],
        #                      self.camera_position[0],
        #                      self.camera_position[1],
        #                      self.camera_position[2],
        #                      self.camera_hpr[0],
        #                      self.camera_hpr[1],
        #                      self.camera_hpr[2])

        self.display_text = "test"

        # self.debug_hud_text_object = OnscreenText(
        #     text=self.debug_hud_display_text,
        #     pos=(0.85, 0.85),
        #     scale=0.07,
        #     fg=(1.0, 1.0, 1.0, 1.0),
        #     align=TextNode.ACenter,
        #     mayChange=1
        # )

        self.display_text_obj = OnscreenText(text=self.display_text,
                                             pos=(0, 0, 0),
                                             # font=self.font,
                                             textMayChange=1)

    def update(self, task):
        # self.player_position = (0, 0, 0)
        # self.player_hpr = (0, 0, 0)
        # self.camera_position = (0, 0, 0)
        # self.camera_hpr = (0, 0, 0)

        if self.game.player:
            self.display_text_obj.setText("test")
            # self.display_text_obj.setText(
            #     "player_position = (x = {}, y = {}, z = {})" +
            #     "player_position = (x = {}, y = {}, z = {})" +
            #     "player_position = (x = {}, y = {}, z = {})" +
            #     "player_position = (x = {}, y = {}, z = {})").format(
            #     self.game.player_position[0],
            #     self.game.player_position[1],
            #     self.game.player_position[2],
            #     self.game.player_hpr[0],
            #     self.game.player_hpr[1],
            #     self.game.player_hpr[2],
            #     self.game.camera_position[0],
            #     self.game.camera_position[1],
            #     self.game.camera_position[2],
            #     self.game.camera_hpr[0],
            #     self.game.camera_hpr[1],
            #     self.game.camera_hpr[2]
            # )

        self.display_text_obj.setText("test2")

        return task.cont
