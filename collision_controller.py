#!/usr/bin/python3
""" collisions.py | Sun, Jan 07, 2018 | Roman S. Collins



"""
from panda3d.core import CollisionRay
from panda3d.core import CollisionHandler
from panda3d.core import CollisionTraverser

class CollisionController:
    def __init__(self, game):
        self.game = game

        traverser = CollisionTraverser('collision traverser')
        self.game.cTrav = traverser

        # traverser.addCollider(fromObject, handler)

        # Show collisions
        # traverser.showCollisions(self.game.render)
