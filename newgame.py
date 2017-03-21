from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 500

green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0.5, black)
grass=ImageAsset("images/grass_texture239.jpg")
grassimage=Sprite(grass, (0,0))

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
