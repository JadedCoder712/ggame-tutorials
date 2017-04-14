from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class SpaceField(Sprite):
    field=ImageAsset("images/starfield.jpg")
    
    
    
    def __init__(self, position):
         super().__init__(SpaceField.field, position)
         self.vx=1
         self.vy=1
         self.vr=0

class Sun(Sprite):
    sun=ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(Sun.sun, position)
        self.vx=0.3
        self.vy=0.3
        self.vr=0
        self.scale = 0.3
    
class Bounce(Sprite):
    
    sun=ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(Bounce.sun, position)
        self.vx=4
        self.vy=4
        self.vr=5
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if (self.x < 0):
            self.vx += 5
        if (self.x > SCREEN_WIDTH):
            self.vx -= 5
        if (self.y < 0):
            self.vy += 5
        if (self.y > SCREEN_HEIGHT):
            self.vy -= 5
        
    
class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/beach-ball-575425_640.png")
    
    
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.scale = 0.1
        self.thrust = 0
        self.thrustframe = 1
        size = 1
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
        """
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
            """
        collidingWith = self.collidingWithSprites(Sun)
        if len(collidingWith) > 0:
            size += 1
        bouncingCollision = self.collidingWithSprites(Bounce)
        if len(bouncingCollision) > 0:
            self.visible = False
        if (self.x < 0):
            self.vx += 1
        if (self.x > SCREEN_WIDTH):
            self.vx -= 0.75
        if (self.y < 0):
            self.vy += 0.75
        if (self.y > SCREEN_HEIGHT):
            self.vy -= 0.75
        growingCollision = self.collidingWithSprites(Sun)
            
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
        
"""
class SpaceBlasts(Sprite):
    blast=ImageAsset("images/bunny.png")
    
    
    def __init__(self, position):
         super().__init__(SpaceBlasts.blast, position)
         self.vx=1
         self.vy=1
         self.vr=0
         SpaceGame.listenKeyEvent("keydown", "p", self.Blast)
         self.blast=False
    def step(self):
        self.x += self.vx
        self.y += self.vy
    def Blast(self, event):
        self.blast=True
         
"""

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
        #SpaceShip((150,150))
        #SpaceShip((200,50))
        Sun((460, 200))
        Bounce((800, 300))
        
        
        
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for death in self.getSpritesbyClass(Bounce):
            death.step()

    
    
        


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
