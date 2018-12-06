### Kinect starter Code from Fletcher Marsh's Flappy Bird
### https://github.com/fletcher-marsh/kinect_python/blob/master/FlapPyKinect.py
### Pygame template from Lukas Peraza
### https://qwewy.gitbooks.io/pygame-module-manual/chapter1/framework.html
### collaborated with @cscheire and @lukez1

### Kinect
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
from SpriteFormat import *
# from pykinec t import nui

import ctypes
import _ctypes
import pygame
import sys
import math
import random

KINECTEVENT = pygame.USEREVENT
DEPTH_WINSIZE = 320,240
VIDEO_WINSIZE = 640,480
pygame.init()

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread
import pygame
import random 

pygame.init()

class Character(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.width = 600
        self.height = 400
        self.health = 100
        self.speed = self.width/30
        self.state = "startMode"
        self.posX = self.width/6
        self.posY = 215 * self.height/400
        self.time = 0
        self.bullets = []
        self.screen = screen
        self.lives = 3
        self.spriteSize = 64
        self.vel = 7
        self.isJump = False
        self.leftPlayerWalk = False
        self.rightPlayerWalk = True
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True        


class Aang(Character):
    def __init__(self, screen):
        super().__init__(screen)
        spriteSizeX = 100
        spriteSizeY = 60
        self.aangLeft = pygame.image.load('images/aang2.png')
        self.aangLeft = pygame.transform.scale(self.aangLeft, (spriteSizeX, spriteSizeY))
        self.aangRight = pygame.image.load('images/aang1.png')
        self.aangRight = pygame.transform.scale(self.aangRight, (spriteSizeX, spriteSizeY))
        self.aangFly = pygame.image.load('images/aangFly.png')
        self.aangFly = pygame.transform.scale(self.aangFly, (spriteSizeX, spriteSizeX))
        self.airball = pygame.image.load('images/AirShield.png')
        self.airball = pygame.transform.scale(self.airball, (20, 20))
        self.isJump = False
        self.leftPlayerWalk = False
        self.rightPlayerWalk = True
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        self.posX = self.width//20
        self.posY = 200
        self.dir = 1
        self.bulletCount = 0
        self.color = (255,165,0)
        
    def draw(self):
        if not(self.standing):
            if self.leftPlayerWalk == True:
                self.screen.blit(self.aangLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.aangRight, (self.posX, self.posY))
                
        else: #never lets man stand straight so he can shoot bullets
            if self.leftPlayerWalk == True:
                self.screen.blit(self.aangLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.aangRight, (self.posX,self.posY))
                
        if self.isJump:
            self.screen.blit(self.aangFly, (self.posX, self.posY))
            
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        pygame.draw.rect(self.screen, self.color, self.hitbox, 5)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))


class Zuko(Character):
    def __init__(self, screen):
        super().__init__(screen)
        spriteSizeX = 100
        spriteSizeY = 60
        self.zukoRight = pygame.image.load('images/zukoRight.png')
        self.zukoRight = pygame.transform.scale(self.zukoRight, (spriteSizeX, spriteSizeY))
        self.zukoLeft = pygame.image.load('images/zuko.png')
        self.zukoLeft = pygame.transform.scale(self.zukoLeft, (spriteSizeX, spriteSizeY))
        self.fireball = pygame.image.load('images/fireball.png')
        self.fireball = pygame.transform.scale(self.fireball, (20, 20))
        self.isJump = False
        self.leftPlayerWalk = True
        self.rightPlayerWalk = False
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        self.bullets = []
        self.posX = 300
        self.posY = 200
        self.dir = 1
        self.jumpTimes = 0
        self.bulletCount = 0
        self.color = (255,165,0)                
    def draw(self):
        if not(self.standing):
            if self.leftPlayerWalk == True:
                self.screen.blit(self.zukoLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.zukoRight, (self.posX, self.posY))
                self.walkCount += 1
        else: #never lets man stand straight so he can shoot bullets
            if self.leftPlayerWalk == True:
                self.screen.blit(self.zukoLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.zukoRight, (self.posX,self.posY))
    
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        pygame.draw.rect(self.screen, self.color, self.hitbox, 5)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))

class Momo(Character):
    def __init__(self, screen):
        super().__init__(screen)
        spriteSizeX = 100
        spriteSizeY = 60
        self.momoLeft = pygame.image.load('images/momo.png')
        self.momoLeft = pygame.transform.scale(self.momoLeft, (spriteSizeX, spriteSizeY))
        self.momoRight = pygame.image.load('images/momo.png')
        self.momoRight = pygame.transform.scale(self.momoRight, (spriteSizeX, spriteSizeY))
        self.momoFly = pygame.image.load('images/momo.png')
        self.momoFly = pygame.transform.scale(self.momoFly, (spriteSizeX, spriteSizeX))
        self.airball = pygame.image.load('images/airballs.png')
        self.airball = pygame.transform.scale(self.airball, (20, 20))
        self.isJump = False
        self.leftPlayerWalk = False
        self.rightPlayerWalk = True
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        self.posX = self.width//10
        self.posY = self.height - 100
        self.dir = 1
        self.bulletCount = 0
        self.color = (255,165,0)
        
    def draw(self):
        if not(self.standing):
            if self.leftPlayerWalk == True:
                self.screen.blit(self.momoLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.momoRight, (self.posX, self.posY))
                
        else: #never lets man stand straight so he can shoot bullets
            if self.leftPlayerWalk == True:
                self.screen.blit(self.momoLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.momoRight, (self.posX,self.posY))
                
        if self.isJump:
            self.screen.blit(self.momoFly, (self.posX, self.posY))
            
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        pygame.draw.rect(self.screen, self.color, self.hitbox, 5)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))

