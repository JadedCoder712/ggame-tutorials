from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

class SpaceField(Sprite):
    field=ImageAsset("images/field.jpg")

    def __init__(self, position):
         super().__init__(SpaceField.field, position)
         self.vx=1
         self.vy=1
         self.vr=0

class Plane(Sprite):
    airplane = ImageAsset("images/
    def __init__(self, position):
        super().__init__(Plane., position)
