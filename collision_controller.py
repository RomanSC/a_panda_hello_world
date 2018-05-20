#!/usr/bin/python3
""" collisions.py | Sun, Jan 07, 2018 | Roman S. Collins



"""
from panda3d.core import CollisionRay
from panda3d.core import CollisionHandler
from panda3d.core import CollisionHandlerFloor
from panda3d.core import CollisionTraverser

from panda3d.core import CollisionPolygon
from panda3d.core import CollisionSphere
from panda3d.core import CollisionPlane
from panda3d.core import Point3
from panda3d.core import BitMask32

from panda3d.core import CollisionNode

class CollisionController:
    def __init__(self, game):
        self.game = game

        self.traverser = CollisionTraverser('collision traverser')
        self.game.cTrav = self.traverser
        self.traverser.showCollisions(self.game.render)

        # self.traverser.addCollider(fromObject, handler)
        # self.player_ray = CollisionRay(*self.game.player.getPos(), 0.0, 0.0, -1.0)

        self.player_from_object = self.game.player.attachNewNode(CollisionNode("player collision node"))
        self.player_from_object.node().addSolid(CollisionRay(0.0, 0.0, 1.0, 
                                                             0.0, 0.0, -1.0))
        self.lifter = CollisionHandlerFloor()
        self.lifter.addCollider(self.player_from_object, self.game.player)

        self.game.ground_object.node().setIntoCollideMask(BitMask32.bit(0))

    def update(self, task):

        return task.cont
