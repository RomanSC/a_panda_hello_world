#!/usr/bin/Python3
""" camera.py | Wed, Jan 03, 2018 | Roman S. Collins
"""
from direct.showbase.ShowBase import Plane
from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBase import Vec3
from direct.showbase.ShowBase import Point3
from direct.showbase.ShowBase import CardMaker
from direct.showbase.ShowBase import CardMaker

import direct.directbase.DirectStart 
from direct.showbase.DirectObject import DirectObject 
# from pandac.PandaModules import * 


class CameraController:
    def __init__(self, game):
        self.game = game
        self.game.disableMouse()

        self.start_pos = (0, -200, 200)
        self.start_hpr = (0, -45, 0)

        self.game.camera.setPos(*self.start_pos)
        self.game.camera.setHpr(*self.start_hpr)

        self.mouse_pointer = MousePointer(self.game)

        self.min_zoom = 100
        self.max_zoom = 500

        self.zoom = 200

    def update(self, task):
        if self.zoom > self.max_zoom:
            self.zoom = self.max_zoom
            return task.cont

        if self.zoom < self.min_zoom:
            self.zoom = self.min_zoom
            return task.cont

        if self.game.keymap.map["zoom-out"] and not self.zoom == self.max_zoom:
            self.zoom += 20
            self.game.keymap.map["zoom-out"] = False
        if self.game.keymap.map["zoom-in"] and not self.zoom == self.min_zoom:
            self.zoom -= 20
            self.game.keymap.map["zoom-in"] = False

        # Zoom
        # camera = self.game.camera
        # if self.game.keymap.map["zoom-in"]:
        #     self.zoom += 1
        # if self.game.keymap.map["zoom-out"]:
        #     self.zoom -= 1

        goto_pos = (self.game.player.getX(),
                    self.game.player.getY() + -(self.zoom),
                    self.game.player.getZ() + (self.zoom))

        self.game.camera.setPos(*goto_pos)

        return task.cont

# class MousePointer:
#     def __init__(self, game):
#         self.game = game
#         z = 0
#         self.plane = Plane(Vec3(0, 0, 1), Point3(0, 0, z))
#         cm = CardMaker("blah")
#         cm.setFrame(-100, 100, -100, 100)

#         self.game.render.attachNewNode(cm.generate()).lookAt(0, 0, -1)

#         self.pos = None

#     def get_point(self, task):
#         if self.game.mouseWatcherNode.hasMouse():
#             mpos = self.game.mouseWatcherNode.getMouse()
#             pos_3d = Point3()
#             nearPoint = Point3()
#             farPoint = Point3()

#             self.game.camLens.extrude(mpos, nearPoint, farPoint)

#             if self.plane.intersectsLine(pos_3d,
#                self.game.render.getRelativePoint(self.game.camera, nearPoint),
#                self.game.render.getRelativePoint(self.game.camera, farPoint)):
#                 # print "Mouse ray intersects ground plane at ", pos_3d
#                 # self.model.setPos(render, pos_3d)
#                 self.pos = pos_3d
#         return task.again

class MousePointer:
    def __init__(self, game):
        self.game = game