class cabbageMan(Character):
    def __init__(self, screen):
        super().__init__(screen)
        spriteSizeX = 100
        spriteSizeY = 60
        self.cabLeft = pygame.image.load('images/cabbageFullBody.png')
        self.cabLeft = pygame.transform.scale(self.cabLeft, (spriteSizeX, spriteSizeY))
        self.cabRight = pygame.image.load('images/cabbageFullBody.png')
        self.cabRight = pygame.transform.scale(self.cabRight, (spriteSizeX, spriteSizeY))
        self.cabFly = pygame.image.load('images/cabbageFullBody.png')
        self.cabFly = pygame.transform.scale(self.cabFly, (spriteSizeX, spriteSizeX))
        self.airball = pygame.image.load('images/airballs.png')
        self.airball = pygame.transform.scale(self.airball, (20, 20))
        self.isJump = False
        self.leftPlayerWalk = False
        self.rightPlayerWalk = True
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        self.posX = self.width//10
        self.posY = self.height - 100
        self.dir = 1
        self.bulletCount = 0
        self.color = (255,165,0)

    def draw(self):
        if not(self.standing):
            if self.leftPlayerWalk == True:
                self.screen.blit(self.cabLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.cabRight, (self.posX, self.posY))
                
        else: #never lets man stand straight so he can shoot bullets
            if self.leftPlayerWalk == True:
                self.screen.blit(self.cabLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.cabRight, (self.posX,self.posY))
                
        if self.isJump:
            self.screen.blit(self.cabFly, (self.posX, self.posY))
            
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        pygame.draw.rect(self.screen, self.color, self.hitbox, 5)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))

class Katara(Character):
    def __init__(self, screen):
        super().__init__(screen)
        spriteSizeX = 100
        spriteSizeY = 60
        self.katLeft = pygame.image.load('image/Katara.png')
        self.katLeft = pygame.transform.scale(self.katLeft, (spriteSizeX, spriteSizeY))
        self.katRight = pygame.image.load('images/Katara1.png')
        self.katRight = pygame.transform.scale(self.katRight, (spriteSizeX, spriteSizeY))
        self.katFly = pygame.image.load('images/katFly.png')
        self.katFly = pygame.transform.scale(self.katFly, (spriteSizeX, spriteSizeX))
        self.airball = pygame.image.load('images/airballs.png')
        self.airball = pygame.transform.scale(self.airball, (20, 20))
        self.isJump = False
        self.leftPlayerWalk = False
        self.rightPlayerWalk = True
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        self.posX = self.width//10
        self.posY = self.height - 100
        self.dir = 1
        self.bulletCount = 0
        self.color = (255,165,0)        
    def draw(self):
        if not(self.standing):
            if self.leftPlayerWalk == True:
                self.screen.blit(self.katLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.katRight, (self.posX, self.posY))
                
        else: #never lets man stand straight so he can shoot bullets
            if self.leftPlayerWalk == True:
                self.screen.blit(self.katLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.katRight, (self.posX,self.posY))
                
        if self.isJump:
            self.screen.blit(self.katFly, (self.posX, self.posY))
            
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        pygame.draw.rect(self.screen, self.color, self.hitbox, 5)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))
class tyLee(Character):
    def __init__(self, screen):
        super().__init__(screen)
        spriteSizeX = 100
        spriteSizeY = 60
        self.tyLeeLeft = pygame.image.load('images/tyLee.png')
        self.tyLeeLeft = pygame.transform.scale(self.tyLeeLeft, (spriteSizeX, spriteSizeY))
        self.tyLeeRight = pygame.image.load('images/tyLee.png')
        self.tyLeeRight = pygame.transform.scale(self.tyLeeRight, (spriteSizeX, spriteSizeY))
        self.tyLeeFly = pygame.image.load('images/tyLeeFly.png')
        self.tyLeeFly = pygame.transform.scale(self.tyLeeFly, (spriteSizeX, spriteSizeX))
        self.airball = pygame.image.load('images/airballs.png')
        self.airball = pygame.transform.scale(self.airball, (20, 20))
        self.isJump = False
        self.leftPlayerWalk = False
        self.rightPlayerWalk = True
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        self.posX = self.width//10
        self.posY = self.height - 100
        self.dir = 1
        self.bulletCount = 0
        self.color = (255,165,0)                
    def draw(self):
        if not(self.standing):
            if self.leftPlayerWalk == True:
                self.screen.blit(self.tyLeeLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.tyLeeRight, (self.posX, self.posY))
                
        else: #never lets man stand straight so he can shoot bullets
            if self.leftPlayerWalk == True:
                self.screen.blit(self.tyLeeLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.tyLeeRight, (self.posX,self.posY))
                
        if self.isJump:
            self.screen.blit(self.tyLeeFly, (self.posX, self.posY))
            
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        pygame.draw.rect(self.screen, self.color, self.hitbox, 5)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))


class combustionMan(Character):
    def __init__(self, screen):
        super().__init__(screen)
        spriteSizeX = 100
        spriteSizeY = 60
        self.cbLeft = pygame.image.load('images/combustionMan.png')
        self.cbLeft = pygame.transform.scale(self.cbLeft, (spriteSizeX, spriteSizeY))
        self.cbRight = pygame.image.load('images/combustionMan.png')
        self.cbRight = pygame.transform.scale(self.cbRight, (spriteSizeX, spriteSizeY))
        self.cbFly = pygame.image.load('images/combustionMan.png')
        self.cbFly = pygame.transform.scale(self.cbFly, (spriteSizeX, spriteSizeX))
        self.airball = pygame.image.load('images/airballs.png')
        self.airball = pygame.transform.scale(self.airball, (20, 20))
        self.isJump = False
        self.leftPlayerWalk = False
        self.rightPlayerWalk = True
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        self.posX = self.width//10
        self.posY = self.height - 100
        self.dir = 1
        self.bulletCount = 0
        self.color = (255,165,0)        
    def draw(self):
        if not(self.standing):
            if self.leftPlayerWalk == True:
                self.screen.blit(self.cbLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.cbRight, (self.posX, self.posY))
                
        else: #never lets man stand straight so he can shoot bullets
            if self.leftPlayerWalk == True:
                self.screen.blit(self.cbLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.cbRight, (self.posX,self.posY))
                
        if self.isJump:
            self.screen.blit(self.cbFly, (self.posX, self.posY))
            
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        pygame.draw.rect(self.screen, self.color, self.hitbox, 5)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))

