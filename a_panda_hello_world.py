#!/usr/bin/python3
""" a_panda_hello_world.py | Roman S. Collins | Mon, Dec 18, 2017

    Following along to "A Panda3D Hello World Tutorial" from the Panda3D
    website.

    https://www.panda3d.org/manual/index.php/A_Panda3D_Hello_World_Tutorial

"""
from math import sin
from math import cos
from math import pi

# import panda3d
from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject
from direct.task import Task

from panda3d.core import Material


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

        self.load_Environment()
        self.adjust_Camera()
        self.load_Player()

        self.update()

    def update(self):
        pass
        # self.taskMgr.add(self.spin_Camera_Task, "spin_Camera_Task")

    def adjust_Camera(self):
        print("Adjusting view port ...")
        self.camera.setPos(10, 10, 10)
        self.camera.setHpr(55, 0, 135)

    def load_Environment(self):
        print("Loading evironment models ...")

        self.ground_object = self.loader.loadModel(
                           "assets/models/environment/plane.egg")

        self.ground_object.setScale(1, 1, 1)
        self.ground_object.setPos(0, 0, 0)
        # self.ground.setHpr(0, 0, 0)

        self.ground_material = Material()
        self.ground_material.setShininess(0.0)
        self.ground_material.setAmbient((0, 0, 1, 1))
        print("DEBUG: in load_Environment: if ground_material.hasAmbient() {}".format(self.ground_material.hasAmbient()))
        print("DEBUG: in load_Environment: if ground_material.hasEmission() {}".format(self.ground_material.hasEmission()))

        self.ground_object.setMaterial(self.ground_material)

        # Always last
        self.ground_object.reparentTo(self.render)

    def load_Player(self):
        print("Loading player ...")
        pass

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
