import pygame as pg
import sys
from pygame.math import Vector2
from support import *
from pytmx.util_pygame import load_pygame

# Screen settings
SCREEN_W = 1280
SCREEN_H = 720
TILE_SIZE = 64
icon_path = "assets/graphics/character/down/0.png"

# frame rate settings
FPS = 60


# Game settings
TITLE = "Py Farm"


# player setings
player_speed = 200
anim_path = "assets/graphics/character/"

# oerlay pos
overlay_path = "assets/graphics/overlay/"
overlay_positions = {"tool":(50,SCREEN_H-75),
                     "seed":(115,SCREEN_H-75)}

# floor settings
floor_path = "assets/graphics/world/ground.png"
layers = {"water":0,
          "ground":1,
          "soil":2,
          "soil water":3,
          "rain floor":4,
          "house bottom":5,
          "ground plant":6,
          "main":7,
          "house top":8,
          "fruit":9,
          "rain drops":10,
          "hud":11,
          }