class Toph(Character):
    def __init__(self, screen):
        super().__init__(screen)
        spriteSizeX = 100
        spriteSizeY = 60
        self.tophLeft = pygame.image.load('images/toph2.png')
        self.tophLeft = pygame.transform.scale(self.tophLeft, (spriteSizeX, spriteSizeY))
        self.tophRight = pygame.image.load('images/toph1.png')
        self.tophRight = pygame.transform.scale(self.tophRight, (spriteSizeX, spriteSizeY))
        self.tophFly = pygame.image.load('images/tophFly.png')
        self.tophFly = pygame.transform.scale(self.tophFly, (spriteSizeX, spriteSizeX))
        self.airball = pygame.image.load('images/airballs.png')
        self.airball = pygame.transform.scale(self.airball, (20, 20))
        self.isJump = False
        self.leftPlayerWalk = False
        self.rightPlayerWalk = True
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        self.posX = self.width//10
        self.posY = self.height - 100
        self.dir = 1
        self.bulletCount = 0
        self.color = (255,165,0)        
    def draw(self):
        if not(self.standing):
            if self.leftPlayerWalk == True:
                self.screen.blit(self.tophLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.tophRight, (self.posX, self.posY))
                
        else: #never lets man stand straight so he can shoot bullets
            if self.leftPlayerWalk == True:
                self.screen.blit(self.tophLeft, (self.posX, self.posY))
            elif self.rightPlayerWalk == True:
                self.screen.blit(self.tophRight, (self.posX,self.posY))
                
        if self.isJump:
            self.screen.blit(self.tophFly, (self.posX, self.posY))
            
        self.hitbox = (self.posX - 10, self.posY - 10, 70, 70) #udpates new (x,y) before redrawing new square
        pygame.draw.rect(self.screen, self.color, self.hitbox, 5)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))

class mainHealthBar(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255,0,0)
        self.score = 0
        self.x = self.x + self.score
        self.width =  self.width - self.score
        self.bulCount = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x + self.score, self.y, self.width - self.score, self.height))

class oppHealthBar(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 0)
        self.score = 0
        self.width = self.width - self.score
        self.bulCount = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x , self.y, self.width - self.score, self.height))

class chargeBar(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (173,255,47)
        self.score = 0
        self.tBTime = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x , self.y, self.width + self.tBTime, self.height))
        
class Bullet(object):
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.rad = radius
        self.color = color
        self.dir = direction #which way the bullet shoots
        speed = 19
        self.vel = speed * self.dir #speed of bullet
        self.bulletList = []
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.rad)

class States(object):
   def __init__(self):
       self.done = False
       self.next = None
       self.quit = False
       self.previous = None
       self.gameMode = "startMode"



# colors for drawing different bodies 
SKELETON_COLORS = [pygame.color.THECOLORS["green"],  
                  pygame.color.THECOLORS["purple"], 
                  pygame.color.THECOLORS["yellow"], 
                  pygame.color.THECOLORS["violet"]]


