
from pygame import *
import pyganim
import os

MOVE_SPEED = 7
WIDTH = 17
HEIGHT = 23
COLOR =  "#888888"
JUMP_POWER = 10
GRAVITY = 0.4 
ANIMATION_DELAY = 0.1 
ICON_DIR = os.path.dirname(__file__) 

ANIMATION_RIGHT = [('%s/char/r1.png' % ICON_DIR),
            ('%s/char/r2.png' % ICON_DIR),
            ('%s/char/r3.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/char/l1.png' % ICON_DIR),
            ('%s/char/l2.png' % ICON_DIR),
            ('%s/char/l3.png' % ICON_DIR)]
ANIMATION_JUMP_LEFT = [('%s/char/jl.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/char/jr.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/char/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/char/0.png' % ICON_DIR, 0.1)]

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   
        self.startX = x 
        self.startY = y
        self.yvel = 0 
        self.onGround = False 
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) 
        self.image.set_colorkey(Color(COLOR)) 

        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
     
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0)) 
        
        self.boltAnimJumpLeft= pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()
        
        self.boltAnimJumpRight= pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()
        
        self.boltAnimJump= pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()
        

    def update(self, left, right, up, platforms, spikes, queen):
        
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))
               
                       
        if left:
            self.xvel = -MOVE_SPEED 
            self.image.fill(Color(COLOR))
            if up: 
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))
 
        if right:
            self.xvel = MOVE_SPEED 
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))
         
        if not(left or right): 
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))
            
        if not self.onGround:
            self.yvel +=  GRAVITY
            
        self.onGround = False;   
        self.rect.y += self.yvel
        lv = self.collide(0, self.yvel, platforms, spikes ,queen)

        self.rect.x += self.xvel 
        lv =self.collide(self.xvel, 0, platforms, spikes ,queen)

        return lv
   
    def collide(self, xvel, yvel, platforms, spikes ,queen):
        for p in platforms:
            if sprite.collide_rect(self, p): 

                if xvel > 0:                      
                    self.rect.right = p.rect.left 

                if xvel < 0:                      
                    self.rect.left = p.rect.right 

                if yvel > 0:                      
                    self.rect.bottom = p.rect.top 
                    self.onGround = True          
                    self.yvel = 0                 

                if yvel < 0:                      
                    self.rect.top = p.rect.bottom 
                    self.yvel = 0             
        for s in spikes:
            if sprite.collide_rect(self, s): 
                return -1
        for q in queen:
            if sprite.collide_rect(self, q): 
                return 1
        return 0
                
                
