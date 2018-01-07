from panda3d.core import loadPrcFileData
loadPrcFileData("", "sync-video #t")
loadPrcFileData("", "depth-bits 24")

from panda3d.core import *
from direct.showbase.ShowBase import ShowBase


def create_cube():

    vertex_format = GeomVertexFormat.get_v3n3cpt2()
    vertex_data = GeomVertexData("cube_data", vertex_format, Geom.UH_static)
    tris = GeomTriangles(Geom.UH_static)

    pos_writer = GeomVertexWriter(vertex_data, "vertex")
    normal_writer = GeomVertexWriter(vertex_data, "normal")

    vert_count = 0

    for direction in (-1, 1):

        for i in range(3):

            normal = VBase3()
            normal[i] = direction

            for a, b in ((-1., -1.), (-1., 1.), (1., 1.), (1., -1.)):

              pos = VBase3()
              pos[i] = direction
              pos[(i + direction) % 3] = a
              pos[(i + direction * 2) % 3] = b

              pos_writer.add_data3f(pos)
              normal_writer.add_data3f(normal)

            vert_count += 4

            tris.add_vertices(vert_count - 2, vert_count - 3, vert_count - 4)
            tris.add_vertices(vert_count - 4, vert_count - 1, vert_count - 2)

    geom = Geom(vertex_data)
    geom.add_primitive(tris)
    node = GeomNode("cube_geom_node")
    node.add_geom(geom)

    return node


class DepthCamera(object):

    def __init__(self, showbase):

        self._world = showbase.render

        # Normally, moving the main camera causes the calculation of the
        # surface point distance/depth to lag behind and yield incorrect
        # results.
        # Having the depth buffer rendered by a secondary GraphicsEngine
        # can fix this problem.

        pipe = showbase.win.get_pipe()
        ge = GraphicsEngine(pipe)
        self._gfx_engine = ge
        fbp = FrameBufferProperties()
        fbp.set_depth_bits(24)
        winprops = WindowProperties.get_default()
        output = ge.make_output(pipe, "depth_buffer", 1, fbp, winprops,
                                GraphicsPipe.BF_refuse_window)
        self._depth_tex = Texture("depth_texture")
        self._depth_tex.set_format(Texture.F_depth_component)
        # create a depth buffer
        buffer = output.make_texture_buffer("buffer", 1, 1,
                                            self._depth_tex,
                                            to_ram=True, fbp=fbp)
        assert buffer

        self._origin = showbase.make_camera(buffer)
        node = self._origin.node()
        self._mask = BitMask32.bit(21)
        node.set_camera_mask(self._mask)
        self._lens = lens = node.get_lens()
        # only a very small part of the scene should be rendered to the
        # single-pixel depth texture
        lens.set_fov(.1)

        self._mouse_watcher = showbase.mouseWatcherNode
        self._main_cam_lens = showbase.camLens

        self._pos = Point3()
        # viewing direction in world space
        self._dir_vec = Vec3()

        showbase.taskMgr.add(self.__update, "update_depth_cam", sort=40)

    def __update(self, task):

        if not self._mouse_watcher.has_mouse():
          return task.cont

        screen_pos = self._mouse_watcher.get_mouse()
        far_point = Point3()
        self._main_cam_lens.extrude(screen_pos, Point3(), far_point)
        origin = self._origin
        origin.look_at(far_point)
        self._pos = origin.get_pos(self._world)
        self._dir_vec = self._world.get_relative_vector(origin, Vec3.forward())

        return task.cont

    def get_surface_point(self):
        """ Return nearest surface point in viewing direction of camera """

        self._gfx_engine.render_frame()
        img = PNMImage(1, 1)
        self._depth_tex.store(img)
        pixel = img.get_xel(0, 0)
        point = Point3()
        self._lens.extrude_depth(Point3(0., 0., pixel[2]), point)
        depth = point[1] * .5

        if depth > 100.:
            # at large distances, the depth precision decreases, so a second
            # depth render is needed;
            # the depth camera is moved forward by the previously retrieved
            # depth (minus a small value, e.g. 1.1, just a little bigger than
            # the near clipping distance of the lens), placing it very close
            # to the surface, which will make the secondary depth value very
            # accurate; the sum of both depth values will therefore yield a
            # very precise distance of the nearest surface point in the viewing
            # direction of the depth camera
            offset = 1.1 # ensures that the camera does not clip the surface
            self._origin.set_y(self._origin, depth - offset)
            self._gfx_engine.render_frame()
            img = PNMImage(1, 1)
            self._depth_tex.store(img)
            pixel = img.get_xel(0, 0)
            point = Point3()
            self._lens.extrude_depth(Point3(0., 0., pixel[2]), point)
            depth2 = point[1] * .5
            depth += depth2 - offset
            self._origin.set_pos(0., 0., 0.)

        return self._pos + self._dir_vec * depth

    def get_mask(self):

        return self._mask


class MyApp(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)

        self.set_frame_rate_meter(True)

        p_light = PointLight("point_light")
        p_light.set_color((1., 1., 1., 1.))
        self._light = self.camera.attach_new_node(p_light)
        self._light.set_pos(5., -10., 7.)
        self.render.set_light(self._light)

        self._depth_cam = DepthCamera(self)

        self._marker = self.render.attach_new_node(create_cube())
        self._marker.set_color(1., 0., 0.)
        # the marker itself should not be visible to the depth camera
        self._marker.hide(self._depth_cam.get_mask())

        self._test_obj = self.render.attach_new_node(create_cube())
        self._test_obj.set_scale(100.)
        self._test_obj.set_pos(0., 500., 0.)
        self._test_obj.set_hpr(30., 30., 0.)
        self._test_obj.set_color(0., 1., 0.)

        # allow copying the marker at its current location for debugging
        self.accept("enter", self.__copy_marker)

        # place the marker on the surface under the mouse cursor;
        # this task should run after the transformation of the depth camera
        # has been updated, but before the primary GraphicsEngine renders
        # the next frame (in a task with sort=50)
        self.taskMgr.add(self.__set_marker_pos, "set_marker_pos", sort=45)

    def __copy_marker(self):

        self._marker.copy_to(self.render)

    def __set_marker_pos(self, task):

        if not self.mouseWatcherNode.has_mouse():
            return task.cont

        self._marker.set_pos(self._depth_cam.get_surface_point())

        return task.cont


app = MyApp()
app.run()
