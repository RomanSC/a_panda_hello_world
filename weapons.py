#!/usr/bin/python
""" weapons.py | Sun, Jan 07, 2018 | Roman S. Collins
"""
from direct.actor.Actor import Actor
from panda3d.core import Material
from location import Location
from physics import Gravity

class Sword(Actor):
    def __init__(self, game):
        super().__init__(self)
        self.game = game

        self.scale = 1
        self.start_pos = (35, 0, 0)
        self.start_hpr = (90, 0, 0)

        self.loadModel("assets/models/weapons/melee/swords/sword.egg")

        self.sword_material = Material()
        self.sword_material.setShininess(10)
        self.sword_material.setDiffuse((1, 0, 0, 1.0))
        self.setMaterial(self.sword_material)

        self.reparentTo(self.game.render)

        self.setScale(self.scale)
        self.setPos(*self.start_pos)
        self.setHpr(*self.start_hpr)

        # Node for the sword
        # self.node = self.game.render.attachNewNode("sword node")
        # self.node.reparentTo(self)

        # self.location = Location(self.game, self)
        # self.gravity = Gravity(self.game, self)

        # self.loop("idle", fromFrame=0, toFrame=49)
        # self.queued_animation = "idle"

    def update(self, task):
        return task.cont


class HenryRifle(Actor):
    def __init__(self, game):
        super().__init__(self)
        self.game = game

        self.scale = 1
        self.start_pos = (45, 0, 0)
        self.start_hpr = (0, 0, 0)

        self.loadModel("assets/models/weapons/ranged/rifles/1860_Henry.egg")

        self.rifle_material = Material()
        self.rifle_material.setShininess(10)
        self.rifle_material.setDiffuse((1, 0, 0, 1.0))
        self.setMaterial(self.rifle_material)

        self.reparentTo(self.game.render)

        self.setScale(self.scale)
        self.setPos(*self.start_pos)
        self.setHpr(*self.start_hpr)

    def update(self, task):
        return task.cont
