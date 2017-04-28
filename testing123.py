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


        
    
    
class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/28293b2fe5801e03f1f70ed61c8397f6_airplane-clipart-transparent-airplane-clipart-transparent-background_2400-1009.png")
    
    
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.scale = 0.1
        self.thrust = 0
        self.size = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.Rotate)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.RotateOpposite)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.Stop)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.Stop)
        SpaceGame.listenKeyEvent("keydown", "w", self.Up)
        SpaceGame.listenKeyEvent("keydown", "s", self.Down)
        SpaceGame.listenKeyEvent("keydown", "a", self.Left)
        SpaceGame.listenKeyEvent("keydown", "d", self.Right)
        SpaceGame.listenKeyEvent("keyup", "w", self.StopMovement)
        SpaceGame.listenKeyEvent("keyup", "a", self.StopMovement)
        SpaceGame.listenKeyEvent("keyup", "s", self.StopMovement)
        SpaceGame.listenKeyEvent("keyup", "d", self.StopMovement)
        SpaceGame.listenKeyEvent("keydown", "r", self.Respawn)
       
        
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
            
            
            
    def Respawn(self, event):
        self.x=1
        self.y=1
        self.visible=True
    def thrustOn(self, event):
        self.thrust = 1
    def thrustOff(self, event):
        self.thrust = 0
    def Rotate(self, event):
        self.vr += 0.1
    def RotateOpposite(self, event):
        self.vr -=0.1
    def Stop(self, event):
        self.vr = 0.0
    def StopMovement(self, event):
        self.thrust = 0
    def Up(self, event):
        self.vy -= 0.5
        self.thrust = 1
    def Down(self, event):
        self.vy += 0.5
        self.thrust = 1
    def Left(self, event):
        self.vx -= 0.5
        self.thrust = 1
    def Right(self, event):
        self.vx += 0.5
        self.thrust = 1
        

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceField((0,0))
        SpaceField((500,0))
        SpaceShip((100,100))
       
        
        
        
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for death in self.getSpritesbyClass(Bounce):
            death.step()

    
    
        


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
