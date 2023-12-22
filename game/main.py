
import pygame
import sys
from pygame import *
from player import *
from levels import *

WIN_WIDTH = 800 
WIN_HEIGHT = 632 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) 
BACKGROUND_COLOR = "#004400"

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
        
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           
    l = max(-(camera.width-WIN_WIDTH), l)   
    t = max(-(camera.height-WIN_HEIGHT), t) 
    t = min(0, t)                           

    return Rect(l, t, w, h)

def level_select(lv_count,entities,platforms,spikes,queen):
        x=y=0 
        for row in level[lv_count]: 
            for col in row: 
                if col == "-":
                    pf = Platform(x,y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "s":
                    sp = Spike(x,y)
                    entities.add(sp)
                    spikes.append(sp)
                if col == "q":
                    qu = Queen(x,y)
                    entities.add(qu)
                    queen.append(qu)

                x += PLATFORM_WIDTH 
            y += PLATFORM_HEIGHT    
            x = 0                   
        
        total_level_width  = len(level[lv_count][0])*PLATFORM_WIDTH 
        total_level_height = len(level[lv_count])*PLATFORM_HEIGHT  
        
        camera = Camera(camera_configure, total_level_width, total_level_height)
        return lv_count,entities,platforms,spikes,queen,camera         


def main():
    pygame.init() 
    screen = pygame.display.set_mode(DISPLAY) 
    pygame.display.set_caption("King adventure") 
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) 
                                         
    bg.fill(Color(BACKGROUND_COLOR))
    image = pygame.image.load("%s/map/bg.png" % ICON_DIR)     
    bg.blit(image,(0,0))
    
    
    hero = Player(55,55) 
    left = right = False 
    up = False
    hp = 3
    
    entities = pygame.sprite.Group() 
    health = pygame.sprite.Group(Health(hp)) 
    platforms = [] 
    spikes = [] 
    queen = [] 
    
    entities.add(hero)
    

    lv_count,entities,platforms,spikes,queen,camera = level_select(0,entities,platforms,spikes,queen)
       
    timer = pygame.time.Clock()
    
    
    while True: 
        timer.tick(60)
        for e in pygame.event.get(): 
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and (e.key == K_w or e.key == K_UP):
                up = True
            if e.type == KEYDOWN and (e.key == K_a or e.key == K_LEFT):
                left = True
            if e.type == KEYDOWN and (e.key == K_d or e.key == K_RIGHT):
                right = True


            if e.type == KEYUP and (e.key == K_w or e.key == K_UP):
                up = False
            if e.type == KEYUP and (e.key == K_d or e.key == K_RIGHT):
                right = False
            if e.type == KEYUP and (e.key == K_a or e.key == K_LEFT):
                left = False

        screen.blit(bg, (0,0))
        



        camera.update(hero) 
        isend = hero.update(left, right, up,platforms, spikes, queen) 
        win = False

        if (isend == 1):
            if (lv_count == 2):
                win = True
                entities = pygame.sprite.Group()
                break
            lv_count,entities,platforms,spikes,queen,camera = level_select(lv_count+1,pygame.sprite.Group(),[],[],[])
            hero.__init__(55,55)
            entities.add(hero)
        elif(isend == -1):
            hp -= 1
            if(hp == 0):
                entities = pygame.sprite.Group()
                break
            else:
                hero.__init__(55,55)
            health = pygame.sprite.Group(Health(hp))
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        for e in health:
            screen.blit(e.image,(WIN_WIDTH -196,32))
        
        pygame.display.update()     
    if(win):
        image = pygame.image.load("%s/map/Win.png" % ICON_DIR)     
    else:
        image = pygame.image.load("%s/map/Lose.png" % ICON_DIR)     
    bg.blit(image,(0,0))
    screen.blit(bg, (0,0))

    while True:
        timer.tick(60)
        for e in pygame.event.get(): 
            if e.type == QUIT or (e.type == KEYDOWN and (e.key == K_n)):
                sys.exit()
            if e.type == KEYDOWN and (e.key == K_y):
                main()
        pygame.display.update()

if __name__ == "__main__":
    main()
