from panda3d.core import AmbientLight
from panda3d.core import DirectionalLight
from panda3d.core import Vec3
from panda3d.core import Vec4
import sys


class Lighting:
    def __init__(self, game):
        self.game = game

        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(0.9, 0.9, 0.9, 0.8))

        # dlight = DirectionalLight("directionalLight")
        # dlight.setDirection(Vec3(0, 0, 0))
        # dlight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        # dlight.setSpecularColor(Vec4(0.2, 0.2, 0.2, 1))

        self.game.render.setLight(self.game.render.attachNewNode(ambientLight))
        # self.game.render.setLight(self.gamerender.attachNewNode(directionalLight))
        # sys.path.insert(0, "./lib/RenderPipeline")

        # from lib.render_pipeline import PointLight
        # from lib.render_pipeline import Spotlight


