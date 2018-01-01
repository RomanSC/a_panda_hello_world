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
from direct.showbase.InputStateGlobal import inputState
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
        self.set_camera_OnscreenText()
        self.mouse_and_cursor()
        self.load_Player()
        self.initialize_Camera()
        self.load_Keys()

        self.init_Updates()

        self.start_done = True

    def init_Updates(self):
        # TODO
        # Add some task manager
        self.taskMgr.add(self.camera_text_Task,
                         "camera_text_Task")


        self.taskMgr.add(self.track_player_PositionRotation,
                         "track_player_PositionRotation")

        # self.taskMgr.add(self.test_rotate_Player,
        #                  "test_rotate_Player")

    def set_camera_OnscreenText(self):
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

    # TODO:
    # make camera a child of the player actor

    def initialize_Camera(self):
        # TODO:
        # https://www.panda3d.org/forums/viewtopic.php?t=1319

        # Player/Camera Node Setup

        # <self.render>
        # |-<player>
        #   |-<player_dummy_node>
        #     |-<camera_dummy_node>
        #       |-camera

        self.camera_Node = self.render.attachNewNode("camera_Node")

        self.camera_Node.setPos(0, 0, 0)
        self.camera_Node.setHpr(0, 0, 0)

        self.camera.reparentTo(self.camera_Node)
        self.camera_Node.reparentTo(self.player_Node)

        self.camera.setPos(0, -35, 18)  # X=left/right, Y=zoom, Z=Up/down.
        self.camera.setHpr(0, -25, 0)   # Heading, pitch, roll.

    # def initialize_Camera(self):
    #     self.camera.setPos(self.player_position[0],
    #                        self.player_position[1] - 16,
    #                        self.player_position[2] + 8)

    #     self.camera_zoom_level = 10
    #     self.camera_zoom_increment = 1
    #     self.camera_zoom_range = (-32, -42)  # in front and behind player, in
    #                                          # that order

    # def camera_Controller(self, a):
    #     # Zoom on scroll
    #     self.camera_zoom_level += a

    #     x = self.player_position[0]
    #     y = self.player_position[1] + self.camera_zoom_level
    #     z = self.player_position[2] + 8

    #     if y > self.camera_zoom_range[0]:
    #         # print("DEBUG: {} > self.camera_zoom_range[0]".format(y))
    #         y = self.camera_zoom_range[0]
    #         self.camera_zoom_level = self.camera_zoom_range[0]

    #     elif y < self.camera_zoom_range[1]:
    #         # print("DEBUG: {} < self.camera_zoom_range[0]".format(y))
    #         y = self.camera_zoom_range[1]
    #         self.camera_zoom_level = self.camera_zoom_range[1]

    #     self.camera.setPos(x, y, z)

    #     # print("DEBUG:\nself.player_position = {}\nself.camera_zoom_level = {}"
    #     #       .format(self.player_position,
    #     #               self.camera_zoom_level))

    #     # Rotation
    #     # self.camera.setHpr(self.player_hpr[0],
    #     #                    self.player_hpr[1] - 25,
    #     #                    self.player_hpr[2])

    # # def camera_controller_Task(self, task):
    # #     # def zoom(a):
    # #     #     self.camera.setPos((self.player_position[0]),
    # #     #                        (self.player_position[0] + a),
    # #     #                        (self.player_position[0]))

    # #     self.accept("wheel_up", self.zoom(-1))
    # #     self.accept("wheel_down", self.zoom(1))

    # #     return task.cont

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

    # def test_rotate_Player(self, task):
    #     self.player.setHpr(self.player_hpr[0] + 1, # Z, up/down axis
    #                        self.player_hpr[1],
    #                        self.player_hpr[2])

    #     return task.cont

    def track_player_PositionRotation(self, task):
        # Player position set once a frame
        # rather than many times within
        # multiple function calls
        self.player_position = self.player.getPos()
        self.player_hpr = self.player.getHpr()


        return task.cont

    def move_player_Forward(self):
        self.player.setPos(self.player_position[0],
                           self.player_position[1] + 1,
                           self.player_position[2])

    def move_player_Backward(self):
        self.player.setPos(self.player_position[0],
                           self.player_position[1] - 1,
                           self.player_position[2])

    def rotate_player_Left(self):
        # X=left/right, Y=zoom, Z=Up/down.
        # Heading, pitch, roll.

        self.player.setHpr(self.player.getHpr()[0] + 1,
                           self.player.getHpr()[1],
                           self.player.getHpr()[2])

    def rotate_player_Right(self):
        self.player.setHpr(self.player.getHpr()[0] - 1,
                           self.player.getHpr()[1],
                           self.player.getHpr()[2])


    def load_Player(self):
        self.player_scale = (0, 0, 0)
        self.player_position = (0, 0, 0)

        self.player = Actor("assets/models/figures/gray_boy.egg",
                            {"run": "assets/models/figures/gray_boy.egg",
                             "walk": "assets/models/figures/gray_boy.egg"})

        self.player.reparentTo(self.render)

        self.player.setScale(0.2)

        self.player.setPos(self.player_position[0],
                           self.player_position[1],
                           self.player_position[2])

        self.player.setHpr(0, 0, 0)

        # Create Player Node

        # Node for player turn
        self.turn_Node = self.render.attachNewNode("turn_Node")

        # Node for the player
        self.player_Node = self.render.attachNewNode("player_Node")
        self.player_Node.reparentTo(self.player)

        # camera_Node becomes a child of player_Node in
        # self.initialize_Camera

    def load_Keys(self):
        self.accept("w", self.move_player_Forward)
        self.accept("a", self.rotate_player_Left)
        self.accept("s", self.move_player_Backward)
        self.accept("d", self.rotate_player_Right)

        # inputState.watchWithModifiers('forward', 'w')
        # inputState.watchWithModifiers('left', 'a')
        # inputState.watchWithModifiers('backward', 's')
        # inputState.watchWithModifiers('right', 'd')


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
