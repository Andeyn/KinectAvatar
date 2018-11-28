
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
        self.jumpSpeed = self.height/5
        self.attackSpeed = self.width/60
        self.fallSpeed = self.jumpSpeed/30
        self.state = "startMode"
        self.characterX = int(self.width/15)
        self.characterY = int(self.height/8)
        self.sphereRad = int(self.width/40)
        self.posX = self.width/6
        self.posY = 215 * self.height/400
        self.time = 0
        self.bullets = []
        self.screen = screen
        self.lives = 3
        self.health = 0
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
        pygame.draw.rect(self.screen, (255,0,0), self.hitbox, 2)
        
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
        pygame.draw.rect(self.screen, (255,0,0), self.hitbox, 2)
        
        for bullet in self.bullets:
            self.screen.blit(self.airball,(bullet[0],bullet[1]))

class BottomBounds(object):
    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.posY = self.screenHeight - 2
        
    def collidesWithChar(self, other):
        if other.posY <= self.posY:
            return True
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (0, self.screenHeight-2, self.screenWidth, 2))

class Bullet(object):
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.rad = radius
        self.color = color
        self.dir = direction #which way the bullet shoots
        speed = random.randint(3, 10)
        self.vel = speed * self.dir #speed of bullet
        self.bulletList = []

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
        self.auraSpheres = pygame.sprite.Group()
        self.width = 600
        self.height = 400
        self.state = "startMode"
        self.startScreen = pygame.image.load("images/start.png")
        self.startScreen =pygame.transform.scale(self.startScreen,(self.width,self.height))
        self.time = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.playScreen = pygame.image.load("images/startScene.jpg")
        self.playScreen = pygame.transform.scale(self.playScreen,(self.width,self.height))
        self.player = Aang(self.screen)
        self.opponent = Zuko(self.screen)
        self.bottom = BottomBounds(self.width, self.height)
        self.gameOver = False
       
    def cleanup(self):
       print('cleaning up Menu state stuff')
    def startup(self):
       print('starting Menu state stuff')
    def get_event(self, event):
        if self.state == "startMode":
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "gameMode"

        if self.state == "gameMode":        
            if event.type == pygame.KEYDOWN:
                if self.player.rightPlayerWalk == True: 
                    dir = 1
                else:
                    dir = -1
                    
                if event.key == pygame.K_LEFT and  self.player.posX > 0 :
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
            
                if not(self.player.isJump): #doesn't allow you to move up/down if jumping or jump again if jumping
                    if event.key == pygame.K_UP and self.player.posX > 0 and self.player.posX <= self.width - self.player.spriteSize:
                        self.player.isJump = True
                        self.player.standing = True
                
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
                if event.key == pygame.K_r:
                    self.state = "startMode"
                        
    def timerFired(self):
        if self.gameOver == False:
            self.player.time += 1
            self.opponent.time += 1
            if self.player.isJump: #when jumping
                if self.player.jumpCount >= -10: 
                    print('up')
                    neg = 1 #start moving up 
                    if self.player.jumpCount < 0:
                        neg = -1 # moving down in the parabola
                    #makes a quadratic parabola to illustrate diff speeds
                    #0.5 scales the jump smaller 
                    self.player.posY -= 0.5 * (self.player.jumpCount ** 2) * neg 
                    self.player.jumpCount -= 1 #change heights
                else:
                    self.player.isJump = False
                    self.player.jumpCount = 10
                    
            if self.opponent.isJump: #when jumping
                if self.opponent.jumpCount >= -10: 
                    print('up')
                    neg = 1 #start moving up 
                    if self.opponent.jumpCount < 0:
                        neg = -1 # moving down in the parabola
                    #makes a quadratic parabola to illustrate diff speeds
                    #0.5 scales the jump smaller 
                    self.opponent.posY -= 0.5 * (self.opponent.jumpCount ** 2) * neg 
                    self.opponent.jumpCount -= 1 #change heights
                else:
                    self.opponent.isJump = False
                    self.opponent.jumpCount = 10
            
            if self.bottom.collidesWithChar(self.player) == False:
                self.player.posY+=self.player.time * 9.8/100
                self.opponent.posY += self.opponent.time * 9.8/100
        else:
            return

    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        if self.state == "startMode":
            screen.blit(self.startScreen,(0,0))
        elif self.state == "gameMode":
           
            screen.blit(self.playScreen,(0,0))
            pygame.init()
                
            if self.gameOver == True:
                pygame.init()
            
                
            pygame.display.update()
            self.bottom.draw(self.screen)
            self.player.draw()
            self.opponent.draw()
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
    
        self.auraSpheres = pygame.sprite.Group()
        self.width = 100
        self.height = 75
        self.state = "startMode"
        self.startScreen = pygame.image.load("images/start.png")
        self.startScreen = pygame.transform.scale(self.startScreen,(self.width,self.height))
        self.time = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.playScreen = pygame.image.load("images/startScene.jpg")
        self.playScreen = pygame.transform.scale(self.playScreen,(self.width,self.height))
        self.player = Aang(self.screen)
        self.opponent = Zuko(self.screen)
        self.bottom = BottomBounds(self.width, self.height)
        self.gameOver = False
    
    def surface_to_array(surface):
        buffer_interface = surface.get_buffer()
        address = ctypes.c_void_p()
        size = Py_ssize_t()
        _PyObject_AsWriteBuffer(buffer_interface,
                                ctypes.byref(address), ctypes.byref(size))
        bytes = (ctypes.c_byte * size.value).from_address(address.value)
        bytes.object = buffer_interface
        return bytes
    

    def drawCircle(self, joints, jointPoints, color, joint1, rad):
        joint1State = joints[joint1].TrackingState

        #start and end points for drawing lines
        end = (int(jointPoints[joint1].x), int(jointPoints[joint1].y))

        # print(end)
        pygame.draw.circle(self._frame_surface, color, end, rad)

    def drawLine(self, prevX, prevY, curX, curY, color):
        pygame.draw.line(self._frame_surface, color, (prevX, prevY), (curX, curY), 40)
            
    
    def clapRight(self, joints,jointPoints):
        self.spineX = jointPoints[PyKinectV2.JointType_SpineMid].x
        self.aboveHead = jointPoints[PyKinectV2.JointType_SpineShoulder].y
        if self.centerCollision and self.LHX >  self.spineX:
            print("right")
            return True
    def clapLeft(self, joints, jointPoints):
        self.spineX = jointPoints[PyKinectV2.JointType_SpineMid].x
        self.aboveHead = jointPoints[PyKinectV2.JointType_SpineShoulder].y
        if self.centerCollision and self.RHX < self.spineX:
            print("left")
            return True

    def clapUp(self, joints, jointPoints):
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
        self.LHX = jointPoints[PyKinectV2.JointType_HandLeft].x
        self.RHX = jointPoints[PyKinectV2.JointType_HandRight].x
        
        self.LHY = jointPoints[PyKinectV2.JointType_HandLeft].y
        self.RHY = jointPoints[PyKinectV2.JointType_HandRight].y
        dist = math.sqrt(((self.RHX - self.LHX)**2)+ (self.RHY - self.LHY)**2)
        if dist <= 40:
            return True
       
            
    def fireBend(self, joints, jointPoints, rad): 
        #make 20 random circles around your hands to "bend"
        bendList = []
        # for i in range(20):
        #     #right and left hands are in the same place
        #     pos = random.randint(PyKinectV2.JointType_HandRight, PyKinectV2.JointType_HandRight)
        #     bendList.append((joints, jointPoints, pygame.color.THECOLORS["red"], pos))
    
        if self.timerStart % 10 == 0:
            self.rad += 10
        
        self.drawCircle(joints, jointPoints, pygame.color.THECOLORS["red"], PyKinectV2.JointType_HandRight, self.rad)
 
            
    def waterBend(self, joints, jointPoints):
        self.change = (self.prevLHY - self.leftHY) + (self.prevRHY - self.rightHY)
        if math.isnan(self.change) or self.change < 0:
            self.change = 0
        # self.drawLine(self.leftHX, self.prevLHY, self.rightHX, self.rightHY, pygame.color.THECOLORS["red"])
        # self.drawLine(self.leftHX, self.leftHY,screenWidth, screenHeight, pygame.color.THECOLORS["red"])
        # print('wattterrr')
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


    def run(self): 
        while not self._done:
                   
            if self.gameOver == True:
                pygame.init()
                
            
                self.bottom.draw(self._frame_surface)
                self.player.draw()
                self.opponent.draw()
                self.timerFired()
                pygame.display.update()
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
            
            pygame.draw.rect(self._frame_surface, (255, 255, 255), [0,0, self.screenWidth, self.screenHeight])
            
            # self._frame_surface.blit(self.startScreen,(0,0))            
            
            #  draw skeletons to _frame_surface
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
                    if body.hand_right_state == 4: #lasso
                        self.lassoDectection(joints, joint_points) #make blue circ
                    elif self.centerCollision(joint_points) == True: 
                        # print("bend THAT SHIT!")
                        self.timerStart += 1
                        self.fireBend(joints, joint_points,self.rad) #collide
                    # elif self.outsideBoxCollision(joints, joint_points):
                        # print('it works')
                        
                    
                    else:
                        self.drawCircPalms(joints, joint_points) #orange
                        
            screen_lock = thread.allocate()


                    
            # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
            # --- (screen size may be different from Kinect's color frame size) 
            h_to_w = float(self._frame_surface.get_height()) / self._frame_surface.get_width()
            target_height = int(h_to_w * self._screen.get_width())
            surface_to_draw = pygame.transform.scale(self._frame_surface, (self._screen.get_width(), target_height))
            self._screen.blit(surface_to_draw, (0,0))
            surface_to_draw = None
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


