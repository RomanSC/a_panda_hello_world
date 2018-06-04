#!/usr/bin/python3
""" player.py | Tue, Jan 02, 2018 | Roman S. Collins
"""
from config import *
from constants import *
from helpers import *

from numpy import arange
from math import sqrt
from direct.actor.Actor import Actor
from panda3d.core import Material
# from panda3d.core import TextureStage
# from panda3d.core import TexGenAttrib
from location import Location
from physics import Gravity

class Player(Actor):
    def __init__(self, game):
        super().__init__(self)
        self.game = game

        self.scale = 1

        self.start_pos = (0.0, 2000.0, 0.0)
        self.start_hpr = (0.0, 0.0, 0.0)

        self.default_speed = 30.0
        self.speed = self.default_speed
        self.sprint_speed = 90.0
        self.jump_height = 8.0

        # TODO:
        # Check variable names for clarity via research
        self.max_velocity = 100
        self.velocity = [0.0, 0.0, 0.0]
        self.acceleration = [self.speed, self.speed, self.speed]
        # self.friction = None

        self.loadModel("assets/models/figures/man/man.egg")
        # self.loadModel("assets/models/figures/textures/h.png")
        # self.setTexGen(TextureStage.getDefault(), TexGenAttrib.MWorldPosition)
        # self.setTexProjector(TextureStage.getDefault(), self.game.render, self)
        # self.setTexPos(TextureStage.getDefault(), 0.44, 0.5, 0.2)
        # self.setTexScale(TextureStage.getDefault(), 0.2)
        self.loadAnims({"walk": "assets/models/figures/man/man-walk.egg",
                        "run": "assets/models/figures/man/man-run.egg",
                        "jump": "assets/models/figures/man/man-jump.egg",
                        "idle": "assets/models/figures/man/man-idle.egg"})

        self.queued_animation = None
        self.is_jumping = False

        self.reparentTo(self.game.render)
        self.material = Material()
        self.setMaterial(self.material)

        self.setColor((1.0, 0, 0, 1), 1)
        self.setScale(self.scale)

        self.setPos(*self.start_pos)
        self.setHpr(*self.start_hpr)

        self.loop("idle", fromFrame=0, toFrame=49)
        self.queued_animation = "idle"

    # Movement etc...
    def movement(self, direction):
        dt = globalClock.getDt()

        # Sprinting
        if self.game.keymap.map["sprint"]:
            self.speed = self.sprint_speed
            self.queued_animation = "run"
        else:
            self.speed = self.default_speed
            self.queued_animation = "walk"

        #
        if direction is "forward":
            # self.setPos(self, (0, ((1 * self.speed) * dt), 0))
            self.velocity[1] += self.acceleration[1]
            return

        #
        if direction is "left":
            # self.setPos(self, (-((1 * self.speed) * dt), 0, 0))
            self.setHpr(self, (((1 * self.speed) * 2 * dt), 0, 0))
            return

        #
        if direction is "backward":
            # self.setPos(self, (0, -((1 * self.speed) * dt), 0))
            self.velocity[1] -= self.acceleration[1]
            return

        #
        if direction is "right":
            # self.setPos(self, (((1 * self.speed) * dt), 0, 0))
            self.setHpr(self, (-((1 * self.speed) * 2 * dt), 0, 0))
            return

    # def jump(self):
    #     pass
    #     dt = globalClock.getDt()

    #     # self.v(self.v[0], self.v[1], (self.v[2] + (self.jump_height * 80)))
    #     pos = self.getPos()
    #     self.setPos(self, (pos[0], pos[1], self.jump_height))

    def start_jump(self):
        self.is_jumping = True
        dt = globalClock.getDt()



    def end_jump(self):
        pass

    def update(self, task):
        dt = globalClock.getDt()

        self.setX(self, self.velocity[0] * dt)
        self.setY(self, self.velocity[1] * dt)

        # Gravity set in physics.py
        self.setZ(self, self.velocity[2] * dt)

        for x in range(len(self.velocity)):
            # Max velocity check
            if abs(self.velocity[x]) > self.max_velocity:
                if self.velocity[x] < 0:
                    self.velocity[x] = -self.max_velocity
                if self.velocity[x] > 0:
                    self.velocity[x] = self.max_velocity
            # Stop check
            if self.velocity[x] < 1 and self.velocity[x] > -1:
                self.velocity[x] = 0.0

            if self.velocity[x] != 0:
                if x != 2:
                    if self.velocity[x] < 0:
                        try:
                            self.velocity[x] += sqrt(self.velocity[x])
                        except ValueError:
                            pass

                    if self.velocity[x] > 0:
                        try:
                            self.velocity[x] -= sqrt(self.velocity[x])
                        except ValueError:
                            pass
                else:
                    if self.velocity[x] > 0:
                        try:
                            self.velocity[x] -= sqrt(self.velocity[x])
                        except ValueError:
                            pass

            self.velocity[x] = round(self.velocity[x], 2)

        print(self.velocity)
        print(tuple([round(i, 2) for i in tuple(self.getPos())]))

        return task.cont

    def controller(self, task):
        # Navigation keys
        if self.game.keymap.map["forward"]:
            self.movement("forward")

        if self.game.keymap.map["left"]:
            self.movement("left")

        if self.game.keymap.map["backward"]:
            self.movement("backward")

        if self.game.keymap.map["right"]:
            self.movement("right")

        if self.game.keymap.map["jump"]:
            self.start_jump()

        # Player rotation to face mouse cursor
        # At game start, mouse_pointer is None
        # mouse_pointer = self.game.camera_controller.mouse_pointer.pos
        # if mouse_pointer:

        #     # if (abs(self.getX() - mouse_pointer[0]) > 10) \
        #     #   or (abs(self.getY() - mouse_pointer[1]) > 10) \
        #     #   or (abs(self.getZ() - mouse_pointer[2]) > 10):
        #     #     self.look_at(mouse_pointer[0],
        #     #                  mouse_pointer[1],
        #     #                  (self.getZ() + self.scale/2))

        #     self.look_at(mouse_pointer[0],
        #                  mouse_pointer[1],
        #                  (self.getZ() + self.scale/2))

        #     # self.look_at(mouse_pointer[0],
        #     #              mouse_pointer[1],
        #     #              mouse_pointer[2])

            print(self.getHpr())
            # print(mouse_pointer)

        return task.cont

    def animate(self, task):
        if not self.moving \
           and self.getCurrentAnim() is not "idle":
            self.loop("idle")
            return task.cont

        if self.moving:
            if self.queued_animation is "walk" \
               and self.getCurrentAnim() is not "walk":
                self.loop("walk", fromFrame=0, toFrame=41)
                return task.cont

            if self.queued_animation is "run" \
               and self.getCurrentAnim() is not "run":
                self.loop("run", fromFrame=0, toFrame=7)
                return task.cont

        # TODO
        # Fix later
        if self.queued_animation is "jump" \
           and self.getCurrentAnim() is not "jump":
            self.loop("jump", fromFrame=0, toFrame=35)

        return task.cont

    def is_moving(self, task):
        moving = ["forward", "left", "right", "backward"]
        accumulate = [v for k, v in self.game.keymap.map.items()
                      if k in moving]

        if any(accumulate):
            self.moving = True
            return task.cont

        else:
            self.moving = False
            return task.cont

        return task.cont
