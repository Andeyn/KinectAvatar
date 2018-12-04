### pygame template by Lukas Peraza
### https://qwewy.gitbooks.io/pygame-module-manual/chapter1/framework.html
### collaborated with @lukez1

import pygame
import random 
import math
import sys

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
        self.posX = self.width//20
        self.posY = self.height - 100
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
        self.posX = self.width//20
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
        self.posX = self.width//20
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
        self.posX = self.width//20
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
        self.posX = self.width//20
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
        self.posX = self.width//20
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
        self.posX = self.width//20
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
        self.posX = self.width*7//8
        self.posY = self.height - 100
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
        speed = random.randint(5, 10)
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

class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.width = 600
        self.height = 400
        self.state = "startMode"
        self.oppCharge = 1
        self.playerCharge = 1
        self.move = False
        self.playerMoveTracker = []
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
        self.charList = [self.charAangScreen, self.charMomoScreen, self.charKataraScreen,self.charCBManScreen, self.charTophScreen, self.charTyLeeScreen, self.charCabScreen, self.charZukoScreen]
        
        
        self.endScreen = pygame.image.load("images/gameOver.png")
        self.endScreen =pygame.transform.scale(self.endScreen,(self.width,self.height))
        self.playScreen = pygame.image.load("images/waternation.jpg")
        self.playScreen = pygame.transform.scale(self.playScreen,(self.width,self.height))
    
        self.player = Aang(self.screen)
        self.opponent = Zuko(self.screen)
        if self.state == "selectAang":
            self.player = Aang(self.screen)
            self.opponent = Zuko(self.screen)
        elif self.state == "selectToph":
            self.player = Toph(self.screen)
            self.opponent = Zuko(self.screen)
        elif self.state == "selectZuko":
            self.player = Zuko(self.screen)
            self.opponent = Zuko(self.screen)
        elif self.state == "selectCombustion":
            self.player = combustionMan(self.screen)
            self.opponent = Zuko(self.screen)
        elif self.state == "selectTyLee":
            self.player = tyLee(self.screen)
            self.opponent = Zuko(self.screen)
        elif self.state == "selectKatara":
            self.player = Katara(self.screen)
            self.opponent = Zuko(self.screen)
        elif self.state == "selectCabbage":
            self.player = cabbageMan(self.screen)
            self.opponent = Zuko(self.screen)
        elif self.state == "selectMomo":
            self.player = Momo(self.screen)
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
        self.bulletPosX = 0
        self.bulletPosY = 0
        self.opponent.dir = -1
        self.player.dir = 1
        
    def cleanup(self):
       print('cleaning up Menu state stuff')
    def startup(self):
       print('starting Menu state stuff')
    def get_event(self, event):
        if self.state == "startMode":
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "selectAang"
        if event.type == pygame.KEYDOWN:
            if self.state == "selectAang":
                if event.key == pygame.K_RIGHT:
                    self.state = "selectZuko"
                if event.key == pygame.K_LEFT:
                    self.state = "selectMomo"
            elif self.state == "selectZuko":
                if event.key == pygame.K_RIGHT:
                    self.state = "selectCabbage"
                if event.key == pygame.K_LEFT:
                    self.state = "selectAang"
            elif self.state == "selectCabbage":
                if event.key == pygame.K_RIGHT:
                    self.state = "selectTyLee"
                if event.key == pygame.K_LEFT:
                    self.state = "selectZuko"
            elif self.state == "selectTyLee":
                if event.key == pygame.K_RIGHT:
                    self.state = "selectToph"
                if event.key == pygame.K_LEFT:
                    self.state = "selectCabbage"
            elif self.state == "selectToph":
                if event.key == pygame.K_RIGHT:
                    self.state = "selectCombustion"
                if event.key == pygame.K_LEFT:
                    self.state = "selectTyLee"
            elif self.state == "selectCombustion":
                if event.key == pygame.K_RIGHT:
                    self.state = "selectKatara"
                if event.key == pygame.K_LEFT:
                    self.state = "selectToph"
            elif self.state == "selectKatara":
                if event.key == pygame.K_RIGHT:
                    self.state = "selectMomo"
                if event.key == pygame.K_LEFT:
                    self.state = "selectCombustion"
            elif self.state == "selectMomo":
                if event.key == pygame.K_RIGHT:
                    self.state = "selectAang"
                if event.key == pygame.K_LEFT:
                    self.state = "selectKatara"
            if event.key == pygame.K_RETURN:
                self.state = "gameMode"

        if self.state == "gameMode":
            if event.type == pygame.KEYDOWN and self.playerChoosing == True:
                if event.key == pygame.K_DOWN:
                    self.playerMove = "shoot"
                
                if event.key == pygame.K_SPACE and self.playerCharge >= 1: #player mirrors w/ space
                    self.playerMove = "mirror"


                if event.key == pygame.K_RETURN:
                    self.playerMove = "charge"

                if event.key == pygame.K_b and self.playerCharge >= 5:
                    self.playerMove = "bigBomb"

                if event.key == pygame.K_LEFT and  self.player.posX > 0:
                    self.player.posX -= self.player.vel
                    self.player.leftPlayerWalk = True
                    self.player.rightPlayerWalk = False
                    self.player.standing = False
                    
                if event.key == pygame.K_RIGHT and self.player.posX < self.width - self.player.spriteSize:
                    self.player.posX += self.player.vel   
                    self.player.leftPlayerWalk = False
                    self.player.rightPlayerWalk = True
                    self.player.standing = False
                else:
                    self.player.standing = True
            
                #doesn't allow you to move up/down if jumping or jump again if jumping
                if not(self.player.isJump): #player pressed up
                    if event.key == pygame.K_UP and self.player.posX > 0 and self.player.posX <= self.width - self.player.spriteSize:
                        self.playerMove = "jump"
                        
               
                if self.oppShot == True:
                    self.opponent.rightPlayerWalk = True
                   

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

    
    def timerFired(self):        
        self.timeBar.tBTime += 8 #timer bar moves
        if self.timeBar.width + self.timeBar.tBTime == self.width: #at the end
            self.timeBar.tBTime = 0
            self.move = True
            self.playerChoosing = False
            self.plzSHOOT = True
        else:
            self.move = False
            self.plzSHOOT = False
        if self.timeBar.width + self.timeBar.tBTime < self.width - 5:
            self.playerChoosing = True
        else:
            self.playerChoosing = False
        
        if self.player.bulletCount == 1 and self.bulletPosX == None:
            self.player.time += 1
            if self.player.time % 20 == 0:
                self.player.bulletCount = 0
        
        self.opponent.time += 1
        
        ## Tracking Player Moves AI
        if self.plzSHOOT == True:
           self.playerMoveTracker.append(self.playerMove)
        # print(self.playerMoveTracker)
        #create a queuing system that prepares the most likely attack
       
        dictComboCount = {}
        ## React to Tracking 
        for curMove in self.playerMoveTracker:
            dictComboCount[curMove] = dictComboCount.get(curMove, 0) + 1
        # print(dictComboCount)
        
        
        ## Hardcoded Random AI
   
        #     for nextMove in recommendedMove:
        #         # if oppMoveLegal == True:
        #         self.oppMove = recommendedMove[0]
        #         recommendedMove.remove(recommendedMove[0])
        #         # else:
        #         # self.oppMove = chargeAI
            
        if self.move == True:
            jumpAI = "jump"
            mirrorAI  = "mirror"
            chargeAI = "charge"
            shootAI = "shoot"
            bigFireAI = "bigboi"
            recommendedMove = []
        ## Countering Moves
            for playerCurMove in self.playerMoveTracker:
                if playerCurMove == "charge":
                    recommendedMove.append(shootAI)
                elif playerCurMove == "shoot":
                    recommendedMove.append(mirrorAI)
                elif playerCurMove == "mirror":
                    recommendedMove.append(chargeAI)
                elif playerCurMove == "jump":
                    recommendedMove.append(chargeAI)
            # print(recommendedMove)
            randomMove = random.choice([jumpAI, mirrorAI, shootAI, chargeAI])
            if len(recommendedMove) == 1:
                randomMove = random.choice([jumpAI, mirrorAI, shootAI, chargeAI])
            else:
                for j in recommendedMove:
                    randomMove = j
            # print(randomMove)
            print(self.playerMove)
        ## Executing AI
            if randomMove != mirrorAI:
                self.opponent.color = (255, 165, 0)
                self.opponentMirrored = False
            if self.oppCharge <= 0: #fix AI
                randomMove = chargeAI
                self.oppCharge += 1
            else:
                if randomMove == jumpAI: #jumping free
                    self.opponent.isJump = True
                elif randomMove == mirrorAI and self.oppCharge >= 1: #mirror cost 1
                    self.opponent.color = (255,255,255)
                    self.opponentMirrored = True
                    self.oppCharge -= 1
                elif randomMove == chargeAI: # charging free
                    self.oppCharge += 1
                    return randomMove
                elif randomMove == shootAI and self.oppCharge >= 1: #shooting cost 1
                    self.oppBulList.append(Bullet(self.opponent.posX, self.opponent.posY, 8, (0,0,0), self.opponent.dir))
                    self.oppCharge -= 1
                elif self.oppCharge == 5: #bigFire cost 5
                    self.oppBulList.append(Bullet(self.opponent.posX, self.opponent.posY, 60, (0,0,0), self.opponent.dir))
                    randomMove = bigFireAI
    
                    
            # print(randomMove)
            print('opCharge', self.oppCharge)



        ##Bullet Tracker
        for bulA in self.playerBulList: #detects if player is shot at
            bulA.x += bulA.vel
            self.bulletPosX = bulA.x
            self.bulletPosY = bulA.y
            self.bulletSpeed = bulA.vel
            if (self.opponent.hitbox[0]< bulA.x and (self.opponent.hitbox[0] + 70) > bulA.x) and (self.opponent.hitbox[1] < bulA.y and (self.opponent.hitbox[1] + 70) > bulA.y) and self.opponentMirrored == False: #normally hit
                print('opponent hit')
                self.oppHealthBar.bulCount += 1
                self.playerBulList.remove(bulA)
                self.playerShot = False
                if bulA.rad > 50:
                    self.oppHealthBar.score += 60
                    self.oppCharge = 0
                else:
                    self.oppHealthBar.score += 20
                    self.oppCharge -= 1
            if (self.opponent.hitbox[0]< bulA.x and (self.opponent.hitbox[0] + 70) > bulA.x) and (self.opponent.hitbox[1] < bulA.y and (self.opponent.hitbox[1] + 70) > bulA.y) and self.opponentMirrored == True: #mirrored
                bulA.vel *= -1
            if bulA.x > self.width or bulA.x < 0: #out of bounds
                self.playerBulList.remove(bulA)
                self.playerShot = False
                
        for bulZ in self.oppBulList: #opponent's bullets that are shooting
            bulZ.x += bulZ.vel
            if (self.player.hitbox[0]< bulZ.x and (self.player.hitbox[0] + 70) > bulZ.x) and (self.player.hitbox[1] < bulZ.y and (self.player.hitbox[1] + 70) > bulZ.y) and self.playerMirrored == False:
                print('player hit')
                self.mainHealthBar.bulCount += 1 #detects gameOver
                self.oppBulList.remove(bulZ)
                if bulZ.rad > 50:
                    self.mainHealthBar.score += 60 #big bomb
                    self.playerCharge = 0
                else:
                    self.mainHealthBar.score += 20
                    self.playerCharge -= 1
            if bulZ.x < 0 or bulZ.x > self.width: #out of bounds
                self.oppBulList.remove(bulZ)
            if (self.player.hitbox[0]< bulZ.x and (self.player.hitbox[0] + 70) > bulZ.x) and (self.player.hitbox[1] < bulZ.y and (self.player.hitbox[1] + 70) > bulZ.y) and self.playerMirrored == True:
                bulZ.vel *= -1
            if (self.opponent.hitbox[0] < bulZ.x) and (self.opponent.hitbox[0] + 70 > bulZ.x) and (self.opponent.hitbox[1] < bulZ.y) and (self.opponent.hitbox[1] + 70 > bulZ.y) and self.playerMirrored == True: #deflected and opponent hit
                self.oppBulList.remove(bulZ)
                if bulZ.rad > 50:
                    self.oppHealthBar.score += 60
                    self.oppCharge = 0
                else:
                    self.oppHealthBar.score += 20   
                    self.oppCharge -= 1
                self.oppHealthBar.bulCount += 1 #detects gameOver
                self.oppShot = False
            # if (self.player.hitbox[0] < bulZ.x and (self.player.hitbox[0] + 70) > bulZ.x) and (self.player.hitbox[1] < bulZ.y and (self.player.hitbox[1] + 70) > bulZ.y) and self.playerMirrored == False: #mirrored
            #     bulZ.vel *= -1
            # if bulZ.x > self.width or bulZ.x < 0:
            #     self.oppBulList.remove(bulZ)
            #     self.oppShot = False

        if self.player.isJump: #when jumping
            if self.player.jumpCount >= -10:
                neg = 1 #start moving up 
                if self.player.jumpCount < 0:
                    neg = -1 # moving down in the parabola
                #makes a quadratic parabola to illustrate diff speeds
                #0.5 scales the jump smaller 
                self.player.posY -= 0.75*(0.5 * (self.player.jumpCount ** 2) * neg)
                self.player.jumpCount -= 1 #change heights
            else:
                self.player.isJump = False
                self.player.jumpCount = 10
                
        if self.opponent.isJump: #when jumping
            if self.opponent.jumpCount >= -10: 
                neg = 1 #start moving up 
                if self.opponent.jumpCount < 0:
                    neg = -1 # moving down in the parabola
                #makes a quadratic parabola to illustrate diff speeds
                #0.5 scales the jump smaller 
                self.opponent.posY -= 0.75*(0.5 * (self.opponent.jumpCount ** 2) * neg)
                self.opponent.jumpCount -= 1 #change heights
            else:
                self.opponent.isJump = False
                self.opponent.jumpCount = 10
        if self.mainHealthBar.bulCount == 10 or self.oppHealthBar.bulCount == 10:
            self.state = "endMode"

        ### Executing Player Moves
        if self.plzSHOOT == True:
            if self.playerMove == "shoot" and self.playerCharge >= 1:
                self.playerCharge -= 1
                self.player.bulletCount += 1
                self.playerShot = True
                self.player.bulletCount = 1
                self.playerBulList.append(Bullet(self.player.posX, self.player.posY, 8, (0,0,0), self.player.dir))

            if self.playerMove == "mirror" and self.playerCharge >= 1:
                self.player.color = (255,255,255)
                self.playerCharge -= 1
                self.playerMirrored = True
                
            if self.playerCharge < 1 and (self.playerMove == "mirror" or self.playerMove == "shoot"):
                self.playerMove = "charge"
                self.playerNotEnough = True
            
            if self.playerMove == "bigBomb" and self.playerCharge >= 5:
                self.playerBulList.append(Bullet(self.player.posX, self.player.posY, 60, (0,0,0), self.player.dir))
                self.playerCharge -= 5
                
            if self.playerMove == "jump":
                self.player.isJump = True
                self.player.standing = True
            
            if self.playerMove == "charge":
                self.playerCharge += 1
            


            
        if self.playerCharge >= 1: #resets "notEnough"
            self.playerNotEnough = False
            # self.playerMove = "charge"
        if self.playerMove != "mirror": #resets color
            self.player.color = (255,165,0)
            self.playerMirrored = False
            print('brhhh')
        #   if math.fabs(self.player.posX + 100) >= self.opponent.posX:
        #     self.opponent.isJump = True
  
        ## opponents
        if self.playerShot == True and self.oppMove == "shoot":
            print('dis dumb')
            if self.bulletSpeed > 5:
                if (self.bulletPosX + 50 >= self.opponent.posX) and self.bulletPosX < self.opponent.posX and self.bulletPosY >= self.opponent.posY:
                    self.opponent.isJump = True
                else:
                    if (self.bulletPosX + 20 >= self.opponent.posX) and self.bulletPosX < self.opponent.posX:
                        self.opponent.isJump = True
    
        if self.oppShot == True and self.playerMove == "shoot": #jump dodge
            if self.bulletSpeed > 5:
                if (self.bulletPosX + 50 >= self.player.posX) and self.bulletPosX < self.palyer.posX and self.bulletPosY >= self.player.posY:
                    self.player.isJump = True
                else:
                    if (self.bulletPosX + 20 >= self.player.posX) and self.bulletPosX < self.player.posX:
                        self.player.isJump = True
    

    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        # print(self.state)
        if self.state == "startMode":
            self.screen.blit(self.startScreen,(0,0))
        if self.state == "selectAang":
            self.screen.blit(self.charAangScreen,(0,0))
        if self.state == "selectZuko":
            self.screen.blit(self.charZukoScreen,(0,0))            
        if self.state == "selectToph":
            self.screen.blit(self.charTophScreen,(0,0))
        if self.state == "selectTyLee":
            self.screen.blit(self.charTyLeeScreen,(0,0))
        if self.state == "selectKatara":
            self.screen.blit(self.charKataraScreen,(0,0))
        if self.state == "selectCabbage":
            self.screen.blit(self.charCabScreen,(0,0))
        if self.state == "selectCombustion":
            self.screen.blit(self.charCBManScreen,(0,0))
        if self.state == "selectMomo":
            self.screen.blit(self.charMomoScreen,(0,0))
        if self.state =="endMode":
            self.screen.blit(self.endScreen, (0,0))
        if self.state == "gameMode":
            self.screen.blit(self.playScreen,(0,0))
            
            basicfont = pygame.font.SysFont(None, 30) #print chosen Move
            textMove = basicfont.render('Your Move:' + " " + str(self.playerMove),True, self.black)
            textrect = textMove.get_rect()
            textrect = ((8,42))
            screen.blit(textMove, textrect)

            basicfont = pygame.font.SysFont(None, 30) #print charge
            textCharge = basicfont.render('Your Charge:' + " " + str(self.playerCharge),True, self.black)
            textrect = textCharge.get_rect()
            textrect = ((8,58))
            screen.blit(textCharge, textrect)
            
            basicfont = pygame.font.SysFont(None, 30) #print charge
            textCharge = basicfont.render('CPU Charge:' + " " + str(self.oppCharge),True, self.black)
            textrect = textCharge.get_rect()
            textrect = ((self.width - 200,58))
            screen.blit(textCharge, textrect)
            
            if self.playerNotEnough == True:
                basicfont = pygame.font.SysFont(None, 30) #print not enough!
                textNotEnough = basicfont.render('Not enough Charge!',True, (255,165,0))
                textrectNE = textNotEnough.get_rect()
                textrectNE.center = ((self.width*0.5,self.height*0.75))
                screen.blit(textNotEnough, textrectNE)
                textChooseCharge = basicfont.render('Choose Charge!', True, (255,165,0))
                textrectCC = textChooseCharge.get_rect()
                textrectCC.center = ((self.width*0.5, self.height*0.7))
                screen.blit(textChooseCharge, textrectCC)
                
            
            for bulZ in self.playerBulList:
                bulZ.draw(self.screen)
            for bulA in self.oppBulList:
                bulA.draw(self.screen)   
                                
            pygame.display.update()
            self.player.draw()
            self.opponent.draw()
            self.timeBar.draw(self.screen)
            self.mainHealthBar.draw(self.screen)
            self.oppHealthBar.draw(self.screen)
            self.timerFired()


