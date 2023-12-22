
from pygame import *
import os

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__) 
 
class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/map/block.png" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Spike(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/map/spike.png" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Queen(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/map/queen.png" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Health(sprite.Sprite):
    def __init__(self, hp):
        sprite.Sprite.__init__(self)
        self.image = Surface((196, 64))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load(f"%s/map/hp{hp}.png" % ICON_DIR)
        

level = [[
       "----------------------------------",
       "-                        q       -",
       "-                       --       -",
       "-            s                   -",
       "-            --                  -",
       "-                                -",
       "--                 -----         -",
       "-                                -",
       "-          s                  -- -",
       "-         ----                   -",
       "--                               -",
       "-                                -",
       "-                            --- -",
       "-                     --         -",
       "-                                -",
       "-              --                -",
       "-     ss                         -",
       "-   -------                      -",
       "-                   ---          -",
       "-                                -",
       "-                          ----  -",
       "-                                -",
       "-                                -",
       "----------------------------------"],
       [
       "----------------------------------",
       "-                                -",
       "-                                -",
       "-                            q   -",
       "-                           --   -",
       "-                                -",
       "---                -----         -",
       "-                                -",
       "-          s                 --- -",
       "-         -----                  -",
       "---                              -",
       "-                              s -",
       "-                      s     --- -",
       "-                    ---         -",
       "-                                -",
       "-              ---               -",
       "-     ss                         -",
       "-   -------                      -",
       "-                   ----         -",
       "-                                -",
       "-     --                    ---  -",
       "-                                -",
       "-                                -",
       "----------------------------------"],
       [
       "----------------------------------",
       "-                                -",
       "-                                -",
       "-            s                   -",
       "-            --                  -",
       "-                                -",
       "--                 -----         -",
       "-                                -",
       "-                            --- -",
       "-         ----                   -",
       "--                               -",
       "-                            q   -",
       "-                            --- -",
       "-                     --         -",
       "-                                -",
       "-              --                -",
       "-                                -",
       "-   -------                      -",
       "-                  ----          -",
       "-                                -",
       "-                           ---  -",
       "-                                -",
       "- sss                            -",
       "----------------------------------"]]