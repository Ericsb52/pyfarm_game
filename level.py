from settings import *
from player import *

class Level:
    def __init__(self):
        self.display_surf = pg.display.get_surface()
        self.all_sprites = pg.sprite.Group()
        self.setup()

    def setup(self):
        self.player = Player((SCREEN_W/2,SCREEN_H/2),self.all_sprites)

    def run(self,dt):
        self.display_surf.fill("black")
        self.all_sprites.draw(self.display_surf)
        self.all_sprites.update(dt)

