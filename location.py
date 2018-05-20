#!/usr/bin/python3
""" location.py | Wed, Jan 03, 2018 | Roman S. Collins

    This file provides the class "location" for objects
    like... what is .forward(), .backward(), .left(),
    .right() of self.player or self.camera?

"""


class Location:
    def __init__(self, game, obj):
        self.game = game
        self.obj = obj

        self.update()

    def update(self):
        self.get_forward()
        self.get_left()
        self.get_backward()
        self.get_right()

    def get_forward(self):
        self.obj.forward = None

    def get_left(self):
        self.obj.left = None

    def get_backward(self):
        self.obj.backward = None

    def get_right(self):
        self.obj.right = None
