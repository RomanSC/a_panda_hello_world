#!/usr/bin/python3
""" collisions.py | Sun, Jan 07, 2018 | Roman S. Collins



"""
from panda3d.core import CollisionRay
from panda3d.core import CollisionNode
from panda3d.core import CollisionHandler
from panda3d.core import CollisionHandlerQueue
from panda3d.core import CollisionHandlerFloor
from panda3d.core import CollisionTraverser
from panda3d.core import CollisionPolygon
from panda3d.core import CollisionSphere
from panda3d.core import CollisionPlane
from panda3d.core import CollideMask
from panda3d.core import BitMask32
from panda3d.core import Point3

class CollisionController:
    def __init__(self, game):
        self.game = game

        self.traverser = CollisionTraverser('collision traverser')
        self.traverser.showCollisions(self.game.render)

        # Attempt with CollisionHandlerFloor

        # self.traverser.addCollider(fromObject, handler)
        # self.player_ray = CollisionRay(*self.game.player.getPos(), 0.0, 0.0, -1.0)

        # self.player_from_object = self.game.player.attachNewNode(CollisionNode("player collision node"))
        # self.player_from_object.node().addSolid(CollisionRay(0.0, 0.0, 1.0, 
        #                                                      0.0, 0.0, -1.0))
        # self.lifter = CollisionHandlerFloor()
        # self.lifter.addCollider(self.player_from_object, self.game.player)

        # self.game.player.node().setIntoCollideMask(BitMask32.bit(0))
        # self.game.ground_object.node().setIntoCollideMask(BitMask32.bit(0))

        # Attempt with CollisionHandlerQueue() and CollisionRay()

        self.player_col_ray = CollisionRay()
        self.player_col_ray.setOrigin(*self.game.player.getPos())
        self.player_col_ray.setDirection(0.0, 0.0, -1.0)
        self.player_gc = CollisionNode("player collision node")
        self.player_gc.addSolid(self.player_col_ray)
        self.player_gc.setFromCollideMask(CollideMask.bit(0))
        self.player_gc.setIntoCollideMask(CollideMask.allOff())
        self.player_col_node = self.game.player.attachNewNode(self.player_gc)

        self.ground_col_handler = CollisionHandlerQueue()
        self.traverser.addCollider(self.player_col_node, self.ground_col_handler)

    def update(self, task):

        entries = list(self.ground_col_handler.getEntries())
        entries.sort(key=lambda x: x.getSurfacePoint(self.game.render).getZ())

        print(entries)

        if len(entries) > 0:
            print("asdfasdf")
            self.game.player.setZ(entries[0].getSurfacePoint(self.game.render).getZ())

        return task.cont
