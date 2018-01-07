#!/usr/bin/python3
""" a_panda_hello_world.py | Roman S. Collins | Mon, Dec 18, 2017

    Following along to "A Panda3D Hello World Tutorial" from the Panda3D
    website.

    https://www.panda3d.org/manual/index.php/A_Panda3D_Hello_World_Tutorial

"""
from direct.showbase.ShowBase import ShowBase

from panda3d.core import Material

from panda3d.core import DirectionalLight

from pandac.PandaModules import WindowProperties

from player import Player
from camera_controller import CameraController
from keymap import Keymap
from update import Update
from lighting import Lighting

import sys


class Alpha(ShowBase):
    def __init__(self):
        super().__init__(self)
        # ShowBase.__init__(self)

        self.messenger.toggleVerbose()

        self.init_render_pipeline()
        self.start()

    def init_render_pipeline(self):
        sys.path.insert(0, "./lib/RenderPipeline")
        # sys.path.insert(0, "../../RenderPipeline")

        from lib.RenderPipeline.rpcore import RenderPipeline

        self.render_pipeline = RenderPipeline()
        self.render_pipeline.pre_showbase_init()
        self.render_pipeline.create(self)

    def start(self):
        self.start_done = False

        # Disable camera mouse control
        # https://www.panda3d.org/manual/index.php/The_Default_camera_Driver
        # self.disableMouse()

        # Keyboard and Mouse camera control
        # self.useDrive()

        # Trackball camera control
        # self.useTrackball()

        # TODO
        # Out of Body Experience camera control
        # self.oobe()

        self.init_sun()
        self.init_environment()
        self.window_properties()

        self.player = Player(self)
        self.camera_controller = CameraController(self)
        # self.test_cam = TestNotCam(self)
        self.keymap = Keymap(self)
        self.update = Update(self)
        self.start_done = True

    def window_properties(self):
        self.window_props = WindowProperties()
        self.window_props.setCursorHidden(False)

        self.window_props.setSize(1920, 1200)
        self.window_props.setFullscreen(False)

        self.win.requestProperties(self.window_props)

    def init_sun(self):
        # print("DEBUG: Loading Sun ... ")
        # self.directional_light = AmbientLight("Sun")
        # self.directional_light.setColor((0.2, 0.2, 0.9, 1.0))

        # self.directional_light.setPos(0, 0, 10)
        # self.directional_light.setHpr(0, 0, 0)

        # Last
        # self.sun = self.render.attachNewNode(self.directional_light)

        # Directional light
        self.sun = DirectionalLight("self.sun")
        self.sun.setColor((1.0, 1.0, 1, 1.0))
        slnp = self.render.attachNewNode(self.sun)
        slnp.setHpr(0, 0, 0)
        self.render.setLight(slnp)
        # print("DEBUG: DONE!")

        # Ambient light
        # self.sun = AmbientLight("self.sun")
        # self.sun.setColor((0, 0, 1.0, 1.0))
        # sun_node = self.render.attachNewNode(self.sun)
        # self.render.setLight(sun_node)

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
    scenes = [Alpha]
    scene = scenes[0]()
    # https://www.panda3d.org/manual/index.php/Starting_Panda3D

    # The run() procedure in ShowBase contains the Panda3D main loop. It
    # renders a frame, handles the background tasks, and then repeats. It does
    # not normally return, so it needs to be called only once and must be the
    # last line in your script.
    scene.run()


if __name__ == "__main__":
    main()