class BodyGameRuntime(object):
    def __init__(self):
        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()
        self.timerStart = 1
        
        # Set the width and height of the screen [width, height]
        self._infoObject = pygame.display.Info()
        self._screen = pygame.display.set_mode((self._infoObject.current_w >> 1, self._infoObject.current_h >> 1), 
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

        self.leftHX = 0
        self.rightHX = 0
        self.leftHY = 0
        self.rightHY = 0
        self.prevLHX = 0
        self.prevRHX = 0
        self.prevLHY = 0
        self.prevRHY = 0
        self.clapOnce = False

        self.rad = 40
        pygame.display.set_caption("Andey's Kinect")
        # Loop until the user clicks the close button.
        self._done = False
        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Kinect runtime object, we want only color and body frames 
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)
        # back buffer surface for getting Kinect color frames, 32bit color, width and height equal to the Kinect color frame size
        self._frame_surface = pygame.Surface((self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height), 0, 32)
        #store skeleton data 
        self._bodies = None

        self.square = (0,0, 50, 50)
        ## Pygame Init
        self.width = 1000
        self.height = 800
        self.draftPlayers = False
        self.themeSong = pygame.mixer.Sound("images/theme.wav")
        self.introVid = pygame.mixer.Sound("images/introVid.wav")
        self.time = 0
        self.state = "startMode"
        self.oppCharge = 1
        self.playerCharge = 1
        self.move = False
        self.playerMoveTracker = []
        self.startRealScreen = 0
        self.playerChoosing = True
        self.playerNotEnough = False
        self.plzSHOOT = False
        self.oppMove = "nothing"
        self.playerMove = "nothing"
        self.playerMirrored = False
        self.opponentMirrored = False
        self.black = (0,0,0)
        self.startScreen = pygame.image.load("images/start.png")
        self.startScreen =pygame.transform.scale(self.startScreen,(self.width,self.height))
        self.screen = pygame.display.set_mode((self.width, self.height))
        ### Character Selection
        self.charAangScreen = pygame.image.load("images/charAangSelect.jpg")
        self.charAangScreen =pygame.transform.scale(self.charAangScreen,(self.width,self.height))
        self.charKataraScreen = pygame.image.load("images/charKataraSelect.jpg")
        self.charKataraScreen =pygame.transform.scale(self.charKataraScreen,(self.width,self.height))
        self.charTophScreen = pygame.image.load("images/charTophSelect.jpg")
        self.charTophScreen =pygame.transform.scale(self.charTophScreen,(self.width,self.height))        
        self.charCabScreen = pygame.image.load("images/charCabbageSelect.jpg")
        self.charCabScreen =pygame.transform.scale(self.charCabScreen,(self.width,self.height))
        self.charCBManScreen = pygame.image.load("images/charCombustionSelect.png")
        self.charCBManScreen = pygame.transform.scale(self.charCBManScreen,(self.width,self.height))
        self.charTyLeeScreen = pygame.image.load("images/charTyLeeSelect.jpg")
        self.charTyLeeScreen = pygame.transform.scale(self.charTyLeeScreen,(self.width,self.height))
        self.charZukoScreen = pygame.image.load("images/charZukoSelect.jpg")
        self.charZukoScreen = pygame.transform.scale(self.charZukoScreen,(self.width,self.height))
        self.charMomoScreen = pygame.image.load("images/charAppaMomoSelect.jpg")
        self.charMomoScreen = pygame.transform.scale(self.charMomoScreen,(self.width,self.height))
        
        self.endScreen = pygame.image.load("images/gameOver.png")
        self.endScreen =pygame.transform.scale(self.endScreen,(self.width,self.height))
        self.playScreen = pygame.image.load("images/waternation.jpg")
        self.playScreen = pygame.transform.scale(self.playScreen,(self.width,self.height))
        self.learnScreen = pygame.image.load("images/aangIntro.jpg")
        self.learnScreen = pygame.transform.scale(self.learnScreen,(self.width,self.height))   
        
        self.player = Aang(self.screen)
        self.opponent = Zuko(self.screen)
        
        self.timeBar = chargeBar(0, 20, 0, 20)
        self.mainHealthBar = mainHealthBar(0,0, self.width//2, 20)
        self.oppHealthBar = oppHealthBar(self.width//2,0, self.width//2, 20)
        self.gameOver = False
        self.playerBulList = []
        self.oppBulList = []
        self.playerShot = False
        self.oppShot = False
        self.bulletSpeed = 0
        self.playerBulPosX = 0
        self.playerBulPosY = 0
        self.oppBulPosX = 0
        self.oppBulPosY = 0
        self.opponent.dir = -1
        self.player.dir = 1
        
    def playerBulletTracker(self):
        for bulA in self.playerBulList: #detects if player is shot at
            bulA.x += bulA.vel
            print(self.playerBulPosX)
            self.playerBulPosX = bulA.x
            self.playerBulPosY = bulA.y
            self.bulletSpeed = bulA.vel
            if (self.opponent.hitbox[0]< bulA.x and (self.opponent.hitbox[0] + 70) > bulA.x) and (self.opponent.hitbox[1] < bulA.y and (self.opponent.hitbox[1] + 70) > bulA.y) and self.opponentMirrored == False: #normally hit
                print('hit')
                self.oppHealthBar.bulCount += 1
                self.playerBulList.remove(bulA)
                self.playerShot = False
                if bulA.rad > 50:
                    self.oppHealthBar.score += 40
                    self.oppCharge = 0
                else:
                    self.oppHealthBar.score += 10
                    self.oppCharge -= 1
            if (self.opponent.hitbox[0]< bulA.x and (self.opponent.hitbox[0] + 70) > bulA.x) and (self.opponent.hitbox[1] < bulA.y and (self.opponent.hitbox[1] + 70) > bulA.y) and self.opponentMirrored == True: #mirrored
                bulA.vel *= -1
            if bulA.x > self.width or bulA.x < 0:
                self.playerBulList.remove(bulA)
                self.playerShot = False
                
    def oppBulletTracker(self):
        for bulZ in self.oppBulList: #opponent's bullets that are shooting
            self.oppBulPosX = bulZ.x
            self.oppBulPosY = bulZ.y
            bulZ.x += bulZ.vel
            if (self.player.hitbox[0]< bulZ.x and (self.player.hitbox[0] + 70) > bulZ.x) and (self.player.hitbox[1] < bulZ.y and (self.player.hitbox[1] + 70) > bulZ.y) and self.playerMirrored == False: #normal hit
                print('aang hit')
                self.mainHealthBar.bulCount += 1 #detects gameOver
                self.oppBulList.remove(bulZ)
                self.oppShot = False
                if bulZ.rad > 50:
                    self.mainHealthBar.score += 40
                    self.playerCharge = 0
                else:
                    self.playerScoreIncr = self.mainHealthBar.score
                    self.mainHealthBar.score += 10
                    self.playerCharge -= 1
            if bulZ.x < 0 or bulZ.x > self.width:
                self.oppBulList.remove(bulZ)
                self.oppShot = False
    
            if (self.player.hitbox[0]< bulZ.x and (self.player.hitbox[0] + 70) > bulZ.x) and (self.player.hitbox[1] < bulZ.y and (self.player.hitbox[1] + 70) > bulZ.y) and self.playerMirrored == True: #deflected off aang
                print('deflected')
                bulZ.vel *= -1.5
            elif (self.opponent.hitbox[0]< bulZ.x): #deflected and opponent
                print('alskdfj')
                self.oppBulList.remove(bulZ)
                if bulZ.rad > 50:
                    self.oppHealthBar.score += 40
                    self.oppCharge = 0
                else:
                    self.oppScoreIncr = self.oppHealthBar.score
                    self.oppHealthBar.score += 10   
                    self.oppCharge -= 1
                self.oppHealthBar.bulCount += 1 #detects gameOver
                self.oppShot = False
        
        if self.player.isJump:
            if self.player.jumpCount >= -10:
                neg = 1.5 #start moving up 
                if self.player.jumpCount < 0:
                    neg = -1.5 # moving down in the parabola
                #makes a quadratic parabola to illustrate diff speeds
                #0.5 scales the jump smaller 
                self.player.posY -= (0.5 * (self.player.jumpCount ** 2) * neg)
                self.player.jumpCount -= 1 #change heights
            else:
                self.player.isJump = False
                self.player.jumpCount = 10
                
        if self.opponent.isJump: #when jumping
            if self.opponent.jumpCount >= -10: 
                neg = 1.5 #start moving up 
                if self.opponent.jumpCount < 0:
                    neg = -1.5 # moving down in the parabola
                #makes a quadratic parabola to illustrate diff speeds
                #0.5 scales the jump smaller 
                self.opponent.posY -= (0.5 * (self.opponent.jumpCount ** 2) * neg)
                self.opponent.jumpCount -= 1 #change heights
            else:
                self.opponent.isJump = False
                self.opponent.jumpCount = 10
        
    def surface_to_array(surface):
        buffer_interface = surface.get_buffer()
        address = ctypes.c_void_p()
        size = Py_ssize_t()
        _PyObject_AsWriteBuffer(buffer_interface,
                                ctypes.byref(address), ctypes.byref(size))
        bytes = (ctypes.c_byte * size.value).from_address(address.value)
        bytes.object = buffer_interface
        return bytes
    
    def startIntroVid(self):
        pygame.mixer.Sound.play(self.introVid)

    def drawCircle(self, joints, jointPoints, color, joint1, rad):
        joint1State = joints[joint1].TrackingState

        #start and end points for drawing lines
        end = (int(jointPoints[joint1].x), int(jointPoints[joint1].y))

        # print(end)
        pygame.draw.circle(self._frame_surface, color, end, rad)

    def drawLine(self, prevX, prevY, curX, curY, color):
        pygame.draw.line(self._frame_surface, color, (prevX, prevY), (curX, curY), 40)
            
    
    def clapRight(self, joints,jointPoints):
        self.clapOnce = True
        self.spineX = jointPoints[PyKinectV2.JointType_SpineMid].x
        self.aboveHead = jointPoints[PyKinectV2.JointType_SpineShoulder].y
        if self.centerCollision and self.LHX >  self.spineX:
            print("right")
            return True
    def clapLeft(self, joints, jointPoints):
        self.clapOnce = True
        self.spineX = jointPoints[PyKinectV2.JointType_SpineMid].x
        self.aboveHead = jointPoints[PyKinectV2.JointType_SpineShoulder].y
        if self.centerCollision and self.RHX < self.spineX:
            print("left")
            return True

    def clapUp(self, joints, jointPoints):
        self.clapOnce = True
        self.LHX = jointPoints[PyKinectV2.JointType_HandLeft].x
        self.RHX = jointPoints[PyKinectV2.JointType_HandRight].x
        self.LHY = jointPoints[PyKinectV2.JointType_HandLeft].y
        self.RHY = jointPoints[PyKinectV2.JointType_HandRight].y
        
        self.spineX = jointPoints[PyKinectV2.JointType_SpineMid].x
        self.aboveHead = jointPoints[PyKinectV2.JointType_SpineShoulder].y
        if self.centerCollision and self.LHY < self.aboveHead:
            print("up")
            return True
    
    def drawCenterBox(self, joints, jointPoints):
        self.shoulderLX = jointPoints[PyKinectV2.JointType_ShoulderLeft].x
        self.shoulderLY = jointPoints[PyKinectV2.JointType_ShoulderLeft].y
        self.shoulderRX = jointPoints[PyKinectV2.JointType_ShoulderRight].x
        self.hipRY = jointPoints[PyKinectV2.JointType_HipRight].y
        box = (self.shoulderLX, self.shoulderLY, self.shoulderRX - self.shoulderLX, self.hipRY)
        pygame.draw.rect(self._frame_surface, pygame.color.THECOLORS['orange'], box, 5)
    
    def drawCircPalms(self, joints, jointPoints): #resting position
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["orange"], PyKinectV2.JointType_HandRight,40)
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["orange"], PyKinectV2.JointType_HandLeft,40)

    def lassoDectection(self, joints, jointPoints):
        #if lasso detected, draw a blue Circle
        print("LASSSO")
        startR = PyKinectV2.JointType_HandTipRight
        startL = PyKinectV2.JointType_HandTipLeft
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["blue"], startR, 40)
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["blue"], startL,40)
   
    def drawSpine(self, joints, jointPoints):
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["orange"], PyKinectV2.JointType_SpineMid,40)
        
    def centerCollision(self, jointPoints):        
        #if joint.x and joint.y is within a specific range, return true
        
        self.clapOnce = True
        self.LHX = jointPoints[PyKinectV2.JointType_HandLeft].x
        self.RHX = jointPoints[PyKinectV2.JointType_HandRight].x
        
        self.LHY = jointPoints[PyKinectV2.JointType_HandLeft].y
        self.RHY = jointPoints[PyKinectV2.JointType_HandRight].y
        dist = math.sqrt(((self.RHX - self.LHX)**2)+ (self.RHY - self.LHY)**2)
        if dist <= 40:
            return True

    def blockDectection(self, jointPoints):
        self.LHX = jointPoints[PyKinectV2.JointType_HandLeft].x
        self.RHX = jointPoints[PyKinectV2.JointType_HandRight].x
        
        self.LHY = jointPoints[PyKinectV2.JointType_HandLeft].y
        self.RHY = jointPoints[PyKinectV2.JointType_HandRight].y
        
        self.rShoulderX = jointPoints[PyKinectV2.JointType_ShoulderRight].x
        self.rShoulderY = jointPoints[PyKinectV2.JointType_ShoulderRight].y

        dist = math.sqrt(((self.RHX - self.rShoulderX)**2)+ (self.RHY - self.rShoulderY)**2)
        if dist <= 40:
            return True
    
    def drawShield(self, joints, jointPoints):
        print("shield!")
        self.shoulderLX = jointPoints[PyKinectV2.JointType_ShoulderLeft].x
        self.shoulderRY = jointPoints[PyKinectV2.JointType_ShoulderLeft].y
        self.shoulderRX = jointPoints[PyKinectV2.JointType_ShoulderRight].x
        self.hipRY = jointPoints[PyKinectV2.JointType_HipRight].y
        self.SpineShoulderX = jointPoints[PyKinectV2.JointType_SpineShoulder].x
        self.SpineShoulderY = jointPoints[PyKinectV2.JointType_SpineShoulder].y
        self.SpineMidY = jointPoints[PyKinectV2.JointType_SpineMid].y
        self.airball = pygame.image.load('images/airballs.png')
        self.airball = pygame.transform.scale(self.airball, (500, 500))
        
        # box = (self.SpineShoulderX + 10, self.SpineShoulderY, self.shoulderRX - self.SpineShoulderX, self.SpineMidY)
        # pygame.draw.rect(self._frame_surface, pygame.color.THECOLORS['green'], box)
        
        self._frame_surface.blit(self.airball,(self.shoulderRX, self.shoulderRY))            

    def fireBend(self, joints, jointPoints, rad): 
        self.rad = rad
        
        if self.timerStart % 10 == 0:
            self.rad += 10
        
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["red"], PyKinectV2.JointType_HandRight, self.rad)
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["red"], PyKinectV2.JointType_HandLeft, self.rad)

    def drawChargeHands(self, joints, jointPoints, rad):
        self.rad = rad
        
        if self.timerStart % 10 == 0:
            self.rad += 10
        
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["orange"], PyKinectV2.JointType_HandRight, self.rad)
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["orange"], PyKinectV2.JointType_HandLeft, self.rad)
    
    def waterBend(self, joints, jointPoints):
        self.change = (self.prevLHY - self.leftHY) + (self.prevRHY - self.rightHY)
        if math.isnan(self.change) or self.change < 0:
            self.change = 0
        self.prevLHY = self.leftHY
        self.prevRHY = self.prevRHY
        
    
    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self._kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()


    def depth_frame_ready(frame):
        if video_display:
            return
    
        with screen_lock:
            address = surface_to_array(screen)
            frame.image.copy_bits(address)
            del address
            if skeletons is not None and draw_skeleton:
                draw_skeletons(skeletons)
            pygame.display.update()    
    
    
    def video_frame_ready(frame):
        if not video_display:
             return
    
        with screen_lock:
            address = surface_to_array(screen)
            frame.image.copy_bits(address)
            del address
            if skeletons is not None and draw_skeleton:
                draw_skeletons(skeletons)
            pygame.display.update()

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and  self.opponent.posX > 0 :
                self.opponent.posX -= self.opponent.vel
                self.opponent.leftPlayerWalk = True
                self.opponent.rightPlayerWalk = False
                self.opponent.standing = False
                
            if event.key == pygame.K_d and self.opponent.posX < self.width - self.opponent.spriteSize:
                self.opponent.posX += self.opponent.vel   
                self.opponent.leftPlayerWalk = False
                self.opponent.rightPlayerWalk = True
                self.opponent.standing = False
            else:
                self.opponent.standing = True
        
            if not(self.opponent.isJump): #doesn't allow you to move up/down if jumping or jump again if jumping
                if event.key == pygame.K_w and self.opponent.posX > 0 and self.opponent.posX <= self.width - self.opponent.spriteSize:
                    self.opponent.isJump = True
                    self.opponent.standing = True

    def run(self): 
        while not self._done:
            
            pygame.init()
           
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self._done = True # Flag to exit loop

                elif event.type == pygame.VIDEORESIZE: # window resized
                    self._screen = pygame.display.set_mode(event.dict['size'], 
                        pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)
        
          
            # Let's fill out back buffer surface with frame's data 
            if self._kinect.has_new_color_frame():
                frame = self._kinect.get_last_color_frame()
                self.draw_color_frame(frame, self._frame_surface)
                frame = None

            # body frame, so can get skeletons
            if self._kinect.has_new_body_frame(): 
                self._bodies = self._kinect.get_last_body_frame()
           

        # Kinect runtime object, we want color and body frames 
            self.kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)

        # back buffer surface for getting Kinect color frames, 32bit color, width and height equal to the Kinect color frame size
            self.frameSurface = pygame.Surface((self.kinect.color_frame_desc.Width, self.kinect.color_frame_desc.Height), 0, 32)
            
            self.screenWidth = self.kinect.color_frame_desc.Width
            self.screenHeight = self.kinect.color_frame_desc.Height
            
            
            if self.state == "startMode":
                self._frame_surface.blit(self.startScreen,(0,0))            
            
            elif self.state == "selectAang":
                self._frame_surface.blit(self.charAangScreen,(0,0))
            elif self.state == "selectZuko":
                self._frame_surface.blit(self.charZukoScreen,(0,0))            
            elif self.state == "selectToph":
                self._frame_surface.blit(self.charTophScreen,(0,0))
            elif self.state == "selectTyLee":
                self._frame_surface.blit(self.charTyLeeScreen,(0,0))
            elif self.state == "selectKatara":
                self._frame_surface.blit(self.charKataraScreen,(0,0))
            elif self.state == "selectCabbage":
                self._frame_surface.blit(self.charCabScreen,(0,0))
            elif self.state == "selectCombustion":
                self._frame_surface.blit(self.charCBManScreen,(0,0))
            elif self.state == "selectMomo":
                self._frame_surface.blit(self.charMomoScreen,(0,0))
            elif self.state =="endMode":
                self._frame_surface.blit(self.endScreen, (0,0))
            elif self.state == "gameMode":
                self._frame_surface.blit(self.playScreen,(0,0))
                pygame.mixer.Sound.play(self.themeSong)
    
                basicfont = pygame.font.SysFont(None, 50) #print chosen Move
                textMove = basicfont.render('Your Move:' + " " + str(self.playerMove),True, self.black)
                textrect = textMove.get_rect()
                textrect = ((8,42))
                self._frame_surface.blit(textMove, textrect)
    
                basicfont = pygame.font.SysFont(None, 50) #print charge
                textCharge = basicfont.render('Your Charge:' + " " + str(self.playerCharge),True, self.black)
                textrect = textCharge.get_rect()
                textrect = ((8,58))
                self._frame_surface.blit(textCharge, textrect)
                
                basicfont = pygame.font.SysFont(None, 50) #print charge
                textCharge = basicfont.render('CPU Charge:' + " " + str(self.oppCharge),True, self.black)
                textrect = textCharge.get_rect()
                textrect = ((self.width - 200,58))
                self._frame_surface.blit(textCharge, textrect)
                
                
                if self.playerNotEnough == True:
                    basicfont = pygame.font.SysFont(None, 30) #print not enough!
                    textNotEnough = basicfont.render('Not enough Charge!',True, (255,165,0))
                    textrectNE = textNotEnough.get_rect()
                    textrectNE.center = ((self.width*0.5,self.height*0.75))
                    self._frame_surface.blit(textNotEnough, textrectNE)
                    textChooseCharge = basicfont.render('Choose Charge!', True, (255,165,0))
                    textrectCC = textChooseCharge.get_rect()
                    textrectCC.center = ((self.width*0.5, self.height*0.7))
                    self._frame_surface.blit(textChooseCharge, textrectCC)
                    
                
                for bulZ in self.playerBulList:
                    bulZ.draw(self._frame_surface)
                for bulA in self.oppBulList:
                    bulA.draw(self._frame_surface)   
                                
                self.timeBar.draw(self._frame_surface)
                self.mainHealthBar.draw(self._frame_surface)
                self.oppHealthBar.draw(self._frame_surface)
                self.player.draw()
                self.opponent.draw()
                pygame.display.update()
            
        
            ## body tracking
            if self._bodies is not None: 
                for i in range(0, self._kinect.max_body_count):
                    body = self._bodies.bodies[i]
                    if not body.is_tracked: 
                        continue 
                    
                    joints = body.joints 
                    
                    # convert joint coordinates to color space 
                    joint_points = self._kinect.body_joints_to_color_space(joints)
                    self.drawSpine(joints, joint_points)
                    self.drawCenterBox(joints, joint_points)
                    self.drawCircPalms(joints, joint_points) #resting hand Position
                    if body.hand_right_state == 4: #lasso
                        self.startIntroVid()
                        print("LASSO")
                        self.lassoDectection(joints, joint_points) #make blue circ
                    elif self.centerCollision(joint, joint_points):
                        self.state = "learnMode"
                    elif self.clapUp(joints, joint_points):
                        print('C UP')
                        self.state = "gameMode"
                    
                    ## Splash screen
                    elif self.state == "learnMode" and self.centerCollision(joint_points) == True: 
                        self.state = "selectAang"
                    elif self.state == "selectAang" and self.clapRight(joints, joint_points):
                        self.state = "selectZuko"
                    elif self.state == "selectAaang" and self.clapLeft(joints, joint_points):
                        self.state = "selectMomo"
                    elif self.state == "selectZuko" and self.clapRight(joints, joint_points):
                            self.state = "selectCabbage"
                    elif self.state == "selectZuko" and self.clapLeft(joints, joint_points):
                        self.state = "selectAang"
                    elif self.state == "selectCabbage" and self.clapRight(joints, joint_points):
                        self.state = "selectTyLee"
                    elif self.state == "selectCabbage" and self.clapLeft(joints, joint_points):
                        self.state = "selectZuko"
                    elif self.state == "selectTyLee" and self.clapRight(joints, joint_points):
                        self.state = "selectToph"
                    elif self.state == "selectTyLee" and self.clapLeft(joints, joint_points):
                        self.state = "selectCabbage"
                    elif self.state == "selectToph" and self.clapRight(joints, joint_points):     
                        self.state = "selectCombustion"
                    elif self.state == "selectToph" and self.clapLeft(joints, joint_points):  
                        self.state = "selectTyLee"
                    elif self.state == "selectCombustion" and self.clapRight(joints, joint_points):
                        self.state = "selectKatara"
                    elif self.state == "selectCombustion" and self.clapLeft(joints, joint_points):      
                        self.state = "selectToph"
                    elif self.state == "selectKatara" and self.clapRight(joints, joint_points):
                        self.state = "selectMomo"
                    elif self.state == "selectKatara" and self.clapLeft(joints, joint_points):
                        self.state = "selectCombustion"
                    elif self.state == "selectMomo" and self.clapRight(joints, joint_points):
                        self.state = "selectAang"
                    elif self.state == "selectMomo" and self.clapLeft(joints, joint_points):
                            self.state = "selectKatara"

                    elif self.state == "gameMode":
                        if self.playerChoosing == True:
                            if body.hand_right_state == 4:
                                self.playerMove = "shoot"
                            
                            if self.blockDectection(joint_points): #player mirrors w/ space
                                self.drawShield(joints, joint_points)
                                self.playerMove = "mirror"
            
                            if self.playerCharge >= 5:
                                self.fireBend(joints, joint_points, 40)
                                self.playerMove = "bigBomb"
            
                            if self.clapLeft(joints, joint_points) and  self.player.posX > 0:
                                self.player.posX -= self.player.vel
                                self.player.leftPlayerWalk = True
                                self.player.rightPlayerWalk = False
                                self.player.standing = False
                                
                            if self.clapRight(joints, joint_points) and self.player.posX < self.width - self.player.spriteSize:
                                self.player.posX += self.player.vel   
                                self.player.leftPlayerWalk = False
                                self.player.rightPlayerWalk = True
                                self.player.standing = False
                           
                            #doesn't allow you to move up/down if jumping or jump again if jumping
                            if not(self.player.isJump): #player pressed up
                                if self.clapUp(joints, joint_points):
                                    self.playerMove = "jump"
                            else:
                                self.drawChargeHands(joints, joint_points, 40)
                                self.player.standing = True
                                self.playerMove = "charge"

                                
            self.timeBar.tBTime += 55 #timer bar moves
            self.time += 0.5
            if self.timeBar.width + self.timeBar.tBTime > self.width: #at the end
                # self.startRealScreen += 1
                self.timeBar.tBTime = 0
                self.move = True
                self.playerChoosing = False
                self.plzSHOOT = True
            else:
                self.move = False
                self.plzSHOOT = False
            if self.timeBar.width + self.timeBar.tBTime < self.width:
                self.playerChoosing = True
            else:
                self.playerChoosing = False

            ##Bullet Tracker
            self.playerBulletTracker()
            self.oppBulletTracker()
                    
                
                        
            if self.mainHealthBar.bulCount == 10 or self.oppHealthBar.bulCount == 10:
                self.state = "endMode"

            ## Execute Player Moves
        
                        
                #opponent moves
                # if self.opponent.rightPlayerWalk == True: 
                #     self.opponent.dir = 1
                # else:
                if self.oppShot == True:
                    self.opponent.rightPlayerWalk = True
                   
                # 
                if event.key == pygame.K_s:
                    self.oppBulList.append(Bullet(self.opponent.posX, self.opponent.posY, 8, (0,0,0), self.opponent.dir))
                    
                if event.key == pygame.K_a and  self.opponent.posX > 0:
                    self.opponent.posX -= self.opponent.vel
                    self.opponent.leftPlayerWalk = True
                    self.opponent.rightPlayerWalk = False
                    self.opponent.standing = False
                    
                if event.key == pygame.K_d and self.opponent.posX < self.width - self.opponent.spriteSize:
                    self.opponent.posX += self.opponent.vel   
                    self.opponent.leftPlayerWalk = False
                    self.opponent.rightPlayerWalk = True
                    self.opponent.standing = False
                else:
                    self.opponent.standing = True
            
                if not(self.opponent.isJump): #doesn't allow you to move up/down if jumping or jump again if jumping
                    if event.key == pygame.K_w and self.opponent.posX > 0 and self.opponent.posX <= self.width - self.opponent.spriteSize:
                        self.opponent.isJump = True
                        self.opponent.standing = True
                if event.key == pygame.K_r:
                    self.state = "startMode"
                    
                    
                    
                    
            if self.plzSHOOT == True:
                if self.playerMove == "shoot" and self.playerCharge >= 1:
                    self.playerCharge -= 1
                    self.player.bulletCount += 1
                    self.playerShot = True
                    self.player.bulletCount = 1
                    self.playerBulList.append(Bullet(self.player.posX, self.player.posY, 8, (0,0,0), self.player.dir))
    
                if self.playerMove == "mirror" and self.playerCharge >= 1:
                    self.playerMirrored = True
                    self.player.color = (255,255,255)
                    self.playerCharge -= 1
                    
                if self.playerCharge < 1 and (self.playerMove == "mirror" or self.playerMove == "shoot"):
                    self.playerMove = "charge"
                    self.playerNotEnough = True
                
                if self.playerMove == "bigBomb":
                    self.playerBulList.append(Bullet(self.player.posX, self.player.posY, 60, (0,0,0), self.player.dir))
                
                if self.playerMove == "jump":
                    self.player.isJump = True
                    self.player.standing = True
                
                if self.playerMove == "charge":
                    self.playerCharge += 1
                if self.playerCharge >= 1: #resets "notEnough"
                    self.playerNotEnough = False
                if self.playerMove != "mirror": #resets color
                    self.player.color = (255,165,0)
                    self.playerMirrored = False
                ## Tracking AI
                if self.plzSHOOT == True:
                    self.playerMoveTracker.append(self.playerMove)
            dictComboCount = {}
            for curMove in self.playerMoveTracker:
                dictComboCount[curMove] = dictComboCount.get(curMove, 0) + 1
            # print(dictComboCount)
            recommendedMove = []
            mostProbMove = []
            best = 0
            for move in dictComboCount:
                count = dictComboCount[move]
                if count > best:
                    best = count
                    mostProbMove.append(move)
            # print(mostProbMove)
            jumpAI = "jump"
            mirrorAI  = "mirror"
            chargeAI = "charge"
            shootAI = "shoot"
            bigFireAI = "bigboi"
            for playerCurMove in self.playerMoveTracker: #optimal defense moves
                if playerCurMove == "charge":
                    recommendedMove.append(chargeAI)
                elif playerCurMove == "shoot":
                    recommendedMove.append(mirrorAI)
                elif playerCurMove == "mirror":
                    recommendedMove.append(shootAI)
                elif playerCurMove == "jump":
                    recommendedMove.append(shootAI)
            # print(recommendedMove)
            if len(recommendedMove) <= 5: #randomMove
                self.oppMove = random.choice([jumpAI, mirrorAI, shootAI, chargeAI])
            else:
                for j in recommendedMove:
                    self.oppMove = j
                    recommendedMove.remove(j)
            # print(self.oppMove)
    
            ## Executing opponent AI
            if self.move == True: 
                if self.oppMove != mirrorAI:
                    self.opponent.color = (255,165,0)
                    self.opponentMirrored = False
                if self.oppCharge <= 0: #fix AI
                    self.oppMove = chargeAI
                    self.oppCharge += 1
                else:
                    if self.oppMove == jumpAI: #free
                        self.opponent.isJump = True
                    elif self.oppMove == mirrorAI and self.oppCharge >= 1: #mirror cost 1
                        self.opponent.color = mirrorAI
                        self.opponentMirrored = True
                        self.oppCharge -= 1
                    elif self.oppMove == chargeAI: #free
                        self.oppCharge += 1
                        return self.oppMove
                    elif self.oppMove == shootAI and self.oppCharge >= 1: #shooting cost 1
                        self.oppBulList.append(Bullet(self.opponent.posX, self.opponent.posY, 8, (0,0,0), self.opponent.dir))
                        self.oppCharge -= 1
                    elif self.oppCharge == 5: #bigFire cost 5
                        self.oppBulList.append(Bullet(self.opponent.posX, self.opponent.posY, 60, (0,0,0), self.opponent.dir))
                        self.oppMove = bigFireAI
                    #reset player moves too
                    self.opponent.color = (255,165,0)
                    self.opponentMirrored = False
            
        
            if self.playerShot == True and self.oppMove == "shoot":
                print('hi')
                if self.bulletSpeed > 5:
                    if (self.playerBulPosX + 50 >= self.opponent.posX) and self.playerBulPosX < self.opponent.posX and self.playerBulPosY >= self.opponent.posY:
                        self.opponent.isJump = True
                    else:
                        if (self.playerBulPosX + 20 >= self.opponent.posX) and self.playerBulPosX < self.opponent.posX:
                            self.opponent.isJump = True
        
            if self.oppShot == True and self.playerMove == "shoot": #jump dodge
                if self.bulletSpeed > 5:
                    if (self.playerBulPosX + 50 >= self.player.posX) and self.playerBulPosX < self.palyer.posX and self.playerBulPosY >= self.player.posY:
                        self.player.isJump = True
                    else:
                        if (self.playerBulPosX + 20 >= self.player.posX) and self.playerBulPosX < self.player.posX:
                            self.player.isJump = True
            
            
            screen_lock = thread.allocate()


                    
            # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
            # --- (screen size may be different from Kinect's color frame size) 
            h_to_w = float(self._frame_surface.get_height()) / self._frame_surface.get_width()
            target_height = int(h_to_w * self._screen.get_width())
            surface_to_draw = pygame.transform.scale(self._frame_surface, (self._screen.get_width(), target_height))
            self._screen.blit(surface_to_draw, (0,0))
            surface_to_draw = None
            pygame.display.update()

            
            
            for event in pygame.event.get():
                self.get_event(event)
            
            pygame.display.update()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self._clock.tick(60)
            
        
        # Close our Kinect sensor, close the window and quit.
        self._kinect.close()
        pygame.quit()
        
__main__ = "Kinect v2 Body Game"
game = BodyGameRuntime()
game.run()


