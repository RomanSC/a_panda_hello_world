#!/usr/bin/python3
""" a_panda_hello_world.py | Roman S. Collins | Mon, Dec 18, 2017

    Following along to "A Panda3D Hello World Tutorial" from the Panda3D
    website.

    https://www.panda3d.org/manual/index.php/A_Panda3D_Hello_World_Tutorial

"""
import time
import datetime
import random
import sys

# from math import *
from math import sin
from math import cos
from math import pi

# import panda3d
# from panda3d.core import *

from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText

from panda3d.core import Material

# Lighting
# https://www.panda3d.org/manual/index.php/Lighting
from panda3d.core import DirectionalLight
from panda3d.core import PointLight
from panda3d.core import AmbientLight
from panda3d.core import Spotlight
from panda3d.core import PandaNode
from panda3d.core import NodePath
from panda3d.core import Camera

from pandac.PandaModules import WindowProperties

class Win(ShowBase):
    def __init__(self):
        super().__init__(self)
        # ShowBase.__init__(self)

        self.start_done = False

        # Disable camera mouse control
        # https://www.panda3d.org/manual/index.php/The_Default_Camera_Driver
        # self.disableMouse()


        self.props = WindowProperties()

        # Keyboard and Mouse camera control
        # self.useDrive()

        # Trackball camera control
        # self.useTrackball()

        # TODO
        # Out of Body Experience camera control
        # self.oobe()

        self.load_Sun()
        self.load_Environment()
        self.set_camera_Task()
        self.mouse_and_cursor()
        self.load_Player()
        # self.load_Keys()

        self.init_Updates()

        self.start_done = True

    def init_Updates(self):
        pass
        # TODO
        # Add some task manager
        self.taskMgr.add(self.camera_text_Task, "camera_text_Task")
        self.taskMgr.add(self.camera_follow_Player, "camera_follow_Player")

    def camera_follow_Player(self, task):
        player_pos = self.player.getPos()
        print("DEBUG: Player position: {} {} {}".format(player_pos[0],
                                                        player_pos[1],
                                                        player_pos[2]))
        self.camera.setPos((player_pos[0] + 0),
                           (player_pos[1] + 0),
                           (player_pos[2] + 0.10))

        self.camera.setHpr(45, 0, 0)

        return task.cont

    def set_camera_Task(self):
        print("DEBUG: Adjusting view port ...")
        # self.camera.setPos(10, 10, 10)
        # self.camera.setHpr(55, 0, 135)

        self.camera_text_pos = (0, 0.90, 0)
        self.camera_info_text = OnscreenText(text="pos:{} hpr:{}".format(
                                self.camera.getPos(),
                                self.camera.getHpr()),
                                pos=self.camera_text_pos)
        print("DEBUG: DONE!")

    def mouse_and_cursor(self):
        # Disable mouse camera control
        self.disableMouse()

        self.props.setCursorHidden(False)

        self.props = WindowProperties()
        self.win.requestProperties(self.props)

    # TODO:
    # Create GUI for editing camera position and snapping to follow the player
    def camera_text_Task(self, task):
        self.camera_info_text.destroy()
        self.camera_info_text = OnscreenText(text="pos:{} hpr:{}".format(
                                self.camera.getPos(),
                                self.camera.getHpr()),
                                pos=self.camera_text_pos)

        return task.cont

    def load_Sun(self):
        print("DEBUG: Loading Sun ... ")
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
        print("DEBUG: DONE!")

        # Ambient light
        # self.sun = AmbientLight("self.sun")
        # self.sun.setColor((0, 0, 1.0, 1.0))
        # sun_node = self.render.attachNewNode(self.sun)
        # self.render.setLight(sun_node)

    def load_Environment(self):
        print("DEBUG: Loading evironment models ...")

        self.ground_object = self.loader.loadModel(
                           "assets/models/environment/plane.egg")

        self.ground_object.setScale(1, 1, 1)
        self.ground_object.setPos(0, 0, 0)
        # self.ground.setHpr(0, 0, 0)

        self.ground_material = Material()
        self.ground_material.setShininess(0.0)
        # self.ground_material.setAmbient((0.0, 0.0, 1.0, 1.0))
        # print("DEBUG: in load_Environment: if ground_material.hasAmbient() {}".format(self.ground_material.hasAmbient()))
        # print("DEBUG: in load_Environment: if ground_material.hasEmission() {}".format(self.ground_material.hasEmission()))

        self.ground_material.setDiffuse((0.2, 0.7, 0.2, 1.0))

        self.ground_object.setMaterial(self.ground_material)

        # Always last
        self.ground_object.reparentTo(self.render)
        print("DEBUG: DONE!")

    def load_Player(self,
                    player_scale={"a": 0, "b": 0, "c": 0},
                    player_position={"a": 0, "b": 0, "c": 0}):
        print("DEBUG: Loading player ... ")

        # self.player_scale = player_scale
        # self.player_position = player_position

        # self.player_model = "assets/models/figures/gray_boy.egg"

        # self.player = self.loader.loadModel(self.player_model)

        # self.player.setScale(self.player_scale["a"],
                    #                 self.player_scale["b"],
                    #                 self.player_scale["c"])

        # self.player.setPos(self.player_position["a"],
                    #               self.player_position["b"],
                    #               self.player_position["c"])

        # # self.player_material = Material()
        # # self.player_material.setShininess(0.0)
        # # self.player_material.setDiffuse((1.0, 1.0, 1.0, 1.0))

        # # self.player.setMaterial(self.player_material)

        # self.player.reparentTo(self.render)
        # print("DEBUG: DONE!")
        self.player_scale = player_scale
        self.player_position = player_position

        self.player = Actor("assets/models/figures/gray_boy.egg",
                            {"run": "assets/models/figures/gray_boy.egg",
                             "walk": "assets/models/figures/gray_boy.egg"})

        self.player.reparentTo(self.render)

        self.player.setScale(0.2)

        self.player.setPos(self.player_position["a"],
                           self.player_position["b"],
                           self.player_position["c"])

        # Floating empty object 2 units above the player for the camera to point at
        self.player_camera_rot = NodePath(PandaNode("player_camera_rot"))
        self.player_camera_rot.reparentTo(self.player)
        self.player_camera_rot.setZ(2.0)

    # def load_Keys(self):
    #     self.accept("escape", sys.exit)
    #     self.accept("arrow_left", self.setKey, ["left", True])
    #     self.accept("arrow_right", self.setKey, ["right", True])
    #     self.accept("arrow_up", self.setKey, ["forward", True])
    #     self.accept("a", self.setKey, ["cam-left", True])
    #     self.accept("s", self.setKey, ["cam-right", True])
    #     self.accept("arrow_left-up", self.setKey, ["left", False])
    #     self.accept("arrow_right-up", self.setKey, ["right", False])
    #     self.accept("arrow_up-up", self.setKey, ["forward", False])
    #     self.accept("a-up", self.setKey, ["cam-left", False])
    #     self.accept("s-up", self.setKey, ["cam-right", False])


    # def spin_Camera_Task(self, task):
    #     print("Spinning Camera ...")

    #     angleDegrees = task.time * 6.0
    #     angleRadians = angleDegrees * (pi / 180.0)

    #     self.camera.setPos(20 * sin(angleRadians),
    #                        -20.0 * cos(angleRadians),
    #                        3)

    #     self.camera.setHpr(angleDegrees, 0, 0)

    #     return Task.cont

def main():
    win = Win()
    # https://www.panda3d.org/manual/index.php/Starting_Panda3D

    # The run() procedure in ShowBase contains the Panda3D main loop. It
    # renders a frame, handles the background tasks, and then repeats. It does
    # not normally return, so it needs to be called only once and must be the
    # last line in your script.
    win.run()


if __name__ == "__main__":
    main()
