#!/usr/bin/python3
""" a_panda_hello_world.py | Roman S. Collins | Mon, Dec 18, 2017

    Following along to "A Panda3D Hello World Tutorial" from the Panda3D
    website.

    https://www.panda3d.org/manual/index.php/A_Panda3D_Hello_World_Tutorial

"""
import os
import sys

from direct.showbase.ShowBase import ShowBase

# CD to current dir
# os.chdir(os.path.realpath(os.path.dirname(__file__)))

from panda3d.core import loadPrcFileData
from panda3d.core import loadPrcFileData
loadPrcFileData("", "sync-video false")
loadPrcFileData("", "sync-video #t")
loadPrcFileData("", "depth-bits 24")

from panda3d.core import Material
from panda3d.core import DirectionalLight

from panda3d.core import WindowProperties

from loading_screen import LoadingScreen
from player import Player
from weapons import Sword
from camera_controller import CameraController
from keymap import Keymap
from update import Update
from lighting import Lighting
from collision_controller import CollisionController


class Game(ShowBase):
    def __init__(self):
        super().__init__(self)

        self.messenger.toggleVerbose()

        self.init_render_pipeline()
        self.start()

    def init_render_pipeline(self):
        sys.path.insert(0, "./lib/RenderPipeline")

        from lib.RenderPipeline.rpcore import RenderPipeline

        self.render_pipeline = RenderPipeline()
        self.render_pipeline.pre_showbase_init()
        self.render_pipeline.create(self)

    def start(self):
        self.start_done = False

        self.loading_screen = LoadingScreen(self)
        self.init_environment()
        self.window_properties()

        self.lighting = Lighting(self)
        self.player = Player(self)
        # self.sword = Sword(self)
        self.camera_controller = CameraController(self)
        self.keymap = Keymap(self)
        self.update = Update(self)
        self.collision_controller = CollisionController

        self.start_done = True

    def window_properties(self):
        self.window_props = WindowProperties()
        self.window_props.setCursorHidden(False)

        self.window_props.setSize(1920, 1200)
        self.window_props.setFullscreen(False)

        self.win.requestProperties(self.window_props)

    def init_environment(self):
        # print("DEBUG: Loading evironment models ...")

        self.ground_object = self.loader.loadModel(
                           "assets/models/environment/plane.egg")

        self.ground_object.setScale(1, 1, 1)
        self.ground_object.setPos(0, 0, 0)
        # self.ground.setHpr(0, 0, 0)

        self.ground_material = Material()
        self.ground_material.setShininess(0.0)
        # self.ground_material.setAmbient((0.0, 0.0, 1.0, 1.0))
        # print("DEBUG: in init_environment: if ground_material.hasAmbient() {}".format(self.ground_material.hasAmbient()))
        # print("DEBUG: in init_environment: if ground_material.hasEmission() {}".format(self.ground_material.hasEmission()))

        self.ground_material.setDiffuse((0.2, 0.7, 0.2, 1.0))

        self.ground_object.setMaterial(self.ground_material)

        # Always last
        self.ground_object.reparentTo(self.render)
        # print("DEBUG: DONE!")


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
