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
    airplane = ImageAsset("images/28293b2fe5801e03f1f70ed61c8397f6_airplane-clipart-transparent-airplane-clipart-transparent-background_2400-1009.png"
    def __init__(self, position):
        super().__init__(Plane.airplane, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.scale = .01
        Game.listenKeyEvent("keydown", "d", self.Forward)
        Game.listenKeyEvent("keydown", "a", self.Slow)
        Game.listenKeyEvent("keydown", "left arrow", self.Up)
        Game.listenKeyEvent("keydown", "right arrow", self.Down)
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        while self.x > 0:
            self.x += self.vx
            self.x -= 0.4
        while self.y > 0:
            self.y += self.vy
            self.y -= 0.4
         self.rotation += self.vr
         """
         if self.rotation > 90:
             self.vx = 0
             self.y -= 
             """
    def Forward(self, event):
        self.vx += 0.7
    def Slow(self, event):
        self.vx -= 0.6
    def Up(self, event):
        self.vr += 0.6
        self.vy += 0.6
    def Down(self, event):
        self.vr -= 0.6
        self.vy -= 0.6
    
    
    
