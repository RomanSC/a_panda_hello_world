#!/usr/bin/python3
""" a_panda_hello_world.py | Roman S. Collins | Mon, Dec 18, 2017

    Following along to "A Panda3D Hello World Tutorial" from the Panda3D
    website.

    https://www.panda3d.org/manual/index.php/A_Panda3D_Hello_World_Tutorial

"""
# import time
# import datetime
# import random
import sys

# from math import *
# import math
# import numpy

# import panda3d
# from panda3d.core import *

from direct.showbase.ShowBase import ShowBase
# from direct.showbase import DirectObject
# from direct.showbase.InputStateGlobal import inputState
# from direct.task import Task
from direct.actor.Actor import Actor
# from direct.gui.OnscreenText import OnscreenText

from panda3d.core import Material

# Lighting
# https://www.panda3d.org/manual/index.php/Lighting
from panda3d.core import DirectionalLight
# from panda3d.core import PointLight
# from panda3d.core import AmbientLight
# from panda3d.core import Spotlight
# from panda3d.core import PandaNode
# from panda3d.core import NodePath
# from panda3d.core import Camera
from panda3d.core import Vec2
from panda3d.core import Vec3
from panda3d.core import Vec4
from panda3d.core import Point2
from panda3d.core import Point3
from panda3d.core import Point4

from pandac.PandaModules import WindowProperties
# from pandac.PandaModules import CompassEffect
# https://www.panda3d.org/manual/index.php/Compass_Effects

from player import Player
from camera import Camera
from keymap import Keymap
from update import Update


class Alpha(ShowBase):
    def __init__(self):
        super().__init__(self)
        # ShowBase.__init__(self)

        self.messenger.toggleVerbose()

        self.start()

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
        self.mouse_and_cursor()

        self.player = Player(self)
        self.camera = Camera(self)
        self.keymap = Keymap(self)
        self.update = Update(self)
        self.start_done = True

    def window_properties(self):
        self.window_props = WindowProperties()
        self.window_props.setCursorHidden(False)

        self.window_props.setSize(1920, 1200)
        self.window_props.setFullscreen(False)

        self.win.requestProperties(self.window_props)

    def mouse_and_cursor(self):
        # Disable mouse camera control
        self.disableMouse()

        # self.props = WindowProperties()
        # self.props.setCursorHidden(False)

        # self.props = WindowProperties()
        # self.win.requestProperties(self.props)

    # TODO:
    # Create GUI for editing camera position and snapping to follow the player
    # def camera_text_task(self, task):
    #     self.camera_info_text.destroy()
    #     self.camera_info_text = OnscreenText(text="pos:{} hpr:{}".format(
    #                             self.camera.getPos(),
    #                             self.camera.getHpr()),
    #                             pos=self.camera_text_pos)

    #     return task.cont

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
        self.sun.setColor((1.0, 1.0, 0.8, 1.0))
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