class Game(States):
   def __init__(self):
       States.__init__(self)
       self.next = 'menu'
   def cleanup(self):
        print('cleaning up Game state stuff')
   def startup(self):
       print('starting Game state stuff')
   def get_event(self, event):
        pass
   def update(self, screen, dt):
        self.draw(screen)
   def draw(self, screen):
        print (self.state)

class Control:
   def __init__(self, **settings):
       self.__dict__.update(settings)
       self.done = False
       self.screen = pygame.display.set_mode(self.size)
       self.clock = pygame.time.Clock()
   def setup_states(self, state_dict, start_state):
       self.state_dict = state_dict
       self.state_name = start_state
       self.state = self.state_dict[self.state_name]
   def flip_state(self):
       self.state.done = False
       previous,self.state_name = self.state_name, self.state.next
       self.state.cleanup()
       self.state = self.state_dict[self.state_name]
       self.state.startup()
       self.state.previous = previous
   def update(self, dt):
       if self.state.quit:
           self.done = True
       elif self.state.done:
           self.flip_state()
       self.state.update(self.screen, dt)
   def event_loop(self):
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.done = True
            self.state.get_event(event)
   def main_game_loop(self):
       while not self.done:
           delta_time = self.clock.tick(self.fps)/1000.0
           self.event_loop()
           self.update(delta_time)
           pygame.display.update()


if __name__ == '__main__':
   settings = {
       'size':(600,400),
       'fps' :60
   }

   app = Control(**settings)
   state_dict = {
       'menu': Menu(),
       'game': Game()
   }
   app.setup_states(state_dict, 'menu')
   app.main_game_loop()
   pygame.quit()
   sys.exit()