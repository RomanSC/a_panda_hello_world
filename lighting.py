from panda3d.core import NodePath
from panda3d.core import AmbientLight
from panda3d.core import Spotlight
from panda3d.core import PointLight
from panda3d.core import DirectionalLight
from panda3d.core import Vec3
from panda3d.core import Vec4
import sys


class Lighting:
    def __init__(self, game):
        self.game = game
        self.player_node = NodePath()
        self.all_node = NodePath()

        # self.a_light = AmbientLight("ambient light")
        # self.a_light.setColor((0.4, 0.4, 0.2, 0.5))

        # s_light = SpotLight("spot light")
        # s_light.setScene(self.game.render)
        # s_light.setShadowCaster(True, 2048, 2048)
        # s_light.getLens().setFov(40, 20)
        # s_light.getLens().setNearFar(1, 20)

        try:
            self.p_light = PointLight("point light")
            self.p_light.setColor((1, 0, 0, 1))
            self.p_light.setPoint(*self.game.player.getPos())
        except AttributeError:
            pass

        # self.d_light = DirectionalLight("directional light")
        # self.d_light.setDirection((0.0, 0.0, 0.0))
        # self.d_light.setColor((0.4, 0.4, 0.2, 0.5))
        # self.d_light.setSpecularColor((0.8, 0.8, 0.8, 1.0))

        # self.game.render.setLight(self.game.render.attachNewNode(self.a_light))
        # self.game.render.setLight(self.game.render.attachNewNode(self.s_light))
        # self.game.render.setLight(self.game.render.attachNewNode(self.d_light))
        # sys.path.insert(0, "./lib/RenderPipeline")

        # from lib.render_pipeline import PointLight
        # from lib.render_pipeline import Spotlight
        self.all_node.reparentTo(self.game.render)

    def update(self, task):
        # self.player_node.setPos(*self.game.player.getPos())
        p = []
        for x in (self.game.player.getX(),
                  self.game.player.getY(),
                  self.game.player.getZ() +
                  self.game.player.scale + 2.0):
            p.append(x)

        self.p_light.setPoint(*p)

        return task.cont
