from panda3d.core import AmbientLight
from panda3d.core import DirectionalLight
from panda3d.core import Vec3
from panda3d.core import Vec4


class Lighting:
    def __init__(self, game):
        self.game = game

        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))

        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))

        self.game.render.setLight(self.game.render.attachNewNode(ambientLight))
        self.game.render.setLight(self.gamerender.attachNewNode(directionalLight))
