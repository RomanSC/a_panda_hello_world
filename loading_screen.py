#!/usr/bin/python
""" loading_screen.py | Sun, Jan 07, 2018 | Roman S. Collins

    https://github.com/tobspr/RenderPipeline/wiki/Customizing-the-Pipeline

"""
import time


class LoadingScreen:
    def __init__(self, game):
        self.game = game

        self.fullscreen_bg = "assets/images/blankloadscreen.png"
        # self.create()

    def create(self):
        self.game.render_pipeline.set_loading_screen_image("assets/images/blankloadscreen.png")

        self.game.graphicsEngine.render_frame()
        self.game.graphicsEngine.render_frame()

    def remove(self):
        pass
