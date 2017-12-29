#!/usr/bin/python3
""" a_panda_hello_world.py | Roman S. Collins | Mon, Dec 18, 2017

    Following along to "A Panda3D Hello World Tutorial" from the Panda3D
    website.

    https://www.panda3d.org/manual/index.php/A_Panda3D_Hello_World_Tutorial

"""
# from math import *
from math import sin
from math import cos
from math import pi

# import panda3d
# from panda3d.core import *

from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject
from direct.task import Task

from panda3d.core import Material

# Lighting
# https://www.panda3d.org/manual/index.php/Lighting
from panda3d.core import DirectionalLight
from panda3d.core import PointLight
from panda3d.core import AmbientLight
from panda3d.core import Spotlight

class Player(DirectObject.DirectObject):
    def __init__(self,
                 game,
                 name="bob",
                 level=1,
                 hp=100,
                 scale={"a": 0, "b": 0, "c": 0},
                 position={"a": 0, "b": 0, "c": 0}):
        # super().__init__(self)
        self.game = game
        self.model = "assets/models/figures/gray_boy.egg"

        # Abstract
        self.name = name
        self.level = level
        self.hp = hp
        self.scale = scale
        self.position = position

        self.object = self.game.loader.loadModel(self.model)

        self.object.setScale(self.scale["a"],
                             self.scale["b"],
                             self.scale["c"])

        self.object.setPos(self.position["a"],
                           self.position["b"],
                           self.position["c"])

        self.material = Material()
        self.material.setShininess(0.0)
        self.material.setDiffuse((1.0, 1.0, 1.0, 1.0))
        self.object.setMaterial(self.material)

        # Always last
        self.object.reparentTo(self.game.render)


    # def load_Player(self):
    #     print("DEBUG: Loading player ...")
    #     self.player_object = self.loader.loadModel(
    #                          "assets/models/figures/gray_boy.egg")
    #     self.player_object.setScale(1, 1, 1)

    #     self.pos = {"a": 0, "b": 0, "c": 0}
    #     self.player_object.setPos(self.pos["a"],
    #                               self.pos["b"],
    #                               self.pos["c"])

    #     self.player_material = Material()
    #     self.player_material.setShininess(0.0)

    #     self.player_material.setDiffuse((1.0, 1.0, 1.0, 1.0))

    #     self.player_object.setMaterial(self.player_material)

    #     # Always last
    #     self.player_object.reparentTo(self.render)


class Win(ShowBase):
    def __init__(self):
        super().__init__(self)
        # ShowBase.__init__(self)

        self.start()

    def start(self):

        # Disable camera mouse control
        # https://www.panda3d.org/manual/index.php/The_Default_Camera_Driver
        self.disableMouse()

        # Keyboard and Mouse camera control
        # self.useDrive()

        # Trackball camera control
        self.useTrackball()

        # TODO
        # Out of Body Experience camera control
        # self.oobe()

        self.load_Sun()
        self.load_Environment()
        self.adjust_Camera()
        self.player = Player(self)

        self.update()

    def update(self):
        pass
        # self.taskMgr.add(self.move_Player(1, 0, 0), "self.move_Player")

    def adjust_Camera(self):
        print("DEBUG: Adjusting view port ...")
        self.camera.setPos(10, 10, 10)
        self.camera.setHpr(55, 0, 135)

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
