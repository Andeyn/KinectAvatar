
### Kinect
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
# from PlayersWithKeys import *
# from pykinect import nui

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
    
    # _PyObject_AsWriteBuffer = ctypes.pythonapi.PyObject_AsWriteBuffer
    # _PyObject_AsWriteBuffer.restype = ctypes.c_int
    # _PyObject_AsWriteBuffer.argtypes = [ctypes.py_object,
    #                                 ctypes.POINTER(ctypes.c_void_p),
    #                                 ctypes.POINTER(Py_ssize_t)]
    
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


    def run(self): #starter code
        # background = pygame.image.load("images/startScene.jpg")
        # self._frame_surface.blit(background, [0,0])
        while not self._done:
            
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self._done = True # Flag to exit loop

                elif event.type == pygame.VIDEORESIZE: # window resized
                    self._screen = pygame.display.set_mode(event.dict['size'], 
                        pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)
        
            
            if self.handsCharging == False: #resets fire size when not touching
                self.rad = 40
        
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
                    elif self.clapLeft(joints,joint_points):
                        myManz.x -= myManz.vel
                        myManz.leftPlayerWalk = True
                        myManz.rightPlayerWalk = False
                        myManz.standing = False
                    
                    else:
                        # self.waterBend(joints,joint_points)
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