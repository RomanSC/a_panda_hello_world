#!/usr/bin/Python3
""" camera.py | Wed, Jan 03, 2018 | Roman S. Collins
"""
# from numpy import tan
# from numpy import arctan2
# from numpy import pi

# from panda3d.core import CollisionRay
# from panda3d.core import CollisionHandler
# from panda3d.core import CollisionNode

from panda3d.core import GraphicsEngine
from panda3d.core import GraphicsPipe
from panda3d.core import FrameBufferProperties
from panda3d.core import WindowProperties
from panda3d.core import Texture
# from panda3d.core import BitMask
# from panda3d.core import BitMask16
from panda3d.core import BitMask32
# from panda3d.core import BitMask64
from panda3d.core import Point3
from panda3d.core import Vec3
from panda3d.core import PNMImage


class CameraController:
    def __init__(self, game):
        self.game = game
        self.game.disableMouse()

        self.start_pos = (0, -200, 200)
        self.start_hpr = (0, -45, 0)

        # self.node = self.game.render.attachNewNode("camera node")
        # self.node.setPos(*self.start_pos)
        # self.node.setHpr(*self.start_hpr)
        # self.game.camera.reparentTo(self.node)
        # self.node.reparentTo(self.game.player.node)

        # TODO:
        # Find out why self.game.camera has no camLens
        # self.game.camera.camLens.setFov(120)

        self.game.camera.setPos(*self.start_pos)
        self.game.camera.setHpr(*self.start_hpr)

        self.depth_camera = DepthCamera(self.game)

    def update(self, task):
        # Zoom
        # camera = self.game.camera
        # if self.game.keymap["zoom-in"]:
        #     camera.setPos(camera.getPos, (0, 1, 0))
        # if self.game.keymap["zoom-out"]:
        #     camera.setPos(camera.getPos, (0, -1, 0))

        # self.game.keymap["zoom-in"] = False
        # self.game.keymap["zoom-out"] = False

        pos_goto = (self.game.player.getX(),
                    self.game.player.getY() - 200,
                    self.game.player.getZ() + 200)

        self.game.camera.setPos(*pos_goto)

        if not self.game.mouseWatcherNode.hasMouse():
            return task.cont

        # mouse = self.game.mouseWatcherNode.getMouse()

        # dy = mouse.getY() - self.game.player.getY()
        # dx = mouse.getX() - self.game.player.getX()
        # angle = arctan2(dy, dx)

        # angle = angle * (180 / pi)

        # pickerNode = CollisionNode('mouseRay')
        # pickerNP = camera.attachNewNode(pickerNode)
        # pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        # pickerRay = CollisionRay()
        # pickerNode.addSolid(pickerRay)
        # myTraverser.addCollider(pickerNP, myHandler)

        # self.game.player.setH(angle)
        # print(self.depth_camera.get_point())

        return task.cont


class DepthCamera:
    def __init__(self, game):
        self.game = game

        self.pipe = self.game.win.get_pipe()
        self.graphics_engine = GraphicsEngine(self.pipe)
        self.frame_buff_props = FrameBufferProperties()
        self.frame_buff_props.set_depth_bits(24)
        self.window_props = WindowProperties.get_default()

        self.output = self.graphics_engine.make_output(self.pipe,
                                                       "depth buffer",
                                                       1,
                                                       self.frame_buff_props,
                                                       self.window_props,
                                                       GraphicsPipe.BF_refuse_window)
        self.depth_texture = Texture("depth texture")
        self.depth_texture.set_format(Texture.F_depth_component)

        buffer = self.output.make_texture_buffer("buffer",
                                                 1,
                                                 1,
                                                 self.depth_texture,
                                                 to_ram=True,
                                                 fbp=self.frame_buff_props)
        assert buffer

        self.origin = self.game.make_camera(buffer)
        self.node = self.origin.node()
        self.mask = BitMask32.bit(21)
        self.node.set_camera_mask(self.mask)
        self.lens = self.node.get_lens()
        self.lens.set_fov(.1)
        self.mouse_watcher = self.game.mouseWatcherNode
        self.main_camera_lens = self.game.camLens

        self.pos = Point3()
        self.direction_vec = Vec3()

    def update(self, task):
        if not self.mouse_watcher.has_mouse():
            return task.cont

        self.mouse_pos = self.mouse_watcher.get_mouse()
        self.far_point = Point3()

        self.main_camera_lens.extrude(self.mouse_pos,
                                      Point3(),
                                      self.far_point)

        self.origin.look_at(self.far_point)
        self.pos = self.origin.get_pos(self.game.render)

        self.direction_vec = self.game.render.get_relative_vector(self.origin,
                                                                  Vec3.forward())


        return task.cont

    def get_point(self):
        self.graphics_engine.render_frame()

        self.img = PNMImage(1, 1)
        self.depth_texture.store(self.img)
        self.pixel = self.img.get_xel(0, 0)
        point = Point3()

        self.lens.extrude_depth(Point3(0.,
                          0.,
                          self.pixel[2]),
                          point)

        self.depth = point[1] * .5

        if self.depth > 100.:
            self.offset = 1.1

            self.origin.set_y(self.origin,
                              self.depth - self.offset)

            self.graphics_engine.render_frame()

            self.img = PNMImage(1, 1)
            self.depth_texture.store(self.img)
            self.pixel = self.img.get_xel(0, 0)
            point = Point3()

            # print(Point3(0.0, 0.0, self.pixel[2]), point)

            self.lens.extrude_depth(Point3(0.0, 0.0,
                              self.pixel[2]),
                              point)

            self.depth2 = point[1] * .5

            self.depth += self.depth2 - self.offset

            self.origin.set_pos(0., 0., 0.)

        return self.pos + self.direction_vec * self.depth
